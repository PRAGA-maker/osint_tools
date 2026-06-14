---
id: museo
name: Museo
description: Use when you want to keyword/color-search public-domain art and museum image collections — returns artworks/images, not people; low direct value for missing-persons.
url: https://museo.app/
category: image-video-face
path:
- image-video-face
bestFor: Visual/keyword search across open museum and public-domain art collections.
selectorsIn:
- name
selectorsOut:
- image
- metadata-exif
status: unknown
pricing: free
costNote: Free to use; aggregates open-access collections (e.g. The Met, Art Institute, Rijksmuseum, NYPL).
opsec: passive
opsecNote: A public art-image search; querying it reveals nothing about a person and leaks only your search terms to the site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Museo is a known art-discovery search engine over open museum APIs; useful and legitimate but it indexes artworks, not people, so its missing-persons value is incidental.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- art-search
- image-search
source: osint4all
lastVerified: ''
enrichment: full
---

# Museo

> A free visual search engine across open museum and public-domain art collections — an art-discovery tool, only tangentially an OSINT image tool.

## When to use
Reach for Museo only in the narrow case where a lead points to a piece of artwork, a museum object, or a public-domain image — for example identifying a painting/photograph that appears in the background of a `image`, or matching an object to a known museum catalogue. It does not search the open web, social media, or faces, so it has little direct missing-persons utility.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://museo.app/.
2. Type a keyword (artist, subject, color) into the search box (`name`/term in).
3. Browse the returned artwork thumbnails and open an item for its source museum, title, date, and license `metadata-exif`.
4. Pivot: follow the link to the originating museum collection for provenance, or use a general reverse-image engine instead if the goal is actually to identify a person.

## Inputs → Outputs
- **In:** `name` / keyword
- **Out:** `image` (artworks), object `metadata-exif` (museum, date, license)
- **Empty/negative result looks like:** no thumbnails returned — the term is not in any indexed open collection; this is expected for ordinary photos of people.

## Gotchas & OpSec
- Human-in-the-loop: none required, but interpreting results is manual.
- OpSec: passive; reveals only the search term. The bigger "gotcha" is scope — it is the wrong tool for finding a missing person and is included here for completeness of an image-search toolbox.

## Overlaps ("do both")
- For actual person/photo identification use a reverse-image or face engine such as [[mxface-ai]] instead; Museo only complements those when an artwork is involved.

## Trust & verifiability
`trust: unverified` — Museo is a recognised open-collections art search engine, but its operator/maintenance status was not independently confirmed here, and it makes no person-level claims to verify.

---
## Metadata
| field | value |
|---|---|
| id | museo |
| category | image-video-face |
| selectorsIn → selectorsOut | name → image, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
