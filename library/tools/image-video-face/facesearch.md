---
id: facesearch
name: facesearch
description: Use when triaging legacy OSINT lists for a reverse face/photo search tool — but this entry's domain is misspelled and likely dead; verify before relying on it.
url: http://facesaerch.com
category: image-video-face
path:
- image-video-face
bestFor: Listed as a reverse photo/face search resource; current availability unconfirmed.
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- name
status: down
pricing: free
costNote: ''
opsec: unknown
opsecNote: If a working face-search endpoint exists, uploading a face would be active third-party collection. Do not upload sensitive imagery until the service is verified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: The listed URL `facesaerch.com` is a misspelling (likely intended "facesearch") and resolves to no recognized live face-search service; treat as unidentified/defunct. Not verified.
missingPersonsRelevance: low
coverage: []
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- reverse-image
- face
source: metaosint
lastVerified: ''
enrichment: full
---

# facesearch

> A legacy OSINT-list entry for a reverse photo/face search tool; the linked domain appears misspelled and non-functional.

## When to use
Only when working through a curated OSINT index and you encounter this entry. In principle it would take an `image`/`face` and return `social-profile`/`name` matches, but the link cannot be confirmed live. For real face search, use a verified engine instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Attempt to load http://facesaerch.com (note the `saerch` typo — also try `facesearch.com`).
2. If a working upload form appears, submit a `face` crop and review returned matches.
3. If the domain is parked, for sale, or dead, abandon and pivot.
4. Pivot: route the face to `[[facecheck-facial-recognition-search]]` or `[[pimeyes]]`.

## Inputs → Outputs
- **In:** `image` / `face` (only if a live endpoint exists).
- **Out:** intended `social-profile` / `name` matches — unverified.
- **Empty/negative result looks like:** the most likely outcome — a parked/non-resolving domain.

## Gotchas & OpSec
- The domain spelling is almost certainly a data-entry error; do not assume it is legitimate.
- OpSec: unknown operator — do not upload case imagery to an unidentified service.

## Overlaps ("do both")
- Replace with a maintained engine: `[[facecheck-facial-recognition-search]]`, `[[pimeyes]]`, `[[faceseek-face-search-engine]]`.

## Trust & verifiability
`trust: unverified` — could not identify a live, reputable tool behind this URL; entry retained for index completeness only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facesearch |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | unknown |
| human-in-loop | no |
