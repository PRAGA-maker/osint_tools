---
id: american-association-of-motor-vehicle-administrators
name: American Association of Motor Vehicle Administrators (AAMVA)
description: Use when you need to understand DMV/vehicle-records systems and verification programs — returns reference/context on how to route a records request, not a public lookup.
url: https://www.aamva.org
category: transportation
path:
- transportation
bestFor: Understanding the US/Canada motor-vehicle administration landscape (DL/ID standards, verification programs, member DMVs) to plan a records request.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public organization website; the verification systems it runs (e.g. DLDV, S2S) are for member agencies, not the public.
opsec: passive
opsecNote: Reading AAMVA's public site is passive with no subject footprint. Note: AAMVA does NOT offer a public person/vehicle lookup — its systems are restricted to member DMVs and authorized users; do not expect (or attempt) direct data access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official trade association of US/Canadian motor-vehicle and law-enforcement agencies; authoritative for standards and program documentation, but not a data source you can query for individuals.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- AAMVA
- aamva.org
tags:
- toddington
- curated-directory
- motor-vehicle
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# American Association of Motor Vehicle Administrators (AAMVA)

> The umbrella body for US/Canadian DMVs — a reference for how driver-licence and vehicle-records systems work and who administers them, not a public lookup tool.

## When to use
This is orientation, not a query. Use it when you need to understand the motor-vehicle records landscape before pursuing a DL/ID or vehicle record: which agency holds what, how driver-licence data standards and verification programs (DLDV, S2S, DL/ID document standards) work, and which state/provincial DMV to approach. It helps you plan a *properly-routed* records request; it will not hand you a person's data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.aamva.org and browse the programs, standards, and member-agency sections.
2. Identify the responsible DMV and the correct records/verification pathway for your jurisdiction.
3. Read DL/ID standards docs if you need to interpret a licence's format/security features.
4. Pivot: go to the specific state/provincial DMV (the actual record holder) with the correct, lawful request process AAMVA helped you identify.

## Inputs → Outputs
- **In:** none (reference/orientation)
- **Out:** program/standards/agency context to route a records request (no person-level data)
- **Empty/negative result looks like:** n/a — it's documentation; the "failure mode" is expecting a lookup it doesn't provide.

## Gotchas & OpSec
- NOT a public data source — AAMVA's verification systems are gated to member agencies and authorized users; individuals cannot query them.
- Actual DL/vehicle records are held (and access-controlled) by each state/provincial DMV under laws like the US DPPA.
- OpSec: passive reading only.

## Overlaps ("do both")
- Complements state-DMV and VIN/plate tools — this explains the system; those (and lawful DMV channels) are where actual records live.

## Trust & verifiability
`trust: trusted` — an authoritative first-party industry body for standards and program documentation; simply not a queryable data source for individuals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | american-association-of-motor-vehicle-administrators |
| category | transportation |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
