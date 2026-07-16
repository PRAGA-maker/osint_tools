---
id: rootabout
name: RootAbout
description: Use when you have an `image` and want to reverse-search it against the Internet Archive and Open Library (plus Google) — returns matching archived/book `image`s that mainstream engines miss.
url: http://rootabout.com/
category: image-video-face
path:
- image-video-face
bestFor: Reverse-image search across Internet Archive and Open Library holdings — a different corpus than Google/Yandex/TinEye.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: free
costNote: Free to use; no account required.
opsec: passive
opsecNote: You upload/point to an image and it queries archive corpora; the search is passive and not tied to any target. Avoid uploading case-sensitive imagery to a third-party site if privacy is critical.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small, long-lived reverse-image tool (Bellingcat-listed) that searches Internet Archive/Open Library; niche but genuinely covers a corpus the big engines don't.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- rootabout.com
tags:
- bellingcat-toolkit
- reverse-image-search
- internet-archive
source: bellingcat-toolkit
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- rootabout-wayback-reverse-image
---

# RootAbout

> A reverse-image search that queries the Internet Archive and Open Library (and Google) — reach it when mainstream reverse-image engines come up empty on historical or book/archive imagery.

## When to use
You have an `image` and the big engines (Google Lens, Yandex, TinEye) return nothing — often the case for older photos, book scans, or archived/digitized material. RootAbout searches the Internet Archive and Open Library corpora, so it can match an image to a scanned book, archived page, or historical collection that the general web index doesn't cover. A complement, not a replacement, for the mainstream tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://rootabout.com/.
2. Load the picture to search (with optional rotate/flip adjustments) and pick which services to query (Internet Archive, Open Library, Google).
3. Set result count (5/10/20/50) and run.
4. Review matches — especially any Internet Archive/Open Library hits pointing to a source document or collection.
5. Pivot: an archive/book match → the source item's metadata (author, date, context); combine with mainstream reverse-image for full coverage.

## Inputs → Outputs
- **In:** `image`
- **Out:** matching `image`s from Internet Archive / Open Library / Google, with links to source items
- **Empty/negative result looks like:** no matches — expected for ordinary modern photos not in archive corpora; a miss here doesn't mean the image is absent from the wider web (check the big engines too).

## Gotchas & OpSec
- Niche corpus: best for historical/book/archive imagery, weak for typical social-media photos.
- Small independent tool — availability can vary; verify it loads before relying on it.
- Uploading sensitive images shares them with a third party; weigh privacy.

## Overlaps ("do both")
- Pairs with `[[tineye-com]]`, Google Lens, and Yandex — always run those too; RootAbout adds the Internet Archive/Open Library angle they lack.

## Trust & verifiability
`trust: community` — a small Bellingcat-listed tool; matches are genuine archive/book hits, but coverage is narrow, so treat it as one lens in a multi-engine reverse-image workflow.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rootabout |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
