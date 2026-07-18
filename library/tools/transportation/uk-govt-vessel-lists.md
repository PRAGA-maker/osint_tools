---
id: uk-govt-vessel-lists
name: UK Govt Vessel Lists
description: Use when you have a UK fishing `vessel-plate`/name and want official registration details — returns vessel name, RSS number, length, and home/administrative port.
url: https://www.gov.uk/government/collections/uk-vessel-lists
category: transportation
path:
- transportation
bestFor: Confirming a UK fishing vessel's registration, home port, and port letters/number from the official MMO datasets.
selectorsIn:
- vehicle-plate
selectorsOut:
- vehicle-plate
- geolocation
status: live
pricing: free
costNote: Free official statistics under Open Government Licence v3.0; downloadable spreadsheets.
opsec: passive
opsecNote: Static government spreadsheets — you download and search offline, so there is zero interaction with any vessel owner or third party. Nothing is logged beyond a normal GOV.UK file download.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the UK Marine Management Organisation as official statistics; authoritative for UK-registered/licensed fishing vessels.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- UK vessel lists
- MMO fishing vessel list
tags:
- toddington
- curated-directory
- maritime
- specialty-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# UK Govt Vessel Lists

> The Marine Management Organisation's official lists of UK-registered fishing vessels — downloadable spreadsheets you grep for a vessel's registration, length, and home port.

## When to use
You have a UK fishing vessel's name or port registration mark (the `vehicle-plate`-style port letters + number painted on the hull, e.g. `PW123`) and need to confirm it against the official registry: does the vessel exist, what is its Registry of Shipping and Seamen (RSS) number, how long is it, and which port is its base? Relevant when a subject is linked to a fishing boat and you need to anchor that boat to a real registration and a geographic home port.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.uk/government/collections/uk-vessel-lists.
2. Download the relevant dataset — there are two lists: **vessels 10 metres and under** and **vessels over 10 metres**.
3. Open the spreadsheet and search (Ctrl-F / filter) by vessel name, RSS number, or port letters/number.
4. Read the row: vessel name, RSS number, overall length, administrative port, home port, and port letters/number (`selectorsOut`).
5. Pivot: the home/administrative port gives a `geolocation` anchor; the vessel identity feeds wider maritime registries and licensing records.

## Inputs → Outputs
- **In:** vessel name or port registration mark (`vehicle-plate`)
- **Out:** RSS number, overall length, administrative + home port (`geolocation`), port letters/number
- **Empty/negative result looks like:** no matching row — the vessel isn't a currently listed UK fishing vessel (it may be a pleasure/other craft, deregistered, or non-UK), not necessarily that it never existed.

## Gotchas & OpSec
- Scope is **fishing vessels only** — not naval, cargo, or pleasure craft — and it does **not** include owner names or IMO numbers, only registration/operational data.
- It's a spreadsheet snapshot updated periodically (latest here June 2026); a very new or recently-removed vessel may not appear.
- OpSec: fully passive — offline document search, nothing leaked.

## Overlaps ("do both")
- Pairs with an international vessel/AIS registry: this gives the authoritative UK fishing registration, then AIS/marine-traffic tools add movement and (sometimes) ownership that the MMO list omits.

## Trust & verifiability
`trust: trusted` — official UK government statistics from the Marine Management Organisation under the Open Government Licence, so the registration data is authoritative for the UK fishing fleet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-govt-vessel-lists |
