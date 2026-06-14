---
id: lenso-ai
name: Lenso.ai
description: Use when you have a face or object image and want AI-powered reverse search across the web — returns visually and facially similar matches with source pages.
url: https://lenso.ai/
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: AI reverse-image and face search that finds the same/similar people, places and objects across the open web.
input: Image or face photo upload
output: Visual matches, related occurrences, and similarity-ranked results
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- name
- geolocation
status: live
pricing: freemium
costNote: Free tier with limited searches; paid plans/credits unlock more results, face mode and higher quotas.
opsec: active
opsecNote: Uploads target imagery to an external AI service for analysis and indexing; assume the photo is transmitted and may be retained. Use a sock-puppet account and avoid sensitive case photos you can't share with a vendor.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Widely cited in the OSINT community as a strong AI reverse-image/face engine. Match quality is good but not authoritative — confirm any identity before acting.
missingPersonsRelevance: high
coverage: [global]
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases: []
tags:
- reverse-image
- face-search
source: arf-seed
lastVerified: ''
enrichment: full
---

# Lenso.ai

> AI-driven reverse image and face search — upload a photo and it finds visually/facially similar matches across the web, grouped by people, places, duplicates and related.

## When to use
You have a `face` or `image` of a missing/unidentified person and want to find where that face appears online — social profiles, news, forum posts. Lenso's AI face mode often surfaces matches that generic engines (Google/Bing) miss, making it a primary candidate-generator. Use when you need to turn a photo into a `name` / `social-profile` lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lenso.ai/ and (for face mode / more results) create or log into a sock-puppet account.
2. Upload the photo (`selectorsIn`: image, face) and choose the relevant search mode (faces / places / related).
3. Review the similarity-ranked clusters; open the source page behind each promising match (`selectorsOut`: social-profile, name, geolocation from place matches).
4. The free tier limits results — a paywall on additional matches is normal, not a failure.
5. Pivot: confirmed matches feed face verification (e.g. `[[kairos-com]]`) and social/people-search enumeration.

## Inputs → Outputs
- **In:** `image`, `face`
- **Out:** `social-profile`, `name`, and `geolocation` from place matches, each with a source URL.
- **Empty/negative result looks like:** only generic/low-similarity clusters with no clear face cluster — common for low-resolution or heavily-cropped inputs.

## Gotchas & OpSec
- Treat matches as leads: AI similarity is not identity confirmation — verify each candidate independently.
- Human-in-the-loop: account login and a partial paywall gate the best results.
- OpSec: active — your image is uploaded to a third-party AI service; use a sock puppet and a clean IP.

## Overlaps ("do both")
- Run the same face through Yandex/Google reverse search (e.g. via `[[labnol-org]]`) for coverage, then score top candidates with a 1:1 verifier like `[[kairos-com]]`.

## Trust & verifiability
`trust: community` — strong, widely-used AI face engine, but similarity ranking can return false positives; corroborate before acting on any identification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lenso-ai |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, name, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
