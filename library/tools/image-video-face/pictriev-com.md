---
id: pictriev-com
name: pictriev.com
description: Use when you have two face photos and want a head-to-head similarity score (the PicTriev face-compare endpoint) — returns a likeness percentage.
url: http://www.pictriev.com/fc.php
category: image-video-face
path:
- image-video-face
bestFor: Direct two-photo face comparison ("are these the same person?") via the PicTriev compare page.
selectorsIn:
- face
- image
selectorsOut:
- face
status: live
pricing: free
costNote: Free to use; no account required.
opsec: active
opsecNote: Both face images are uploaded to PicTriev for comparison.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: This is the face-comparison (fc.php) endpoint of PicTriev, listed on uk-osint.net under "Facial Comparison Sites". Same engine and limits as the main PicTriev site.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- facial-comparison
- face
source: uk-osint
lastVerified: ''
enrichment: full
relatedTools:
- pictriev
---

# pictriev.com

> The dedicated face-compare page of PicTriev — upload two photos and get a likeness percentage to support (not confirm) a same-person hypothesis.

## When to use
You have two `face`/`image` samples — e.g. a missing-person reference photo and an unidentified image — and want a quick numeric similarity estimate before deeper analysis. Tie-in: two `face` inputs in, a similarity-scored `face` comparison out. Use as a triage signal, not proof.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.pictriev.com/fc.php (the face-comparison page).
2. Upload the two clear, front-facing `face` photos.
3. Read the returned similarity percentage.
4. Use the score as supporting signal only; confirm identity through independent evidence.
5. For one-photo-to-the-web identity search, use the main site [[pictriev]] or [[pimeyes-2]].

## Inputs → Outputs
- **In:** `face`, `image` (two photos)
- **Out:** `face` (similarity score)
- **Empty/negative result looks like:** a low percentage or a failure to detect a face — common with poor angles, lighting, or occlusion; rerun with better images.

## Gotchas & OpSec
- Human-in-the-loop: the score needs human interpretation; never treat a number as identity confirmation.
- OpSec: active — both images are uploaded to a third party. Avoid sensitive case photos.
- Same engine/limits as PicTriev; quality depends heavily on frontal, well-lit faces.

## Overlaps ("do both")
- Pairs with [[pictriev]] (same service, lookalike-search mode) and [[pimeyes-2]] (web-wide identity search).

## Trust & verifiability
`trust: community` — a real, directory-listed comparison endpoint of an established tool; output is a soft similarity signal, not biometric confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pictriev-com |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → face |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
