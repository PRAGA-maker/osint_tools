---
id: jump-cutter
name: Jump Cutter
description: Use when you must review long video/audio evidence (`image`/media, lectures, streams) and want to skip silent gaps — an extension that fast-forwards silence, saving analyst review time.
url: https://chromewebstore.google.com/detail/jump-cutter/lmppdpldfpfdlipofacekcfleacbbncp
category: social-networks
path:
- social-networks
bestFor: Speeding up review of long recorded videos/streams by auto-skipping silent sections.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (AGPL-3.0); no account.
opsec: passive
opsecNote: The extension runs entirely locally on video already playing in your browser and collects no data. It sends nothing to any subject or third party — the only footprint is whatever site is hosting the video you're watching. It's an analyst aid, not a collection tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular open-source extension (~10k users, 4.8★, AGPL-3.0); it processes playback locally and touches no personal data of its own.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Jump Cutter extension
tags:
- social-media
- youtube
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Jump Cutter

> A browser extension that fast-forwards (or skips) the silent stretches of any video in real time — a time-saver for wading through hours of recorded footage.

## When to use
You have long-form video/audio evidence to review — a subject's lecture, livestream, unedited body-cam or surveillance clip, a captured X Space, a rambling YouTube upload — and most of it is dead air. Jump Cutter automatically speeds through silence so you cover the same material in a fraction of the time. It's a workflow accelerator for the review phase, not a source of selectors.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Jump Cutter" from the Chrome Web Store into your OSINT browser profile.
2. Play any video in the browser (it works on YouTube, Coursera, Twitch, and local files).
3. The extension detects quiet segments and fast-forwards or skips them per your settings; tune the silence threshold, skip vs. speed-up, and keyboard shortcuts.
4. Watch/listen at the compressed pace; slow back to normal when speech resumes.
5. Pivot: use it to triage long footage quickly, then note timestamps of relevant segments for closer analysis or transcription.

## Inputs → Outputs
- **In:** none as a selector — it operates on a video you're already playing
- **Out:** none as a selector — it changes *how* you watch, not what data you get
- **Empty/negative result looks like:** N/A — if a video has no silence, it simply plays normally; there's no lookup to come back empty.

## Gotchas & OpSec
- It only affects playback in your browser; it does not download or capture — pair with a downloader if you need to preserve the file.
- Aggressive silence thresholds can clip the start of quiet speech — loosen the setting if you miss words.
- OpSec: fully passive and local; the only footprint is the video host you're already visiting.

## Overlaps ("do both")
- Pairs with a capture/download tool like [[spaces-down]] (or a YouTube downloader) and a transcription tool — download to preserve, transcribe for search, and use Jump Cutter to eyeball long footage fast.

## Trust & verifiability
`trust: community` — a well-reviewed open-source (AGPL) extension that processes playback locally and handles no personal data; nothing to verify beyond your own review notes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jump-cutter |
| category | social-networks |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
