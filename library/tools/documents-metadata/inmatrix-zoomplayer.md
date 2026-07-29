---
id: inmatrix-zoomplayer
name: Inmatrix Zoom Player
description: Use when you have a recovered/unusual `image` or video file that standard players will not open — plays a very wide range of media formats so you can view the content. Not a selector-extraction tool.
url: http://www.inmatrix.com/files/zoomplayer_download.shtml
category: documents-metadata
path:
- documents-metadata
bestFor: Playing obscure or codec-heavy video/audio files during evidence review on Windows.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Zoom Player has a free edition; the MAX/Pro tiers are paid ("Buy Now"). Windows only. The free edition covers ordinary playback needs.
opsec: passive
opsecNote: A local desktop media player — it plays files on your machine and makes no network queries about a target. Review evidence on an isolated/analysis machine, since opening unknown media can still trigger codec-level exploits.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: unverified
trustNote: Long-running independent Windows product (Inmatrix); reputable but closed-source, so behavior on untrusted files cannot be audited.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Zoom Player
- ZoomPlayer
tags:
- toddington
- media-player
- evidence-review
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Inmatrix Zoom Player

> A highly customizable Windows media player that opens formats mainstream players choke on — a viewing utility for recovered video/audio, not an intelligence source.

## When to use
You have a media file — a clip pulled from a device, a CCTV export, an odd container from a download — that Windows Media Player or the browser refuses to play. Zoom Player, paired with a codec pack, plays a very wide range of formats so you can actually watch/listen to the content during review. It extracts no selectors itself; its value is that it *renders the file at all*.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the installer from the Inmatrix page (free edition is sufficient for playback) and install on a Windows analysis machine — ideally isolated, since you may be opening untrusted media.
2. If a file still will not play, install a reputable codec pack (e.g. LAV Filters / K-Lite) so Zoom Player can decode it.
3. Open the file and review it frame by frame; use Zoom Player's zoom, aspect, and audio controls to inspect detail (faces, plates, signage, timestamps burned into frames).
4. Capture what matters as stills, then hand those to the appropriate analysis tool.
5. Pivot: any faces, `vehicle-plate`s, or location cues you *see* feed dedicated face/plate/geolocation tools — Zoom Player only gets the pixels on screen.

## Inputs → Outputs
- **In:** a local video/audio file (no case selectors)
- **Out:** rendered playback so a human can view the content (no case selectors)
- **Empty/negative result looks like:** the file still fails to play even with a codec pack — the container is corrupt or the codec is genuinely missing; try ffmpeg/VLC to diagnose before assuming the file is unrecoverable.

## Gotchas & OpSec
- Human-in-the-loop: this is entirely manual viewing; nothing is automated or extracted for you.
- OpSec: local and passive, but opening unknown media can carry codec-level exploit risk — review on an isolated machine, not your daily driver.
- Windows-only and closed-source; on macOS/Linux use VLC/ffmpeg for the same job.
- The MAX tier is paid, but format playback — the reason it is here — is available in the free edition.

## Overlaps ("do both")
- Overlaps with VLC and ffmpeg as universal players/decoders; use whichever opens the file, then pull stills into `metadata-exif` and face/plate tools. Zoom Player is a viewer, not an analyzer — always pair it with something that extracts.

## Trust & verifiability
`trust: unverified` — an established but closed-source commercial player; fine as a rendering tool, but not something to point at untrusted files without sandboxing, and it produces no analyzable output on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inmatrix-zoomplayer |
| category | documents-metadata |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (manual-review) |
