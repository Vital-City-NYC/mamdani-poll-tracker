# Mamdani poll tracker — handoff

Started 2026-10-02. This file is the pickup point for whichever session continues the work.

## Where the live copy is (read this first)
On 2026-10-02 Josh split this project out of the chat that launched it (that chat also launched the "Who pays for NYC" explainer and keeps that one). The tracker now lives in the session that opens the worktree branch `claude/admiring-jennings-cf96be` (the Code-tab session named "admiring-jennings"). Its copy of this folder is canonical.

Main's copy of this folder (commits 6c673007 and the follow-up that added `data/prior-mayors.json`) is stale and will not be updated further. When this branch is merged into main, take this branch's version of every file in `mamdani-poll-tracker/`. The original chat's uncommitted `experiments-root` entry in main's `.claude/launch.json` is theirs; this session previews from its own `experiments-worktree` entry (python http.server on 8978, serving the worktree root) at http://localhost:8978/mamdani-poll-tracker/index.html.

Live at https://vitalcity-nyc.github.io/mamdani-poll-tracker/ from the repo vitalcity-nyc/mamdani-poll-tracker (the user account, which Josh chose on 2026-10-02 over the org). The repo holds this folder as its root; push by re-copying the folder into a clone (see `scripts` note below) or with the one-shot vitalcity-nyc token, never by `gh auth switch` while other sessions are live.

## The brief
"The Mamdani Poll Tracker: What New Yorkers think of the mayor." A permanent Vital City reference page: every reputable citywide poll since January 2026, with field dates, population, sample, approval/disapproval, performance ratings and favorability kept clearly distinct. One chart of the series over time. Updated with every new poll. Living data page, not commentary. Search case: 103,137 impressions YTD for "mamdani approval rating"; VC ranks ~10 with no matching article.

## Why comparability is the editorial problem
Marist (March 2026) measured job approval among adults (48%) and registered voters (49%). Suffolk (September 2026) asked registered voters to rate performance and got 57% excellent/good. Different questions on different populations; the page never puts them on one line. Three mark shapes (circle approve, square excellent+good, triangle favorable), hollow triangles for city subsamples of statewide polls, and a population filter.

## Josh's direction, in order received
1. Make as clean as possible without eliminating nuance. Add a filter to layer other mayors' performance at the same point in their first terms. All table numbers sans serif. (All done.)
2. Make all points on the chart yield hover-overs. (Done: HTML tooltip on every mark, including subsamples and prior-mayor points; tap works on touch.)
3. Be clear on hover whether a poll is of all adults, registered voters or likely voters, and be right. (Done: every tooltip, table row and stat tile spells the population out, read per measure from the data. Marist is adults and RV separately; Emerson and Suffolk RV; Honan LV; Siena RV through June then LV from August; Quinnipiac LV.)
4. Mix the city subsamples of statewide polls into the main table chronologically, with a slight marking or in grey. (Done: one table, subsample rows grey, pollster labelled "statewide", n "not published".)
5. The stats band was not well designed informationally; each box should show one of the three questions with its flip side inside the box, from the most recent poll that measured it. (Done: three boxes, latest citywide poll per question, negative and unsure inside, source line with pollster, dates, population and n. Registered voters preferred when a poll publishes both adults and RV. Favorability box also carries the latest city column of a statewide poll, labelled.)
6. Push account: vitalcity-nyc (user), confirmed by Josh 2026-10-02.

## Status, 2026-10-02 evening
- `data/polls.json`: 4 citywide polls (Marist Mar 26-31, Emerson/PIX11 Apr 5-6, Honan Jun 12-17 with no citywide topline, Suffolk Sep 1-3) plus 9 statewide entries of which 7 have a usable NYC column. All citywide entries HIGH from the pollsters' own releases. Siena February NYC column (63/25/12) verified today from Siena's own crosstabs, upgraded to HIGH. Siena March has no dates and April's NYC figure rests on the June release text (MEDIUM); Data for Progress is aggregator-only (LOW) and filtered out of the page.
- `data/prior-mayors.json`: 20 first-year readings (Adams 5, de Blasio 9, Bloomberg 5, Giuliani 1), compiled by the original chat's research agent with URL + quote per row, notes in `research/prior-mayors-notes.md`. Two independent re-verification agents run from this session confirmed every Adams and de Blasio number against the pollsters' pages (their files are in `research/prior-mayors/`). Bloomberg and Giuliani re-verification done the same evening: Quinnipiac rows matched; added CBS News/New York Times Bloomberg polls (June and August 2002, adults) from CBS's own pages, New York Times/WCBS-TV Giuliani polls (June 1994, adults; September-October 1994, a 495-person city subsample of a statewide poll) from Internet Archive copies of the Times' own articles, and field dates for Marist March 2002 from Marist's archived release. Now 24 readings (Adams 5, de Blasio 9, Bloomberg 7, Giuliani 3). The main session fetched and quoted every addition itself. Details at the end of `research/prior-mayors-notes.md`.
- Known weak rows in prior-mayors: Marist Bloomberg "March 2002" and Marist Giuliani "December 1994" come from Marist's 2022 trend table with no field dates (months assumed mid-month; tooltips say so); NYT/NY1/Siena April 2014 de Blasio has numbers from Siena's own December release but field dates and n from news coverage (MEDIUM; tooltip says so). Giuliani's Marist reading is at 11.4 months, past the chart's range until mid-December 2026; the page explains any out-of-range reading when a mayor is selected. The Times' Sept-Oct 1994 Giuliani figure is a city subsample of a statewide poll and the tooltip says so.
- `index.html`: Vital City card system, no wordmark. Headline and dek derived from the data. Chart draws at the container's pixel width (ResizeObserver), 0 to 100 axis, hover tooltips, population filter, previous-mayor select (circles and dotted line for approve/disapprove, squares for excellent/good, a caption that names what is drawn). One table, grouped rows per poll, grey subsample rows. `?embed=1` mode posts height for the Ghost iframe pattern.
- Bug fixed today: stat tiles showed field-end dates one day early (UTC parsing of bare ISO dates). All dates now parse at local noon.

