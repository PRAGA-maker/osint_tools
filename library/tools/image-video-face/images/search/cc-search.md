---
id: cc-search
name: CC Search
description: Use when you need openly-licensed images for reports/illustration — it searches CC and public-domain media, not the open web of people photos.
url: https://search.creativecommons.org/
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Finding Creative-Commons and public-domain images (now via Openverse) with license and attribution details.
input: ''
output: ''
selectorsIn:
- name
selectorsOut:
- image
- metadata
status: degraded
pricing: free
opsec: passive
opsecNote: Keyword search over open repositories; no target interaction. Now redirects to Openverse (openverse.org); the old domain is effectively a legacy entry point.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Creative Commons / Openverse search over openly-licensed collections. It indexes license-free media, not arbitrary web photos — limited use for identifying a specific person.
missingPersonsRelevance: low
coverage: [global]
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Openverse
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# CC Search

> Creative Commons' openly-licensed media search (now Openverse) — built to find reusable images, not to find a specific person.

## When to use
You need a license-safe image for a flyer, report, or briefing, or you want to see whether a `name`/keyword appears in openly-licensed collections (Flickr CC, Wikimedia, museum sets). It is a poor fit for identifying a missing person, because it only indexes deliberately license-tagged media, not the broad social/news web where sighting photos live.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://search.creativecommons.org/ (it redirects to Openverse).
2. Enter keywords and filter by license, source, and media type.
3. Review results with their attribution and license terms.
4. Pivot: use a found image's source page/uploader as a weak `social-profile`/`metadata` lead, or just download a properly attributed illustration.

## Inputs → Outputs
- **In:** `name`/keyword query
- **Out:** `image` results + license/attribution `metadata`
- **Empty/negative result looks like:** no openly-licensed matches — expected for most private individuals, since their photos are not CC-licensed.

## Gotchas & OpSec
- Scope is openly-licensed media only; absence of a person here means almost nothing investigatively.
- The legacy domain redirects to Openverse — bookmark openverse.org going forward.
- Passive; safe to use without a sock account.

## Overlaps ("do both")
- For actually finding a person's photos, use general/reverse image search instead; reserve CC Search for license-clean illustration.

## Trust & verifiability
`trust: trusted` — official Creative Commons project. Reliable for what it does, but `missingPersonsRelevance: low` because its index is licensing-curated, not person-finding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cc-search |
| category | image-video-face |
| selectorsIn → selectorsOut | name → image, metadata |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
