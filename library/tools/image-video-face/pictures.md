---
id: pictures
name: Pictures
description: Use when you have a name, keyword, or place and want broad keyword image-search results aggregated across the web — returns candidate images to triage and pivot from.
url: https://www.picsearch.com/
category: image-video-face
path:
- image-video-face
bestFor: Keyword/text image search via the Picsearch aggregator to surface candidate photos.
selectorsIn:
- name
- address
selectorsOut:
- image
status: degraded
pricing: free
costNote: Free, ad-supported keyword image search.
opsec: passive
opsecNote: Keyword search only; no image upload and no target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: "Pictures" maps to Picsearch, an older third-party image-search aggregator. It is a keyword (text-in) image engine, not reverse-image or face search; coverage today is thin versus Google/Bing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Picsearch
tags:
- image-search
source: osint4all
lastVerified: ''
enrichment: full
---

# Pictures

> The Picsearch image-search aggregator — a keyword-driven image engine for surfacing candidate photos by text, not a reverse-image or face tool.

## When to use
You have a `name`, place/`address`, or descriptive keywords and want a second image-search engine beyond Google/Bing to find candidate photos. Tie-in: text (`name`/`address`) in, `image` out. It does not accept an image as input.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.picsearch.com/.
2. Enter keywords — the subject's `name`, an event, or a location.
3. Scan results for candidate photos; click through to source pages for context.
4. Take any promising photo and pivot it into a reverse-image or face tool ([[pimeyes-2]]).

## Inputs → Outputs
- **In:** `name`, `address` (keywords/text)
- **Out:** `image`
- **Empty/negative result looks like:** sparse or generic results — likely for low-profile subjects; fall back to Google/Bing image search.

## Gotchas & OpSec
- Human-in-the-loop: none for searching.
- OpSec: passive — text search only, no uploads, nothing reaches a target.
- It is keyword-only (no reverse-image), and its index is dated; treat as a supplementary engine, not primary.

## Overlaps ("do both")
- Pairs with Google/Bing image search (broader index) and reverse-image tools (which this can feed).

## Trust & verifiability
`trust: community` — a real but aging image aggregator; functional as a keyword engine, limited reach. Verify and pivot any hit elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pictures |
| category | image-video-face |
| selectorsIn → selectorsOut | name, address → image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
