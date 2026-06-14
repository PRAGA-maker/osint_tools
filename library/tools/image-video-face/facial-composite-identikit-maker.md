---
id: facial-composite-identikit-maker
name: Facial composite (identikit) maker
description: Use when you have only a witness/verbal physical description and need to build a composite face image (identikit) to use as a search or circulation reference.
url: http://facemaker.uvrg.org/
category: image-video-face
path:
- image-video-face
bestFor: Assembling an identikit/composite face image from descriptive features when no photo exists.
selectorsIn:
- physical-description
selectorsOut:
- image
- face
status: unknown
pricing: free
costNote: ''
opsec: passive
opsecNote: You assemble facial features locally in the browser; nothing about the subject is uploaded unless you choose to share the result. Low leakage.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: A free web-based facial-composite/identikit builder; output quality is illustrative, not photographic, and composites are inherently subjective. Tool availability not independently verified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- identikit maker
- facemaker
tags:
- Image Search and Identification
- composite
source: cyb-detective
lastVerified: ''
enrichment: full
---

# Facial composite (identikit) maker

> A browser-based identikit builder: assemble a face from interchangeable feature parts to visualize a person described in words.

## When to use
You have a `physical-description` (witness account, written description) but **no photo** of the person, and you need a visual reference `image`/`face` to attach to an alert, jog memory, or seed downstream review. It generates a likeness, not an identification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://facemaker.uvrg.org/.
2. Select and adjust feature components (face shape, eyes, nose, mouth, hair) to match the description.
3. Iterate with the witness/source until the composite is acceptable.
4. Export/screenshot the resulting `image`.
5. Pivot: the composite can support a circulation poster, but it is **not** reliable input for facial-recognition search engines — those need a real photo.

## Inputs → Outputs
- **In:** `physical-description`
- **Out:** `image` / `face` (a synthetic composite likeness).
- **Empty/negative result looks like:** a composite that the witness does not recognize as a good match — discard and rebuild.

## Gotchas & OpSec
- Human-in-the-loop: composite assembly is entirely manual and judgment-based; quality depends on the operator and the witness.
- OpSec: **passive** — work happens client-side; nothing is leaked unless you publish the output. Do not feed composites into face-search engines as if they were photographs.

## Overlaps ("do both")
- A composite is a precursor step. Once you have a real photo of the candidate, switch to `[[facecheck-facial-recognition-search]]` / `[[faceplusplus-com]]` for actual matching.

## Trust & verifiability
`trust: unverified` — a free utility producing subjective likenesses; useful for visualization and circulation, not for biometric matching.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facial-composite-identikit-maker |
| category | image-video-face |
| selectorsIn → selectorsOut | physical-description → image, face |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
