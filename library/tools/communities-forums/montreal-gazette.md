---
id: montreal-gazette
name: Montreal Gazette
description: Use when you have a `name` and a Montreal/Quebec tie and want news, obituary or local-event coverage — returns articles, obituaries and associated names/dates.
url: https://montrealgazette.com
category: communities-forums
path:
- communities-forums
bestFor: Searching Montreal/Quebec news and obituaries for a named person or local event.
selectorsIn:
- name
selectorsOut:
- name
- associate
- dob
status: live
pricing: freemium
costNote: Free to search and read many articles; some content sits behind a metered paywall/subscription. Obituaries and news search are generally accessible.
opsec: passive
opsecNote: Reading the newspaper site is passive and discloses nothing to any subject. Use a VPN if you want the query private; consider reader/archive views to bypass metering rather than logging in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major, long-established English-language daily newspaper for Montreal (Postmedia); reporting is edited and generally reliable, though not a primary record.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- montrealgazette.com
- The Gazette (Montreal)
tags:
- toddington
- curated-directory
- news-journalism
- obituaries
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Montreal Gazette

> Montreal's major English-language daily — a searchable source of local news, obituaries, and event coverage that can place a person in Quebec with dates, relatives, and context.

## When to use
You have a `name` with a Montreal/Quebec connection and want press coverage: obituaries (which name relatives, dates, and hometowns), local news mentions (accidents, courts, community events, business), or historical context. Newspapers are a strong missing-persons resource — obituaries in particular link a person to family `associate`s, a `dob`/age, and a locale.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://montrealgazette.com and use the site search, or run a site-scoped Google query: `site:montrealgazette.com "<name>"`.
2. Search the `name`; check the Obituaries/Remembering section separately, which often has its own search.
3. Read matches for identifying detail — dates, relatives, employer, neighbourhood, event specifics.
4. Pivot: relatives named in an obituary feed people-search; dates/locations corroborate a timeline; a byline/topic can confirm the right individual.

## Inputs → Outputs
- **In:** `name` (best with a Montreal/Quebec context)
- **Out:** articles/obituaries — related `name`s/`associate`s, `dob`/age, dates, locale
- **Empty/negative result looks like:** no coverage — most people are never in the news; absence is expected and not meaningful. Metered articles may show a paywall rather than a true "no result."

## Gotchas & OpSec
- A **metered paywall** limits free reads; use archive/reader views or a library database rather than assuming an article doesn't exist.
- Coverage is Montreal/Quebec-centric and English-language — pair with French-language Quebec papers for fuller local coverage.
- News is edited reporting, not a primary record; corroborate names/dates against official sources.
- OpSec: fully passive reading.

## Overlaps ("do both")
- Pair with French-language Quebec outlets and a newspaper-archive service — different papers cover different people/events, and archives reach coverage the live site has dropped.

## Trust & verifiability
`trust: trusted` — an established mainstream newspaper with editorial standards; reliable as reporting, though details should still be confirmed against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | montreal-gazette |
| category | communities-forums |
| selectorsIn → selectorsOut | name → name, associate, dob |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
