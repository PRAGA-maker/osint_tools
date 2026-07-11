---
id: jpegsnoop-image-decoder
name: JPEGsnoop
description: Use when you have an `image` and want its embedded metadata plus signs of editing/manipulation — returns EXIF, camera/software fingerprint, and forgery indicators.
url: https://www.impulseadventure.com/photo/jpeg-snoop.html
category: image-video-face
path:
- image-video-face
bestFor: Deep JPEG/EXIF decoding and detecting whether a photo was edited or re-saved (not straight from a camera).
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, open-source Windows desktop application (by Calvin Hass / ImpulseAdventure). The old CNET download link is dead; get it from impulseadventure.com or GitHub.
opsec: passive
opsecNote: JPEGsnoop runs entirely offline on your machine — nothing is uploaded, so analysis is fully passive and leaks nothing about the target. The only exposure is if you obtained the image itself by an active means; the decoding step is safe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: A well-regarded forensic JPEG decoder used in the OSINT community; its compression-signature database is heuristic, so "edited" verdicts are indicative, not court-proof.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- JPEGsnoop
- JPEG Snoop
tags:
- toddington
- curated-directory
- exif
- image-forensics
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# JPEGsnoop

> A forensic JPEG decoder — reads every scrap of embedded metadata and flags whether a photo came straight from a camera or was edited/re-saved.

## When to use
You have an `image` (a suspect photo, a profile picture, a piece of evidence) and want two things: (1) all embedded `metadata-exif` — camera make/model, timestamps, GPS if present, editing software — and (2) whether the file's compression signature matches a known camera or a photo editor, i.e. a manipulation check. This makes it valuable both for extracting location/device leads and for judging whether an image can be trusted.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download JPEGsnoop from `impulseadventure.com` (or the project's GitHub) and run it on Windows.
2. **File → Open** the image (JPEG, and it reads other formats' embedded data too).
3. Read the decoded report: EXIF (camera, lens, timestamp, GPS), embedded thumbnail (which may differ from the visible image!), and the compression-signature assessment.
4. Note the verdict: a signature matching a camera suggests an original; one matching Photoshop/other editors suggests it was re-saved/edited.
5. Pivot: GPS/timestamp → geolocation and timeline; camera model → device correlation; a mismatched embedded thumbnail → evidence of cropping/editing.

## Inputs → Outputs
- **In:** `image` (local file)
- **Out:** `metadata-exif` (full EXIF, GPS, timestamps, camera/software fingerprint, edit indicators)
- **Empty/negative result looks like:** stripped metadata and a generic/editor compression signature — common for images downloaded from social platforms, which re-encode and strip EXIF. That absence is itself a finding (the image is not an original).

## Gotchas & OpSec
- Social-media images are almost always stripped/re-compressed, so expect little EXIF from them; original files (email attachments, direct camera dumps) are where JPEGsnoop shines.
- The "edited" verdict is heuristic from a signature database — indicative, not definitive proof.
- OpSec: fully **passive/offline** — nothing is uploaded.

## Overlaps ("do both")
- Pairs with `[[profileimageintel]]` and reverse-image tools — JPEGsnoop reads a file you already hold; ProfileImageIntel pulls timestamps from live platform images, and reverse-image finds where the picture appears.

## Trust & verifiability
`trust: community` — a respected forensic decoder; EXIF it reports is authoritative, but manipulation verdicts are heuristic and should be corroborated for any high-stakes claim.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jpegsnoop-image-decoder |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
