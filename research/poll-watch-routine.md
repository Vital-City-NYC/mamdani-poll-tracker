# Weekly poll-watch routine (drafted, not scheduled)

Proposed scheduled task. Not created yet: it is a standing task, so it waits for Josh's yes.

- Cadence: weekly, Monday 8 a.m. Eastern.
- Model tier: sonnet (per the routine model tiers note).
- Output: a Slack self-DM to Josh only. It never edits the data files and never publishes.

## Prompt

Look for new public polls of New York City Mayor Zohran Mamdani released in the last 10 days. Check the pollsters' own sites first: maristpoll.marist.edu, poll.qu.edu (New York City and New York State releases), sri.siena.edu, emersoncollegepolling.com, suffolk.edu/academics/research-at-suffolk/political-research-center (CityView), manhattan.institute, honanstrategy.com. Then run two web searches: "Mamdani approval poll" and "Mamdani job approval New York City poll" restricted to the last two weeks.

Compare what you find against the polls already in https://vitalcity-nyc.github.io/mamdani-poll-tracker/data/polls.json (match on pollster and field dates).

For each poll not already listed, fetch the pollster's own release and report: pollster and sponsor, field dates, who was surveyed (all adults, registered voters or likely voters), sample size, margin of error, the question type (job approval, performance grade or favorability), the positive, negative and unsure figures, the exact URL, and one verbatim sentence from the release that contains the headline numbers. Say whether it is a citywide poll or a New York City column of a statewide poll. If you could only find news coverage and not the pollster's release, say so and do not report the numbers as verified.

If nothing new was found, say "No new Mamdani polls this week" and list the sites checked. Never invent a poll, a number or a URL.

Send the result as a Slack direct message to Josh himself and to no one else.
