---
id: fatal-encounters
name: Fatal Encounters
description: Use when you have a `name`, `geolocation`, or date and need to check whether a person died during a police interaction in the US since 2000 — returns identity, location, date, and cause as a possible case resolution.
url: https://fatalencounters.org/people-search/
category: public-records
path:
- public-records
bestFor: Searching a national US database of people killed during interactions with police (since 1 Jan 2000) by name, place, date, or demographics — a potential fate-resolution source for a missing person.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- dob
- address
status: live
pricing: free
costNote: Free to search and to download the full dataset; the project runs on donations.
opsec: passive
opsecNote: Searching a public, static database reveals nothing to anyone and touches no live target. Handle any match with care — these are records of deaths; corroborate before informing anyone or drawing conclusions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A respected, long-running crowd-/journalist-sourced dataset compiled from public records and news; broad but, being volunteer-compiled, may have gaps or errors — verify a hit against primary records.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- the-charley-project
- namus
aliases:
- FatalEncounters.org
tags:
- deaths
- public-records
- police
- missing-persons
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Fatal Encounters

> A searchable national database of people who died during interactions with US police since 2000 — a place to check whether a missing person's disappearance ended in an unidentified or unlinked death.

## When to use
A grim but important line of inquiry in US missing-persons work: when someone vanished, one possible fate is death during a police encounter that was never connected back to the missing-person report. Search here by `name`, `geolocation` (city/county/state), date range, or demographics (race/age/gender) to check for a matching record. A hit can resolve a case or open a records trail; the dataset is also downloadable for bulk cross-referencing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://fatalencounters.org/people-search/.
2. Search across the available fields — first/last `name` separately, location (city/county/state), year/date of injury, cause, agency, and demographics.
3. Review candidate records: name, age, race, gender, date, location, cause of death, and involved agency.
4. For a plausible match, verify against primary sources (medical examiner, court, news) — the data is volunteer-compiled.
5. Pivot: a confirmed identity/date/place → `[[namus]]` and death-index/records tools; an unresolved-but-plausible match → local ME/coroner records.

## Inputs → Outputs
- **In:** `name`, `geolocation`, date range, or demographics
- **Out:** matching death records — `name`, age/`dob` indicators, `address`/location, date, cause, agency
- **Empty/negative result looks like:** no matching record — the person isn't in this dataset (which is US-only, since 2000, and volunteer-compiled). A miss is not proof of anything; it's one database among several.

## Gotchas & OpSec
- **US-only, 2000-onward, volunteer-compiled** — expect gaps and occasional errors; always verify a match against primary records.
- Emotionally and legally sensitive data — corroborate rigorously before communicating any conclusion to families or investigators.
- Passive; nothing is disclosed by searching.

## Overlaps ("do both")
- Pairs with `[[namus]]` and `[[the-charley-project]]` — those catalogue missing and unidentified persons directly; Fatal Encounters adds the specific police-interaction-death angle. Cross-check a candidate across all three.

## Trust & verifiability
`trust: community` — a well-regarded, transparent dataset built from public records and journalism, but volunteer-maintained. Treat a match as a strong lead to be confirmed against primary sources, not as proof on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fatal-encounters |
| category | public-records |
| selectorsIn → selectorsOut | name, geolocation → name, dob, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
