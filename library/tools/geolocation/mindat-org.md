---
id: mindat-org
name: Mindat.org
description: Use when an `image` or sample shows a distinctive rock/mineral and you want to narrow where it came from — returns mineral locality data and maps as geolocation leads.
url: https://www.mindat.org/countrylist.php
category: geolocation
path:
- geolocation
bestFor: Locating regions/mines where a specific mineral occurs — a geology-based geolocation lead for photos or samples.
selectorsIn:
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to browse and search the full database and locality maps; a free account is optional for contributing. No paywall on core data.
opsec: passive
opsecNote: Browsing a public mineralogy database is read-only and unrelated to any subject; nothing is contacted or logged against a person. Standard clean-session hygiene applies to the site itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Mindat is the world's largest, long-established mineralogical reference, maintained with the Hudson Institute of Mineralogy and a large expert community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- google-earth
- geonames
aliases:
- mindat.org
tags:
- geolocation
- geology
- minerals
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Mindat.org

> The world's largest mineralogy database, with locality records and maps; a niche geolocation aid when a photo contains a distinctive rock, mineral, or mine and you need to narrow where it was taken.

## When to use
You are geolocating an `image` in which the geology is a clue — a distinctive coloured rock face, an unusual mineral specimen, a quarry or mine setting — and you want to constrain the region. Mindat maps where specific minerals occur worldwide and documents individual localities/mines with coordinates, so identifying the material in a photo can point you to the countries or specific sites where it's found, tightening a location hypothesis when landmarks are absent.

## How to use it (`bestInteractionPattern`: web-manual)
1. Identify the candidate mineral/rock in the image (colour, crystal habit, host rock) — use a mineral-ID guide if unsure.
2. Search that mineral on https://www.mindat.org/ or browse localities via the country list.
3. Read the locality records: countries/regions of occurrence, specific mines with coordinates, and photos of specimens from each site to compare against your image.
4. Narrow to localities whose setting (terrain, mine type, associated minerals) matches the photo, then verify those coordinates in satellite imagery.
5. Pivot: candidate coordinates → `[[google-earth]]` for visual confirmation; place names → `[[geonames]]` and mapping tools.

## Inputs → Outputs
- **In:** `image` (containing identifiable geology/minerals)
- **Out:** `geolocation` (candidate countries/regions/mine coordinates where the mineral occurs)
- **Empty/negative result looks like:** the mineral is too common/widespread to localize (occurs everywhere), or you can't identify it confidently — in which case Mindat narrows nothing and you should rely on other geolocation cues.

## Gotchas & OpSec
- Only useful when the material is distinctive; common minerals (quartz, calcite) occur globally and won't constrain a location.
- Correct mineral identification is the hard prerequisite — a wrong ID sends you to the wrong continent; treat results as hypotheses to confirm with imagery.
- OpSec: **passive** — purely a reference database, no subject interaction.

## Overlaps ("do both")
- Pairs with `[[google-earth]]` — Mindat suggests candidate localities, and satellite/terrain imagery confirms which one actually matches the photo's setting.

## Trust & verifiability
`trust: trusted` — Mindat is the authoritative, community- and institution-maintained mineralogy reference; locality data is well-curated, though your own mineral ID is the step that most needs verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mindat-org |
| category | geolocation |
| selectorsIn → selectorsOut | image → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
