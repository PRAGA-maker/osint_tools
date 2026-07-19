---
id: find-food-support
name: Find Food Support
description: Use when you have a US `address`/area and want nearby free-food resources — returns food pantries, meal services and EBT-accepting stores by location.
url: https://findfoodsupport.withgoogle.com/
category: geolocation
path:
- geolocation
bestFor: Mapping food pantries, meal programs, and EBT/SNAP retailers near a US address.
selectorsIn:
- geolocation
- address
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free Google.org tool; no account needed.
opsec: passive
opsecNote: Searching for food resources near an address is passive and reveals nothing about your subject; it queries Google's directory, not any person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A Google.org project surfacing verified food-assistance locations and USDA EBT retailer data; the underlying location data is from vetted sources.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Google Find Food Support
tags:
- Maps, Geolocation and Transport
- Urban and industrial infrastructure
- food-assistance
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Find Food Support

> Google's map of US free-food resources — pantries, meal services, and EBT-accepting stores near an address. A niche locator most useful for welfare-oriented searches around a vulnerable subject.

## When to use
Its OSINT use is narrow: when a missing or vulnerable subject may rely on food assistance, the pantries, soup kitchens, and meal programs near their last-known `address` are plausible places to canvass or share a "have you seen" notice. It's an environmental/welfare-context tool, not a person-finder (hence low MP relevance).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://findfoodsupport.withgoogle.com/.
2. Enter the address, neighborhood, or ZIP of interest.
3. Review the mapped results: food pantries, free-meal services, and (via the SNAP/EBT layer) grocery stores accepting EBT.
4. Open a location for its `address`, hours, appointment requirements, and services (grocery pickup vs on-site meals).
5. Build a list of nearby resources to canvass or to inform a welfare-oriented inquiry.
6. Pivot: resource locations near a last-known point → physical canvassing/outreach; clustering of resources → where a person without means might travel.

## Inputs → Outputs
- **In:** a US `address`/`geolocation`
- **Out:** nearby food pantries, meal services, and EBT-accepting store `address`es with `geolocation`
- **Empty/negative result looks like:** few or no resources near a rural address — coverage follows where verified programs exist, which is denser in cities. It never returns information about an individual.

## Gotchas & OpSec
- Not a person-locator: it maps resources, never people. Its investigative value is contextual and situational.
- US-only; hours/appointment rules change, so confirm before relying.
- OpSec: fully passive.

## Overlaps ("do both")
- Complements general mapping tools — use it specifically for the food-assistance layer around a location when a subject's circumstances make that relevant.

## Trust & verifiability
`trust: trusted` — a Google.org tool drawing on verified pantry listings and USDA EBT-retailer data; reliable for what it maps, with the usual caveat to confirm current hours/availability at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-food-support |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
