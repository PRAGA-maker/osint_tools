---
id: kosmos-2
name: Kosmos 2
description: Use when you have an `image` and want an AI description that names objects, text and landmarks in it (with bounding boxes) — returns `physical-description` and grounded scene captions, not a map location.
url: https://huggingface.co/spaces/ydshieh/Kosmos-2
category: image-video-face
path:
- image-video-face
bestFor: Grounded image captioning — getting a multimodal model to describe and localise what is visible in a photo (objects, signage text, landmarks).
selectorsIn:
- image
selectorsOut:
- physical-description
- metadata-exif
status: down
pricing: free
costNote: Free Hugging Face Space; no account needed when running. As of the last check the Space throws a runtime error (model download fails) — self-host the open Kosmos-2 model or use another HF mirror if it stays down.
opsec: passive
opsecNote: You upload the image to a third-party Hugging Face Space, so the photo leaves your machine and transits Microsoft/HF infrastructure. Strip anything you don't want disclosed and never upload a sensitive victim image to a public demo — self-host for those.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Community-hosted demo (by HF user ydshieh) of Microsoft's open-source Kosmos-2 model; the model is legitimate research, but this specific Space is an unofficial, currently-broken deployment.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- google-lens
- efficientnetv2
- get-text-from-video
- hugging-face-ai-detector
- huggingface-co
- huggingface-co-4
- instruct-pix2pix
- pix2pix-video
- scene-edit-detection
- youtube-whisperer
- scene-detection
aliases:
- Kosmos-2
- Kosmos 2 grounding
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- geo-location-mapping-tools
- artificial-intelligence
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# Kosmos 2

> A grounded multimodal captioner (Microsoft's Kosmos-2) — it tells you *what* is in a photo and boxes it, generating description leads; it does **not** geolocate the image despite how it is sometimes listed.

## When to use
You have an `image` and want a machine-generated `physical-description`: objects, people, signage/text, and recognisable landmarks, each tied to a bounding box in the frame. That description is a lead generator — extracted place names, brand text, or landmark labels become queries for a reverse-image or search-engine geolocation pass. Do **not** reach for this expecting coordinates: Kosmos-2 grounds language to image regions; it has no location-inference capability, and the stub's "geolocate a photo" framing is inaccurate. Note also that as of the last check the public Space is throwing a runtime error, so plan to self-host the model if you need it now.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://huggingface.co/spaces/ydshieh/Kosmos-2. If it shows a runtime error, either wait for the Space to restart or run the open-source `microsoft/kosmos-2-patch14-224` model locally / via another mirror.
2. Upload your `image` and (optionally) a grounding prompt such as "Describe this image in detail" or "<grounding> What landmarks are here?".
3. Read the output: a caption with grounded phrases and bounding boxes over the detected objects/text/landmarks.
4. Extract leads — any place name, business/brand signage, monument, or distinctive object.
5. Pivot: feed those extracted terms into a reverse-image search / search engine to attempt actual geolocation, and cross-read against EXIF if the file carries `metadata-exif`.

## Inputs → Outputs
- **In:** `image` (+ optional text prompt)
- **Out:** grounded `physical-description` — object/landmark/text labels with bounding boxes (leads, not coordinates)
- **Empty/negative result looks like:** a vague, generic caption ("a photo of a building") with no useful named entities, or a Space runtime error / blank — in either case it gave you nothing to pivot on; move to a dedicated reverse-image tool.

## Gotchas & OpSec
- Human-in-the-loop: the captions are suggestive, not authoritative — a "landmark" label may be a hallucinated near-match; you must manually verify every extracted entity before trusting it.
- OpSec: **passive** toward the target, but you disclose the image to a public third-party demo. Never upload a sensitive or victim-linked photo here; self-host for those cases.
- Status: the hosted Space frequently fails to load the model — treat availability as unreliable.

## Overlaps ("do both")
- Pairs with `[[google-lens]]` — Kosmos-2 verbalises and boxes what's in the frame, while Lens does the actual match-to-known-places/reverse-image lookup; run the description through Lens (or a search engine) to convert it into a location.

## Trust & verifiability
`trust: community` — the underlying Kosmos-2 model is legitimate Microsoft research, but this is an unofficial community Space that is currently broken, and the model's outputs are probabilistic captions. Verify any named landmark/text independently; do not treat a caption as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kosmos-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | image → physical-description, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
