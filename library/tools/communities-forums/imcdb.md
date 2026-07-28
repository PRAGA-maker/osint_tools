---
id: imcdb
name: IMCDb (Internet Movie Cars Database)
description: Use when you need to identify a vehicle's make/model/year from styling cues — a large, image-rich reference of cars, useful as a visual comparison aid — returns vehicle identification.
url: https://www.imcdb.org/
category: communities-forums
path:
- communities-forums
bestFor: Identifying or confirming a car's make/model/year by comparing against a large, well-labelled image database.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free, community-run, ad-supported; no account required to browse or search.
opsec: passive
opsecNote: Passive browsing of a public film-car database; you disclose nothing about a target. Its use in real investigations is as a visual reference, not a query against the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A hobbyist community database cataloguing vehicles appearing in films/TV; identifications are crowd-contributed and generally careful, but its scope is on-screen cars, not a universal vehicle identifier.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Internet Movie Cars Database
- imcdb.org
tags:
- vehicles
- identification
- reference
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# IMCDb (Internet Movie Cars Database)

> A large, meticulously-labelled catalogue of cars seen in films and TV — primarily a fan resource, but a handy visual reference when you're trying to put a make, model and year to a vehicle.

## When to use
You have an `image` of a vehicle (from CCTV, a photo, a video still) and need to pin down its make/model/year from styling cues — grille, lights, body shape, badges. IMCDb isn't a plate or VIN lookup; its real-world OSINT value is as a deep, searchable image reference of vehicles you can browse by make/model/year to compare against your unknown car. Treat it as a comparison aid alongside proper vehicle-ID methods, not a primary identifier.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.imcdb.org/ and browse/search by make, model and year.
2. Compare your unknown vehicle's visible features against the labelled images to narrow the make/model/generation.
3. Confirm the identification against a dedicated car-ID resource or forum before relying on it.
4. Note the model/year as context (a rare/distinctive model narrows a search; a common one doesn't).
5. Pivot: with a confirmed make/model/year and any partial plate, move to jurisdiction-appropriate vehicle/plate tools.

## Inputs → Outputs
- **In:** an `image`/visual description of a vehicle
- **Out:** a likely make/model/year identification by visual comparison (no direct plate/VIN `selectorsOut`)
- **Empty/negative result looks like:** no close visual match — the vehicle may be too new, regional, or a variant absent from the film-focused catalogue; use a general car-identification tool instead.

## Gotchas & OpSec
- OpSec: passive reference browsing; nothing about your target is disclosed.
- Scope is cars that appeared on screen — it is not a comprehensive vehicle registry or a plate/VIN lookup; it only helps with visual make/model ID.
- Crowd-labelled: identifications are usually careful but should be corroborated for anything that matters.

## Overlaps ("do both")
- Use as a visual comparison aid alongside dedicated vehicle/plate/VIN tools in `transportation` — IMCDb helps you name the model; those resolve registration/ownership where legal.

## Trust & verifiability
`trust: community` — a careful hobbyist database, but scoped to on-screen vehicles; confirm any identification with a purpose-built car-ID source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | imcdb |
| category | communities-forums |
| selectorsIn → selectorsOut | image → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
