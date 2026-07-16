---
id: facecheckid
name: FaceCheckID
url: https://facecheck.id/
category: people-search
path:
- people-search
- general-people-search
description: Use when you have a `face`/`image` and want to identify the person — returns matching faces across social media, news, mugshots and sex-offender sources as `social-profile` links.
bestFor: Reverse face search across social, news, mugshot and offender sources to put a name/profile to an unknown face.
selectorsIn:
- face
- image
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free searches return limited/blurred results; buying credits unlocks more matches per search and clearer thumbnails. Account optional to start.
opsec: active
opsecNote: You upload the target's face to a commercial facial-recognition engine that processes and logs it server-side. This is a disclosure of the image; use a sock-puppet account and avoid uploading sensitive/evidential faces you wouldn't want retained. The subject is not notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely-used face-search engine with real reach into social/news/mugshot imagery; matches carry confidence ratings and its own disclaimer warns unrelated people look alike — treat hits as leads to confirm.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- FaceCheck.ID
- facecheck
tags:
- face-search
- reverse-image
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- facecheck-facial-recognition-search
---

# FaceCheckID

> A reverse face-search engine — upload a face and it hunts matching faces across social media, news, blogs, mugshots and sex-offender databases, ranked by confidence.

## When to use
You have a `face`/`image` of an unknown person and need to put an identity to it. FaceCheckID indexes imagery the general reverse-image engines miss (mugshots, offender registries, scam-warning sites, social profiles), so it's a strong complement to `[[pimeyes-com]]`/Yandex when a face is your only selector — common in catfish, scam, and unidentified-person cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://facecheck.id/ (ideally in a sock-puppet browser).
2. Upload a clear, front-facing crop of the target `face`.
3. Run the search; review ranked results with confidence bands (weak → certain) and blurred/limited free thumbnails.
4. Buy credits if the free preview is too limited, then open promising matches to confirm identity by context (bio, cross-links).
5. Pivot: a confirmed `social-profile`/`name` feeds username and people-search; a mugshot/offender hit feeds public-records lookups.

## Inputs → Outputs
- **In:** `face` / `image`
- **Out:** ranked matching `social-profile`s, `name`s, news/mugshot pages
- **Empty/negative result looks like:** only low-confidence ("weak") matches or unrelated lookalikes — the engine explicitly warns many people look alike, so a weak match is NOT an identification. Treat sub-"strong" results as noise.

## Gotchas & OpSec
- Confidence matters: only high-confidence matches, corroborated by context, count as leads. Never treat a weak match as the person.
- Free results are deliberately limited/blurred; full value needs paid credits.
- OpSec: **active** — you upload the face to a commercial engine that retains/logs it; use a puppet account and avoid sensitive images. Per its own terms, don't use it for employment/tenant/credit decisions.

## Overlaps ("do both")
- Pairs with `[[pimeyes-com]]` and Yandex reverse image via `[[search-by-image-chrome-google-com]]` — each indexes different face imagery; run several and confirm the person appears consistently.

## Trust & verifiability
`trust: community` — an effective, widely-used face engine, but a commercial black box whose matches are probabilistic; every hit must be confirmed by independent context before you attach a name.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facecheckid |
| category | people-search |
| selectorsIn → selectorsOut | face, image → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
