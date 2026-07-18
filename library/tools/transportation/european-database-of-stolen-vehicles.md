---
id: european-database-of-stolen-vehicles
name: European Database of Stolen Vehicles
description: Use when you have a VIN and want to check whether the vehicle is reported stolen across European registers — returns a stolen/not-found status to flag illicit vehicles.
url: http://www.stolencars.eu/en
category: transportation
path:
- transportation
bestFor: Free public VIN check against a European stolen-vehicle database aggregating police and insurer reports.
selectorsIn:
- vin
selectorsOut: []
status: live
pricing: free
costNote: The site states the service is completely free; no account required.
opsec: passive
opsecNote: You enter a VIN, not personal data, and no owner is notified. As with any third-party checker, the operator can log what you look up — use a clean browser for sensitive checks. It returns only theft status, not owner identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates ~140k stolen-vehicle records from police statistics and insurance reports; coverage is partial and it is not an official government register, so a clean result is not authoritative.
missingPersonsRelevance: medium
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- stolencars.eu
- Stolen Cars EU
tags:
- transportation
- stolen-vehicles
- vin-check
- europe
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# European Database of Stolen Vehicles

> A free public VIN checker that flags whether a vehicle appears in a European stolen-vehicle database compiled from police and insurer reports.

## When to use
You have a `vin` for a vehicle connected to a subject (from a listing, a document, or a sighting) and want a quick check on whether it's reported stolen in Europe. A hit is a strong red flag (fraud, trafficking, handling stolen goods); a clean result is a weak all-clear, since the database is partial. Useful before treating a vehicle as a legitimately-owned asset in your analysis.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.stolencars.eu/en.
2. Enter the 17-character VIN (the site checks by VIN, not plate).
3. Read the result: whether a matching vehicle is recorded as stolen in its ~140k-record European dataset.
4. Pivot: a stolen hit is actionable — report through proper channels and tie the vehicle to the subject. A clean result should be corroborated against national police registers (e.g. `[[cpic-stolen-property-search]]` for Canada) and a full VIN-history report.

## Inputs → Outputs
- **In:** `vin`
- **Out:** stolen / not-found status (no owner identity is returned)
- **Empty/negative result looks like:** "not found in database" — meaning only that this dataset has no theft record; the vehicle could still be stolen but unreported here, or reported outside Europe.

## Gotchas & OpSec
- Human-in-the-loop: none; VIN-only public form.
- OpSec: passive — a VIN, not personal data, and no owner notification. The third-party operator may log queries; use a clean browser for sensitive checks.
- Not authoritative: it is an aggregator, not an official register, with partial coverage. Never treat "not found" as proof of clean title — cross-check official sources.

## Overlaps ("do both")
- Pairs with national police stolen-property searches like `[[cpic-stolen-property-search]]` and with paid VIN-history reports — this gives a fast European theft flag, the others add jurisdiction-specific authority and full history.

## Trust & verifiability
`trust: community` — a useful free aggregator, but coverage is incomplete and unofficial; confirm any theft flag (or clean result) against an authoritative police/registry source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | european-database-of-stolen-vehicles |
| category | transportation |
| selectorsIn → selectorsOut | vin → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
