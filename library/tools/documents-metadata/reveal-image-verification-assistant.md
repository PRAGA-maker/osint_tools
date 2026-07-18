---
id: reveal-image-verification-assistant
name: Image Verification Assistant (REVEAL / WeVerify)
description: Use when you have an `image` and want to detect tampering — returns eight forensic filters (ELA, double-quantization, noise, DCT, etc.) plus metadata and GPS.
url: https://weverify.eu/tools/image-verification-assistant/
category: documents-metadata
path:
- documents-metadata
bestFor: Running a battery of image-forensics filters on a photo to spot splices, clones, and re-compression, alongside metadata/GPS extraction.
selectorsIn:
- image
- metadata-exif
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free, EU-funded (InVID / REVEAL / WeVerify, Horizon 2020); also bundled in the free InVID-WeVerify browser plugin. No payment.
opsec: active
opsecNote: Active in that you upload the target image to an EU-project server for processing. Use a non-sensitive copy; assume the file is retained for analysis. The InVID plugin runs the same filters and is the option when you'd rather not hand the image to a hosted page unnecessarily.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by EU research projects (InVID, REVEAL, WeVerify) and widely used by journalists/fact-checkers; the forensic algorithms are documented in academic literature.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- invid-verification-plugin
aliases:
- REVEAL Image Verification Assistant
- WeVerify Image Verification Assistant
- InVID image forensics
tags:
- bellingcat-toolkit
- metadata
- image-forensics
- verification
source: bellingcat-toolkit
lastVerified: '2026-07-18'
enrichment: full
---

# Image Verification Assistant (REVEAL / WeVerify)

> A multi-filter image-forensics workbench from the EU verification projects — run eight complementary tampering detectors on one photo, plus a full metadata/GPS read, when a single ELA view isn't enough.

## When to use
You have an `image` whose authenticity matters — a photo attached to a tip, a viral image, a piece of purported evidence — and you want more than one forensic angle on it. Where a basic ELA tool gives you one filter, this runs eight (Error Level Analysis, Double Quantization, Median/Noise, Laplacian, DCT, and more), so inconsistent findings across filters strengthen or weaken a tampering hypothesis. It also parses metadata and GPS, making it a strong single stop for "is this photo real, and where/when was it taken?"

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Image Verification Assistant at https://weverify.eu/tools/image-verification-assistant/ (or run the same filters via the free InVID-WeVerify browser plugin).
2. Submit the image by URL or upload (use a non-sensitive copy).
3. Step through the forensic filters — each highlights a different manipulation signature (splices, clones, re-compression, local edits).
4. Read the metadata panel for EXIF/IPTC and any GPS `geolocation`.
5. Corroborate across filters: a suspected edit is credible when *multiple* independent filters flag the same region, not just one.

## Inputs → Outputs
- **In:** an `image` (URL or upload) and its embedded `metadata-exif`
- **Out:** eight forensic filter overlays, parsed `metadata-exif`, and GPS `geolocation` where present
- **Empty/negative result looks like:** a clean original shows consistent, unremarkable filter outputs and (often) intact metadata; a stripped/social-media image yields little metadata and noisy filters — absence of metadata is normal and not proof of tampering.

## Gotchas & OpSec
- **Upload leaves your control:** the image goes to an EU-project server; use a copy and prefer the InVID plugin when you'd rather not host the file.
- **Read filters together:** any single filter produces false positives under heavy compression/resizing — trust convergence across filters, not one bright map.
- Social-media images are usually re-compressed and stripped, degrading both metadata and filter reliability.

## Overlaps ("do both")
- Pairs with `[[forensic-analyzer]]` (a lighter ELA+EXIF tool) and the `[[verification-handbook]]` methodology — run this for the multi-filter deep read, cross-check with a second forensics tool, and let the Handbook structure the overall verification.

## Trust & verifiability
`trust: trusted` — developed and maintained by the InVID/REVEAL/WeVerify EU research projects and standard in the fact-checking community; the underlying algorithms are published and reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reveal-image-verification-assistant |
| category | documents-metadata |
| selectorsIn → selectorsOut | image, metadata-exif → metadata-exif, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
