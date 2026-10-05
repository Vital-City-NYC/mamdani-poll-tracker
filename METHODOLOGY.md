# Mamdani poll tracker: methodology

Live page: https://vitalcity-nyc.github.io/mamdani-poll-tracker/

This file explains where every number on the page comes from, what is included and excluded, and every calculation the page performs. Nothing is estimated, averaged or modeled.

## What the page tracks

Public opinion of New York City Mayor Zohran Mamdani since he took office on January 1, 2026, in polls of the city. Three kinds of question appear and are never combined:

- **Job approval.** "Do you approve or disapprove of the job Zohran Mamdani is doing as mayor?" The positive figure is approve and the negative is disapprove.
- **Performance rating.** A grade of excellent, good, fair or poor. The positive figure is excellent plus good and the negative is fair plus poor, following the pollster's own grouping. Fair is not disapproval, so these numbers are not comparable with job approval.
- **Favorability.** An opinion of the person rather than the job. The positive figure is favorable and the negative is unfavorable.

## Sources

Every figure is read from the pollster's own release, tables or crosstabs. Each row on the page links to that document. The files:

- `data/polls.json`: the citywide polls and the statewide polls with a New York City column. Each entry carries the source link, a verbatim quote containing the headline numbers, the exact question wording where published, field dates, who was surveyed, sample size, margin of error and mode.
- `data/prior-mayors.json`: first-year polls of Eric Adams (2022), Bill de Blasio (2014), Michael Bloomberg (2002) and Rudolph Giuliani (1994), each with a source link and verbatim quote.
- `research/polls-notes.md` and `research/prior-mayors-notes.md`: the quotes and reading notes for each entry.
- `research/gaps.md`: polls that were reported somewhere but could not be verified, and pollsters checked with nothing found.

Citywide polls of Mamdani: Marist (March 26 to 31, 2026), Emerson College for PIX11 (April 5 to 6), Honan Strategy Group (June 12 to 17) and Suffolk University (September 1 to 3).

Statewide polls with a city column: Siena (January, February, April, June, August and September 2026) and Quinnipiac (September 2026).

Previous mayors: Quinnipiac University; Marist; Siena for The New York Times and NY1 (2014) and for NY1 (2022); CBS News and The New York Times (2002), from CBS's own published write-ups; The New York Times and WCBS-TV (1994), from Internet Archive copies of the Times' own articles.

## What is included and excluded

Included: polls by a named polling organization that publishes field dates, sample size and question wording.

Excluded:

- Campaign or interest-group polls released without crosstabs, and straw polls.
- Polls of a single congressional district or a primary electorate.
- Any poll whose numbers could be found only in news coverage or on an aggregator. One Data for Progress statewide poll (May 2026) is held in the data file at low confidence for this reason and is filtered off the page.
- Siena's March 2026 statewide poll, because its release and field dates could not be fetched.

Honan Strategy Group published approval among Jewish and non-Jewish likely voters but no figure for all respondents. The page reports the two figures it published and does not calculate a combined one, because the weighted share of each group was not published.

## City columns of statewide polls

Siena and Quinnipiac survey New York State and publish a column for New York City respondents. The size of that city sample is not published, so the error is wider than in a citywide poll and unknown. These readings are drawn as hollow triangles, shown in grey in the table and never counted among the citywide polls. Two of them rest on weaker sourcing: Siena's April 2026 city figure comes from the text of Siena's June release rather than from the April crosstabs.

## Who was surveyed

Each reading is labeled all adults, registered voters or likely voters, as the pollster describes its sample. Marist published both all adults and registered voters from one survey; both appear. Where a single figure is needed (the three boxes at the top), the page uses registered voters when a poll published both, so the boxes share a population.

## Calculations

- **Position on the chart.** Each mark sits at the midpoint of the poll's field dates.
- **Margin.** Positive minus negative, in percentage points, from the same poll and the same population. The headline states the range of margins across citywide job-approval readings. If any reading showed more disapproval than approval, the headline would instead state the ranges of approve and disapprove.
- **Days since the last approval poll.** Today's date minus the last field date of the most recent citywide poll that published a job-approval figure.
- **Latest poll per question.** For each of the three question types, the citywide poll with the latest field midpoint.
- **Months since inauguration.** For previous mayors, the midpoint of the field dates minus January 1 of the inauguration year, in days divided by 30.4375. A previous mayor's poll is drawn at the same number of months after January 1, 2026.
- **The predecessor comparison.** The table is anchored on today. It takes the number of months since January 1, 2026, and shows each previous mayor's two most recent approve-or-disapprove polls fielded by that same number of months into his own first term (with a tolerance of a quarter of a month). Mamdani's rows are his two most recent citywide polls that published a job-approval figure, however old they are; the months-in column shows the age of every reading. Excellent-or-good grades are left out of that table. When a mayor has no poll by that point, his first reading is stated in words.
- **Rounding.** Figures are shown as the pollster published them. Suffolk's unrounded results give 56.6 percent excellent or good; Suffolk's release rounds this to 57 and the page follows the release.

## Known limitations

- Polls differ in mode, weighting and wording. Emerson offers "neutral or no opinion" as an answer, which lowers both approve and disapprove compared with a poll where unsure must be volunteered. The margin between approve and disapprove is less sensitive to this than either figure alone.
- There are few polls. As of October 2026 only two citywide polls had published a job-approval figure, a week apart.
- Previous mayors' polls come from different pollsters and populations than Mamdani's. The like-for-like pairs are Marist among all adults (Adams 2022 and Mamdani 2026) and registered voters with registered voters.
- Three previous-mayor readings have incomplete details. Marist's December 1994 reading for Giuliani comes from a later Marist trend table with no field dates or sample size, and is placed at mid-December. The Times and WCBS-TV's reading of September 29 to October 2, 1994 is 495 city residents within a statewide poll, and the article gives no disapprove figure. The Times, NY1 and Siena poll of March 29 to April 3, 2014 has its figures confirmed in a later Siena release, but its field dates and sample size come from news coverage.
- The New York Times' site could not be fetched during research. Any poll reported only there may be missing.

## Updating

A poll is added only after its primary release has been fetched and a verbatim quote recorded. After any change to the data files, run `python3 build.py`, which regenerates the downloadable CSV files and the page's search description from the data.
