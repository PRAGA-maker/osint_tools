---
id: canadian-civil-aircraft-register-search-canada
name: Canadian Civil Aircraft Register Search (Canada)
description: Use when you have a Canadian tail number (`vehicle-plate`) or owner `name` and want registration details — returns registered owner `name`/`address` and aircraft make/model/serial.
url: https://wwwapps.tc.gc.ca/saf-sec-sur/2/ccarcs-riacc/RchSimp.aspx
category: transportation
path:
- transportation
bestFor: Looking up the registered owner and details of a Canadian civil aircraft by registration mark, name, model, or serial.
selectorsIn:
- vehicle-plate
- name
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free public government search; no account or payment. Results capped at 1000 records per query.
opsec: passive
opsecNote: An official Transport Canada public-record search — you query a government database, not the owner, so nobody is notified. Purely passive; only your own IP touches the tc.gc.ca site. Use a VPN if the collection itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Transport Canada Civil Aircraft Register (CCARCS) — first-party, authoritative registration data for Canadian civil aircraft.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CCARCS
- Transport Canada aircraft registry
- Canadian Civil Aircraft Register
tags:
- toddington
- aviation
- aircraft-registry
- government
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Canadian Civil Aircraft Register Search (Canada)

> Transport Canada's official aircraft registry — decode a Canadian tail number into its registered owner, or find every aircraft a name owns.

## When to use
You have a Canadian aircraft registration mark (a `vehicle-plate`, e.g. `C-GABC`, from a photo, spotting report, or ADS-B track) and want the registered owner and aircraft details; or you have an owner `name`/company and want the aircraft(s) registered to them. This is the authoritative source for Canadian civil-aviation ownership — useful for tying a person or company to an aircraft, corroborating wealth/assets, or geolocating a base of operations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CCARCS quick search at wwwapps.tc.gc.ca.
2. Search by any combination of registration mark, common (owner) name, model name, or serial number, using match modes (Beginning With / Exact / Ending With / Anywhere).
3. Read the result: registered owner `name` and `address`, plus aircraft make/model, serial number, and status.
4. For an owner search, note all aircraft returned (up to 1000) to build an asset/ownership picture.
5. Pivot: an owner name/address feeds people-search and property records; a company owner feeds corporate-registry OSINT; the base address feeds geolocation.

## Inputs → Outputs
- **In:** `vehicle-plate` (registration mark) and/or owner `name`/model/serial
- **Out:** registered owner `name`, `address`, `employer-org` (if company-owned), aircraft make/model/serial/status
- **Empty/negative result looks like:** "no records" — the mark may be deregistered, non-Canadian (wrong registry), or mistyped; owner details can be a numbered company or trustee rather than an individual.

## Gotchas & OpSec
- Canada only — a non-`C-` mark belongs to another country's registry; decode the prefix first.
- Ownership is often held by a company or trust, so the "owner" may be an `employer-org`, not the operator/pilot you're after.
- Fully passive government record; no target interaction.

## Overlaps ("do both")
- Pairs with aircraft prefix/registry references and flight trackers in the [[transportation]] set — this gives the authoritative Canadian owner, while trackers show the aircraft's actual movements.

## Trust & verifiability
`trust: trusted` — first-party Transport Canada data, authoritative for Canadian registrations. Owner records are reliable but may point to corporate shells; corroborate the human behind a company owner separately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-civil-aircraft-register-search-canada |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, name → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
