---
id: stegonline
name: StegOnline
description: Use when you have an `image` suspected of hiding data — returns extracted bit-planes, embedded strings/files, and `metadata-exif` from in-browser steganalysis.
url: https://stegonline.georgeom.net/upload
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Browser-based steganography analysis — pulling hidden bit-planes, strings, and payloads out of an image.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- document-id
status: live
pricing: free
costNote: Free, open-source web app; no account required.
opsec: passive
opsecNote: "StegOnline processes images in your browser, but you are uploading the image to georgeom.net's page — for a sensitive exhibit prefer the open-source local version (run it offline) so the file never leaves your machine. Analysis is passive toward any subject; the risk is exposing evidence to a third-party host."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known open-source stego tool by George Om (source on GitHub); widely used in CTF/forensics, so its behavior is transparent and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Steg Online
- georgeom StegOnline
tags:
- steganography
- image-forensics
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# StegOnline

> A browser-based steganography workbench: upload an image and explore its bit-planes, colour channels, and embedded data to reveal anything hidden inside.

## When to use
You have an `image` that might conceal data — a payload, a message, an unexpected embedded file — and want to inspect its bit-planes and extract hidden content without installing anything. Useful for verifying whether a photo shared by/about a subject carries covert data, and for reading anomalies alongside `metadata-exif`. A niche forensic step, so direct missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://stegonline.georgeom.net/upload (or run the open-source build locally for sensitive files) and upload the `image`.
2. Use the bit-plane browser to toggle individual RGBA bit-planes and spot patterns/text hidden in the least-significant bits.
3. Use "Extract Files/Data" to pull embedded strings or files (LSB extraction), and inspect the colour/steg analysis views.
4. Combine with a dedicated EXIF viewer to correlate hidden data with the file's `metadata-exif`.
5. Save any extracted payload/`document-id` as a lead for further analysis.

## Inputs → Outputs
- **In:** `image` (PNG works best for LSB techniques; JPEG's lossy compression limits it)
- **Out:** revealed bit-planes, extracted strings/files, `metadata-exif`, potential embedded `document-id`
- **Empty/negative result looks like:** bit-planes look like uniform noise and extraction yields nothing readable — likely no steganographic payload (or one using a scheme/tool this doesn't cover); absence isn't proof of a clean image.

## Gotchas & OpSec
- Uploading to the hosted version discloses the image to georgeom.net — use the local build for evidence you must keep private.
- LSB techniques work on lossless formats (PNG/BMP); JPEG re-compression usually destroys or masks LSB payloads.
- It won't crack password-protected/encrypted stego schemes — a null result only rules out what it can test.

## Overlaps ("do both")
- Pairs with EXIF/metadata viewers and file-carving tools — StegOnline handles the pixel-level hidden data while metadata tools handle the header-level story; run both on a suspicious image.

## Trust & verifiability
`trust: community` — a transparent, open-source, widely-used stego tool; results are reproducible, and for chain-of-custody you can run the identical code offline.
