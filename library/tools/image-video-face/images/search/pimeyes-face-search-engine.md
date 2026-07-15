---
id: pimeyes-face-search-engine
name: PimEyes Face Search Engine
description: Use when you have a `face`/`image` of someone and want to find other web pages showing that face — returns matched images and the source-page links (paid to unlock).
url: https://pimeyes.com/en
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: High-coverage reverse face search — locating other photos of the same person across the web and the pages hosting them.
selectorsIn:
- face
- image
selectorsOut:
- image
- social-profile
status: live
pricing: freemium
costNote: Free tier shows blurred thumbnails proving matches exist but WITHOUT source links; you must pay (from ~$29.99/mo) to see the URLs that make results actionable. Effectively paywalled for investigative use.
opsec: active
opsecNote: You upload a biometric face image to a third-party facial-recognition provider that indexes 10B+ images and logs searches. Do not upload images of yourself or non-targets; use a clean/sock-puppet account, and be aware some jurisdictions restrict biometric processing.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Widely-used, high-recall commercial face search — its results are real and among the best in coverage, but it is a controversial biometric service; treat each match as a lead to confirm at the source page.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- PimEyes
- reverse face search
tags:
- face-search
- facial-recognition
- reverse-image
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# PimEyes Face Search Engine

> The high-coverage reverse face search: upload a face and find where else on the web that same face appears — with the source pages (behind a paywall) to pivot from.

## When to use
You have a `face`/`image` of a subject and want to find *other* photos of the same person elsewhere on the web — different accounts, news pages, forums, dating profiles — to expand identity, confirm a match, or find a name. PimEyes indexes 10B+ images and matches on facial geometry, so it often surfaces appearances that reverse-*image* search (which needs the same photo) misses. It is one of the strongest tools for turning a single face into a web-wide presence map.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register an account and open https://pimeyes.com/en (use a research identity; you'll need to confirm you're searching lawfully).
2. Upload a clear, front-facing `face` crop of the subject.
3. Review matches: thumbnails of pages where a similar face appears, ranked by similarity.
4. On the free tier you see blurred thumbnails only — to get the **source URLs** (the actionable part) you need a paid plan.
5. Pivot: open source pages to harvest names, `social-profile`s, and context; feed newly found handles into username/social tools.

## Inputs → Outputs
- **In:** `face`/`image` (a photo containing the subject's face)
- **Out:** matched `image`s and their source pages → `social-profile`s/identity leads
- **Empty/negative result looks like:** few or no matches. A poor-quality, angled, or partially-occluded face suppresses results; a genuinely low-web-presence person may not appear. Try a better/alternate photo before concluding absence.

## Gotchas & OpSec
- **Paywall:** the free tier deliberately hides source links — you can confirm matches exist but not act on them without paying.
- **Active/biometric:** you upload a face to a facial-recognition service that logs it; only upload the target, use a clean account, and mind local biometric laws.
- Similarity matches can include look-alikes — always verify the match on the source page, don't assume identity.
- Human-in-the-loop: account + (for usable results) payment.

## Overlaps ("do both")
- Do alongside classic reverse-image search (finds the *same* photo's other appearances) — PimEyes finds the *same face* in *different* photos, so the two are complementary. Combine with face-comparison to confirm a candidate match.

## Trust & verifiability
`trust: community` — a mature, high-recall commercial engine whose matches are genuine, but it is a controversial biometric provider and its similarity results can include false matches. Confirm every hit at its source page before treating it as the same person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pimeyes-face-search-engine |
</content>
