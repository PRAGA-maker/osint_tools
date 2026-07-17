---
id: ship-ais
name: Ship AIS
description: Use when you have a vessel name or MMSI (or a UK waterway of interest) and want its live position — returns current location, track, and vessel details from public AIS.
url: https://shipais.uk/
category: transportation
path:
- transportation
- marine-records
bestFor: Live-tracking vessels in and around UK waters by name/MMSI using community-received AIS.
selectorsIn:
- name
- document-id
selectorsOut:
- geolocation
- name
status: live
pricing: free
costNote: Free community AIS aggregator; no account or payment to view positions.
opsec: passive
opsecNote: Reads publicly broadcast AIS transponder signals relayed through volunteer receivers; the vessel and its crew get no signal that you looked. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Volunteer-run UK AIS aggregation site; coverage depends on hobbyist receiver stations, so it's a community source rather than an official authority.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- marinetraffic
- vesselfinder
aliases:
- shipais.uk
- Ship AIS UK
tags:
- marine
- vessel-tracking
- ais
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Ship AIS

> A volunteer-run UK AIS aggregator — a free way to see where a named vessel is right now (and where it's been) in British coastal and inland waters.

## When to use
You have a vessel `name` or MMSI/IMO (`document-id`), or you just want to know what's moving through a specific UK port or waterway, and you need current position, heading, and a recent track. Relevant to a missing-persons case only in the narrow situation where a subject is associated with a boat — confirming a vessel's whereabouts, its last known position, or which craft were near a location/time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://shipais.uk/.
2. Use **Vessel Search** to look up by name or MMSI, or browse the live map and the "Ships Underway" / "Ships At Anchor" lists.
3. Open a vessel to read its details (name, MMSI, type, destination if broadcast) and its recent movement track.
4. Note the timestamp of the last AIS fix — an old fix means the vessel is out of receiver range or has AIS off, not necessarily stationary.
5. Pivot: for global coverage or history beyond UK receivers, cross-check the same MMSI on `[[marinetraffic]]` / `[[vesselfinder]]`; a destination port feeds harbour/CCTV and arrivals inquiries.

## Inputs → Outputs
- **In:** vessel `name`, MMSI/IMO (`document-id`), or a UK area of interest
- **Out:** current position and track (`geolocation`), vessel `name`, type, and broadcast destination
- **Empty/negative result looks like:** vessel not shown / stale last-fix — the boat is outside volunteer-receiver range, has its transponder off, or is too small to carry AIS; try a global tracker.

## Gotchas & OpSec
- Coverage is UK-only and depends on hobbyist receiver placement — gaps are common offshore and inland; absence is not proof a vessel isn't there.
- AIS is self-reported by the vessel and can be switched off or spoofed; treat position as a lead.
- Marked "Not for nav" — it's situational awareness, not a navigational authority.
- Fully passive: no login, and the target is never alerted.

## Overlaps ("do both")
- Pairs with `[[marinetraffic]]` and `[[vesselfinder]]` — those give global coverage and historical tracks; Ship AIS can have denser live UK coverage from local receivers. Run the MMSI on all of them.

## Trust & verifiability
`trust: community` — a volunteer AIS project, not an official maritime authority. Positions come straight from vessels' own transponders (authoritative when present) but coverage and uptime depend on hobbyist infrastructure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ship-ais |
| category | transportation |
| selectorsIn → selectorsOut | name, document-id → geolocation, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
