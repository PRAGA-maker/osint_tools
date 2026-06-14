---
id: lycos-image-search
name: Lycos Image Search
description: Use when you want a secondary keyword image-search index outside Google/Bing — returns image results for a text query.
url: https://search.lycos.com
category: image-video-face
path:
- image-video-face
bestFor: A legacy alternative search portal for keyword-based image lookups (not reverse-image).
selectorsIn:
- name
- employer-org
selectorsOut:
- image
- social-profile
status: degraded
pricing: free
costNote: Free, ad-supported portal.
opsec: passive
opsecNote: Keyword search only; no image upload. Queries go to Lycos's servers and likely third-party search backends.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Lycos is a long-standing legacy search portal; its image search is keyword-based and largely powered by other engines, so results overlap mainstream engines and value as a distinct source is limited.
missingPersonsRelevance: low
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- image-search
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Lycos Image Search

> A legacy search portal's keyword image search — a minor secondary index to run text-based image queries, not a reverse-image tool.

## When to use
You are running a `name` or `employer-org` as a text query and want a non-Google/Bing image index for breadth — occasionally a different engine surfaces a photo the majors deprioritise. This is keyword image search, NOT upload-an-image reverse search; for face/photo matching use a dedicated reverse-image engine instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://search.lycos.com and choose the Images tab.
2. Enter the text query (`selectorsIn`: name, employer-org).
3. Browse image results; click through to source pages (`selectorsOut`: image, social-profile via the host page).
4. Pivot: a source page or profile feeds people-search / social enumeration.

## Inputs → Outputs
- **In:** `name`, `employer-org` (text)
- **Out:** `image` results and the `social-profile`/pages hosting them
- **Empty/negative result looks like:** thin or generic results — Lycos largely mirrors mainstream backends, so unique finds are rare.

## Gotchas & OpSec
- Not reverse image search — you cannot upload a face here.
- Results overlap heavily with mainstream engines; low marginal value.
- OpSec: passive — text query only, no upload; queries are logged by Lycos/backends.

## Overlaps ("do both")
- For actual photo matching use reverse/face engines (`[[lenso-ai]]`, `[[labnol-org]]`); Lycos is only a breadth-on-keywords backstop.

## Trust & verifiability
`trust: community` — legacy portal that still functions but offers little beyond mainstream engines; hence low MP relevance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lycos-image-search |
| category | image-video-face |
| selectorsIn → selectorsOut | name, employer-org → image, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
