---
id: tiktok-save-addons-mozilla-org
name: tiktok save (addons.mozilla.org)
description: Use when you have a TikTok video (from a target's `social-profile`/`username`) and want a local copy for offline analysis — returns the downloaded video file to inspect frames, audio, background and on-screen text.
url: https://addons.mozilla.org/en-GB/firefox/addon/tiktok-save/
category: social-networks
path:
- social-networks
bestFor: Saving a TikTok video as-seen in the browser so you can analyse it offline before it's deleted.
selectorsIn:
- username
- social-profile
selectorsOut:
- geolocation
- physical-description
status: live
pricing: free
costNote: Free Firefox add-on. No account or payment.
opsec: passive
opsecNote: The extension only saves the video already loaded in your browser — it does not follow, like, or message the account, so the target is not notified. Viewing the profile itself is what carries risk; do that from a sock-puppet/logged-out session. The download step adds no extra exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A minor third-party Firefox add-on (~1k users, last updated 2022) that simply enables right-click save of the currently-playing TikTok video. Not affiliated with TikTok; vet before installing. It only captures what the browser already displays.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- tiktok-com
- vdownloader
aliases:
- TikTok Save
- tiktok-save firefox
tags:
- tiktok
- TikTok Related Sites
- video-download
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# tiktok save (addons.mozilla.org)

> A lightweight Firefox add-on that turns a playing TikTok into a right-click "Save Video As…" — grab the clip locally before the account or platform pulls it.

## When to use
You are working a subject's TikTok (`username`/`social-profile`) and need a durable local copy of a specific video — because TikTok content is ephemeral (deleted, blocked, geo-restricted) and evidence should be preserved. Once saved, you can scrub frames for background `geolocation` clues, faces/`physical-description`, on-screen text, reflections, and audio the live scroll won't let you pause on.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "TikTok Save" from the Firefox Add-ons page (URL above); it's a small, older add-on, so review its permissions first.
2. In Firefox, open the target TikTok video from a sock-puppet/logged-out session and let it play.
3. Right-click the video and choose "Save Video As…" to download it as it appears in the browser (note: no watermark removal — you get the clip as displayed).
4. Analyse the saved file offline: step through frames, read signage/reflections, note landmarks and clothing.
5. Pivot: a geolocatable background feeds mapping tools; a visible face feeds reverse-image/face search; preserve the file with a hash for evidentiary integrity.

## Inputs → Outputs
- **In:** a TikTok video from a `username`/`social-profile`
- **Out:** a downloaded video file — from which you derive `geolocation`, `physical-description`, and on-screen intelligence
- **Empty/negative result looks like:** the save option doesn't appear or downloads a broken file — the add-on (last updated 2022) may not match TikTok's current player; fall back to a downloader like `[[vdownloader]]` or a URL-based service.

## Gotchas & OpSec
- Human-in-the-loop: none for the save itself; you must still open the profile to reach the video.
- OpSec: **passive** — the download doesn't interact with the account. The exposure is in *viewing* the profile, so browse logged-out or from a sock puppet. Preserve provenance (source URL, timestamp, hash) if the video may be evidence.
- The add-on is old and low-maintenance; expect it to break as TikTok changes and keep a fallback downloader ready.

## Overlaps ("do both")
- Pairs with `[[vdownloader]]` and native `[[tiktok-com]]` — this add-on is the quickest in-browser grab; a dedicated downloader handles bulk/quality/format and works when the add-on breaks. Capture the same video both ways if it matters.

## Trust & verifiability
`trust: community` — a small unaffiliated utility that only saves what your browser already shows, so it introduces no data-quality risk itself. Vet the extension's permissions before installing, and verify the saved file plays and matches the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tiktok-save-addons-mozilla-org |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → geolocation, physical-description |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
