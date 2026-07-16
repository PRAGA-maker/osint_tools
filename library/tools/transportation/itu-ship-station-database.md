---
id: itu-ship-station-database
name: ITU Ship Station Database
description: Use when you have a vessel `name`, callsign, MMSI, or IMO number and want the licensed station record — returns name, document-id.
url: https://www.itu.int/en/ITU-R/terrestrial/mars/Pages/default.aspx
category: transportation
path:
- transportation
bestFor: Resolving a ship's callsign / MMSI / name to its official ITU-registered station record and cross-referenced identifiers.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- document-id
status: live
pricing: free
costNote: Free public access. No account or payment; ITU MARS is an open reference service.
opsec: passive
opsecNote: A read-only query against the ITU's public register — no notification to any vessel owner and no login. Standard passive-recon hygiene (VPN/clean browser) is sufficient; nothing here is intrusive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the International Telecommunication Union (a UN agency); records are official administration-reported registrations, updated daily.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ITU MARS
- Maritime mobile Access and Retrieval System
- MARS ship station search
tags:
- toddington
- specialty-search
- maritime
- transportation
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# ITU Ship Station Database

> ITU's MARS register: the authoritative free lookup that turns a ship's callsign, MMSI, or name into its official station record and cross-identifiers.

## When to use
You have a maritime lead tied to a person — a vessel `name`, radio callsign, MMSI, IMO number, or EPIRB Hex ID (from an AIS track, a photo of the hull/lifebuoy, or a registration document) — and you want to confirm the station and pull its other identifiers and the licensing administration (flag/country). Useful for placing a subject on a specific boat, corroborating an owner/operator's claimed vessel, or seeding a marine-traffic pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the MARS portal at https://www.itu.int/en/ITU-R/terrestrial/mars/Pages/default.aspx and choose the **Ship stations** search.
2. Query by any known identifier: call sign, ship name, MMSI, IMO number, EPIRB Hex ID, or national registration number.
3. Read the record: reported vessel identity, the responsible administration/country, station class, and the linked identifiers (MMSI ↔ callsign ↔ IMO).
4. Pivot: take the MMSI/IMO into AIS trackers (MarineTraffic/VesselFinder) for live/historical position, and the flag/administration into national vessel registries for ownership.

## Inputs → Outputs
- **In:** vessel `name`, or a `document-id`-class identifier (callsign, MMSI, IMO, EPIRB Hex ID, national reg number)
- **Out:** confirmed vessel `name` and the cross-referenced `document-id` set (MMSI/callsign/IMO), plus responsible administration/country
- **Empty/negative result looks like:** "no records found" — the identifier isn't in the ITU register (small/unlicensed craft, or a wrong/spoofed MMSI). It does not itself return a personal owner name.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a public web form.
- OpSec: **passive** — a reference lookup with no owner notification.
- MARS holds *station licensing* data, not ownership; expect flag state and identifiers, then chase ownership in national registries. Coverage skews to larger/commercially-licensed vessels.
- MMSIs can be reprogrammed or spoofed on AIS; the ITU record is the ground-truth check against a spoofed broadcast.

## Overlaps ("do both")
- Use alongside AIS-tracking sites (e.g. MarineTraffic-style tools in the transportation category) — MARS confirms the registered identity, AIS trackers supply position and movement history.

## Trust & verifiability
`trust: trusted` — a UN agency's official maritime register, updated daily from member-state administrations; identifiers are authoritative and independently checkable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | itu-ship-station-database |
| category | transportation |
| selectorsIn → selectorsOut | name, document-id → name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
