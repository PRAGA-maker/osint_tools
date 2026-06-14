---
id: fotoforensics-com
name: fotoforensics.com
description: Use when you need a fast Error Level Analysis and metadata dump on a photo to check for editing — returns ELA heatmap, EXIF/JPEG metadata, and hidden-string clues.
url: http://fotoforensics.com/
category: image-video-face
path:
- image-video-face
bestFor: One-click ELA plus full metadata/JPEG analysis of an uploaded or URL-linked image.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free public analyzer; paid/enterprise tiers exist for bulk and API but not needed for casework.
opsec: active
opsecNote: Image is uploaded to Hacker Factor's servers and publicly retrievable by hash/URL — do NOT upload sensitive or non-public case images you don't want exposed.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by Dr. Neal Krawetz (Hacker Factor); the canonical public ELA tool, widely referenced in forensics and journalism.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- FotoForensics
tags:
- photosites
- Photo Related Sites
- forensics
- ela
source: uk-osint
lastVerified: ''
enrichment: full
---

# fotoforensics.com

> The best-known public Error Level Analysis tool: upload a photo and get an ELA heatmap plus a deep metadata read.

## When to use
You have an `image` and need a quick, authoritative check on whether it was edited, plus any embedded camera/GPS data. Tie-in: input `image`, output `metadata-exif` and `geolocation` (when GPS EXIF survives).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://fotoforensics.com/ and upload a file or paste an image URL.
2. Review the **ELA** view — uniformly bright edges around an object suggest a splice/paste; uniform image-wide noise is typical of unedited or re-saved photos.
3. Open the **Metadata**, **JPEG %**, **Hidden Pixels**, and **Strings** tabs for camera make/model, timestamps, editing software, GPS, and embedded text.
4. Pivot: take GPS `geolocation` to a map; corroborate ELA findings with [[forensically]] (client-side, no upload) for a privacy-safe second pass.

## Inputs → Outputs
- **In:** `image`
- **Out:** `metadata-exif`, `geolocation` (if GPS EXIF present)
- **Empty/negative result looks like:** Metadata panel sparse (platform-stripped) and ELA flat — neither proves authenticity; absence of evidence is not evidence.

## Gotchas & OpSec
- Human-in-the-loop: ELA is interpretive; it flags re-compression, not guaranteed forgery.
- OpSec: **active** — uploads are stored on a public server and can be re-found via the image hash. Use [[forensically]] instead for confidential images.
- Social-platform downloads usually have EXIF stripped, so empty metadata is expected.

## Overlaps ("do both")
- Pairs with [[forensically]] for a local, no-upload ELA, and with [[ghiro]] for automated batch analysis of many files.

## Trust & verifiability
`trust: trusted` — operated by Dr. Neal Krawetz (Hacker Factor Solutions), the reference implementation for public ELA.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fotoforensics-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
