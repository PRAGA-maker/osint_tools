---
id: facecheck-facial-recognition-search
name: FaceCheck Facial Recognition Search
description: Use when you have a face photo of a missing person and need to find public web/social profiles, news, and forum posts showing the same face.
url: https://facecheck.id/
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Reverse facial recognition across social media, news, and the open/dark web.
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- name
- face
status: live
pricing: freemium
costNote: Searching is free; viewing/unblurring full result links and source URLs requires paid credits.
opsec: active
opsecNote: You upload the target's face to a third-party biometric engine; the image and query are processed/retained server-side. Use a sock-puppet account and never upload sensitive case imagery you cannot disclose.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Widely used and discussed in the OSINT community as one of the stronger consumer face-search engines; results vary by person and require human verification.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- pimeyes
- faceseek-face-search-engine
aliases:
- FaceCheck.ID
tags:
- facial-recognition
- reverse-image
source: arf-seed
lastVerified: ''
enrichment: full
---

# FaceCheck Facial Recognition Search

> Consumer face-search engine that matches an uploaded face against social media, news sites, and open/dark-web sources.

## When to use
You have an `image` containing a clear `face` of the missing person (or an unidentified associate) and want to find `social-profile` links, a `name`, or any web page showing the same person. Strong for confirming aliases or locating recent photos when name-based search has stalled.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://facecheck.id/ and create/log in to an account (sock puppet recommended).
2. Upload a tight, front-facing crop of the `face`. Multiple angles/photos improve recall.
3. Run the search; it returns blurred thumbnails ranked by a similarity score.
4. Strong candidates score roughly 80+; unblurring full thumbnails and source URLs consumes paid credits.
5. Pivot: open the source page, confirm identity, then feed the discovered `social-profile`/`name` into username and people-search tools.

## Inputs → Outputs
- **In:** `image` / `face`
- **Out:** `social-profile`, `name`, `face` matches with similarity scores and source links.
- **Empty/negative result looks like:** all candidates with low scores (sub-50) and no consistent identity across hits — treat as no match, not confirmation.

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHA on signup; meaningful source links sit behind a credit paywall.
- OpSec: this is **active** — biometric upload to a third party. Assume the image is retained. Verify every "match" manually; high scores still produce look-alike false positives.

## Overlaps ("do both")
- Pairs with `[[pimeyes]]` and `[[faceseek-face-search-engine]]`; each indexes different corpora, so run the face across all three and union the hits.

## Trust & verifiability
`trust: community` — popular, frequently reviewed OSINT face engine, but a commercial black box with no published accuracy figures. Always corroborate identity from a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facecheck-facial-recognition-search |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, name, face |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
