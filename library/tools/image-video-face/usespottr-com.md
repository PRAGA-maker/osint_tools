---
id: usespottr-com
name: Spottr
description: Use when you have a long `image`/video and want to find a person, vehicle plate or scene inside it — returns matched moments, incl. OCR'd plates and physical descriptions.
url: https://usespottr.com/
category: image-video-face
path:
- image-video-face
bestFor: "\"Ctrl+F for video\" — natural-language search inside your own uploaded footage (CCTV, dashcam) for people, vehicles, plates and scenes."
selectorsIn:
- image
selectorsOut:
- vehicle-plate
- physical-description
status: live
pricing: freemium
costNote: Freemium SaaS; sign-up typically required and heavier processing/longer video is gated behind paid tiers. Check current limits on the site.
opsec: passive
opsecNote: You upload your footage to Spottr's servers for AI processing, so the video leaves your control — do not upload sensitive or legally-restricted evidence to a third party without authorization. The subject is not contacted.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Early-stage commercial video-search SaaS. Capable AI (object detection, OCR, speech-to-text) but detections are probabilistic — treat hits as leads to eyeball, not confirmed identifications.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- usespottr
- Spottr video search
tags:
- videosites
- Video Related Sites
- video-analysis
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Spottr

> "Ctrl+F for videos": upload footage and search it in plain language for a person, a vehicle, a license plate, or a moment — instead of scrubbing hours by hand.

## When to use
You have long video you control — CCTV, dashcam, bodycam, event footage — and need to find the needle: a person matching a `physical-description`, a specific vehicle, a `vehicle-plate` (it OCRs plates), or a described scene ("red car entering after 10 PM"). It collapses hours of manual review into a semantic search over the footage's visual and audio content. It searches *your uploads*, not the open web.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://usespottr.com/ and sign up.
2. Upload the video (MP4/MOV/AVI). Spottr indexes it with object detection, OCR, and speech-to-text.
3. Search in natural language: describe the person/clothing, the vehicle, a plate fragment, or an action.
4. Read results: matched timestamps/clips with the detected object/text. Open each to verify by eye.
5. Pivot: an OCR'd `vehicle-plate` feeds plate/registration tools; a clear face frame feeds face-search; a scene confirms presence at a time/place.

## Inputs → Outputs
- **In:** `image`/video you upload plus a natural-language query
- **Out:** matched moments, OCR'd `vehicle-plate`, and people matching a `physical-description`
- **Empty/negative result looks like:** no matches for the query. Low light, distance, motion blur, or an over-specific query degrade detection — loosen the query and re-check, and never treat "no match" as proof of absence.

## Gotchas & OpSec
- Human-in-the-loop: requires an account; free tier caps video length/processing.
- Detections (objects, plates, transcripts) are probabilistic — confirm every hit against the actual frame before relying on it.
- **Upload risk:** footage goes to a third-party server; do not upload restricted evidence without authorization.
- OpSec: passive toward the subject, but your footage now lives on Spottr's infrastructure.

## Overlaps ("do both")
- Do alongside face-search and plate/vehicle tools: Spottr *finds* the frame containing a face or plate inside your video; those tools then *identify* what Spottr surfaced.

## Trust & verifiability
`trust: unverified` — a young commercial SaaS with capable but probabilistic AI. Treat its plate reads and person matches as leads: open the source frame and confirm visually before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usespottr-com |
</content>
