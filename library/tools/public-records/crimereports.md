---
id: crimereports
name: CrimeReports (LexisNexis Community Crime Map)
description: Use when you have an `address`/`geolocation` and want to see recent reported crime incidents around it — returns block-level incident locations, types, and dates.
url: https://www.crimereports.com
category: public-records
path:
- public-records
bestFor: Mapping recent police-reported crime incidents around a location, block by block, from participating US agencies.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free public crime map; the CrimeReports brand is now LexisNexis Community Crime Map (communitycrimemap.com). No account needed to view.
opsec: passive
opsecNote: Viewing a public crime map is passive and reveals nothing about your interest in a specific person — you query a location, not a subject. Safe to use openly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Incident data is fed directly by participating law-enforcement agencies to LexisNexis and geocoded to block level; authoritative where an agency participates, blank where it does not.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- spotcrime
- nsopw
- crimereports-com
aliases:
- CrimeReports
- Community Crime Map
- communitycrimemap.com
tags:
- court
- inmate
- crime-map
- public-records
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# CrimeReports (LexisNexis Community Crime Map)

> A location-based public crime map: enter an address and see the reported incidents around it, block by block, from participating US police departments.

## When to use
You have an `address` or `geolocation` tied to a subject (last-known residence, a place they frequent, an incident location) and you want situational context — what crime has been reported nearby and when. It answers "what's happening around this location," which can corroborate a timeline, explain a police-report reference, or add area context to a case. It is not a person-search: you cannot look up an individual by name here.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.crimereports.com (now the LexisNexis **Community Crime Map**, communitycrimemap.com).
2. Enter the `address` or pan/zoom the map to the location of interest.
3. Filter by date range and crime type; the map plots incidents at block level with type, location-type, date, and time.
4. Read the incidents around your point — note dates that line up with your timeline.
5. Pivot: an incident near your subject's address/date can point you to a specific police report or agency (`document-id` to request via records channels); the area profile informs canvassing.

## Inputs → Outputs
- **In:** `address` or `geolocation`.
- **Out:** nearby reported crime incidents — block-level `geolocation`/`address`, crime type, and date/time.
- **Empty/negative result looks like:** an empty map for an area — usually the local agency does not share data with the platform, not that the area is crime-free. Coverage is entirely dependent on agency participation.

## Gotchas & OpSec
- Not a name search — you cannot look up a person or arrest record here; it is incident-by-location only. (The stub's name/DOB framing is inaccurate.)
- Coverage is patchy: only participating US agencies feed data, and addresses are deliberately shown at block (not exact) level.
- Incident feeds can lag and categorizations vary by department; treat as context, not a definitive record.

## Overlaps ("do both")
- Pairs with `[[spotcrime]]` — SpotCrime aggregates a different (overlapping) set of agencies, so an area blank on one may have data on the other; check both. For offender lookups by name, use `[[nsopw]]` instead.

## Trust & verifiability
`trust: trusted` — data comes straight from participating law-enforcement agencies via LexisNexis and is geocoded to block level. It is authoritative where an agency participates and simply absent where one doesn't; never read a blank map as "no crime."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crimereports |
| category | public-records |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
