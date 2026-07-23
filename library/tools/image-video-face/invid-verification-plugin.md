---
id: invid-verification-plugin
name: InVID / WeVerify Verification Plugin
description: Use when you have an `image` or a social-media video and want to verify it — fragment video into keyframes, run reverse-image search, read metadata and apply forensic filters — returns keyframes, metadata-exif and origin leads.
url: https://weverify.eu/verification-plugin/
category: image-video-face
path:
- image-video-face
bestFor: The Swiss-army-knife browser toolkit for debunking/verifying videos and images (keyframes, reverse image, metadata, forensics, geolocation).
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
- image
status: live
pricing: free
costNote: Free browser extension (Chrome/Firefox/Edge) developed under EU research projects (InVID, WeVerify, vera.ai); no payment required.
opsec: passive
opsecNote: Mostly passive analysis you run in your browser, but individual actions vary — reverse-image searches query third-party engines (Google, Yandex, Bing, TinEye) and loading a social video fetches it from the platform. None of this notifies the content's author. Use a sock-puppet browser session as usual.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Built by academic/journalism consortia (InVID, WeVerify, now vera.ai) and the standard verification toolkit in newsroom/fact-checking workflows.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- reveal-image-verification-assistant
aliases:
- InVID
- WeVerify
- Verification Plugin
- Fake News Debunker
tags:
- video-verification
- reverse-image
- forensics
- fact-checking
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# InVID / WeVerify Verification Plugin

> The newsroom-standard browser toolkit for verifying videos and images: keyframe extraction, multi-engine reverse image search, metadata, forensics, magnifier and geolocation.

## When to use
You have an `image` or a social-media video (YouTube, X/Twitter, Facebook) and need to establish whether it's authentic, where it originally came from, and when — the core task in verifying UGC around a missing-person sighting, incident, or claim. The plugin bundles the tools you'd otherwise juggle separately into one context menu.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Verification Plugin from your browser's store (Chrome/Firefox/Edge).
2. Open the plugin and pick a tool:
   - **Keyframes** — paste a video URL to fragment it into stills, then reverse-search each.
   - **Analysis** — pull a YouTube/X/Facebook video's metadata, upload time, and comments.
   - **Image / Magnifier** — reverse-search an image across Google/Yandex/Bing/TinEye and zoom for detail.
   - **Metadata** — read EXIF from an image/video.
   - **Forensics** — error-level analysis and filters to spot manipulation.
3. Cross-reference the reverse-image hits to find the earliest appearance (original source).
4. Use visible clues (signage, landmarks) plus the magnifier to attempt geolocation.
5. Pivot: an earlier posting or a geolocated frame feeds timeline and location analysis.

## Inputs → Outputs
- **In:** an `image`, or a social-media video URL
- **Out:** keyframes, `metadata-exif`, reverse-image matches (earliest source), forensic indicators, `geolocation` leads
- **Empty/negative result looks like:** no reverse-image matches and clean metadata — could mean genuinely original, or simply not indexed/stripped; absence isn't proof of authenticity.

## Gotchas & OpSec
- Reverse-image results depend on each engine's index — run several (the plugin makes this one click) and don't trust a single miss.
- Social platforms strip EXIF, so uploaded videos/images often have no camera metadata — lean on keyframes + reverse search instead.
- Forensic/ELA filters are suggestive, not conclusive — corroborate with source-tracing.

## Overlaps ("do both")
- Pairs with dedicated reverse-image engines and EXIF viewers — the plugin orchestrates them, but a standalone tool (Yandex, an EXIF reader) can go deeper on a specific step; and with geolocation tools for pinning a keyframe.

## Trust & verifiability
`trust: trusted` — a free tool from EU academic/journalism research consortia, widely adopted as the verification standard; its individual steps (reverse search, EXIF) are independently reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | invid-verification-plugin |
