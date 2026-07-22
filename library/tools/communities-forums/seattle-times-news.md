---
id: seattle-times-news
name: Seattle Times News
description: Use when you have a `name` and a Seattle/Pacific-Northwest tie and want news, obituary or local-event coverage — returns articles, obituaries and associated names/dates.
url: https://www.seattletimes.com
category: communities-forums
path:
- communities-forums
bestFor: Searching Seattle/Washington news and obituaries for a named person or local event.
selectorsIn:
- name
selectorsOut:
- name
- associate
- dob
status: live
pricing: freemium
costNote: Free to search and read some articles; a metered paywall/subscription covers much of the content. News search and obituaries are generally accessible.
opsec: passive
opsecNote: Reading the newspaper site is passive and discloses nothing to any subject. Use a VPN to keep the query private; prefer reader/archive views over logging in to read metered pieces.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major, long-established daily newspaper for Seattle and the Pacific Northwest; edited reporting that is generally reliable, though not a primary record.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- seattletimes.com
- The Seattle Times
tags:
- toddington
- curated-directory
- news-journalism
- obituaries
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Seattle Times News

> Seattle's major daily — a searchable source of Pacific-Northwest news, obituaries, and local-event coverage that can place a person in Washington with dates, relatives, and context.

## When to use
You have a `name` with a Seattle/Washington/Pacific-Northwest connection and want press coverage: obituaries (naming relatives, dates, and hometowns), local news mentions (courts, accidents, community, business), or historical context. Obituaries and local reporting are a strong missing-persons resource, tying a person to family `associate`s, a `dob`/age, and a locale.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.seattletimes.com and use the site search, or run a site-scoped Google query: `site:seattletimes.com "<name>"`.
2. Search the `name`; check the Obituaries section, which usually has its own search.
3. Read matches for identifying detail — dates, relatives, employer, neighbourhood, event specifics.
4. Pivot: relatives named in an obituary feed people-search; dates/locations corroborate a timeline; a byline/topic can confirm the right individual.

## Inputs → Outputs
- **In:** `name` (best with a Seattle/Washington context)
- **Out:** articles/obituaries — related `name`s/`associate`s, `dob`/age, dates, locale
- **Empty/negative result looks like:** no coverage — most people are never in the news; absence is expected. A paywall on an article is not the same as "no result."

## Gotchas & OpSec
- A **metered paywall** limits free reads; use archive/reader views or a library news database rather than assuming an article doesn't exist.
- Coverage is Seattle/Pacific-Northwest-centric — pair with other regional outlets for fuller local coverage.
- News is edited reporting, not a primary record; corroborate names/dates against official sources.
- OpSec: fully passive reading.

## Overlaps ("do both")
- Pair with other Washington/regional papers and a newspaper-archive service — different outlets cover different people/events, and archives reach coverage the live site has dropped.

## Trust & verifiability
`trust: trusted` — an established mainstream newspaper with editorial standards; reliable as reporting, though details should still be confirmed against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seattle-times-news |
| category | communities-forums |
| selectorsIn → selectorsOut | name → name, associate, dob |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
