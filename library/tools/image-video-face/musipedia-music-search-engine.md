---
id: musipedia-music-search-engine
name: Musipedia Music Search Engine
description: Use when you have a melody (hummed, whistled, or tapped) — e.g. background music in a subject's video — and want to identify the tune; returns candidate song/composition titles (`metadata-exif`-style media identification).
url: http://www.musipedia.org/query_by_humming.0.html
category: image-video-face
path:
- image-video-face
bestFor: Identifying a piece of music from its melody when you don't have the original recording to fingerprint.
selectorsIn: []
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, open, community-run music encyclopedia and melody search engine; no account needed.
opsec: passive
opsecNote: You submit a melody you hum/enter, not any target data; nothing about the subject is transmitted. Purely passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running community/academic melody-search project; reliable for what it does (tune ID) but of narrow, indirect OSINT value.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Musipedia
- query by humming
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- audio
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Musipedia Music Search Engine

> A "query by humming" melody search engine — identify a tune from its notes rather than an exact recording. Its OSINT use is narrow: naming the music in a subject's media.

## When to use
Rarely, and indirectly. If a subject's video, voicemail greeting, or livestream contains a melody you can reproduce (hum, whistle, tap the rhythm, or enter on a virtual keyboard) but you don't have the original audio file to fingerprint with Shazam, Musipedia can identify the composition. Unlike fingerprinting, it matches the *melody*, so it works for covers, hums, and live performances. It yields media context (what track is playing), not any identifier about a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.musipedia.org/query_by_humming.0.html (or the site's keyboard/Parsons-code search pages).
2. Input the melody: hum/whistle into the mic, play the on-screen piano, tap the rhythm, or enter Parsons code (up/down/repeat contour).
3. Submit; read the ranked candidate matches (song/composition titles).
4. Confirm the best candidate against the source media by ear.
5. Pivot: a named track can date/contextualise a clip or hint at a subject's tastes/region — weak, corroborating signal only.

## Inputs → Outputs
- **In:** a melody (hummed/whistled/keyed/rhythm/Parsons code) — no personal selector
- **Out:** candidate music titles/compositions (`metadata-exif`-style media identification)
- **Empty/negative result looks like:** no confident match — common for obscure, non-Western, or heavily-produced tracks the melody DB doesn't hold.

## Gotchas & OpSec
- Not a people-finder; its investigative value is marginal and indirect.
- Melody matching is approximate; off-key humming and complex arrangements reduce accuracy.
- For an exact recording, an audio fingerprinter (Shazam/AudioTag) will usually beat it.

## Overlaps ("do both")
- Pairs with audio-fingerprinting tools — use fingerprinting when you have the original recording, Musipedia when you only have the melody.

## Trust & verifiability
`trust: community` — a stable, well-regarded academic/community project; results are trustworthy tune IDs, but the tool's relevance to person-focused investigations is deliberately limited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | musipedia-music-search-engine |
| category | image-video-face |
| selectorsIn → selectorsOut |  → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
