---
id: canadian-vessel-registration-query-system
name: Canadian Vessel Registration Query System
description: Use when you have a vessel name, official number, or an owner `name` and want Canadian vessel registration detail — returns registered/licensed vessel records including owner, port, and vessel particulars.
url: http://wwwapps.tc.gc.ca/saf-sec-sur/4/vrqs-srib
category: transportation
path:
- transportation
bestFor: Looking up Canadian-registered vessels by name, official number, or owner to link a person to a boat and home port.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- address
- document-id
status: live
pricing: free
costNote: Free Transport Canada online query; certified transcripts of registry cost extra but the online search is free.
opsec: passive
opsecNote: You query a Transport Canada public registry; the search is not attributed to you and the vessel owner is not notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Transport Canada Vessel Registration Query System; data comes from the national vessel register, though TC advises a certified Transcript of Registry for legal/official use rather than the online snapshot.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Transport Canada VRQS
- Canadian vessel registry
tags:
- transportation
- maritime
- vessels
- public-records
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Canadian Vessel Registration Query System

> Transport Canada's official vessel-registry search — look up a Canadian-registered or licensed vessel by name, official number, or owner to connect a person to a boat, a home port, and vessel particulars.

## When to use
You have a vessel name, an official/registration number (`document-id`), or an owner `name`, and you want to establish ownership or particulars of a Canadian vessel — to link a subject to a boat, identify a home port/region, corroborate an owner's identity, or resolve a vessel seen in imagery. Useful in cases with a maritime element (a subject known to own or operate a boat, or a boat spotted in relevant footage).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the Transport Canada VRQS at http://wwwapps.tc.gc.ca/saf-sec-sur/4/vrqs-srib.
2. Search by **Official Number**, **Vessel Name**, or **Owner Name** (advanced search allows other attributes). Note that Small Vessel Register entries may have no vessel name.
3. Open a result for the vessel particulars — type, tonnage, port of registry, owner details, and registration status.
4. For anything official/legal, request a certified Transcript of Registry rather than relying on the online snapshot.
5. Pivot: an owner `name`/`address` feeds people- and address-search; the port of registry gives a `geolocation` anchor; the official number ties the record together.

## Inputs → Outputs
- **In:** vessel name, official number (`document-id`), or owner `name`
- **Out:** registered vessel record — owner `name`, port/`address`, vessel particulars, registration `document-id`
- **Empty/negative result looks like:** no match — the vessel may be unregistered, foreign-flagged, licensed rather than registered (limited detail), or the search term differs from the record; try owner name and official number as alternates.

## Gotchas & OpSec
- Human-in-the-loop: none; direct web query.
- OpSec: fully **passive**; a government registry lookup with no exposure to the owner.
- Data currency: the online result is "believed to accurately reflect" the register but is not certified; for legal use obtain a Transcript of Registry. Small-vessel licences carry less detail than full registrations.
- Scope is Canadian vessels only — foreign or U.S. vessels need their own national registries.

## Overlaps ("do both")
- Pairs with global AIS/vessel-tracking (MarineTraffic, VesselFinder) and other national registries — this gives the Canadian ownership/particulars, while AIS trackers give live/historical position and foreign registries cover non-Canadian craft.

## Trust & verifiability
`trust: trusted` — it is Transport Canada's first-party vessel registry; the ownership and particulars are authoritative for Canadian vessels, with the only caveat being that the online snapshot is uncertified (a certified transcript is the legal-grade record).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-vessel-registration-query-system |
| category | transportation |
| selectorsIn → selectorsOut | name, document-id → name, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
