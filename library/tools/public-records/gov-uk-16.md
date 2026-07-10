---
id: gov-uk-16
name: gov.uk (Check for Flooding)
description: Use when you have an `address`/postcode in England and want its flood risk and live water levels — returns flood alerts, 5-day forecast, long-term risk and nearby river/sea gauge readings.
url: https://check-for-flooding.service.gov.uk/
category: public-records
path:
- public-records
bestFor: Adding environmental/geographic context (flood risk, live water levels) to an English address or area.
selectorsIn:
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free official UK government (Environment Agency) service; no account or payment.
opsec: passive
opsecNote: A public government mapping service — you query a location, not a person, and nothing is logged against any subject. No sock puppet strictly needed, though routine browser hygiene is sensible. It reveals nothing about who lives at an address; it is purely environmental.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the UK Environment Agency via gov.uk — an authoritative first-party source for England flood data (does not cover Scotland/Wales/NI, which have their own agencies).
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Check for flooding
- Environment Agency flood service
tags:
- propertysites
- Property Related Sites
- flood
- environment-agency
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# gov.uk (Check for Flooding)

> The Environment Agency's flood service — enter an English town, postcode or address and see its flood risk, live alerts and nearby water levels. Geography/property context, not people.

## When to use
You have an `address` or area in England and want environmental context around it: is it in a flood-risk zone, are there active flood warnings, what are the live river/sea/rainfall levels nearby? Useful as supporting geographic intelligence — e.g. corroborating that an area was flooded on a given date, or understanding the physical setting of a location tied to a case. It does **not** tell you who lives there.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://check-for-flooding.service.gov.uk/.
2. Search a town, city, postcode or address in England.
3. Read the three layers:
   - **Current alerts/warnings** for that location.
   - **5-day flood forecast** (risk level).
   - **Long-term risk** from rivers, sea, surface water and groundwater (separate linked tool).
4. Open nearby measuring stations for live river, sea, groundwater and rainfall readings.
5. Pivot: combine the location/`geolocation` context with property records and mapping; use live-level history to corroborate flooding on a specific date.

## Inputs → Outputs
- **In:** `address` / postcode / place name (England)
- **Out:** flood alerts, forecast and long-term risk for the location, plus nearby gauge `geolocation` readings
- **Empty/negative result looks like:** "no flood alerts or warnings" and a "very low" risk — the area is not currently at risk; it is not an error. Locations outside England return no data (wrong agency).

## Gotchas & OpSec
- **England only.** Scotland (SEPA), Wales (Natural Resources Wales) and Northern Ireland have separate services; this returns nothing for them.
- It is environmental data — do not expect any person, occupant, or ownership information. Low direct people-OSINT value; it is context, not attribution.
- OpSec: **passive**, first-party government mapping; nothing about a subject is disclosed.

## Overlaps ("do both")
- Pairs with property/land-registry and mapping tools — this supplies flood/environment context for an address, while those supply ownership and the built environment. Combine for a full picture of a location.

## Trust & verifiability
`trust: trusted` — the official UK Environment Agency service on gov.uk; the flood and gauge data are authoritative for England.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-16 |
| category | public-records |
| selectorsIn → selectorsOut | address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
