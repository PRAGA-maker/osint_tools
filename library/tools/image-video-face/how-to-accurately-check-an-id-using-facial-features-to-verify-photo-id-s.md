---
id: how-to-accurately-check-an-id-using-facial-features-to-verify-photo-id-s
name: How to Accurately Check An ID Using Facial Features To Verify Photo ID's
description: Use when you need a human reference method for comparing a face against a photo ID — this is an instructional article on facial-feature comparison, not an automated tool.
url: https://joellesteele.com/face-accurately-check-photo-ID.html
category: image-video-face
path:
- image-video-face
bestFor: Learning a manual facial-feature comparison method to judge whether a face matches a photo ID.
selectorsIn:
- face
- image
selectorsOut:
- physical-description
status: live
pricing: free
costNote: Free to read; it is a web article.
opsec: passive
opsecNote: Reading a static reference page leaks nothing about your subject. The actual comparison you perform is offline by eye.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: An instructional article by Joelle Steele on manual facial comparison, listed under "Facial Comparison Sites" on uk-osint.net. It is reference material / methodology, not an automated matching tool; accuracy of the method is not independently validated here.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- facialcomparison
- Facial Comparison Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# How to Accurately Check An ID Using Facial Features To Verify Photo ID's

> An instructional article on manually comparing a person's face to a photo ID by examining stable facial features — a methodology reference, not an automated tool.

## When to use
You have a `face` photo and a photo ID (or two images you suspect are the same person) and need a structured, by-eye method to judge whether they match — focusing on features that don't change (ear shape, eye spacing, nose bridge, philtrum) rather than hairstyle or weight. Useful background reading when no automated face-matching tool is available or admissible, and for documenting how you reached a manual comparison conclusion.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the article to learn which facial landmarks are reliable for comparison.
2. Apply the method by eye to your two images: compare stable structural features, ignore easily-changed traits.
3. Record your feature-by-feature reasoning as a `physical-description` and a confidence note — do not overstate certainty.
4. Treat any conclusion as a lead; corroborate with other evidence before asserting identity.

## Inputs → Outputs
- **In:** `face`, `image` (a face photo and a comparison image/ID)
- **Out:** `physical-description` (a structured manual comparison and confidence judgement)
- **Empty/negative result looks like:** features genuinely differ, or image quality is too poor to compare — in which case do not force a match.

## Gotchas & OpSec
- Human-in-the-loop by definition: this is a manual method whose reliability depends entirely on the analyst and image quality. It is not forensic facial recognition and should not be presented as such.
- OpSec: passive; reading the page and comparing offline leaks nothing.

## Trust & verifiability
`trust: unverified` — a third-party instructional article, not a validated tool; useful as methodology but its claims are not independently confirmed here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | how-to-accurately-check-an-id-using-facial-features-to-verify-photo-id-s |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → physical-description |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
