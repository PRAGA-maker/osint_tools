---
id: global-biodiversity-information-facility
name: Global Biodiversity Information Facility
description: Use when you have a species name or a `geolocation` and want to know where a plant/animal occurs — returns mapped occurrence points that help constrain where an image or clue was captured.
url: https://www.gbif.org/
category: geolocation
path:
- geolocation
bestFor: Constraining the possible location of a photo/video by the geographic range of a plant, bird, or animal visible in it.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, open-data. No account needed to search or view maps; free registration only if you want to download bulk datasets with a citation DOI.
opsec: passive
opsecNote: Purely a public scientific database of species occurrences; queries reveal nothing about your target and touch no one connected to the case. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: GBIF is an intergovernmental research infrastructure funded by governments worldwide, aggregating occurrence records from museums, herbaria, and citizen-science platforms.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- inaturalist
- google-earth
aliases:
- GBIF
- gbif.org
tags:
- Maps, Geolocation and Transport
- Nature
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Global Biodiversity Information Facility

> A global, open occurrence database of plants and animals — an image-geolocation aid: if you can name the species in a photo, GBIF maps where on Earth it's actually recorded.

## When to use
You're geolocating a photo or video and it contains a distinctive plant, bird, insect, or animal. GBIF tells you the documented geographic range of that species, letting you rule regions in or out (e.g. "this cactus only occurs in the Sonoran Desert" narrows a US kidnapping-scene photo dramatically). Also useful to sanity-check a claimed location against what could plausibly be growing/living there.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.gbif.org/ and search the species (common or scientific name) — e.g. `/occurrence/map?q=cobra`.
2. Open the **occurrence map** to see every recorded sighting as points/heat; zoom to judge the range.
3. Filter by country, dataset, basis-of-record, or date to tighten the picture.
4. For programmatic use, hit the free GBIF REST API (`api.gbif.org`) to pull occurrences by taxon and bounding box.
5. Pivot: an occurrence cluster gives you a candidate `geolocation` region → confirm the exact spot with terrain/imagery in `[[google-earth]]`; cross-check individual sightings against `[[inaturalist]]`, which often carries the original geotagged photo.

## Inputs → Outputs
- **In:** a species name (identified from an image), or a `geolocation`/bounding box to list what occurs there
- **Out:** mapped occurrence points and their coordinates → a plausible `geolocation` range
- **Empty/negative result looks like:** few or no points — either the species is under-recorded in GBIF (absence of data ≠ absence of the species) or you've mis-identified it; re-check the ID.

## Gotchas & OpSec
- Coverage is uneven: heavily sampled in North America/Europe, sparse elsewhere, so "no records here" can be a data gap, not a true absence.
- Records include cultivated/captive specimens (zoos, gardens) — a point isn't proof of a wild population; check basis-of-record.
- You must correctly identify the organism first; a wrong species ID sends you to the wrong continent.

## Overlaps ("do both")
- Pairs with `[[inaturalist]]` — GBIF aggregates the range at scale; iNaturalist often has the individual geotagged, photo-verified sighting.
- Pairs with `[[google-earth]]` — narrow the region by species range here, then confirm the precise scene in satellite/terrain imagery.

## Trust & verifiability
`trust: trusted` — GBIF is a government-funded international scientific infrastructure; records are sourced from vetted institutions and citizen-science platforms and carry provenance you can inspect.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-biodiversity-information-facility |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
