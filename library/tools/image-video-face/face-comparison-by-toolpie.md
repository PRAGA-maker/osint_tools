---
id: face-comparison-by-toolpie
name: Face Comparison by ToolPie
description: Use when you have two `face`/`image` photos and want to know whether they show the same person — returns a same-person similarity score.
url: https://facecomparison.toolpie.com/
category: image-video-face
path:
- image-video-face
bestFor: Quick 1:1 verification of whether two face photos are the same individual.
selectorsIn:
- image
- face
selectorsOut:
- face
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: active
opsecNote: You upload the target's photos to a third-party (ToolPie) server for AI processing. The site states photos are deleted after comparison, but uploading a subject's face to an unknown third party is an active disclosure — avoid for sensitive cases, or self-host an offline comparator instead. No target is notified.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Listed in the Bellingcat online investigation toolkit. A convenience AI face-matcher; the vendor's stated accuracy is self-reported and unverified.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- pimeyes
aliases:
- ToolPie Face Comparison
tags:
- bellingcat-toolkit
- facial-recognition
- face-match
source: bellingcat-toolkit
lastVerified: '2026-07-14'
enrichment: full
---

# Face Comparison by ToolPie

> A free 1:1 face matcher: upload two photos, get a same-person similarity percentage.

## When to use
You have two face images — e.g. a photo from a family member and a face pulled from a social profile, or two profiles you suspect are the same person — and need a quick objective read on whether they match. This is verification (1:1), not search (1:many): it confirms/denies a specific pairing rather than finding a face across the web.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://facecomparison.toolpie.com/ in a sock-puppet browser.
2. Upload the two face photos (clear, front-facing, single face each works best).
3. Read the returned similarity score — the tool suggests scores above ~80% indicate the same individual.
4. Apply analyst judgement (**manual-review**): treat the score as one signal, weighing pose, age gap, and image quality. Pivot: to *find* where a face appears online instead of comparing two, use a 1:many engine like `[[pimeyes]]`.

## Inputs → Outputs
- **In:** `image`/`face` ×2
- **Out:** `face` (same-person similarity score/verdict)
- **Empty/negative result looks like:** low similarity, or an error if no clear face is detected — poor lighting, occlusion, or extreme angle can suppress a true match, so a low score is not proof of different people.

## Gotchas & OpSec
- Human-in-the-loop: **manual-review** — never treat the percentage as conclusive; corroborate identity with non-biometric evidence.
- OpSec: **active** upload of a subject's face to a third party. Photos are said to be deleted post-comparison, but for sensitive missing-persons work prefer an offline/local face comparator.
- 1:1 only — it will not tell you where else a face appears.

## Overlaps ("do both")
- Pairs with `[[pimeyes]]` — PimEyes searches a face across the web (1:many), then use ToolPie to verify a specific candidate pairing (1:1).

## Trust & verifiability
`trust: community` — a free vendor tool surfaced via the Bellingcat toolkit. Accuracy claims are self-reported; use the score as corroboration, not identification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | face-comparison-by-toolpie |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → face |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (manual-review) |
