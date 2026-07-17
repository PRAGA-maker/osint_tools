---
id: fotoforensics
name: FotoForensics
description: Use when you have an `image` and want to test for manipulation and read embedded metadata — returns `metadata-exif` and any `geolocation` GPS tags.
url: https://fotoforensics.com/
category: image-video-face
path:
- image-video-face
- source-verification
bestFor: Checking whether a photo has been edited and extracting its EXIF/metadata (including GPS).
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free to use; no account required for standard analysis.
opsec: active
opsecNote: Uploads are sent to a third party (Hacker Factor) and are RETAINED and can appear in the public feed of recent submissions. Never upload a sensitive/private image or one that could tip off a subject. Analyse a copy, and prefer a local tool if the image must stay private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by Neal Krawetz / Hacker Factor, a recognised authority on image forensics; ELA is an indicator, not proof — interpretation requires care.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- fotoforensics-com
aliases:
- Foto Forensics
- Hacker Factor FotoForensics
tags:
- image-forensics
- ela
- exif
- metadata
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# FotoForensics

> A free image-forensics workbench — Error Level Analysis plus a full metadata/EXIF viewer to spot edits and pull hidden GPS/camera data from a photo.

## When to use
You have an `image` (a photo of a person, a location, a document) and you need to (a) judge whether it has been digitally altered, and (b) read any embedded metadata — camera make/model, timestamps, software, and crucially GPS `geolocation` — that could place or date the shot. Good for vetting a photo before you trust it in an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://fotoforensics.com/ and upload the image file, or paste an image URL. Accepted: JPEG, PNG, WebP, HEIC, AVIF.
2. Review the **Error Level Analysis (ELA)** view: uniformly-compressed originals look even, while pasted/edited regions often show brighter, differently-textured error levels. Treat this as a lead, not a verdict.
3. Open the **Metadata** tab to read EXIF: camera make/model, capture timestamp, editing software (Photoshop tags suggest post-processing), and any GPS latitude/longitude.
4. Check the JPEG "Last Save Quality" and hidden-pixels/digest panels for further tampering signals.
5. Pivot: GPS `geolocation` feeds a map lookup; camera model + timestamp corroborate device and time claims; a Photoshop software tag flags a doctored source.

## Inputs → Outputs
- **In:** `image` (upload or URL)
- **Out:** ELA visualisation, full `metadata-exif`, GPS `geolocation` when present, save-quality/tampering indicators
- **Empty/negative result looks like:** stripped metadata (common for images downloaded from social platforms, which re-encode and remove EXIF) and a flat ELA — absence of tampering signals is not proof of authenticity, and missing EXIF just means it was scrubbed in transit.

## Gotchas & OpSec
- Human-in-the-loop: none, but read the caveats — ELA is an *indicator* and is easy to over-read; it does not "prove" a fake.
- OpSec: **active in a data-handling sense** — your upload is retained by a third party and may surface in the site's public recent-submissions feed. Do not upload anything sensitive or attributable; use a local EXIF/ELA tool instead when privacy matters.
- Social-media images are almost always re-compressed, which destroys EXIF and muddies ELA — analyse the highest-fidelity original you can obtain.

## Overlaps ("do both")
- Pairs with `[[fotoforensics-com]]` — same service, alternate index entry.
- Combine with a reverse-image search: FotoForensics tells you *whether/how* an image was edited, while reverse search tells you *where else* it appears and its likely origin.

## Trust & verifiability
`trust: trusted` — maintained by a well-known forensics researcher; the tooling is sound, but conclusions depend on careful, trained interpretation of ELA rather than the raw output alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fotoforensics |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
