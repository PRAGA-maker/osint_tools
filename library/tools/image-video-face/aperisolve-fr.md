---
id: aperisolve-fr
name: Aperi'Solve
description: Use when you have an `image` and want a fast all-in-one steganography/forensics pass (layers plus zsteg, steghide, exif, binwalk, strings) — returns hidden data, embedded files, and `metadata-exif`.
url: https://aperisolve.fr
category: image-video-face
path:
- image-video-face
bestFor: One-click layered steganalysis of an image — running the standard stego/forensics toolchain in the browser.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- document-id
status: live
pricing: free
costNote: Free web service; no account. Also open source (self-hostable) for offline/sensitive use.
opsec: active
opsecNote: The public site processes the image on its servers, so you disclose the picture to a third party. For sensitive imagery, self-host Aperi'Solve or run the underlying tools (zsteg, steghide, binwalk) locally instead of uploading.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open-source project wrapping well-known, trusted stego/forensics utilities; the tools are standard, but interpreting their output requires judgement and the hosted service sees your upload.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fotoforensics-com
- exiftool-2
aliases:
- Aperi'Solve
- aperisolve.fr
tags:
- Image Search and Identification
- Image Analyze
- steganography
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Aperi'Solve

> A browser-based "run everything" steganalysis platform: upload an image and it fires the whole standard toolchain — colour-layer analysis, zsteg, steghide, outguess, exiftool, binwalk, foremost, strings — in one pass.

## When to use
You have an `image` and suspect it hides more than it shows — an embedded file, a steganographic payload, an appended archive, or telling metadata. Rather than run each tool by hand, Aperi'Solve applies the common CTF/forensics battery at once and lays out the results, so you quickly see whether the picture carries hidden data, EXIF/GPS, or a smuggled file. Common in CTFs, but equally useful when a suspicious photo turns up in an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://aperisolve.fr and drag-and-drop the image (PNG/JPG/GIF/BMP/TIFF, etc.); optionally supply a password for steghide/outguess.
2. Review the outputs by panel:
   - **Layers** (superimposed, R/G/B bit planes) — visual patterns that reveal LSB stego.
   - **zsteg / steghide / outguess** — extracted hidden payloads if present.
   - **exiftool** — full `metadata-exif`, including any GPS.
   - **binwalk / foremost** — embedded/appended files carved out.
   - **strings** — readable text buried in the binary.
3. Download any carved files and inspect them; treat all extracted content as untrusted.
4. Pivot: embedded GPS feeds mapping tools; a carved document feeds document/metadata analysis; extracted text may contain selectors.

## Inputs → Outputs
- **In:** `image` (optionally a stego password)
- **Out:** `metadata-exif`, extracted hidden payloads / embedded files (`document-id`), bit-plane visualisations, and raw strings
- **Empty/negative result looks like:** clean layers, no zsteg/steghide hits, no carved files, sparse metadata — the image is probably a plain re-saved photo; not absolute proof of no stego (strong tools/passwords can evade these), but a solid negative.

## Gotchas & OpSec
- Upload exposure: the public instance sees your image — **active**. Self-host or run the CLI tools locally for anything sensitive.
- False positives/negatives: automated stego tools miss custom schemes and can flag benign noise; interpret, don't trust blindly.
- Malware in carvings: files pulled out by binwalk/foremost are untrusted — sandbox before opening.
- Format-dependent: some analyses (zsteg) apply mainly to PNG/BMP, not JPEG.

## Overlaps ("do both")
- Pairs with `[[fotoforensics-com]]` (ELA/tampering focus) and `[[exiftool-2]]` (deep metadata) — Aperi'Solve is the fast all-in-one first pass; use the specialised tools to go deeper on whatever it flags, and run locally when the image can't be uploaded.

## Trust & verifiability
`trust: community` — an open-source wrapper around standard, well-trusted forensic utilities; the extraction results are as reliable as those tools, but conclusions need human interpretation and the hosted service sees your upload.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aperisolve-fr |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
