---
id: saucenao
name: SauceNAO
description: Use when you have an `image` (especially art/anime/illustration or an avatar) and want its origin — returns the source posting, artist, and duplicate appearances (`social-profile`/`name` of the creator).
url: https://saucenao.com/
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Tracing an illustration, anime frame, or avatar back to its original source and creator.
input: Image upload or image URL
output: Likely source links, matching images, and similarity metrics
selectorsIn:
- image
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free tier allows a limited number of searches per day/per 30s (short + long rate limits). A paid account raises the limits and unlocks API access.
opsec: passive
opsecNote: You upload the image or an image URL to SauceNAO's index — the image transits a third party, but nothing reaches the target. Strip EXIF from sensitive uploads; the subject is never notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running, well-known reverse-image index specialised in art/anime/booru sources. Reliable within its domain; it indexes creative-media databases (Pixiv, Danbooru, DeviantArt, etc.) rather than the general web.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- yandex-images
- tineye
- google-lens
aliases:
- SauceNAO
- saucenao.com
tags:
- reverse-image
- art
- avatar-tracing
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# SauceNAO

> A reverse-image engine tuned for illustrations, anime, and avatars — paste an image and it finds the original posting, the artist, and everywhere it's been re-used.

## When to use
Your subject uses an illustrated/anime avatar, or you have an art `image` and need its source. Where Google/Yandex struggle with drawn/stylised images, SauceNAO indexes the creative databases (Pixiv, Danbooru, DeviantArt, Twitter/X art posts, etc.) and returns the original post — which often names the artist (`name`) and links their `social-profile`. A shared avatar traced to its Pixiv/Twitter origin can reveal an account the subject follows, made, or lifted the image from.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://saucenao.com/.
2. Upload the `image` or paste its URL and search.
3. Read results ranked by similarity %: each hit shows the source database, a link to the original posting, and the creator/handle.
4. Prioritise high-similarity hits (>80%); open the source posting to capture the artist `name`/`social-profile`.
5. Pivot: the source account feeds username/social work; if SauceNAO misses (photographic image), fall back to `[[yandex-images]]`/`[[tineye]]`/`[[google-lens]]`.

## Inputs → Outputs
- **In:** `image` (upload or URL) — best on illustrations/avatars
- **Out:** ranked source matches → original posting, creator `name`, linked `social-profile`
- **Empty/negative result looks like:** low-similarity results or "no results above threshold" — the image isn't in its art databases (common for ordinary photos). Switch to a general reverse-image engine; don't conclude the image has no source.

## Gotchas & OpSec
- Human-in-the-loop: none, but watch the rate limits (short-term and daily) on the free tier — space out searches or use an account.
- OpSec: **passive** — a reverse-image lookup; the target sees nothing. Scrub EXIF from anything sensitive before uploading.
- It is domain-specific: excellent for art/anime, weak for real-world photos and faces.

## Overlaps ("do both")
- Pairs with `[[yandex-images]]`, `[[tineye]]`, and `[[google-lens]]` — SauceNAO owns the art/avatar niche; the others cover photographic and general-web imagery. For an avatar of unknown type, run SauceNAO first, then a general engine.

## Trust & verifiability
`trust: community` — a dependable, specialised index. Matches are strong leads within art/anime sources; confirm the artist/account by opening the original posting, and switch tools for non-illustrated images.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | saucenao |
| category | image-video-face |
| selectorsIn → selectorsOut | image → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
