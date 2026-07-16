---
id: carnet-ai
name: Carnet.ai
description: Use when you have an `image` of a car and want to identify its make, model and generation — returns a physical-description of the vehicle to narrow an ID.
url: https://carnet.ai/
category: transportation
path:
- transportation
- vehicle-records
bestFor: Recognising a vehicle's make/model/generation from a photo when you can't identify it by eye.
selectorsIn:
- image
selectorsOut:
- physical-description
status: live
pricing: freemium
costNote: Interactive web demo is free to try; API access is free for personal/educational or public link-back projects, otherwise paid. Recognises 300+ brands / 3100+ models built since ~1995.
opsec: passive
opsecNote: You upload only a vehicle image to a hosted inference service; no vehicle owner is contacted. Strip or avoid uploading images whose metadata/background you don't want on a third-party server, and consider a sock-puppet where sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent ML service claiming ~97% make/model accuracy; predictions are probabilistic and unverified against ground truth, so confirm before relying on them.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- CarNet.AI
- carnet.ai
tags:
- vehicle
- image-recognition
- visual-osint
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Carnet.ai

> A car-recognition service: upload a vehicle photo and it predicts the make, model, generation, color, and angle with a confidence score.

## When to use
You have an `image` showing a vehicle — from a social post, CCTV still, or scene photo — and you cannot identify the car by eye. Carnet.ai narrows it to a make/model/generation (`physical-description`), which helps corroborate a vehicle tied to a subject, match it against a plate/VIN decode, or filter candidate cars in a geolocation task.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://carnet.ai/ and use the interactive demo (or one of the example images to see how it behaves).
2. Upload the vehicle image (a clear, front/rear/side angle works best) or pass an image URL.
3. Read the prediction: make, model, generation/year range, color, camera angle, and a confidence/probability score.
4. For batch/automated use, request API access (free tier for personal/educational or link-back projects).
5. Pivot: feed the identified make/model into a VIN/plate decoder like `[[vin-check-and-get-vehicle-history-report]]`, or use it to confirm/deny a car seen in another photo of the subject.

## Inputs → Outputs
- **In:** `image` of a vehicle (file or URL)
- **Out:** predicted `physical-description` — make, model, generation, color, angle — with a confidence score.
- **Empty/negative result looks like:** a low-confidence guess or "not recognised" — obscured, partial, very old (pre-1995), or heavily modified vehicles defeat it; treat low confidence as no answer.

## Gotchas & OpSec
- Predictions are probabilistic; a low confidence score is a non-answer, not a weak yes.
- It identifies the *model*, never the owner or plate — do not conflate a make/model match with attribution.
- Angle, lighting, and occlusion strongly affect accuracy; try multiple crops/frames of the same car.

## Overlaps ("do both")
- Pairs with `[[vin-check-and-get-vehicle-history-report]]` — Carnet.ai IDs the car from a picture, the VIN tool decodes and screens a specific vehicle once you have its number.

## Trust & verifiability
`trust: community` — a capable but independent ML model; its make/model claim is a strong lead, so confirm against a second image or a plate/VIN before treating it as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | carnet-ai |
| category | transportation |
| selectorsIn → selectorsOut | image → physical-description |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
