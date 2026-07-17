---
id: stolencars24
name: Stolencars24
description: Use when you have a vehicle `vin` (or plate) and want to check if it's reported stolen across European databases — returns theft status (no owner data).
url: https://www.stolencars24.eu/en/main.php
category: transportation
path:
- transportation
bestFor: Free, anonymous check of whether a vehicle (by VIN/chassis number) is recorded as stolen in Stolencars24's own database and linked European police databases.
selectorsIn:
- vin
- vehicle-plate
selectorsOut: []
status: live
pricing: free
costNote: Query is free of charge and anonymous; no account required.
opsec: passive
opsecNote: Checking a VIN against a stolen-vehicle database is passive — you query a database, not any person or the current keeper. Nothing is revealed to a vehicle's owner or seller.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates its own reports plus direct access to several European police databases (Lithuania, Slovenia, Slovakia, Czech Republic, Hungary, Romania); coverage is regional, so a clean result isn't a global all-clear.
missingPersonsRelevance: medium
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Stolencars24
- stolencars24.eu
tags:
- vehicle
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
---

# Stolencars24

> A free European stolen-vehicle database — enter a VIN to check it against Stolencars24's own reports and directly-linked police databases across several EU countries.

## When to use
You have a vehicle `vin` (chassis number) or plate connected to a subject or a transaction and want to know whether it's flagged as stolen. In a missing-persons or fraud context, a subject's vehicle showing up as stolen (or a vehicle they're selling/buying being stolen) is a significant lead; conversely, confirming a vehicle is not reported can rule a line of inquiry out (within the databases' coverage).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.stolencars24.eu/en/main.php.
2. Enter the Vehicle ID (VIN/chassis number) and press Search.
3. Read the result — whether the vehicle appears in Stolencars24's database or one of the linked European police databases as stolen/sought.
4. If flagged, note the reporting source/country; if clean, remember coverage is regional, not global.
5. Pivot: a stolen flag warrants contacting the relevant police via proper channels; a plate/VIN also feeds national vehicle-registration and other stolen-vehicle registries.

## Inputs → Outputs
- **In:** `vin` (chassis number) or `vehicle-plate`
- **Out:** theft status — whether the vehicle is recorded as stolen/sought in the covered databases. It does NOT return the owner's name or address (queries are anonymous).
- **Empty/negative result looks like:** "not found / not reported" — the vehicle isn't in these particular databases; it could still be stolen and reported only in a country not covered here.

## Gotchas & OpSec
- Coverage is Europe-centric (own reports + police DBs of LT, SI, SK, CZ, HU, RO); a clean result is not a worldwide all-clear — check national registries too.
- It returns theft status only, not vehicle ownership/history — pair with a VIN-decoder/registration check for the fuller record.
- OpSec: passive and anonymous.

## Overlaps ("do both")
- Complements national stolen-vehicle registries and VIN-history/registration tools — Stolencars24 covers several EU police databases at once; national tools add jurisdictions it misses and add ownership/history.

## Trust & verifiability
`trust: community` — draws on its own crowd reports plus genuine police-database access; a positive hit is strong, but a clean result only clears the covered databases, so corroborate across jurisdictions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stolencars24 |
| category | transportation |
| selectorsIn → selectorsOut | vin, vehicle-plate → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
