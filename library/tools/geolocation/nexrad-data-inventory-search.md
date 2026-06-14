---
id: nexrad-data-inventory-search
name: NEXRAD Data Inventory Search
description: Use when you need to prove or check the weather at a US place and time — pull archived NWS Doppler radar for chronolocation and timeline corroboration.
url: https://www.ncdc.noaa.gov/nexradinv/
category: geolocation
path:
- geolocation
bestFor: Finding archived US NEXRAD weather-radar coverage for a station/date to corroborate weather seen in photos or claimed in statements.
selectorsIn:
- geolocation
- metadata-exif
selectorsOut:
- metadata-exif
status: degraded
pricing: free
costNote: US government (NOAA/NCEI) public archive; free. Bulk downloads are also free via NOAA's open data on AWS/Google.
opsec: passive
opsecNote: Querying a public government weather archive reveals nothing to the subject; you search by station and date, not by person.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party NOAA/National Centers for Environmental Information archive — authoritative US weather-radar data of record.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- NEXRAD Inventory
- NCEI Radar Inventory
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# NEXRAD Data Inventory Search

> NOAA's inventory/search for archived US NEXRAD Doppler weather-radar data — the authoritative way to check what the weather actually was at a place and time.

## When to use
You have a US `geolocation` and a candidate date/time (often from `metadata-exif` or a witness statement) and need to corroborate or refute weather conditions — rain, snow, storms visible in a photo, or a claimed clear/stormy day. Useful as an independent timeline check in chronolocation: weather that matches narrows confidence; weather that contradicts breaks an alibi or timestamp. Not a person-finder, hence medium MP relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the NCEI radar inventory and identify the nearest WSR-88D station to your coordinates (each station has a 4-letter ID, e.g., KOKX).
2. Select the station and the date range; query the inventory for available Level II/III products.
3. Review or download the archived scans; visualize via NOAA's Weather and Climate Toolkit if needed.
4. Compare radar-indicated precipitation/storms to the photo or statement. Pivot timestamps back to image/EXIF analysis and to sun/moon chronolocation tools.

## Inputs → Outputs
- **In:** `geolocation` (to pick the station) + date/time (`metadata-exif` or claim).
- **Out:** archived radar coverage as corroborating `metadata-exif`-class evidence (verified weather context for that time/place).
- **Empty/negative result looks like:** no archived scans for that station/interval (gap or outage), or the nearest station too far to be conclusive.

## Gotchas & OpSec
- The legacy ncdc.noaa.gov/nexradinv interface is dated and may redirect/be flaky; modern access is via NCEI's archive and the NEXRAD open-data buckets (AWS/Google). Treat the URL as a starting point.
- You must reduce raw radar to a human-readable picture (use NOAA WCT) — that is the manual-review step.
- Times are UTC; convert carefully to local for comparison.
- OpSec: fully passive; no subject contact.

## Overlaps ("do both")
- Pairs with sun/moon chronolocation (e.g., [[mooncalc]]) — combine celestial geometry and weather for stronger time/place confirmation.

## Trust & verifiability
`trust: trusted` — first-party NOAA data of record; results are reproducible and court-grade. Status set to degraded because the specific legacy URL is unreliable even though the underlying archive is fully live.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nexrad-data-inventory-search |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, metadata-exif → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
