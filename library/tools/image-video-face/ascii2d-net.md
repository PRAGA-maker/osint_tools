---
id: ascii2d-net
name: ascii2d.net
description: Use when you have an `image` (especially artwork, avatars, or anime-style images) and want to find its source and higher-res copies — returns `social-profile`/`domain` source links and `metadata-exif`.
url: https://ascii2d.net
category: image-video-face
path:
- image-video-face
bestFor: Reverse image search that excels at illustrations, avatars, and anime/2D art, matching by both colour and feature ("bag") hashes to find the original posting.
selectorsIn:
- image
selectorsOut:
- social-profile
- domain
- metadata-exif
status: live
pricing: free
costNote: Free to use; browser extensions for Chrome/Firefox/Edge. No account.
opsec: passive
opsecNote: You upload an image to a Japanese third-party service — the query hits ascii2d, not the image's owner, so it's passive toward the subject. Avoid uploading sensitive/case-identifying imagery to a public service; strip anything you don't want stored.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known, long-running Japanese reverse-image service widely used in OSINT for art/avatar sourcing; results are matches to index, to be verified visually.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ascii2d
- 2D reverse image search
tags:
- Image Search and Identification
- Reverse Image Search Engines and automation tools
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# ascii2d.net

> A Japanese reverse-image engine that shines where Google/TinEye stumble — illustrations, avatars, and anime-style art — matching on both colour and "feature" hashes to find where an image originally appeared.

## When to use
You have an `image` — especially a profile avatar, a piece of artwork, a fan image, or a manga/anime-style picture — and want its source: the original posting (often on Twitter/X, Pixiv, or a blog), a higher-resolution copy, or the artist. Because subjects frequently reuse a distinctive avatar across platforms, tracing that avatar to its source and other appearances can link accounts and reveal a real handle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ascii2d.net and either paste an image URL or upload a file.
2. It returns two result sets — a **colour** search and a **feature/"bag"** search; check both, as they surface different matches.
3. Open the source links (Pixiv, Twitter/X, blogs) to find the original poster, artist, or highest-resolution version.
4. Note any EXIF/image properties ascii2d exposes.
5. Pivot: a source account/handle feeds username search; the same avatar found on other platforms links profiles.

## Inputs → Outputs
- **In:** `image` (URL or upload)
- **Out:** `social-profile`/`domain` source links to where the image appears, the artist/poster, higher-res copies, and any `metadata-exif` shown.
- **Empty/negative result looks like:** no matches in either colour or feature search — the image isn't in ascii2d's index (which skews toward East-Asian art/social platforms); try Google Lens, Yandex, or TinEye for photographic images.

## Gotchas & OpSec
- Strongest for illustrations/avatars and East-Asian sources; for real-world photos, Yandex/Google Lens usually beat it — run those too.
- Two search modes give different hits; always check both.
- OpSec: passive; but don't upload sensitive case imagery to a public third-party service.

## Overlaps ("do both")
- Complements Yandex, Google Lens, and TinEye — ascii2d owns the art/avatar niche those miss; combine them so an avatar-to-account link isn't lost to one engine's blind spot.

## Trust & verifiability
`trust: community` — an established community tool; matches are index hits you confirm by eye against the linked source, not authoritative attributions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ascii2d-net |
| category | image-video-face |
| selectorsIn → selectorsOut | image → social-profile, domain, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
