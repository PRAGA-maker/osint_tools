---
id: radio-locator
name: Radio-Locator
description: Use when you have a `geolocation`/`address` (or a station's call letters) and want the local AM/FM stations, formats and coverage there — returns nearby stations and broadcast geography.
url: https://radio-locator.com/
category: geolocation
path:
- geolocation
bestFor: Finding which radio stations cover a location, or mapping a station's broadcast area.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to search stations, formats and coverage; some detailed engineering/coverage maps may be gated behind paid/pro features.
opsec: passive
opsecNote: Passive — you browse a public broadcast directory; no subject is involved. It's a reference database, not a query about any person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established, widely-cited AM/FM directory (17,000+ station links, 12,000+ streams); US/Canada coverage is strongest.
missingPersonsRelevance: low
coverage:
- us
- ca
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- radio-locator.com
- Radio Locator
tags:
- radio
- broadcast
- geolocation
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Radio-Locator

> A long-running AM/FM radio directory: find stations covering a location by zip/city, look up call letters, and see broadcast coverage.

## When to use
You have a `geolocation`/`address` and want to know which radio stations serve it — for example to identify a station heard in the background of a video/call, to find local media covering an area during a search, or to bound where a received signal could originate using coverage maps. You can also start from a station's call letters and work back to its location/format.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://radio-locator.com/.
2. Search by US city/zip, by call letters, by format (news, sports, a music genre), or by state/province/country.
3. Open a station's entry for its call sign, frequency, format, city of licence and coverage information.
4. Use coverage/geography to match a heard station to an area, or to list media outlets for a location.
5. Pivot: a local station → its news desk/social feeds for area coverage; a coverage map → narrows a signal's likely origin.

## Inputs → Outputs
- **In:** `geolocation`/`address` (or call letters/format)
- **Out:** `geolocation` context — nearby stations, frequencies, formats, city of licence, coverage
- **Empty/negative result looks like:** thin listings outside the US/Canada, or no station matching a partial call sign — coverage is strongest in North America.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; it's a reference directory.
- Some detailed engineering/coverage features may require paid access; the core search is free. Coverage maps are predictive, not a guarantee of reception at a specific address.

## Overlaps ("do both")
- Pairs with mapping tools like `[[quick-geolocation-search]]` — Radio-Locator identifies the station/area, then map the transmitter/coverage geography for a location argument.

## Trust & verifiability
`trust: community` — an established, widely-cited directory; station facts are reliable for the US/Canada, but treat coverage maps as engineering predictions and confirm licensing details against the regulator (FCC/ISED) when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radio-locator |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
