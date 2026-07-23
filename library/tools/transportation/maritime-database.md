---
id: maritime-database
name: Maritime-Database
description: Use when you have a vessel name, port, or shipping-company name and want directory details linking ships, ports and maritime companies — returns company `address`es, vessel and port records.
url: https://www.maritime-database.com
category: transportation
path:
- transportation
bestFor: Looking up shipping companies, vessels and ports and the links between them (company addresses, fleets, port data).
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free directory; companies can self-register listings.
opsec: passive
opsecNote: Passive — browsing a public maritime directory. No target is contacted. Because companies can self-list, treat entries as claimed rather than verified and cross-check against official registries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community maritime directory (50k+ vessels, 2k+ ports); useful for leads but partly self-submitted, so verify critical facts against IMO/flag-state registries.
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
- Maritime Database
- maritime-database.com
tags:
- maritime
- vessels
- shipping-companies
- ports
source: metaosint
lastVerified: '2026-07-23'
enrichment: full
---

# Maritime-Database

> A global directory of vessels, ports and shipping companies and the relationships between them.

## When to use
You have a vessel name, a port, or a shipping/maritime `employer-org` and want to explore the surrounding network — which company operates a ship, where a company is based, what ports connect a region. Useful for building context around a maritime business or a subject's stated shipping employer, and as a starting directory before moving to authoritative vessel registries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.maritime-database.com.
2. Browse or search by company `name`, vessel, or port (or drill down by region → country).
3. Open a company listing for its `address`, contact details, and associated vessels/services.
4. Open a port entry for coordinates, time zone, and country context.
5. Verify anything critical (vessel identity/ownership) against an IMO number lookup or the flag-state registry, since some entries are self-submitted.

## Inputs → Outputs
- **In:** vessel `name`, port, or shipping-company `employer-org`
- **Out:** company `address`/contacts, vessel and port records, company↔vessel↔port links
- **Empty/negative result looks like:** no listing found — the entity may simply not be in this directory (it's not exhaustive); check an official vessel registry before concluding it doesn't exist.

## Gotchas & OpSec
- Partly self-registered — treat company claims as unverified until cross-checked.
- Not a real-time AIS tracker; for live vessel positions use a dedicated AIS service.
- Coverage is broad but incomplete; absence here is not proof of absence.

## Overlaps ("do both")
- Pairs with IMO number lookups and live AIS trackers (MarineTraffic, VesselFinder) — this gives the directory/company context, those give authoritative identity and real-time position.

## Trust & verifiability
`trust: community` — a useful but partly user-submitted directory; confirm vessel ownership and identity against official IMO/flag-state records before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maritime-database |
