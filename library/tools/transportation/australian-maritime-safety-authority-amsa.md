---
id: australian-maritime-safety-authority-amsa
name: AMSA — Australian Register of Ships
description: Use when you have a vessel name/ID or an owner `name` and want Australian ship-registration detail — returns `employer-org`/owner, vessel `document-id` and registration status.
url: http://www.amsa.gov.au/vessels/shipping-registration/list-of-registered-ships
category: transportation
path:
- transportation
bestFor: Looking up an Australian-registered ship, its owner and registration details.
selectorsIn:
- name
- vin
selectorsOut:
- employer-org
- name
- document-id
status: live
pricing: free
costNote: Free public register from a government agency; the searchable list of registered ships is browsable without payment.
opsec: passive
opsecNote: A public government register; searching it is passive and reveals nothing to any subject. Only AMSA's servers log your query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Australian Maritime Safety Authority, a federal government agency; registration data is authoritative.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- AMSA
- Australian Register of Ships
- amsa.gov.au
tags:
- maritime
- vessel-registration
- public-records
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# AMSA — Australian Register of Ships

> Australia's official register of ships — a government-authoritative way to tie a vessel to its owner, or an owner to their registered vessels.

## When to use
You have a vessel (name or official/IMO number) or a suspected owner `name`, and want to confirm Australian ship registration. The register links a ship to its registered owner/operator (often an `employer-org` or individual), tonnage/type, port of registry and status — useful for asset-tracing, confirming ownership of a boat linked to a subject, or identifying who is behind a vessel seen in imagery or a listing. Note the term `vin` is used loosely here for a vessel's official/registration number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the AMSA "list of registered ships" page and use its search/browse.
2. Search by vessel name or official number, or scan for an owner `name`.
3. Read the entry: vessel name, official/IMO number, type/tonnage, port of registry, registered owner/operator and status.
4. Pivot: an owner `employer-org`/name feeds ASIC company and directory checks; the vessel number feeds international maritime databases (AIS/MarineTraffic, IMO); port of registry narrows geography.

## Inputs → Outputs
- **In:** vessel name / official number (`vin`, loosely), or owner `name`
- **Out:** `employer-org`/owner `name`, vessel `document-id` (official number), type, port and status
- **Empty/negative result looks like:** no match — the vessel isn't on the Australian register (it may be foreign-flagged or unregistered/recreational below the threshold); check international registries.

## Gotchas & OpSec
- Only Australian-registered commercial/qualifying vessels appear; small recreational craft may not be listed.
- Registered owner can be a corporate shell — follow the `employer-org` into company records for the beneficial owner.
- Passive government-register lookup; no subject exposure.

## Overlaps ("do both")
- Pairs with AIS/vessel-tracking (MarineTraffic), IMO/international ship registries and ASIC company search — AMSA gives the AU registration + owner; those give live position and corporate beneficial ownership.

## Trust & verifiability
`trust: trusted` — a first-party federal government register; registration and ownership data are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | australian-maritime-safety-authority-amsa |
| category | transportation |
| selectorsIn → selectorsOut | name, vin → employer-org, name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
