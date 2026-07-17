---
id: sherloq
name: Sherloq
description: Use when you have an `image` and want to test whether it was edited, staged, or re-saved and pull its embedded metadata — returns `metadata-exif` plus tampering/forensic signals.
url: https://github.com/GuidoBartoli/sherloq
category: image-video-face
path:
- image-video-face
bestFor: Local, offline forensic analysis of a suspect photo — EXIF, ELA, clone/splice detection, and compression history.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free and open source (GPL-3.0). No account or payment; runs locally after you clone and install its Python dependencies.
opsec: passive
opsecNote: Analysis is fully local — the image never leaves your machine and no third party sees it. This makes Sherloq the safest option for sensitive imagery you must not upload to a web forensics service.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: community
trustNote: An open-source research toolset by photographer/developer Guido Bartoli implementing published forensic algorithms; the code is transparent, but outputs are indicators requiring expert interpretation, not verdicts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- fotoforensics-com
- jimpl
- verexif
- exiftool-2
aliases:
- Sherloq
- GuidoBartoli/sherloq
tags:
- Image Search and Identification
- Image Analyze
- image-forensics
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Sherloq

> An open-source, run-it-locally digital image forensics suite: EXIF/metadata extraction plus a battery of tampering-detection algorithms (ELA, clone/splice, resampling, compression history).

## When to use
You have an `image` — a ransom photo, a "proof of life," a dating-profile picture, a claimed crime-scene shot — and you need to know whether it is authentic, edited, or recycled, without uploading it anywhere. Sherloq bundles the forensic techniques (Error Level Analysis, copy-move/splice detection, noise and PRNU analysis, quantization-table quality estimates) alongside a full metadata dump, so you can both read the embedded `metadata-exif` (including any `geolocation`) and probe for manipulation offline.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install once: clone `https://github.com/GuidoBartoli/sherloq`, create a Python 3.11 virtual environment (the repo recommends `uv`), install dependencies, and launch the GUI with `python -m gui.sherloq_app`.
2. Open the target image in the app.
3. Start with the **Metadata** panels — EXIF, full metadata dump, embedded thumbnail, and any GPS/geolocation — to capture ground-truth camera/edit data.
4. Run the tampering tools — **ELA**, copy-move, splicing (DCT), resampling, contrast enhancement — and read them as a panel: several independent signals pointing the same way is what matters, not any one heatmap.
5. Manually interpret: these are indicators. Pivot embedded GPS to mapping tools and an embedded thumbnail (which can differ from an edited main image) to reverse-image search.

## Inputs → Outputs
- **In:** `image` (local file)
- **Out:** `metadata-exif` (full metadata + embedded thumbnail), any embedded `geolocation`, and forensic tampering indicators (ELA, clone/splice, resampling, compression history)
- **Empty/negative result looks like:** stripped metadata (common for social-media downloads) and inconclusive forensic panels — meaning the image was re-saved/scrubbed, which is itself a finding, not a dead end.

## Gotchas & OpSec
- Setup cost: it is a local Python app, not a website — you must install it before an investigation, not during.
- Interpretation required: ELA and clone-detection produce heatmaps that mislead the untrained; corroborate across multiple algorithms and treat outputs as leads.
- Metadata is easily faked or stripped: present EXIF supports a hypothesis but does not prove origin.
- OpSec: fully passive and offline — the strongest reason to use Sherloq over web tools when the image must not be disclosed to a third party.

## Overlaps ("do both")
- Web counterparts `[[fotoforensics-com]]` and `[[jimpl]]` give a fast ELA/metadata read with no install (but require upload); `[[verexif]]` and `[[exiftool-2]]` focus on metadata. Use Sherloq when the image is sensitive or you want the deeper algorithm battery locally.

## Trust & verifiability
`trust: community` — open-source and transparent (you can read exactly what each analysis does), maintained by a single expert developer; the outputs are research-grade indicators that need human forensic judgement, not automatic conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sherloq |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (manual-review) |
