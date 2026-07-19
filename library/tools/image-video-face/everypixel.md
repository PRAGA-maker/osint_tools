---
id: everypixel
name: EveryPixel
description: Use when you have an `image` and want to find it across stock-photo agencies (and check if it's AI-generated) — returns matching stock listings and an AI-image likelihood score.
url: https://www.everypixel.com/
category: image-video-face
path:
- image-video-face
bestFor: Reverse-image search across ~50 stock agencies to spot when a "personal" photo is actually stock, plus an AI-generated-image detector.
selectorsIn:
- image
selectorsOut:
- image
- metadata-exif
status: live
pricing: freemium
costNote: Reverse stock-image search and the AI-image detector are free to use in-browser; heavy/programmatic use via the API is paid.
opsec: passive
opsecNote: You upload the query image to a third party (EveryPixel) — don't upload sensitive originals; crop to the relevant region. The search is passive toward any subject; no one is notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial stock-image aggregator with an AI-detection feature; useful and generally accurate for stock matching, but the AI-detector is probabilistic and its index is limited to stock catalogues.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Every Pixel
- everypixel.com
tags:
- Image Search and Identification
- Reverse Image Search Engines and automation tools
- ai-detection
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# EveryPixel

> A reverse-image search across ~50 stock-photo agencies, plus an AI-image detector — the fast way to catch when a profile/"personal" photo is really stock or AI-generated (a classic catfish/fake-account tell).

## When to use
You have an `image` — a dating/social profile photo, a supposed selfie, a "witness" photo — and you suspect it isn't genuine. EveryPixel checks whether the image appears in stock catalogues (meaning it's a generic stock shot, not a real person's own photo) and estimates whether it's AI-generated. Both are strong signals of a fake or stolen identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.everypixel.com/ and use the reverse-image search (upload or paste an image URL).
2. Review stock matches — a hit means the photo is a licensed stock image, not the subject's own.
3. Use the AI-image detector to get an AI-generated likelihood score for the same image.
4. Combine the two signals: stock match OR high AI-score → treat the identity as likely fake.
5. Pivot: if it's stock/AI, discount the photo and refocus on other identifiers; if it's not, run mainstream reverse-image engines (Google/Yandex/TinEye) for real matches.

## Inputs → Outputs
- **In:** `image` (a photo to test)
- **Out:** stock-agency matches, an AI-generated likelihood score, and image `metadata-exif`-style attributes
- **Empty/negative result looks like:** no stock match and a low AI-score — the image isn't stock or obviously AI, but that doesn't prove it's genuinely the subject; run other reverse-image engines, which cover the open web this doesn't.

## Gotchas & OpSec
- Index is stock catalogues, not the whole web — a "no match" doesn't clear the image; it only rules out stock.
- The AI-detector is probabilistic — treat scores as evidence, not proof.
- OpSec: you upload the image to a third party; avoid sensitive originals.

## Overlaps ("do both")
- Pairs with Google/Yandex/TinEye reverse search and dedicated AI-image detectors — EveryPixel nails the stock/AI question, while general engines find real-world reuse of the photo.

## Trust & verifiability
`trust: unverified` — a commercial aggregator; stock matches are verifiable by opening the listed source, while the AI-score is an estimate to weigh alongside other signals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | everypixel |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image, metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
