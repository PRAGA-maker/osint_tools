---
id: pimeyes-2
name: PimEyes
description: Use when you have a clear face photo and need to find where else that face appears online — returns matched source pages you can pivot to names and profiles.
url: https://pimeyes.com
category: image-video-face
path:
- image-video-face
bestFor: Web-wide reverse face search to locate other photos of the same person.
selectorsIn:
- face
- image
selectorsOut:
- image
- social-profile
- name
status: live
pricing: freemium
costNote: Free search shows blurred/partial results; viewing source URLs and running alerts requires a paid subscription (monthly plans).
opsec: active
opsecNote: The face image is uploaded to PimEyes' biometric search service; full results require login and payment, increasing your footprint with the provider.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: PimEyes is a widely-used commercial facial-recognition search engine. Powerful and well-known, but privacy/ethics-sensitive and source links are paywalled; subject to legal/usage restrictions in some jurisdictions.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- pimeyes.com
tags:
- image-search
- face
- facial-recognition
source: awesome-osint
lastVerified: ''
enrichment: full
relatedTools:
- pimeyes-face-search-engine
---

# PimEyes

> A powerful commercial reverse-face search engine — upload a face and find other places that same face appears across the public web.

## When to use
You have a clear `face`/`image` of a missing person (or an unidentified individual) and want to find other online photos of them to recover names, profiles, and recent activity. This is one of the highest-yield face tools for missing-persons work. Tie-in: `face` in, `image` + `social-profile` + `name` (after pivoting through source pages) out.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://pimeyes.com and upload a clear, front-facing `face` photo.
2. Run the search; the free tier shows blurred/partial thumbnails of matches.
3. To open the source URLs (where you actually recover identity/profile data), subscribe and log in.
4. Open each source page; extract names, usernames, and profile links; verify it is the same person.
5. Pivot recovered `social-profile`/`name` into people-search and social tools; set alerts for new appearances if subscribed.

## Inputs → Outputs
- **In:** `face`, `image`
- **Out:** `image` (matched photos), `social-profile`, `name`
- **Empty/negative result looks like:** few or no matches, or only low-confidence faces — common for low-online-presence subjects; corroborate before concluding.

## Gotchas & OpSec
- Human-in-the-loop: requires an account, and the meaningful output (source URLs) sits behind a paywall.
- OpSec: active — the face image is uploaded and processed by a third-party biometric provider, and your account is tied to the query. Use a dedicated/sock account where policy permits.
- Ethical/legal: facial recognition is restricted or scrutinized in some jurisdictions and platforms; ensure your use is authorized for the case.

## Overlaps ("do both")
- Same service as [[pimeyes-face-search-engine]] (the /en entry). Pairs with [[pictriev]] for cheap similarity checks and with Yandex reverse image as a complementary net.

## Trust & verifiability
`trust: community` — a real, widely-used commercial face-search engine; reliability is good but results are paywalled and matches still require human confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pimeyes-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → image, social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
