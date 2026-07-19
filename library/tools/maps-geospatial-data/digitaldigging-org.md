---
id: digitaldigging-org
name: digitaldigging.org
description: Use when you have an `image`/`geolocation` puzzle and want current technique guidance — Henk van Ess's OSINT newsletter on AI-powered geolocation and image analysis — returns methods and tool pointers, not a lookup.
url: https://www.digitaldigging.org/p/the-dawn-of-ai-powered-geolocation
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Learning current AI-assisted geolocation and image-investigation methods (e.g. GeoSpy-style location prediction) from a respected practitioner.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Substack newsletter — many posts (including this one) are free to read; some deeper/interview content sits behind a paid subscription. No paywall for the core methodology of the free posts.
opsec: passive
opsecNote: You are reading an article — nothing about your subject is disclosed. Passive. (The AI tools it describes have their own OpSec; evaluate those separately before uploading a target image to any of them.)
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Written by Henk van Ess, a well-known OSINT trainer and investigative journalist; a credible methodology source, though it is guidance/reading, not a data service.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Digital Digging
- Henk van Ess newsletter
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- geolocation
- methodology
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- ai-search-whisper
- deleted-tweet-finder-digital-digging-cache
- digitaldigging-org-2
- visualorigins-digitaldigging-org
---

# digitaldigging.org

> Henk van Ess's OSINT newsletter — a methodology source for AI-powered geolocation and image investigation, not a lookup tool.

## When to use
You have an `image` you need to geolocate, or a `geolocation` problem, and you want current *technique* — how to use AI location-prediction tools (like GeoSpy), what they get right and wrong, and how to combine them with traditional chronolocation/landmark analysis. Reach for this when the bottleneck is knowing *how* to work an image, not needing another database. It's a reading resource that points you at the right tools and workflows.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the article at https://www.digitaldigging.org/p/the-dawn-of-ai-powered-geolocation.
2. Read the walkthrough of AI geolocation (this piece covers GeoSpy — CLIP/OCR-based location prediction — with real accuracy examples).
3. Note the caveats van Ess flags (where AI guesses well vs badly) and the tools he names; browse the wider newsletter for adjacent techniques.
4. Apply the method with the actual tools on your own image; keep the AI's guess as a lead to verify with landmarks/shadows, not as fact.
5. Pivot: feed a predicted area into a mapping tool (`[[atlas-co]]`) or satellite browse (`[[nasa-worldview]]`) and confirm with street-level imagery.

## Inputs → Outputs
- **In:** `image` / `geolocation` question (you bring the puzzle; the site brings the method)
- **Out:** technique, tool pointers, and worked examples for AI-assisted geolocation → a `geolocation` hypothesis you then verify
- **Empty/negative result looks like:** it never "returns" a location — if you wanted an automated lookup you're on the wrong resource; use the tools it describes and verify their output yourself.

## Gotchas & OpSec
- Human-in-the-loop: part of the newsletter is behind a `payment-wall-partial`; the free posts carry the core method.
- This is guidance, not a data source — record the *tool* you actually ran (e.g. GeoSpy) as your source, not the article.
- AI geolocation is probabilistic; treat any predicted location as a lead requiring independent corroboration.

## Overlaps ("do both")
- Sits alongside the other Digital Digging entries (`[[visualorigins-digitaldigging-org]]`, `[[deleted-tweet-finder-digital-digging-cache]]`, `[[ai-search-whisper]]`) — this one teaches the AI-geolocation method; those are specific tools/tricks from the same author.

## Trust & verifiability
`trust: trusted` — authored by Henk van Ess, an established OSINT practitioner; credible as methodology. Verifiability rests on the tools he recommends: always corroborate an AI location guess with independent visual evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | digitaldigging-org |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | image, geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
