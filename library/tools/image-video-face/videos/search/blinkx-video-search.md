---
id: blinkx-video-search
name: blinkx Video Search
description: Use when researching legacy video-search options — blinkx is defunct and no longer functions as a video search engine.
url: https://blinkx.com/
category: image-video-face
path:
- image-video-face
- videos
- search
bestFor: Historical reference only — blinkx was a speech-indexed video search engine, now discontinued.
input: ''
output: ''
selectorsIn:
- name
selectorsOut: []
status: down
pricing: free
opsec: passive
opsecNote: Site no longer operates as a search engine; treat the domain as defunct/parked. No target interaction in any case.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: blinkx Inc. became RhythmOne years ago and the consumer video-search product was shut down; the domain no longer provides working video search. Status inferred from product history, not freshly fetched.
missingPersonsRelevance: low
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: true
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# blinkx Video Search

> A once-notable video search engine (speech-to-text indexed clips) that is no longer operational — kept here so investigators don't waste time on a dead lead.

## When to use
Practically, do not rely on this for live work. blinkx historically let you search spoken-word content inside videos, which would have been useful to find a `name` mentioned in news/broadcast footage. The product was discontinued after blinkx pivoted to RhythmOne, so there is no working search to run today.

## How to use it (`bestInteractionPattern`: web-manual)
1. If you must confirm, open https://blinkx.com/ — expect a parked/redirect page, not a search engine.
2. For the actual capability (search by spoken words inside video), substitute a live engine: YouTube search (which indexes auto-captions), Bing Videos, or a transcript-search service.

## Inputs → Outputs
- **In:** `name` / keywords (historically)
- **Out:** none — service is down
- **Empty/negative result looks like:** a landing/parked page or redirect with no functional search box. That is the expected current state.

## Gotchas & OpSec
- Dead tool: marked `status: down` / `deprecated: true`. Do not cite results from it.
- Passive regardless; the only risk is wasted time.

## Overlaps ("do both")
- Replace entirely with `[[bing-videos]]` and YouTube/Google video search for caption- and speech-aware discovery.

## Trust & verifiability
`trust: unverified` — status derived from known product history (blinkx → RhythmOne shutdown), not from a fresh page fetch. Verify the parked state before relying on this note.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blinkx-video-search |
| category | image-video-face |
| selectorsIn → selectorsOut | name → (none) |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
