---
id: ads-b-nl
name: ADS-B.NL
description: Use when you have an aircraft registration or callsign and want to track its movements — returns flight traces and movement history, with a focus on European and military aircraft.
url: https://www.ads-b.nl/index.php?pageno=9999
category: transportation
path:
- transportation
- air-traffic-records
bestFor: Monitoring aircraft movements over Europe — notably military and government flights — from publicly broadcast ADS-B data.
selectorsIn:
- vehicle-plate
status: live
pricing: free
costNote: Free, read-only community ADS-B monitoring site; no account required.
opsec: passive
opsecNote: The data is aircraft-broadcast ADS-B aggregated by volunteers; viewing it is passive and reveals nothing about you or any person on the ground.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A volunteer/community ADS-B aggregator; coverage depends on receiver placement, so tracks can be incomplete, especially for aircraft that switch off or spoof transponders.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- ads-b.nl
tags:
- aircraft
- flight-tracking
- ads-b
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# ADS-B.NL

> A Dutch community flight-tracking site that aggregates publicly broadcast ADS-B signals, with particular strength for European military and government aircraft that mainstream trackers may filter out.

## When to use
Your case involves a specific aircraft — a tail number seen in a photo, mentioned in a document, or tied to an entity — and you want its movement history or to monitor it. ADS-B.NL is useful when the aircraft is European or military/government, categories that public trackers like FlightRadar24 sometimes hide but that appear here. Aircraft-tracking rarely locates a missing person directly, hence low MP relevance; it's asset/movement intelligence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ads-b.nl/ and use its aircraft/registration and live-map views.
2. Search or filter by aircraft registration (tail number) or military callsign.
3. Read the flight trace: route, altitude, timestamps, and movement history where captured.
4. Note the aircraft type/classification context the site provides (civil vs military/government).
5. Correlate the timeline against your case (was the aircraft where/when a document claims?).
6. Pivot: registration → aircraft-ownership registries; route/airports → ground-side inquiries; recurring routes → pattern-of-life for the asset.

## Inputs → Outputs
- **In:** aircraft registration/tail number or military callsign (recorded here as `vehicle-plate`)
- **Out:** flight traces, movement history, and aircraft classification context
- **Empty/negative result looks like:** no track for the aircraft — it may be outside receiver coverage, have its transponder off, or be broadcasting a filtered/anonymous code. Absence of a track is not proof the aircraft didn't fly.

## Gotchas & OpSec
- Coverage is receiver-dependent (volunteer network), best over the Netherlands/Europe and patchy elsewhere; gaps are normal.
- Military/sensitive aircraft may transmit blocked, spoofed, or intermittent signals — treat identifications cautiously.
- Not a person-locator; it tracks aircraft, and linking an aircraft to a specific individual requires separate ownership/charter research.
- OpSec: fully passive.

## Overlaps ("do both")
- Complements mainstream flight trackers — ADS-B.NL surfaces European/military traffic others filter, so cross-check a tail number across multiple ADS-B sources for the fullest picture.

## Trust & verifiability
`trust: community` — a volunteer ADS-B aggregator; the underlying transponder data is real but coverage is incomplete, so confirm critical tracks against a second ADS-B source and note capture gaps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ads-b-nl |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
