# Giuliani, first 12 months (Jan–Dec 1994): job-approval polls from primary pages

Compiled Oct 2, 2026. Citywide polls only, read from the pollster's own page. Internet Archive copies are marked as such.

## Verified

### 1. New York Times/WCBS-TV News Poll, June 12–15, 1994 (adults, n=1,189): approve 49, disapprove 31

- URL fetched (Internet Archive, 2015 capture of the Times' own article): https://web.archive.org/web/20150526104703/http://www.nytimes.com/1994/06/21/nyregion/poll-shows-support-for-giuliani-on-not-cutting-police-budget.html
- Original: https://www.nytimes.com/1994/06/21/nyregion/poll-shows-support-for-giuliani-on-not-cutting-police-budget.html (direct fetch returned HTTP 403)
- Quote: "The poll, which was taken June 12 to 15 amid last week's euphoria of a hometown hockey championship but well before the city begins feeling the impact of Mr. Giuliani's budget cuts, found that 49 percent of the 1,189 people questioned said they approved of Mr. Giuliani's job performance while 31 percent disapproved. The margin of sampling error for all respondents was plus or minus 3 percentage points."
- Population: "The latest poll represented a cross section of all New Yorkers, not just voters."
- Unsure (20) is derived, not stated.
- ICPSR catalogues the dataset as "CBS News/New York Times New York City Poll, June 1994" (study 6598); the Times credits WCBS-TV News.

### 2. New York Times/WCBS-TV News Poll, Sept 29–Oct 2, 1994 (adults, n=495 city residents): approve 61, disapprove not stated

- URL fetched (Internet Archive, 2015 capture): https://web.archive.org/web/20150526102225/http://www.nytimes.com/1994/10/07/nyregion/the-1994-campaign-poll-giuliani-s-approval-rating-rises-to-61.html
- Original: https://www.nytimes.com/1994/10/07/nyregion/the-1994-campaign-poll-giuliani-s-approval-rating-rises-to-61.html
- Quote: "The poll, taken between Sept. 29 and Oct. 2 with 495 city residents participating, shows that the Mayor's approval rating has shot upward in the last three months, increasing to 61 percent from 49 percent in June."
- Also: "The poll had a margin of sampling error of plus or minus 4 percentage points among city residents and 3 percentage points among registered voters statewide."
- City residents were a subsample of a statewide poll. No disapprove or undecided figure anywhere in the article.

### 3. Marist Institute for Public Opinion, December 1994 (registered voters, n unknown): excellent 12, good 39, fair 31, poor 13, unsure 5 → excellent+good 51, fair+poor 44

- Type: performance (grade question), not approve/disapprove.
- URL fetched (Internet Archive copy of Marist's Oct 13, 1999 release, which carries the trend table from December 1994 on): https://web.archive.org/web/20010308020000/http://www.maristpoll.marist.edu:80/nycpolls/991013MY.html
- Quote: "Question Wording : Would you rate the job Mayor Rudolph Giuliani is doing in office as excellent, good, fair, or poor? Registered Voters … December 1994 12% 39% 31% 13% 5%"
- Corroborated directly on maristpoll.marist.edu (March 2022 NYC tables, p. 4, table NYC005TRND): https://maristpoll.marist.edu/wp-content/uploads/2022/03/Marist-Poll_NYC-NOS-and-Tables_202203091244.pdf
- Quote: "NYC005TRND. Marist Poll New York City Trend / NYC Registered Voters … Rudolph Giuliani December 1994 51% 44% 12% 39% 31% 13% 5%"
- Marist's series starts with this reading; no earlier Marist Giuliani job rating exists. Exact field dates, sample size and sponsor (WNBC or Daily News) are not in either document.

## Quinnipiac in 1994: polled, but no job-approval question found

Quinnipiac's own trend archive as captured Aug 26, 2000 (https://web.archive.org/web/20000826212400/http://www.quinnipiac.edu:80/polls/archives.html) shows NYC releases dated June 22, July 21 and December 20, 1994. Note at top of the NYC section: "Polls released on or before February 15, 1996, were conducted among a random sampling of New York City adults."

- Favorability, "Is your opinion of Mayor Rudolph Giuliani favorable, unfavorable, mixed, or haven't you heard enough about him?": June 22, 1994: 52 / 20 / 22 / 4 / 2 (ref). July 21, 1994: 53 / 21 / 20 / 5 / 2.
- Issue approvals, June 22, 1994: crime 59–32–9; education 36–44–20; budget deficit 44–40–16; race relations 53–35–13.
- The overall "Do you approve or disapprove of the way Rudolph Giuliani is handling his job as Mayor?" table begins Feb 11, 1997 (race breakdown version begins June 15, 1995). Quinnipiac's Nov 19, 1996 and April 21, 1996 releases cite back only to November 1995 (44–46).
- Quinnipiac's current legacy database (poll.qu.edu/Poll-Release-Legacy?releaseid=N, scanned N=1..1299) begins in 1997. The Oct 29, 1997 release says: "When the independent Quinnipiac College Poll first asked this question in December, 1994, only 37 percent of New Yorkers were satisfied" (satisfaction with life in the city, not approval). Only pre-1997 NYC PDF on poll.qu.edu: nyc04211996_re-released12052013.pdf.

These favorability readings are recorded in giuliani.json under other_measures, not polls.

## Unverified

- Marist December 1994 original release: field dates, n, sponsor. Not online; Internet Archive has no Marist pages before 1999.
- Quinnipiac 1994 overall job approval: no evidence it was asked; no 1994 release online.
- ICPSR 6598 codebook: icpsr.umich.edu, pcms.icpsr.umich.edu blocked by Cloudflare for WebFetch, curl and the browser pane.
- Daily News / Newsday / WNBC polls in 1994: secondhand mentions only (City & State, Wikipedia); not used.
- NYT/WCBS first-anniversary poll, Jan 1995: sitemap sweep (Jan 1, 1994–Jan 31, 1995) found none with "poll" or "survey" in the slug.

## How the pages were found

- WebSearch (about 20 queries, standard and extended) surfaced no 1994 primary page; results were ICPSR catalogue entries, Quinnipiac 1997+ releases and secondhand coverage.
- nytimes.com/sitemap/YYYY/MM/DD/ pages are fetchable by curl and list every article URL for a day; swept all of 1994 plus Jan 1995 for nyregion slugs containing "poll" or "survey". Article pages themselves return 403, so each was read from the Internet Archive (archive.org/wayback/available, then web.archive.org/web/<ts>id_/<url>).
- Wayback CDX API (web.archive.org/cdx/search/cdx) located the 1996–2002 quinnipiac.edu/polls and 1999–2005 maristpoll.marist.edu/nycpolls pages. Wildcard CDX queries on nytimes.com are refused ("requires authorization"); exact-URL lookups work.
- Fetch tally: roughly 15 WebFetch calls, several dozen curl requests, one browser-pane attempt (nytimes.com blocked by policy, icpsr.umich.edu blocked by Cloudflare).
