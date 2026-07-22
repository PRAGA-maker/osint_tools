---
id: usa-today-news
name: USA Today News
description: Use when you have a `name` and want US national or local news coverage — returns articles and obituaries naming people, relatives and dates.
url: https://www.usatoday.com
category: communities-forums
path:
- communities-forums
bestFor: Searching US national news (and its local network) for coverage of a named person or event.
selectorsIn:
- name
selectorsOut:
- name
- associate
- dob
status: live
pricing: freemium
costNote: Free to search and read some articles; a metered paywall/subscription covers much content and full archive access. Basic search is free.
opsec: passive
opsecNote: Reading and searching the site is passive and discloses nothing to any subject. Use a VPN to keep the query private; prefer reader/archive views over logging in for metered pieces.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major US national newspaper (Gannett), also the hub of a large local-paper network; edited reporting, generally reliable, though it is press coverage rather than a primary record.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- eu-usatoday-com
aliases:
- usatoday.com
- USA Today
tags:
- toddington
- curated-directory
- news-journalism
- obituaries
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# USA Today News

> A major US national daily and the front door to Gannett's large local-paper network — a broad news source for coverage, obituaries, and event mentions of a named person across the country.

## When to use
You have a `name` and want US press coverage: national news mentions, or — via Gannett's local-paper network and obituary partners — community-level coverage and obituaries that name relatives, dates, and hometowns. News (especially obituaries and local incident reporting) is a strong missing-persons resource, tying a person to family `associate`s, a `dob`/age, and a place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.usatoday.com and use the site search, or a site-scoped Google query: `site:usatoday.com "<name>"`.
2. Search the `name`; for obituaries, use the obituaries/legacy section (often a partner search) and the relevant local Gannett paper.
3. Read matches for identifying detail — dates, relatives, employer, location, event specifics.
4. Pivot: relatives named in an obituary feed people-search; dates/locations corroborate a timeline; a byline/topic confirms the right individual.

## Inputs → Outputs
- **In:** `name`
- **Out:** articles/obituaries — related `name`s/`associate`s, `dob`/age, dates, locale
- **Empty/negative result looks like:** no coverage — most people are never in the news; absence is expected. A paywall on an article is not the same as "no result."

## Gotchas & OpSec
- A **metered paywall** limits free reads and full-archive access; use reader/archive views or a library news database rather than assuming an article doesn't exist.
- National coverage is broad but shallow on any one person; the local Gannett papers carry the community-level detail — search those too.
- News is edited reporting, not a primary record; corroborate names/dates against official sources.
- OpSec: fully passive reading.

## Overlaps ("do both")
- Pair with the specific local paper for a subject's town and a dedicated obituary/newspaper-archive service — national search finds the big hits, local papers and archives find the person-specific coverage.

## Trust & verifiability
`trust: trusted` — an established mainstream newspaper with editorial standards; reliable as reporting, with the usual caveat that details should be confirmed against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usa-today-news |
| category | communities-forums |
| selectorsIn → selectorsOut | name → name, associate, dob |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
