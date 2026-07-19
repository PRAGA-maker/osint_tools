---
id: licenseplates
name: License Plates of the World
description: Use when you have an `image` of an unknown `vehicle-plate` and want to identify its origin — returns the country/state/era a plate design belongs to as a geolocation lead.
url: http://www.worldlicenseplates.com/
category: people-search
path:
- people-search
bestFor: Identifying which country, US state or era a license plate is from by matching its design, colours and format.
selectorsIn:
- vehicle-plate
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public reference gallery; no account, no payment, no registration.
opsec: passive
opsecNote: You browse a static reference gallery — nothing is submitted about your subject, no lookup is logged against a target, and no one is notified. Entirely passive; the plate number itself never leaves your notes.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing enthusiast reference (cited in the Bellingcat toolkit) documenting plate designs worldwide; excellent for design/origin identification, but it is a design catalog, not a registration database — it never returns an owner.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- world-license-plates
aliases:
- worldlicenseplates.com
- License Plates of the World
tags:
- expert-search
- vehicle
- plate-identification
- geolocation
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# License Plates of the World

> A comprehensive reference gallery of license-plate designs by country, US state and era — the tool for turning a plate you can *see* into a place you can *name*.

## When to use
You have a photo or partial view of a `vehicle-plate` from CCTV, a social post, or a spot photo, and you don't know where it's from. Match the plate's colours, layout, slogan, serial format, and validation stickers against this catalog to identify the issuing country/state and often the approximate year. That converts an anonymous plate into a `geolocation` lead — narrowing which jurisdiction's registration channel to pursue next. It does NOT look up the plate number or the owner; it identifies the design.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.worldlicenseplates.com/ and pick the region/country (or US-state) index.
2. Compare your plate image to the samples: base colour, font, slogan/state name, serial pattern, and any date/validation markings.
3. Narrow to the matching jurisdiction and era — the site notes design changes over time, which helps date a sighting.
4. Pivot: the identified jurisdiction tells you which DMV/registration or plate-lookup service to use, and confirms/denies a claimed location.

## Inputs → Outputs
- **In:** `image` of a `vehicle-plate` (even partial)
- **Out:** `geolocation` — the country/state/era the plate design belongs to
- **Empty/negative result looks like:** no clean design match (a heavily obscured plate, a custom/novelty plate, or a very recent redesign not yet cataloged) — treat as "origin unresolved," not "no such plate."

## Gotchas & OpSec
- Human-in-the-loop: none — it's manual visual comparison you do yourself.
- It identifies the *design/jurisdiction*, never the owner; pair with a registration lookup for the person.
- Recent redesigns may lag in the catalog; cross-check against another plate-design gallery if unsure.
- Novelty, diplomatic, and vanity plates can mislead — note the plate *type*, not just the region.

## Overlaps ("do both")
- Pairs with `[[world-license-plates]]` and other plate galleries (cross-check design matches), and with a jurisdiction DMV/registration lookup once you know the country/state.

## Trust & verifiability
`trust: community` — a well-regarded enthusiast reference used by investigators (incl. Bellingcat's toolkit); authoritative for design identification, but confirm the final origin by comparing more than one sample.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | licenseplates |
| category | people-search |
| selectorsIn → selectorsOut | vehicle-plate, image → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