## Oct 3 2026: the "think boldly" pass (Josh asked for aggressive improvement, no specifics)
Built and published:
- Headline leads with the margin, not the range: Marist's 49 and Emerson's 43 look like a disagreement, but approve minus disapprove is +18 and +16; the gap is how each handles the undecided. Falls back to the range form automatically if any poll shows net disapproval. Claims only "the citywide polls that asked".
- Dek counts the days since the last citywide approval topline (April 6).
- Chart is two-sided: each mark drops a stem to the negative answer in the same poll, with a toggle. Marks from one poll are dodged sideways so Marist's four readings separate.
- New section: approve-or-disapprove polls for the four predecessors within about five weeks of Mamdani's latest approval poll (months since inauguration), as stacked approve / unsure / disapprove bars with the margin. The window moves automatically when a newer approval poll is added.
- "details" button per citywide poll: verbatim wording, strength breakdown, mode, n, margin of error, release date, links to tables, issue ratings and results by group (party, borough, age, race, etc.). All from data already verified in polls.json.
- Search plumbing: title "Mamdani approval rating: every citywide poll, tracked", numeric meta description, schema.org Dataset JSON-LD, CSV downloads. `python3 build.py` regenerates `data/polls.csv`, `data/prior-mayors.csv` and the meta description / dateModified from the JSON. Run it after every data change, then `node --check`.
- Suffolk's Tisch item was mislabeled approve/disapprove; issues can now carry `positive_label` / `negative_label`.

Later the same day (Josh said "continue"): added `METHODOLOGY.md` (linked from the page footer to its GitHub-rendered copy), `ghost-embed.html` (the standard iframe + postMessage snippet, slug `mamdani-poll-tracker`), `share.html` + `share.sh` + `share.png` (1200x630 preview image shot with headless Chrome; wired as og:image), and static headline/dek stamping in `build.py` so crawlers see the finding without running the script.

Update checklist after a new poll: edit `data/polls.json` (primary URL + quote, set `compiled`), `python3 build.py`, `node --check` the script, preview, `./share.sh` if the headline or boxes changed, commit, publish.

Not built (need Josh's call): emailing Honan and Siena for the missing toplines and crosstabs; a "by borough across polls" view (kept inside each poll's details because the questions differ); the weekly poll-watch routine (a standing scheduled task; prompt drafted in `research/poll-watch-routine.md`, not created).

## Oct 5 2026: predecessor table re-anchored
Josh: spotlighting "three months in" felt wrong when the term is nine months old. The table now anchors on today's months-since-inauguration and shows each mayor's two most recent approve-or-disapprove polls as of that point (Mamdani's own two latest, however old, with the sub-line saying they date from month three). Do not anchor comparisons on the date of Mamdani's last poll again.

## Still to do
1. (Done Oct 3: `ghost-embed.html` exists.)
2. Update routine: a weekly scheduled task (sonnet tier) that searches for new citywide Mamdani polls and opens a draft row for Josh to approve; never publishes a poll unverified. Candidates to watch: Marist (NY1), Quinnipiac NYC (none since Oct 2025), Siena/NYT, Emerson/PIX11, Suffolk CityView, Manhattan Institute.
3. The Oct 1-2 New York Times piece on Mamdani's approval is still unchecked by a human (nytimes.com not fetchable). Josh should confirm it cites no poll missing here.
4. Optional: ask Honan Strategy Group for the full June topline; ask Siena for the March and April 2026 crosstabs so those two subsample rows can go HIGH.

## Rules that apply
- Never add a poll without a fetched primary URL and a verbatim quote (`feedback_external_data_rigor`, `feedback_research_anti_fabrication`).
- `node --check` the script before every preview (`feedback_syntax_check_pages`).
- Confirm the GitHub account before every push (`feedback_github_account`).
