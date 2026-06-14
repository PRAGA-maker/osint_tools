---
id: forensically
name: Forensically
description: Use when you need to forensically inspect a single photo for manipulation, cloning, or hidden metadata before trusting it as evidence — returns ELA/noise/clone-detection views and EXIF.
url: https://29a.ch/photo-forensics/
category: image-video-face
path:
- image-video-face
- images
- forensics
bestFor: Free in-browser image forensics (ELA, clone detection, noise, magnifier, EXIF/metadata) on one photo.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Fully free; no account; runs client-side in the browser.
opsec: passive
opsecNote: Image is processed locally in the browser (29a.ch is client-side); nothing is searched against a third party, so it does not tip off a subject. Still treat any cloud upload cautiously.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-standing tool by Jonas Wagner (29a.ch), widely cited in OSINT/journalism forensics guides.
missingPersonsRelevance: high
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
- ghiro
aliases:
- 29a.ch photo forensics
tags:
- forensics
- ela
- metadata
source: arf-seed
lastVerified: ''
enrichment: full
---

# Forensically

> A free, browser-based image forensics toolkit for spotting manipulation and reading hidden metadata in a single photo.

## When to use
You have an `image` (a tip photo, a "proof of life" image, a social-media picture of a missing person or location) and need to judge whether it is authentic or edited, and pull any embedded clues. Tie-in: input `image`, outputs `metadata-exif` and sometimes `geolocation` (from GPS EXIF), plus visual evidence of tampering.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://29a.ch/photo-forensics/ and drag in or open your image.
2. Step through the left-panel tools: **Magnifier** (pixel-level zoom), **Error Level Analysis (ELA)** (re-saved/edited regions glow), **Clone Detection** (copy-paste regions), **Noise Analysis**, **Level Sweep**, **Luminance Gradient**, and **Metadata/Geo Tags**.
3. Read the **Metadata** panel for camera make/model, timestamps, software, and GPS coordinates if present.
4. Pivot: feed any GPS `geolocation` into a map/geo tool; cross-check a suspicious image against [[fotoforensics-com]] for a second ELA opinion, or run a batch in [[ghiro]].

## Inputs → Outputs
- **In:** `image`
- **Out:** `metadata-exif`, `geolocation` (when GPS EXIF present)
- **Empty/negative result looks like:** Metadata panel empty (stripped by upload platforms) and ELA showing uniform noise — common for screenshots and social-media re-encodes, not proof of authenticity.

## Gotchas & OpSec
- Human-in-the-loop: results are heuristic; ELA and clone hits require expert interpretation, not automated verdicts.
- Most social platforms strip EXIF, so missing metadata is expected and not suspicious by itself.
- OpSec: passive — processing is client-side, so it does not query the subject or a vendor.

## Overlaps ("do both")
- Pairs with [[fotoforensics-com]] (different ELA implementation, second opinion) and [[ghiro]] (automated, batchable for many files).

## Trust & verifiability
`trust: trusted` — maintained by Jonas Wagner (29a.ch); a staple in journalism and OSINT image-verification curricula.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forensically |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
