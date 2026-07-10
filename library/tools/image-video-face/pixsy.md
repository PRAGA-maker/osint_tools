---
id: pixsy
name: Pixsy
description: Use when you have an `image` (ideally your own/authorised) and want to find everywhere it appears online via deep match monitoring — returns source pages/`social-profile`s reusing the image.
url: https://www.pixsy.com/
category: image-video-face
path:
- image-video-face
bestFor: Deep reverse-image match monitoring — finding all online uses of an image, with match volume its makers claim exceeds Google/TinEye.
selectorsIn:
- image
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free forever to monitor up to 500 images after signup; larger libraries and its takedown/legal-recovery services are paid. Requires an account.
opsec: passive
opsecNote: You upload images to Pixsy's account-based platform, which retains and indexes them. It does not contact the people whose pages it finds. Register with a sock-puppet identity, and don't upload sensitive/victim imagery you can't entrust to a commercial third party.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial image-monitoring/copyright service (200k+ users); its match engine is strong for finding reuse, but it is built for rights-holders monitoring their own images, not for arbitrary third-party face search.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- tineye
- google-reverse-image-search
- social-catfish-reverse-image-search
aliases:
- Pixsy
- pixsy.com
tags:
- image-search
- reverse-image
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Pixsy

> A copyright-enforcement platform whose engine is, for OSINT purposes, a powerful reverse-image monitor — it finds where an image is reused across the web, reportedly catching matches Google and TinEye miss.

## When to use
You have an `image` and want the most exhaustive list of where it appears online. Pixsy is built for photographers monitoring their own work, so it fits best when the image is yours or you're authorised to track it (e.g. a photo released in a missing-persons appeal, and you want to see every site republishing it). Its deep matching can surface reposts, scraper sites, and profiles that shallow reverse-image tools overlook.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at https://www.pixsy.com (free monitoring for up to 500 images).
2. Upload the `image`(s) to your library or connect a source platform.
3. Let Pixsy monitor the web; review the matches it reports — source pages and profiles reusing the image.
4. Use the free monitoring for intelligence; its takedown/legal-recovery features are a separate paid service you likely don't need for OSINT.
5. Pivot: matched pages may expose a `social-profile` or republisher; corroborate with quick reverse-image checks on `[[tineye]]` and `[[google-reverse-image-search]]`.

## Inputs → Outputs
- **In:** `image` (uploaded to your account)
- **Out:** source pages/`social-profile`s where the image appears
- **Empty/negative result looks like:** no matches after monitoring — the image may be original/unindexed; monitoring is ongoing, so results can accrue over time rather than instantly.

## Gotchas & OpSec
- Human-in-the-loop: **account required**; it is monitoring-oriented, not a paste-and-go instant search like TinEye.
- Designed for rights-holders' own images — using it to hunt arbitrary faces is off-label and slower than dedicated face engines.
- OpSec: passive toward the people it finds, but your uploads live in a commercial account — use a sock puppet and avoid sensitive imagery.

## Overlaps ("do both")
- Complements `[[tineye]]` and `[[google-reverse-image-search]]` for quick checks and `[[social-catfish-reverse-image-search]]` for identity-oriented matching; use Pixsy when you need exhaustive, ongoing reuse monitoring of one image.

## Trust & verifiability
`trust: community` — a reputable commercial service with a strong match engine, but oriented to copyright monitoring. Treat reported matches as real source pages to verify, and confirm any identity inference on the page itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pixsy |
| category | image-video-face |
| selectorsIn → selectorsOut | image → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
