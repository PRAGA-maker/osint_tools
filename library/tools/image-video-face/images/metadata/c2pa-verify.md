---
id: c2pa-verify
name: C2PA Verify
description: Use when you have an image and want to read its C2PA Content Credentials — provenance, origin app, AI-generation flags, and edit history.
url: https://c2paviewer.com/
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Inspecting C2PA "Content Credentials" manifests to check whether a photo was AI-generated, edited, or carries signed provenance.
input: ''
output: ''
selectorsIn:
- image
- metadata-exif
selectorsOut:
- metadata
- metadata-exif
status: live
pricing: free
opsec: passive
opsecNote: You upload/inspect a file in-browser; many C2PA viewers parse locally, but assume the file may be sent to the service unless verified. Never upload sensitive case images without checking.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party C2PA manifest viewer (not the official Content Authenticity Initiative verifier). The C2PA standard is legitimate; this particular viewer's handling is not independently confirmed here.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# C2PA Verify

> A browser viewer for C2PA Content Credentials — tells you if an image carries signed provenance, was made by an AI tool, or was edited, and by what software.

## When to use
You have an `image` (a tip photo, a social-media upload, a possible AI-generated likeness of a missing person) and you want to know whether it embeds C2PA/Content-Credentials provenance. This answers: was it produced by a generative-AI app, what tool/app signed it, and was it modified — all of which help you judge if a "sighting" image is authentic.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://c2paviewer.com/.
2. Drag in or select the image file (or paste a URL if supported).
3. Read the manifest: look for the signing claim generator (e.g. a camera app, Photoshop, an AI model), assertions like `ai-generated`, ingredient/edit history, and signature validity.
4. Pivot: a valid signature naming an app or device is a `metadata` lead; absence of credentials is also informative (most web photos have none).

## Inputs → Outputs
- **In:** `image` (file) with possible C2PA manifest; complements `metadata-exif`
- **Out:** `metadata` — provenance chain, generator app, AI flags, edit assertions, signature status
- **Empty/negative result looks like:** "no Content Credentials found." Most ordinary web/social images carry none — this is normal, not a failure, and tells you nothing was provably signed.

## Gotchas & OpSec
- Human-in-the-loop: you must read and interpret the manifest; presence of credentials ≠ truth, and they can be stripped or absent.
- OpSec: confirm whether parsing is local or server-side before uploading sensitive case material; treat as potentially active upload until verified.
- C2PA is sparsely adopted; a "no credentials" result is the common case and does not prove tampering.

## Overlaps ("do both")
- Run alongside a full EXIF/metadata extractor — C2PA covers signed provenance, EXIF covers camera/GPS fields the two rarely overlap.

## Trust & verifiability
`trust: unverified` — the underlying C2PA standard is sound, but this is a third-party viewer (not the official CAI Verify at contentcredentials.org). Cross-check important findings on the official verifier.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | c2pa-verify |
| category | image-video-face |
| selectorsIn → selectorsOut | image, metadata-exif → metadata, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
