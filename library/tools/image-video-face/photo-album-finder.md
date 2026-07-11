---
id: photo-album-finder
name: Photo Album Finder (Google CSE)
description: Use when you have a `name`, `username`, or `email` and want to find public photo albums/galleries hosting that person's images across photo-sharing sites — returns image, social-profile and metadata-exif leads.
url: https://cse.google.com/cse/publicurl?cx=013991603413798772546:bldnx392j6u
category: image-video-face
path:
- image-video-face
bestFor: Keyword-searching a curated set of photo-hosting/album sites for a person's public galleries.
selectorsIn:
- name
- username
- email
selectorsOut:
- image
- social-profile
- metadata-exif
status: live
pricing: freemium
costNote: Free to use in the browser. It is a Google Custom Search Engine, so results are ad-supported Google results restricted to a preset list of photo sites; no account needed.
opsec: passive
opsecNote: Runs as a normal Google search, so it does not touch the target or the hosting sites directly beyond ordinary indexing. Only your query and IP reach Google. Search from a sock-puppet if you don't want the query tied to you.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A community-configured Google CSE (owner-defined site list). Coverage depends entirely on the CSE's configuration and Google's index, and can silently degrade as the config ages.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Photo Album Finder CSE
- Google Custom Search photo albums
tags:
- image-search
- photo-albums
- google-cse
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Photo Album Finder (Google CSE)

> A pre-built Google Custom Search Engine scoped to photo-hosting and album sites — search a name or handle to surface someone's public galleries.

## When to use
You have a `name`, `username`, or `email` and want to find public photo albums, galleries, or image collections that a person has posted to dedicated photo-sharing sites (the kind of hosts that fall outside a plain Google image search). Use it to locate original, un-stripped image files (which may still carry EXIF/`metadata-exif`) and additional photos of a subject beyond their main social profiles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE: https://cse.google.com/cse/publicurl?cx=013991603413798772546:bldnx392j6u
2. Enter your `selectorsIn` — a full `name` in quotes, a `username`, or an `email` — and consider adding a place/event keyword to cut noise.
3. Review the results, which are Google hits limited to the CSE's configured photo-site list. Open promising albums.
4. Manually verify each album belongs to your subject (same-name and common-handle collisions are frequent), then download originals to inspect for embedded metadata.
5. Pivot: an album URL/handle feeds username sweeps and social-profile enrichment; downloaded originals feed `[[photome-exif-metadata-viewer]]` for GPS/EXIF.

## Inputs → Outputs
- **In:** `name`, `username`, or `email`
- **Out:** links to photo albums/galleries (`image` sources), `social-profile` handles, and `metadata-exif` leads via downloadable originals
- **Empty/negative result looks like:** no results or only generic same-name pages — the CSE's site list may not cover where your subject posts, or the config has aged out; fall back to a general image search.

## Gotchas & OpSec
- Human-in-the-loop: results need manual disambiguation — a name/handle match is not identity confirmation.
- The value hinges on the CSE owner's site list, which you cannot see or edit and which may be stale; don't treat empty results as authoritative.
- Passive: this is an ordinary Google query; the target isn't notified. Use a sock-puppet browser to avoid tying the search to you.

## Overlaps ("do both")
- Pairs with `[[photome-exif-metadata-viewer]]` — this finds the albums/original images; PhotoME extracts GPS/EXIF from the files you download.
- Pairs with a general reverse-image search — the CSE finds galleries by name/handle, reverse-image finds copies of a specific photo the CSE would miss.

## Trust & verifiability
`trust: community` — a third-party-configured Google CSE. The underlying results are Google's (reliable), but the scope is an opaque, owner-defined site list that determines everything the tool can and cannot find.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | photo-album-finder |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username, email → image, social-profile, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
