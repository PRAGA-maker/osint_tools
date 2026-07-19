---
id: iqdb-org
name: IQDB.org
description: Use when you have an `image` that looks like anime/manga/game art and want its source — returns matching booru-database entries (source, artist tags) via reverse image search.
url: https://iqdb.org/
category: image-video-face
path:
- image-video-face
bestFor: Reverse-image-searching anime/manga/game artwork to find its original source and tags across booru databases.
selectorsIn:
- image
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, no account, no payment; upload an image (up to 8MB) or paste a URL.
opsec: passive
opsecNote: The image you submit is sent to IQDB's servers and matched against public booru databases. The image owner is not notified. Avoid uploading sensitive/private images you don't want a third party to process; use a research browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running community reverse-image engine specialized in anime art databases (Danbooru, Gelbooru, yande.re, etc.); reliable for that niche, useless for photos of real people or places.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- IQDB
- Multi-service image database
tags:
- Image Search and Identification
- Reverse Image Search Engines and automation tools
- anime
source: cyb-detective
lastVerified: '2026-07-19'
---

# IQDB.org

> A reverse image search built for anime/manga/game art — feed it an illustration and it finds the source and tags across the major "booru" databases.

## When to use
You have an `image` that is anime/manga/game artwork — an avatar, a shared illustration, a profile picture drawn in that style — and you want its origin: the original source post, the artist, and descriptive tags. IQDB searches eight booru databases (Danbooru, Konachan, yande.re, Gelbooru, Sankaku, e-shuushuu, Zerochan, Anime-Pictures) at once. In an investigation this is niche but real: an avatar's source or artist can link accounts that reuse the same art, or reveal a fandom a subject belongs to. It is NOT for photographs of real people, faces, or places — use a general reverse-image engine for those.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://iqdb.org/ and either upload the image (JPEG/PNG/GIF ≤8MB) or paste its URL.
2. Optionally enable "ignore colors" for recolored variants; submit.
3. Read the ranked matches with similarity scores; open the source booru entry for artist, tags, and the original post.
4. Pivot: an identified source/artist can link a `social-profile` that reuses the art, or place the subject in a specific fandom/community.

## Inputs → Outputs
- **In:** `image` (anime/manga/game-style artwork)
- **Out:** matching booru source entries, artist/tags → a linkable `social-profile`/source
- **Empty/negative result looks like:** no matches or only low-similarity noise — meaning the image isn't in these anime databases (very common for real photos or original/private art); switch to a general reverse-image engine.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Strictly for anime/art databases — it will NOT match photographs of real people or locations.
- Low similarity scores are false-positive prone; only trust high-confidence, verifiable matches.

## Overlaps ("do both")
- Pairs with general reverse-image engines (Google/Yandex/TinEye) and with SauceNAO — those cover photos and broader art indexes; IQDB is the booru-specialized net.

## Trust & verifiability
`trust: community` — an established niche community engine; matches link to public source databases you can verify directly, within its anime-art scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iqdb-org |
| category | image-video-face |
| selectorsIn → selectorsOut | image → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
