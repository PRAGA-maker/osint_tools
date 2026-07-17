---
id: search4faces-com-ch00
name: Search4Faces — Clubhouse
description: Use when you have a `face`/`image` of a person and want to match it against Clubhouse profile avatars — returns candidate Clubhouse `social-profile`s for the face.
url: https://search4faces.com/ch00/index.html
category: social-networks
path:
- social-networks
bestFor: Reverse face search against a database of ~4.6M Clubhouse user avatars to find a matching profile.
selectorsIn:
- face
- image
selectorsOut:
- social-profile
- face
status: live
pricing: freemium
costNote: Free tier allows a limited number of searches; more searches/higher quality require a paid subscription. No login needed to run a basic search.
opsec: active
opsecNote: You upload the target's face image to a Russia-based service, which retains and processes it. Assume the image and your IP are logged. Use a sock-puppet browser/VPN, upload only a cropped face (no surrounding metadata), and never upload images you're not authorised to search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known Russia-based facial-recognition tool cited in Bellingcat's toolkit. The Clubhouse dataset is a partial 2021-era snapshot, so matches are real leads but coverage is incomplete and dated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- search4faces
- search4faces-com
aliases:
- Search4Faces Clubhouse
- search4faces ch00
tags:
- face-search
- clubhouse
- facial-recognition
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Search4Faces — Clubhouse

> The Clubhouse-avatar index of Search4Faces: upload a face and see whether it matches one of ~4.6M scraped Clubhouse profile pictures.

## When to use
You have a `face` or `image` of an unknown (or claimed) person and want to test whether they had a Clubhouse account, by matching the photo against Search4Faces' scraped avatar database. Facial recognition can link an anonymous photo to a named social profile — a powerful identity pivot when other selectors are exhausted. This specific index is the Clubhouse dataset; Search4Faces also has VK, Odnoklassniki, and TikTok indexes for the same face.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search4faces.com/ch00/index.html in a sock-puppet browser (VPN recommended).
2. Upload a clear, front-facing crop of the target `face`.
3. Adjust the facial landmarks if prompted, then run the search.
4. Review ranked candidate avatars with similarity scores; open a promising match to its Clubhouse profile name/handle.
5. Pivot: a matched avatar gives you a `social-profile`/handle to run through username-search and cross-platform tools. Also run the same face through the VK/TikTok indexes for broader coverage.

## Inputs → Outputs
- **In:** `face` / `image` (a face crop)
- **Out:** candidate Clubhouse `social-profile`s ranked by facial similarity
- **Empty/negative result looks like:** no high-similarity matches — the person may not be in the (partial, 2021-era) Clubhouse snapshot, or the photo angle/quality is poor. Absence is not proof they never used Clubhouse.

## Gotchas & OpSec
- The Clubhouse dataset is a partial, historical (~2021) scrape — coverage is incomplete and won't reflect recent accounts.
- OpSec: **active** — you hand a target's face to a Russia-based operator. Treat uploads as retained; use only images you're authorised to search, and never upload evidence you need to keep confidential.
- Similarity scoring can surface look-alikes; confirm a match with a second signal before asserting identity.

## Overlaps ("do both")
- Pairs with `[[search4faces]]` and `[[search4faces-com]]` — run the same face across the VK, Odnoklassniki and TikTok indexes, since the person may appear in one dataset but not the Clubhouse one.

## Trust & verifiability
`trust: community` — a widely-cited (Bellingcat toolkit) facial-recognition service, but results are probabilistic matches against an incomplete, dated dataset. Every hit is a lead to verify, not a confirmed identification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search4faces-com-ch00 |
| category | social-networks |
| selectorsIn → selectorsOut | face, image → social-profile, face |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
