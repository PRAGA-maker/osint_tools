---
id: news-myseldon
name: News Myseldon
description: Use when you have an `image` of a face and want to identify a public or semi-public figure (officials, politicians, local media figures) and pull their news mentions — returns a `name` plus biography and recent events.
url: https://news.myseldon.com/en/
category: image-video-face
path:
- image-video-face
bestFor: Naming lesser-known officials, politicians, or media figures from a photo and surfacing their news coverage.
selectorsIn:
- image
- face
selectorsOut:
- name
- social-profile
status: degraded
pricing: freemium
costNote: Free to run a photo search; the platform is a Russian news-aggregation/monitoring service (Seldon) whose deeper media-monitoring features are commercial. Site availability is intermittent.
opsec: active
opsecNote: You upload the subject's face to a third-party Russian service, which processes and may retain it. Use a sock-puppet session, strip metadata from the image first, and never upload a photo you are not willing to disclose to that operator.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: Operated by Seldon (a Russian news/analytics company); matches are best for people already covered in (largely Russian-language) news, and results skew to that media sphere, so verify any identification independently.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- search4faces
- pimeyes
- yandex-russia
aliases:
- Myseldon
- MySeldon News
- Seldon News face search
tags:
- Image Search and Identification
- Reverse Image Search Engines and automation tools
- face-recognition
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# News Myseldon

> A Russian news-aggregator with a face-search front end: upload a portrait and it tries to name the person from news photos, returning a bio, a popularity score, and recent coverage.

## When to use
You have an `image`/`face` and suspect the subject is a public or semi-public figure — an official, a politician, a business figure, a local TV anchor — especially in the Russian-language media sphere. Where mainstream face engines skew to celebrities, Myseldon is notably good at *minor* officials and regional figures because it indexes news photography. A hit gives you a `name`, a short biography, a popularity ranking, and links to the articles the face appears in.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://news.myseldon.com/en/ (it may redirect to myseldon.com; retry if the service is temporarily unavailable).
2. Use the face/photo search to upload a clear, front-facing crop of the subject's face.
3. Review the ranked candidate matches — each comes with a name, a popularity score, a brief biography, and linked news events.
4. Manually verify: compare the candidate's other photos against your source image before accepting any name. Treat the score as confidence, not proof.
5. Pivot: a confirmed `name` feeds people-search and social tools; the linked articles feed timeline and associate mapping.

## Inputs → Outputs
- **In:** `image` / `face` (a clear portrait crop)
- **Out:** `name`, biography, popularity score, and news-mention links (`social-profile` leads via bylines/coverage)
- **Empty/negative result looks like:** no confident candidates, or matches that are clearly different people — meaning the face is not a media-covered figure in its index, not that the person doesn't exist.

## Gotchas & OpSec
- Index bias: strongest for people with news coverage, especially Russian-language; ordinary private individuals will not be found here.
- Human-in-the-loop: matches require manual visual confirmation — face engines routinely return look-alikes.
- OpSec: this is **active** — you hand a Russian third party the subject's face. Sanitise the image, use a sock puppet, and never upload sensitive imagery.

## Overlaps ("do both")
- Complements `[[search4faces]]`, `[[pimeyes]]`, and `[[yandex-russia]]` — run the same face across several engines because each indexes a different slice (social-media crops, the open web, news photography); Myseldon uniquely covers minor officials.

## Trust & verifiability
`trust: unverified` — a commercial Russian aggregator with opaque matching and a regional bias; every identification must be independently corroborated before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | news-myseldon |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → name, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (manual-review) |
