---
id: invid-weverify-verification-plugin
name: InVID-WeVerify Verification Plugin
description: Use when you have an `image` or video and want to verify it and pull it apart — returns reverse-search pivots, extracted keyframes, `metadata-exif`, and forensic/deepfake signals.
url: https://www.invid-project.eu/tools-and-services/invid-verification-plugin/
category: image-video-face
path:
- image-video-face
- deepfake-detection
bestFor: One-click multi-engine reverse image search, video keyframing, EXIF/metadata extraction, and image forensics on social-media media.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free browser extension (Chrome/Firefox/Edge), maintained by the EU-funded InVID/WeVerify/vera.ai projects. No account required.
opsec: active
opsecNote: Reverse-search and analysis modules send the image/keyframe to third-party engines (Google, Bing, Yandex, Baidu, TinEye), creating query telemetry there. EXIF and forensic (ELA/copy-move) modules run locally in the browser with no upload. Do the reverse searches from a sock-puppet browser/IP if the collection is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Developed by the EU InVID/WeVerify/vera.ai research consortium and endorsed in Bellingcat's toolkit; a long-standing, widely-used verification standard among journalists and OSINT investigators.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- InVID
- WeVerify
- Fake News Debunker
- InVID plugin
tags:
- verification
- reverse-image-search
- image-forensics
- deepfake-detection
- browser-extension
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# InVID-WeVerify Verification Plugin

> The "Swiss Army knife" of media verification — one browser extension bundling reverse image search, video keyframing, metadata extraction, magnification, and image forensics.

## When to use
You have an `image` or a video (a social-media post, a photo of a missing person, a suspicious clip) and need to establish where else it appears, when/where it was taken, and whether it has been manipulated. Ideal for locating the earliest instance of a photo, extracting a face/landmark keyframe to reverse-search, reading in-browser EXIF for `geolocation`, or flagging edited/AI-generated media before you build on it.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the "Fake News Debunker — InVID & WeVerify" extension in Chrome/Firefox/Edge on your investigation profile.
2. Open the plugin's toolbar. For a still, use **Image → Keyframes/Magnifier** or paste the URL; for a clip, use **Video → Analysis** to extract keyframes.
3. Right-click a keyframe or image to fire **reverse image search** across Google, Bing, Yandex, Baidu, and TinEye in one action — Yandex is often strongest for faces.
4. Use **Image → Metadata** to read EXIF (including GPS `geolocation`) locally, and the **Forensics** tab (ELA, copy-move, eight filters) plus the experimental **Deepfake** tab for manipulation signals.
5. Pivot: reverse-search hits feed geolocation/chronolocation and social-profile discovery; EXIF GPS feeds mapping tools; a manipulation flag tells you to distrust the media before acting.

## Inputs → Outputs
- **In:** `image` (still or video keyframe)
- **Out:** `metadata-exif` (EXIF incl. GPS), `geolocation` leads (via reverse search + EXIF), reverse-search pivots to other appearances, forensic/deepfake probability signals
- **Empty/negative result looks like:** reverse search returns no visual matches and EXIF is stripped (common on re-uploaded social media) — absence of matches is not proof of originality; it usually means engines haven't indexed it, not that it is authentic.

## Gotchas & OpSec
- It does NOT output a true/false verdict — it generates leads you must confirm with source-checking, geolocation, and archives.
- Reverse-search modules are **active** (they hit external engines); metadata/forensics are local. Segregate the two if you need to stay quiet.
- The Deepfake tab is experimental — treat its 0–1 score as a prompt to investigate, never as proof.

## Overlaps ("do both")
- Pairs with dedicated reverse-image and face engines in the [[image-video-face]] set and with standalone [[metadata-exif]] extractors — the plugin is the fast all-in-one first pass; specialised tools go deeper on any single lead it surfaces.

## Trust & verifiability
`trust: trusted` — a mature EU-funded, Bellingcat-endorsed verification toolkit. The tooling is reliable; the interpretation is on you, since it deliberately avoids automated verdicts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | invid-weverify-verification-plugin |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
