---
id: face-recognition
name: face_recognition (Python)
description: Use when you have `face`/`image` files and want to detect, encode, and match faces locally — returns face locations, encodings, and same-person match results across your own image set.
url: https://github.com/ageitgey/face_recognition
category: image-video-face
path:
- image-video-face
bestFor: Offline face detection and 1:1 / 1:N matching across a local set of images (dlib-based).
selectorsIn:
- face
- image
selectorsOut:
- face
status: live
pricing: free
costNote: Free and open-source (dlib-backed). No fees or API; you run it on your own hardware.
opsec: passive
opsecNote: Runs entirely offline on your machine — no image is uploaded to any third party, so it's fully passive and privacy-preserving. Nothing is disclosed. (It does NOT search the internet; it only compares images you already have.)
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: python-lib
trust: community
trustNote: Extremely popular, well-documented open-source library wrapping dlib's ResNet face model. Reliable for detection/encoding, but matching accuracy depends on image quality and your threshold — verify matches by eye.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- face_recognition
- ageitgey/face_recognition
tags:
- Image Search and Identification
- Face recognition and search
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# face_recognition (Python)

> The go-to offline face library — detect faces in images, turn them into encodings, and decide whether two photos are the same person, all locally with no upload.

## When to use
You have one or more `image`s/`face`s and need to compare them programmatically: confirm two photos are the same person, cluster a folder of images by identity, or filter a large image set down to those containing a target face. Ideal when privacy or evidence-handling means you must NOT upload the photo to an online engine — everything runs on your machine. Note it matches within images you supply; it does not crawl the web.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install (needs dlib): `pip install face_recognition` (or use the CLI tools it ships).
2. Load images and get encodings:
   ```python
   import face_recognition
   known = face_recognition.face_encodings(face_recognition.load_image_file("known.jpg"))[0]
   unknown = face_recognition.face_encodings(face_recognition.load_image_file("unknown.jpg"))[0]
   print(face_recognition.compare_faces([known], unknown))  # -> [True/False]
   ```
3. For a folder, batch-encode and cluster, or use the `face_recognition` CLI over a directory.
4. Tune the distance threshold; always eyeball claimed matches — automated matches can be wrong.
5. Pivot: confirmed same-person images consolidate a subject's photo set to push into online face/reverse-image engines like `[[berify]]`.

## Inputs → Outputs
- **In:** `image`/`face` files (a known photo + candidates)
- **Out:** face locations, 128-d encodings, and same-person match booleans/distances
- **Empty/negative result looks like:** "no face found" (bad angle/lighting/low-res) or all-False comparisons. Poor images cause both false negatives and false positives — a result is a computed similarity, not proof of identity.

## Gotchas & OpSec
- Human-in-the-loop: treat every match as a hypothesis to verify visually; set thresholds conservatively.
- Not a web search: it only compares images you provide — pair it with an online engine to find new photos.
- OpSec: fully offline/passive — nothing leaves your machine, which is exactly why it's preferred for sensitive faces.

## Overlaps ("do both")
- Pairs with `[[berify]]` and reverse-image/face engines — those find candidate photos online, then face_recognition verifies offline whether they're the same person before you rely on them.

## Trust & verifiability
`trust: community` — a mature, widely used library; the mechanics are solid, but match accuracy is image- and threshold-dependent, so confirm identities manually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | face-recognition |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → face |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | yes |
