---
id: athlinks
name: Athlinks
description: Use when you have a `name` and want a subject's endurance-race history — returns race results with dates, `geolocation`, finish times, and age, corroborating identity and whereabouts over time.
url: https://www.athlinks.com
category: search-engines
path:
- search-engines
bestFor: Searching the largest aggregated database of running, triathlon, cycling, and swimming race results by athlete name.
selectorsIn:
- name
selectorsOut:
- geolocation
- dob
- social-profile
status: live
pricing: free
costNote: Free to search results by name and view public race histories; a free account lets athletes claim/link their own results but is not needed to search.
opsec: passive
opsecNote: Searching returns public race data and does not notify the athlete. Reading is anonymous; only if you create an account and "claim" or message do you become attributable. Use a sock-puppet account if you need to interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregator of timing-company and event results; data is as accurate as the source race timing, but name collisions are common and self-claimed profiles are user-curated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- athlinks.com
tags:
- toddington
- specialty-search
- race-results
- endurance-sports
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Athlinks

> The definitive aggregated results database for endurance athletes — a name search returns years of race history with dates, places, and times.

## When to use
You have a subject's `name` (and ideally a rough age or region) and suspect they run, cycle, swim, or race triathlons. Athlinks aggregates results across event timing companies, so a single search can reconstruct where a person physically was on specific dates over many years — powerful for corroborating whereabouts, confirming a person is alive/active, narrowing age via age-group placings, and tying an alias to a real identity through a claimed athlete profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.athlinks.com/ and switch the search type to "Results" (next to the search bar).
2. Type the subject's `name`; results auto-suggest as you type.
3. Open a matching athlete/result: read event name, date, city/`geolocation`, distance, finish time, and age or age-group at the time of the race.
4. If the athlete has a claimed profile, note linked photos, gear, upcoming-event schedule, and the "rivals" list of frequently-co-competing athletes (potential associates).
5. Pivot: race locations + dates give a movement timeline; age-group placings narrow `dob`; a claimed profile and photos feed social and face OSINT.

## Inputs → Outputs
- **In:** `name`
- **Out:** `geolocation` (race cities/dates → movement timeline), `dob` (narrowed from age-group), `social-profile` (claimed athlete profile, photos, rivals/associates)
- **Empty/negative result looks like:** no results, or only same-name strangers in other regions — common for casual/non-racing subjects. Absence is not proof; many events are not indexed and results can be filed under a nickname or bib-only entry.

## Gotchas & OpSec
- Name collisions are frequent — disambiguate with age, city, and event type before attributing any result.
- A "claimed" profile is self-curated and can be padded or vanity-managed; raw timing results are the harder evidence.
- Passive to search; only account creation and interaction (claiming, messaging) make you attributable.

## Overlaps ("do both")
- Complements general people-search and social tools — Athlinks uniquely places a person at a specific location on a specific date, which name-only databases cannot, while those tools supply the current address/contact Athlinks does not.

## Trust & verifiability
`trust: community` — sourced from race-timing providers, so individual result rows are usually solid, but the aggregation layer and self-claimed profiles need corroboration. Cross-check a critical date/location against the original event's official results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | athlinks |
| category | search-engines |
| selectorsIn → selectorsOut | name → geolocation, dob, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
