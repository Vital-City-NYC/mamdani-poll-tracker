# polls.json field spec

Each entry is one poll release. One release can carry several measures; keep them as separate `measures` entries so the chart never conflates them.

| field | type | notes |
|---|---|---|
| id | string | pollster-yyyymmdd, e.g. marist-20260318 |
| pollster | string | organisation that fielded it |
| sponsor | string or null | media partner or client |
| field_start, field_end | ISO date | |
| release_date | ISO date | |
| population | "adults" / "RV" / "LV" | |
| n | integer | sample size for the headline measure |
| moe | number or null | percentage points |
| mode | string | phone, online panel, text-to-web, mixed |
| measures | array | see below |
| issues | array | {topic, approve, disapprove, population} |
| splits | array | {dimension, group, measure_type, value} |
| url | string | primary source, fetched |
| quote | string | verbatim text carrying the headline numbers |
| confidence | HIGH / MEDIUM / LOW | HIGH = primary release fetched |

measures entry: `{type: "approval" | "performance" | "favorability", approve_or_positive, disapprove_or_negative, unsure, buckets: {excellent, good, fair, poor} or null, wording: "verbatim question if available"}`
