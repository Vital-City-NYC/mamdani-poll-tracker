#!/usr/bin/env python3
"""Regenerate the downloadable CSVs and the search metadata in index.html
from data/polls.json and data/prior-mayors.json. Run after every data change:

    python3 build.py

It never invents a number: everything is read from the two JSON files.
"""
import csv, json, re, datetime as dt
from pathlib import Path

HERE = Path(__file__).parent
polls = json.loads((HERE / "data/polls.json").read_text())
prior = json.loads((HERE / "data/prior-mayors.json").read_text())
POP = {"adults": "all adults", "RV": "registered voters", "LV": "likely voters"}
POSW = {"approval": "approve", "performance": "excellent or good", "favorability": "favorable"}


def fd(a, b):
    A, B = dt.date.fromisoformat(a), dt.date.fromisoformat(b)
    m = lambda d: d.strftime("%b")
    return f"{m(A)} {A.day} to {B.day}" if A.month == B.month else f"{m(A)} {A.day} to {m(B)} {B.day}"


# ---- polls.csv -------------------------------------------------------------
rows = []
for p in polls["polls"]:
    for m in p.get("measures", []):
        pop = m.get("population") or p["population"]
        n = next((s["n"] for s in p.get("subsamples") or [] if s["population"] == pop), p.get("n"))
        rows.append(dict(scope="citywide", pollster=p["pollster"], sponsor=p.get("sponsor") or "",
                         field_start=p["field_start"], field_end=p["field_end"], population=POP.get(pop, pop), n=n,
                         question=m["type"], positive=m.get("approve_or_positive"), negative=m.get("disapprove_or_negative"),
                         unsure=m.get("unsure"), wording=m.get("wording") or "", source=p["url"]))
for p in polls.get("statewide_context", []):
    s = p.get("nyc_subsample") or {}
    if not p.get("field_start") or s.get("favorable") is None or "LOW" in (p.get("confidence") or ""):
        continue
    pop = p["population"].replace("NYS ", "")
    rows.append(dict(scope="city column of a statewide poll (city n not published)", pollster=p["pollster"], sponsor="",
                     field_start=p["field_start"], field_end=p["field_end"], population=POP.get(pop, pop), n="",
                     question="favorability", positive=s["favorable"], negative=s.get("unfavorable"), unsure=s.get("dk"),
                     wording=p.get("wording") or "", source=p.get("crosstabs_url") or p["url"]))
rows.sort(key=lambda r: r["field_end"], reverse=True)
with open(HERE / "data/polls.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# ---- prior-mayors.csv ------------------------------------------------------
prow = []
for x in prior["mayors"]:
    for q in x["polls"]:
        prow.append(dict(mayor=x["name"], inaugurated=x["inaugurated"], pollster=q["pollster"], sponsor=q.get("sponsor") or "",
                         field_start=q.get("field_start") or "", field_end=q.get("field_end") or "",
                         months_since_inauguration=q.get("months_since_inauguration"),
                         population=q.get("subsample") or POP.get(q.get("population"), q.get("population")), n=q.get("n") or "",
                         question="excellent or good grade" if q.get("metric") == "excellent_good" else "approve or disapprove",
                         positive=q.get("approve"), negative=q.get("disapprove"), source=q["url"]))
with open(HERE / "data/prior-mayors.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(prow[0].keys())); w.writeheader(); w.writerows(prow)

# ---- search metadata in index.html ----------------------------------------
ap = [m for p in polls["polls"] for m in p["measures"] if m["type"] == "approval" and m.get("approve_or_positive") is not None]
latest = {}
for p in sorted(polls["polls"], key=lambda p: p["field_end"]):
    for m in p["measures"]:
        if m.get("approve_or_positive") is not None:
            latest[m["type"]] = (p, m)
desc = "Mayor Zohran Mamdani's approval rating in every citywide poll."
if ap:
    a = [m["approve_or_positive"] for m in ap]; d = [m["disapprove_or_negative"] for m in ap]
    desc += f" Job approval has run {min(a)} to {max(a)} percent, with {min(d)} to {max(d)} percent disapproving."
newest = max(latest.values(), key=lambda pm: pm[0]["field_end"]) if latest else None
if newest:
    p, m = newest
    short = p["pollster"].split(" ")[0]
    desc += f" Latest citywide poll: {short}, {fd(p['field_start'], p['field_end'])}, {m['approve_or_positive']} percent {POSW[m['type']]}."
desc += " Field dates, who was surveyed, sample sizes and sources for each."
html = (HERE / "index.html").read_text()
# Static headline and dek for crawlers and no-JavaScript readers; the page's script
# overwrites both with the same finding plus the live day count.
WORD = ["zero", "one", "two", "three", "four", "five", "six"]
if ap:
    nets = [m["approve_or_positive"] - m["disapprove_or_negative"] for m in ap]
    ap_polls = [p for p in polls["polls"] if any(m["type"] == "approval" and m.get("approve_or_positive") is not None for m in p["measures"])]
    k = len(ap_polls)
    which = "the one citywide poll" if k == 1 else "both citywide polls" if k == 2 else f"all {WORD[k] if k < len(WORD) else k} citywide polls"
    rng = str(min(nets)) if min(nets) == max(nets) else f"{min(nets)} to {max(nets)}"
    h1 = (f"More New Yorkers approve of Mamdani than disapprove, by {rng} points, in {which} that asked" if min(nets) > 0
          else f"Mamdani's job approval has run between {min(a)} and {max(a)} percent in citywide polls this year, with disapproval between {min(d)} and {max(d)}")
    last = max(ap_polls, key=lambda p: p["field_end"])
    le = dt.date.fromisoformat(last["field_end"])
    lede = (f"Approval has run from {min(a)} to {max(a)} percent and disapproval from {min(d)} to {max(d)} across the citywide polls that published a topline. "
            f"The most recent ended {le.strftime('%B')} {le.day}, {le.year}. Performance grades and favorability are different questions and are kept apart below.")
    html0 = (HERE / "index.html").read_text()
    html0, a1 = re.subn(r'(<h1 id="finding">)[^<]*(</h1>)', lambda mm: mm.group(1) + h1 + mm.group(2), html0, count=1)
    html0, a2 = re.subn(r'(<p class="dek" id="lede">)[^<]*(</p>)', lambda mm: mm.group(1) + lede + mm.group(2), html0, count=1)
    assert a1 == 1 and a2 == 1, "headline markers not found in index.html"
    (HERE / "index.html").write_text(html0)
    html = html0
html, n1 = re.subn(r'(<meta name="description" content=")[^"]*(")', lambda mm: mm.group(1) + desc + mm.group(2), html, count=1)
html, n2 = re.subn(r'("dateModified":")[^"]*(")', lambda mm: mm.group(1) + polls["compiled"] + mm.group(2), html, count=1)
assert n1 == 1 and n2 == 1, "metadata markers not found in index.html"
(HERE / "index.html").write_text(html)
print(f"polls.csv: {len(rows)} rows; prior-mayors.csv: {len(prow)} rows")
print("meta description:", desc)
print("If the headline or the three boxes changed, re-shoot the share image: ./share.sh")
