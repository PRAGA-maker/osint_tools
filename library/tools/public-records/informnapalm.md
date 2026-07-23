---
id: informnapalm
name: InformNapalm
description: Use when investigating Russian military involvement in aggression against Ukraine/Georgia — a volunteer OSINT database of units, personnel, and equipment returning name, employer-org, and associate leads.
url: https://informnapalm.org/db/russian-aggression/#lang=en&page=m_unit
category: public-records
path:
- public-records
bestFor: Researching identified Russian military units, servicemen, and equipment tied to documented aggression.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
opsec: passive
opsecNote: Reading the published database is passive; the site is a volunteer-run investigative resource, not a live query against any individual, so no subject is alerted. It is an advocacy-aligned OSINT project documenting a conflict — findings are curated investigations; corroborate names/units against primary evidence before treating them as established fact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Volunteer international OSINT community focused on Russian aggression; well-known in the field, but partisan by mission — treat as sourced leads to verify.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- INFORMNAPALM
- informnapalm.org
tags:
- military-osint
- conflict
- ukraine
- russia
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# InformNapalm

> A volunteer OSINT database documenting Russian military aggression — searchable records of units, servicemen, and equipment identified through open-source investigations.

## When to use
Your investigation touches the Russo-Ukrainian (or 2008 Georgian) conflict and you need to identify or corroborate a Russian military unit, serviceman, or piece of equipment. InformNapalm's database links personnel to units, units to operations, and documents equipment sightings — useful for confirming a `name`'s military affiliation, mapping a unit's members (`associate`), or tying an individual to documented conflict activity. Genuinely relevant to identifying people in a conflict/missing-persons context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the database: https://informnapalm.org/db/russian-aggression/ (switch language to English; browse the unit/personnel/equipment views).
2. Search or browse by unit, serviceman `name`, or `employer-org` (military formation).
3. Read the record: identified individuals, their unit, linked investigations, and supporting evidence/sources (`selectorsOut`).
4. Pivot: named servicemen and their units feed further social-media and registry research; linked investigations provide the underlying evidence to verify.

## Inputs → Outputs
- **In:** `name` (serviceman) or `employer-org` (military unit/formation)
- **Out:** `name` (identified individuals), `employer-org` (units), `associate` (fellow unit members), linked investigations/evidence
- **Empty/negative result looks like:** no record for the person/unit — they may not have been documented, not that no connection exists; check the linked source investigations and other conflict-OSINT databases.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — reading a published database; nobody is queried or alerted.
- Mission-driven: InformNapalm is an advocacy-aligned volunteer project. Its investigations are typically sourced, but treat entries as leads and verify names/units against the underlying primary evidence.

## Overlaps ("do both")
- Pairs with Bellingcat conflict investigations, the [[bellingcat]] toolkit, and Ukrainian databases (e.g. Myrotvorets-type sources) — cross-reference identifications, since each project documents different units/individuals and evidence.

## Trust & verifiability
`trust: community` — a respected but partisan volunteer OSINT community. Records are generally evidence-backed and valuable for leads, but its advocacy mission means you should confirm any identification against the cited primary sources before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | informnapalm |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
