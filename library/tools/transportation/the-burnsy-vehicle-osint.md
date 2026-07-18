---
id: the-burnsy-vehicle-osint
name: The Burnsy Vehicle OSINT Collection
description: Use when you have a `vehicle-plate`, `vin`, or vehicle photo and need the right lookup — a curated directory of vehicle-OSINT tools and registries for 50+ countries.
url: https://github.com/theburnsy/vehicle-osint-collection
category: transportation
path:
- transportation
bestFor: A one-stop, country-indexed directory of license-plate lookups, VIN decoders, and vehicle-image recognition tools to route a vehicle query to the correct resource.
selectorsIn:
- vehicle-plate
- vin
- image
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Free, open-source GitHub collection (a curated README); the individual tools it links vary from free government portals to paid services.
opsec: passive
opsecNote: Passive — the collection itself is a static list, safe to read. OpSec depends on the linked tool you then use; some plate/VIN lookups are active queries against registries, so apply each tool's own precautions and a sock puppet where needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-regarded, actively-maintained community repository (~1k stars) by TheBurnsy; it curates third-party tools it doesn't operate, so vet each linked resource individually.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Vehicle OSINT Collection
- theburnsy vehicle-osint
tags:
- vehicle
- open-source
- directory
- license-plate
- vin
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# The Burnsy Vehicle OSINT Collection

> A curated, country-by-country map of vehicle-OSINT resources — when you have a plate, VIN, or vehicle photo, this tells you *which* tool actually covers that jurisdiction, so you don't waste time on lookups that can't help.

## When to use
You have a vehicle selector — a `vehicle-plate`, a `vin`, or a photo of a car — and need the right lookup for the relevant country. Plate/registration tools are highly jurisdiction-specific, and this collection organizes 50+ countries' registries, VIN decoders, image-recognition tools (make/model from a photo), and ancillary resources (recalls, tires, transit maps, dashcam/webcam networks). It's the routing layer for transportation OSINT — start here to find the correct downstream tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo at https://github.com/theburnsy/vehicle-osint-collection and read the README.
2. Jump to the section that matches your selector and jurisdiction — Image Analysis, License Plate Lookups (by country), VIN Decoders, or Mapping/Surveillance.
3. Pick the specific linked tool for your country/need and follow it out.
4. Apply that tool's own workflow and OpSec (some registry lookups are active and may require captcha/registration).
5. Pivot: a plate/VIN resolved via a linked registry can yield an owner `name`/`address` (jurisdiction-dependent); an image tool yields make/model to narrow identification.

## Inputs → Outputs
- **In:** a `vehicle-plate`, `vin`, or vehicle `image` (plus the country)
- **Out:** the right tool/registry to run — which, downstream, can produce owner `name`/`address`, make/model, or history
- **Empty/negative result looks like:** if no tool is listed for a jurisdiction, that country likely has no public lookup — a coverage gap in the vehicle-OSINT landscape, not a fault of the collection.

## Gotchas & OpSec
- **It's a directory, not a lookup:** it points you to tools — the actual query (and its cost/OpSec) happens on the linked site.
- Linked tools vary widely: some are free government portals, some paid, some intermittently up — vet each before relying on it.
- Owner-data availability from plates/VINs is heavily jurisdiction-restricted (privacy law); many registries won't return a name at all.

## Overlaps ("do both")
- Complements individual plate/VIN tools in this library — use the collection to *find* the correct one for a country, then run that specific tool; cross-check owner data against official registries.

## Trust & verifiability
`trust: community` — an actively-maintained, popular open-source directory; because it curates third-party tools rather than operating them, verify each linked resource (and any result it returns) independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-burnsy-vehicle-osint |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, vin, image → name, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
