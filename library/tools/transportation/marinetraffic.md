---
id: marinetraffic
name: MarineTraffic
description: Use when you have a vessel name, MMSI, or IMO number and want its live/last-known position and voyage details — returns geolocation plus vessel identity.
url: https://www.marinetraffic.com/
category: transportation
path:
- transportation
bestFor: Locating a specific ship in near-real-time and confirming its identity/particulars.
selectorsIn:
- name
- vin
selectorsOut:
- geolocation
- name
- image
status: live
pricing: freemium
costNote: Live map, vessel search, and current position are free without an account; historical track playback, past port calls, and voyage analytics sit behind a paid subscription. A free login raises some viewing limits.
opsec: passive
opsecNote: Passive — you are reading a public AIS aggregation portal, not signalling the vessel or crew. Browsing never touches the target. Only creating a paid account or setting alerts ties activity to your identity; use a sock-puppet login if you subscribe.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established commercial AIS aggregator (Kpler-owned) sourcing terrestrial and satellite receivers; the identity/position data is the vessel's own AIS broadcast, so it is authoritative while the transponder is on.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- marine-traffic-geolocation-search
aliases:
- Marine Traffic
- marinetraffic.com
tags:
- maritime
- ais
- vessel-tracking
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# MarineTraffic

> The default live AIS map of world shipping: type a vessel name or MMSI/IMO and see where the ship is right now, or was last heard.

## When to use
You have a lead tying a person to a specific vessel — a ship `name`, an MMSI (9-digit AIS ID), or an IMO/hull number — and you want to place that vessel on a map, confirm it is real and active, or check its stated destination. Useful when a missing person is believed to be aboard a ferry, cargo ship, fishing vessel, or yacht, or to corroborate a claimed maritime job or itinerary.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.marinetraffic.com/ and use the search box at the top of the live map.
2. Enter the vessel `name`, MMSI, or IMO number. Auto-complete disambiguates same-named ships — pick the one whose type and flag match your lead.
3. Read the vessel page:
   - **Current position** on the map with the timestamp of the last AIS report, speed, course, and the destination the crew keyed in.
   - **Particulars**: type, flag, dimensions, year built, callsign, and often a user-contributed photo (`image`).
4. For where-it-has-been, the recent-track and past-port-calls tabs show history — most of that timeline is paywalled; current position and basic particulars are free.
5. Pivot: the flag state, IMO, and owner/manager hints feed ship registries and company lookups; a user photo can feed reverse-image search.

## Inputs → Outputs
- **In:** vessel `name`, MMSI, or IMO (`vin`)
- **Out:** `geolocation` (last-known lat/long + timestamp), vessel `name`/identity particulars, sometimes an `image`
- **Empty/negative result looks like:** no search hit (name misspelled or vessel never AIS-tracked), or a vessel page whose "last seen" is days or weeks old — meaning AIS is off, the ship is out of receiver range, or it is idle in port. Absence of a live fix is not proof the ship is gone.

## Gotchas & OpSec
- AIS can be switched off, spoofed, or simply out of terrestrial range mid-ocean; a frozen or missing position is common and not evidence of wrongdoing.
- Small craft, naval, and many fishing vessels may not transmit AIS at all — coverage skews toward commercial shipping.
- Rate limits and bot protection appear under heavy anonymous browsing; slow down or log in.
- OpSec: browsing is passive and safe. A paid subscription or saved alerts create an account trail — use a dedicated identity.

## Overlaps ("do both")
- Pairs with `[[marine-traffic-geolocation-search]]` for the geolocation-first workflow; cross-check a position against another AIS aggregator (VesselFinder and similar), since receiver coverage differs and one may hold a fresher fix than the other.

## Trust & verifiability
`trust: trusted` — a mature commercial aggregator of the vessel's own AIS broadcasts; identity and position are authoritative while AIS is transmitting, and the main caveat is coverage/transponder state, not data honesty.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | marinetraffic |
