---
id: perceptual-image-analysis
name: Perceptual Image Analysis
description: Use when you have an `image` and want quick in-browser forensic checks for manipulation — returns Error Level Analysis, PCA, and `metadata-exif` views.
url: https://chromewebstore.google.com/detail/perceptual-image-analysis/gidmeabdffonnejjlkbglmppmfniakdf
category: image-video-face
path:
- image-video-face
bestFor: One-click Error Level Analysis, Principal Component Analysis, and metadata inspection of an image directly in Chrome.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free Chrome extension; no account or payment. Requires installing the extension in a Chromium browser.
opsec: passive
opsecNote: Analysis runs locally in your browser on the image you point it at; nothing is sent to the target. Note that fetching a remote image to analyze does hit that image's host from your IP — use a sock-puppet browser if the source could log you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Independently published extension (developer Martin Saturka), ~750 users, last updated 2020; it wraps well-understood forensic techniques whose output you interpret yourself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Perceptual image analysis Chrome extension
tags:
- Image Search and Identification
- Image Analyze
- image-forensics
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Perceptual Image Analysis

> A Chrome extension that puts image-forensics tools (Error Level Analysis, PCA slopes, metadata) one right-click away — a fast first pass on whether a photo has been edited.

## When to use
You have an `image` tied to a case — a profile photo, a "proof of life" picture, a suspicious screenshot — and want a quick manipulation check before trusting it: is it a spliced composite, has a region been cloned/erased, does the metadata contradict the visible content? This extension surfaces the standard forensic overlays inline in the browser so you don't have to upload the image to a third-party server first.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Perceptual Image Analysis" from the Chrome Web Store into a Chromium browser (ideally a sock-puppet profile).
2. Navigate to (or open) the target `image`.
3. Invoke the extension on the image to run the analyses: **Error Level Analysis** (edited regions compress differently and stand out), **Principal Component Analysis / slopes** (reveals otherwise-invisible tampering), and the **metadata** view.
4. Interpret the overlays: uniform ELA across a region that looks "pasted" suggests splicing; metadata (camera, timestamps, software like Photoshop) that conflicts with the scene is a red flag.
5. Pivot: send a clean copy of the image to reverse-image/face tools, and read full EXIF/GPS with a dedicated metadata viewer to extract `geolocation`.

## Inputs → Outputs
- **In:** an `image` (local or on a web page)
- **Out:** ELA / PCA forensic overlays and a `metadata-exif` readout → a manipulation likelihood judgement
- **Empty/negative result looks like:** clean, consistent ELA/PCA and coherent metadata — consistent with (but not proof of) an unedited image; re-saved/social-media images often lose the signal, so "clean" can be inconclusive.

## Gotchas & OpSec
- Requires installing an extension (localInstall) — do it in a disposable browser profile.
- Forensic overlays are **indicative, not conclusive**; recompression by social platforms strips ELA usefulness, so absence of artifacts isn't proof of authenticity.
- The extension is old (2020) and small-userbase — verify anything critical with a second forensic tool.

## Overlaps ("do both")
- Pairs with dedicated EXIF/GPS metadata viewers and with reverse-image/face search — this flags *whether* an image is trustworthy, those extract *where/who* it points to.

## Trust & verifiability
`trust: unverified` — a third-party extension, but it applies transparent, well-documented forensic methods; you judge the overlays yourself rather than trusting an opaque verdict.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | perceptual-image-analysis |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
