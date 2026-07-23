---
id: mever-gr
name: MeVer Image Verification Assistant
description: Use when you have an `image` and want to know whether it has been digitally manipulated (face-swap, splice, copy-move, object add/delete) — returns tampering-localisation heatmaps and extracted metadata.
url: https://mever.gr/forensics/
category: documents-metadata
path:
- documents-metadata
bestFor: Detecting and localising digital forgery in a suspect photo before you trust it as evidence.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free web tool run by the MeVer / CERTH-ITI research group; no account or payment.
opsec: passive
opsecNote: You upload the image to a third-party academic server (CERTH-ITI, Greece) for processing, so the picture leaves your control. Do not upload material that is itself sensitive/evidential without authority. The analysis never touches the person who created the image, so it is passive toward the target.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by the Multimedia Knowledge & Social Media Analytics Lab (MeVer) at CERTH-ITI, the peer-reviewed research group behind the EU REVEAL and WeVerify verification projects.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- forensically
- fotoforensics
aliases:
- MeVer
- Image Verification Assistant
- CERTH-ITI forensics
tags:
- exifdata
- EXIF Data Related Sites
- image-forensics
source: uk-osint
lastVerified: '2026-07-23'
enrichment: full
---

# MeVer Image Verification Assistant

> Academic image-forensics service that maps where a photo was likely tampered — a second opinion when a picture is "too good to be true."

## When to use
You have an `image` (a claimed sighting photo, a profile picture, a "proof of life" image) and need to judge whether it was edited before you act on it. MeVer runs a battery of forensic filters (double-JPEG, noise, DCT, splicing / copy-move detection) and returns per-pixel tampering-probability maps, so you can spot face-swaps, pasted-in objects, or cloned regions that the eye misses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mever.gr/forensics/ in a browser.
2. Accept the privacy notice, then upload the suspect image (or paste an image URL).
3. Wait — processing can take a few minutes for large files. The tool returns several forensic filter panels; bright/anomalous regions in the tampering maps flag likely edits.
4. Read each panel: consistent, uniform maps suggest an untouched image; localised hotspots (e.g. only the face, only one object) suggest a manipulation there.
5. Export the PDF report for your case file. Pivot: if tampering is suspected, corroborate with `[[fotoforensics]]` / `[[forensically]]` and reverse-image-search the untouched regions.

## Inputs → Outputs
- **In:** `image`
- **Out:** tampering-localisation heatmaps, forensic filter panels, extracted `metadata-exif`, downloadable PDF report
- **Empty/negative result looks like:** uniform maps across all filters with no localised hotspots — i.e. no evidence of manipulation (absence of detected tampering, not a guarantee of authenticity).

## Gotchas & OpSec
- Human-in-the-loop: interpreting the maps takes judgement — a heavily re-saved or resized image produces artefacts that mimic tampering. Treat hotspots as leads, not proof.
- OpSec: the image is uploaded to a Greek academic server; assume it is retained for research. Do not submit legally sensitive evidence without authority.
- Screenshots and social-media-recompressed images degrade the signal; use the highest-quality original you can obtain.

## Overlaps ("do both")
- Pairs with `[[fotoforensics]]` and `[[forensically]]` — run the same image through all three; each uses different error-level and noise algorithms, so agreement across tools strengthens a manipulation finding.

## Trust & verifiability
`trust: trusted` — maintained by the MeVer lab at CERTH-ITI, a recognised research group behind the EU-funded REVEAL and WeVerify media-verification programmes; the methods are published, not a black box.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mever-gr |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
