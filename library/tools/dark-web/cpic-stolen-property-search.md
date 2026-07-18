---
id: cpic-stolen-property-search
name: CPIC Stolen Property Search
description: Use when you have a serial number, VIN, or plate and want to check if it is reported stolen in Canada — returns a stolen/not-found status to flag illicit property or a subject's assets.
url: http://www.cpic-cipc.ca/index-eng.htm
category: dark-web
path:
- dark-web
bestFor: Public check of the Canadian Police Information Centre for stolen vehicles, boats, bicycles, firearms, and property by identifier.
selectorsIn:
- vin
- vehicle-plate
- document-id
selectorsOut:
- vehicle-plate
status: live
pricing: free
costNote: Free public service of the RCMP-operated Canadian Police Information Centre; no account or payment.
opsec: passive
opsecNote: An official Canadian police portal — assume searches are logged. It is a legitimate public lookup, but run only queries you can justify; do not treat it as anonymous. Use a clean browser for sensitive checks.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the RCMP/Canadian Police Information Centre; the stolen-property data is authoritative Canadian law-enforcement data.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- CPIC
- Canadian Police Information Centre
- cpic-cipc.ca
tags:
- stolen-property
- canada
- law-enforcement
- vehicles
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# CPIC Stolen Property Search

> The Canadian Police Information Centre's public search — check whether a vehicle, boat, bicycle, firearm, or serial-numbered item has been reported stolen in Canada.

## When to use
You have an identifier for property connected to a subject — a `vin`, a `vehicle-plate`, or a serial number (`document-id`) on a bike, boat motor, or firearm — and want to know if it is flagged stolen. A hit exposes that a subject is holding illicit property (a lead in fraud, trafficking, or missing-property cases); a clean result helps rule that out before you rely on an asset in your analysis.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.cpic-cipc.ca/index-eng.htm and pick the relevant public search: vehicles, boats, boat motors, bicycles, firearms, or property.
2. Enter the identifier the category asks for (VIN/serial for vehicles and equipment, serial number for bikes/firearms, etc.).
3. Read the result: the system reports whether an item matching that identifier is recorded as stolen in CPIC.
4. Pivot: a stolen hit is actionable intelligence to report through proper channels and to tie the subject to the item; a clean result feeds ownership/valuation checks (e.g. `[[canadian-black-book-values]]` for a vehicle).

## Inputs → Outputs
- **In:** `vin`, `vehicle-plate`, or a serial number (`document-id`)
- **Out:** stolen / not-found status for that identifier (and item type)
- **Empty/negative result looks like:** "no record found" — the item isn't in CPIC's stolen database, which does not by itself prove clean provenance (it may be unreported, or reported outside Canada).

## Gotchas & OpSec
- Human-in-the-loop: none for the public search; it does not return owner identities, only stolen status.
- OpSec: this is an official police portal — treat searches as logged and run only justifiable queries. Not an anonymous tool.
- Scope: Canada only, and only items reported to CPIC. A clean result is not a warranty of clear title — cross-check registration and history.

## Overlaps ("do both")
- Pairs with vehicle valuation/history tools like `[[canadian-black-book-values]]` and with national stolen-bike/firearm registries — CPIC confirms stolen status, the others confirm identity, spec, and value.

## Trust & verifiability
`trust: trusted` — it is the RCMP-operated Canadian Police Information Centre, so a stolen flag is authoritative Canadian law-enforcement data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cpic-stolen-property-search |
| category | dark-web |
| selectorsIn → selectorsOut | vin, vehicle-plate, document-id → vehicle-plate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
