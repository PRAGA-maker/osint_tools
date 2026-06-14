---
id: myheritage-photo-enhancer
name: MyHeritage Photo Enhancer
description: Use when a missing-person photo is blurry/low-res and you need an AI-sharpened, face-focused version for human review — returns an enhanced image; treat as cosmetic, not forensic.
url: https://www.myheritage.com/photo-enhancer
category: image-video-face
path:
- image-video-face
bestFor: AI enhancement/sharpening of blurry or low-resolution face photos for easier human recognition.
selectorsIn:
- image
- face
selectorsOut:
- image
- face
status: live
pricing: freemium
costNote: Free preview enhancements; downloading full-resolution results and bulk use typically require a MyHeritage account/subscription.
opsec: active
opsecNote: The photo is uploaded to MyHeritage servers and retained on their platform; do not upload sensitive case images you do not want stored by a genealogy company.
humanInLoop: true
humanInLoopReason:
- account-login
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: MyHeritage is a large, established genealogy company; the enhancer is a real, popular AI tool. But "enhancement" invents plausible detail and is NOT forensically reliable identification.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases: []
tags:
- photo-enhance
- face
source: osint4all
lastVerified: ''
enrichment: full
---

# MyHeritage Photo Enhancer

> A popular AI face-enhancement tool that sharpens blurry/low-res photos for easier human recognition — cosmetic improvement, not forensic identification.

## When to use
You have a poor-quality `image` of a missing person (old scan, low-res screenshot, distant shot) and you want a clearer, sharper version of the `face` to help a human recognise them or to publish in an appeal. It improves perceived clarity. Do **not** rely on its output to make an automated identity match — the AI fills in detail that may not be true to the real face.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.myheritage.com/photo-enhancer.
2. Upload the `image` (sign in / create a MyHeritage account; `account-login` is required to download full results).
3. The tool detects faces and applies AI sharpening/enhancement; preview the result.
4. Download the enhanced `image` (may require a subscription for full resolution).
5. Pivot: send the clearer face to a human reviewer or to a face-compare step like [[mxface-ai]] — but flag that it was AI-enhanced.

## Inputs → Outputs
- **In:** `image` containing a `face`
- **Out:** enhanced `image` / sharper `face`
- **Empty/negative result looks like:** no face detected, or output that looks "smoothed"/plastic — a sign the AI hallucinated features rather than recovering real detail.

## Gotchas & OpSec
- Human-in-the-loop: account login and human judgment of whether the enhancement is faithful are both required.
- **Forensic caveat:** AI enhancement is generative — it can alter facial features. Never present an enhanced image as proof of identity; use it only as a recognition aid and keep the original.
- OpSec: **active** — the photo is uploaded to and stored by MyHeritage; unsuitable for sensitive case material you need to keep private.

## Overlaps ("do both")
- Pairs with [[neural-network-image-super-resolution-and-enhancement]] (Let's Enhance) for upscaling and [[minipaint]] for manual crop/adjust; run the manual edit first, then enhancement, then a face check.

## Trust & verifiability
`trust: community` — built by a major, reputable genealogy company and widely used, but its enhancement is generative and not verifiable as a true likeness; outputs are leads/aids only.

---
## Metadata
| field | value |
|---|---|
| id | myheritage-photo-enhancer |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, face |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
