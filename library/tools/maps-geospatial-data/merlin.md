---
id: merlin
name: Merlin
description: Use when you have an `image` or audio of a bird from footage/photos and want to identify the species — returns the bird's identity, a geolocation-narrowing clue.
url: https://merlin.allaboutbirds.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Identifying a bird by photo or sound to constrain the geographic region where a photo/video was taken.
selectorsIn:
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free app and web tool from the Cornell Lab of Ornithology; no payment. A free Cornell/eBird account is optional for syncing but not required to identify.
opsec: passive
opsecNote: You upload only the bird crop of a photo (or an audio clip) to Cornell's identifier — never the full sensitive image with identifying context. Identification runs against Cornell/eBird data; treat it as a passive research query. Strip metadata from any media before upload if provenance matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Built by the Cornell Lab of Ornithology on eBird's global observation dataset; an authoritative, science-backed species identifier widely used in geolocation research.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- global-forest-watch
aliases:
- Merlin Bird ID
- Cornell Merlin
tags:
- bellingcat-toolkit
- environment-wildlife
- geolocation
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# Merlin

> Cornell's free bird-identification app — a geolocation aid in image/video forensics: the bird species in a scene narrows *where on Earth* the footage was shot.

## When to use
You're geolocating a photo or video and it contains a bird — visible in frame or audible in the soundtrack. Identifying the species (via Merlin's photo ID or Sound ID) constrains the plausible region, because most species have a defined geographic range and season. Reach for it as one corroborating signal in a chronolocation/geolocation stack, not as a standalone locator.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Merlin Bird ID (iOS/Android) or use the web ID at merlin.allaboutbirds.org; download the relevant regional bird pack if prompted.
2. **Photo ID:** crop the frame to the bird and upload it; **Sound ID:** feed the audio clip. Upload only the bird, not the whole sensitive image.
3. Read the suggested species and confidence.
4. Look up that species' native range/season (Merlin/eBird range maps) — that's the geographic constraint.
5. Combine with vegetation, architecture, sun position, and other cues to tighten the location.

## Inputs → Outputs
- **In:** `image` (bird crop) or an audio clip
- **Out:** species identity → a `geolocation` range/season constraint
- **Empty/negative result looks like:** low-confidence or multiple candidate species (common, wide-ranging birds give little geographic signal) — treat as weak evidence, not a fix.

## Gotchas & OpSec
- A cosmopolitan species (pigeon, house sparrow) narrows almost nothing; the value is in range-restricted species.
- Captive/escaped exotics and migratory birds can mislead — cross-check season and habitat.
- Upload only the cropped bird, never the full contextual image, to avoid leaking the scene to a third-party service.

## Overlaps ("do both")
- Pairs with `[[global-forest-watch]]` and other environment/terrain tools — the bird gives the biome/range, those confirm the land-cover and habitat at candidate locations.

## Trust & verifiability
`trust: trusted` — Cornell Lab of Ornithology / eBird is an authoritative scientific source; the ID engine is reliable, though the *geolocation inference* you draw from a species is only as strong as that species' range specificity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | merlin |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | image → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |
