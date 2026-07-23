---
id: image-scrubber
name: Image Scrubber
description: Use when you (the investigator) are about to publish a photo and want to strip its EXIF and redact faces/identifiers first — a client-side tool that removes metadata and lets you blur sensitive areas.
url: https://everestpipkin.github.io/image-scrubber/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Anonymising a photo before sharing — stripping EXIF and painting/blurring over faces or identifying details.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free and open source; runs entirely in the browser (or offline from GitHub), no account or payment.
opsec: passive
opsecNote: A defensive tool for images YOU are about to release — it removes EXIF (GPS, device) and lets you redact faces so a shared photo doesn't dox subjects or reveal your location. All processing is client-side; nothing is uploaded. Verify redactions are irreversible (paint over, don't just blur lightly) before publishing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known open-source tool by Everest Pipkin, widely recommended (Bellingcat and protest-safety guides); client-side and inspectable on GitHub.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- image scrubber
- everestpipkin image-scrubber
tags:
- opsec
- metadata-removal
- redaction
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Image Scrubber

> A browser-based tool to anonymise a photo before you share it: strips EXIF metadata and lets you paint over faces and identifying details — all client-side, nothing uploaded.

## When to use
You are about to publish or send a photo — evidence for a report, a protest image, a screenshot — and need to remove data that could identify people or leak your location. Reach for Image Scrubber to strip the EXIF (which can carry GPS coordinates and device serials) and to manually blur or paint over faces, badges, plates, and backgrounds. This is a defensive OpSec/redaction tool for your own outbound images, not a way to read a target's metadata.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://everestpipkin.github.io/image-scrubber/ (or add to homescreen / run from the GitHub code for offline use).
2. Load the photo; the tool shows the EXIF metadata it will remove.
3. Use the brush to paint over faces and any identifying details — prefer solid paint over light blur, since blur can sometimes be reversed.
4. Save the scrubbed copy; confirm it's the redacted version you share (keep the original separately if you need it).
5. Pivot: this is the terminal step before publishing — the scrubbed image is the safe artifact.

## Inputs → Outputs
- **In:** an `image` you're about to share (max ~2500×2500 px)
- **Out:** a metadata-stripped, redacted copy of the image (it removes/obscures data, doesn't extract it)
- **Empty/negative result looks like:** an image with no EXIF and nothing to redact — fine; verify and proceed.

## Gotchas & OpSec
- Redaction quality is on you: paint over sensitive areas solidly. Light Gaussian blur or pixelation can be partially reversed — don't rely on it for faces/text you must hide.
- Direction: it *removes* metadata for privacy; to *read* a subject's EXIF use a viewer/extractor instead.
- OpSec: fully client-side and offline-capable — nothing is uploaded, which is exactly why it's trusted for sensitive images.

## Overlaps ("do both")
- The counterpart to EXIF viewers/extractors (which read a target's metadata). Pair with a metadata viewer to confirm your scrubbed image truly has no EXIF left before release.

## Trust & verifiability
`trust: community` — a widely-endorsed open-source tool with inspectable, client-side code; still, verify your own redactions are irreversible before publishing, since the safety depends on how you use it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | image-scrubber |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | image →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
