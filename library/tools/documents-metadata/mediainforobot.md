---
id: mediainforobot
name: '@mediainforobot'
description: Use when you have a media file (or Telegram media) and want its technical MediaInfo, screenshots, or audio spectrogram — returns codec/container metadata and derived visuals.
url: https://t.me/mediainforobot
category: documents-metadata
path:
- documents-metadata
bestFor: Pulling detailed MediaInfo (codecs, container, duration) and spectrograms/screenshots from a video or audio file via Telegram.
selectorsIn:
- metadata-exif
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free Telegram bot; requires a Telegram account to message it. Open-source (GitLab spechide/MediaInfoRoBot).
opsec: active
opsecNote: You must SEND the file (or its link) to a third-party Telegram bot, so the media leaves your control and passes through Telegram's and the bot operator's infrastructure. Never submit media containing a subject's private/sensitive content. Use a sock-puppet Telegram account and, ideally, only non-sensitive samples.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: An open-source community Telegram bot (source on GitLab); the tool is transparent, but you are trusting an unaffiliated operator with whatever you upload.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- exiftool
- mediainfo
aliases:
- mediainforobot
- MediaInfo Bot
- mi bot
tags:
- metadata
- media-analysis
- telegram-bot
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# @mediainforobot

> A Telegram bot that returns detailed MediaInfo for a video/audio file — codecs, container, duration — plus generated screenshots and audio spectrograms, all inside a chat.

## When to use
You have a media artifact (`metadata-exif` carrier) — a video or audio clip from a subject's post, a shared file, an evidence sample — and want its technical fingerprint without local tooling: exact codecs, container, bitrate, duration, and derived views (frame screenshots, an audio spectrogram that can expose hidden tones/edits). Handy when you're mobile or lack a workstation. For anything sensitive, prefer local tools instead of sending the file away.

## How to use it (`bestInteractionPattern`: mobile-app)
1. In Telegram, open https://t.me/mediainforobot and start the bot.
2. Send it a media file or a supported link.
3. Choose an action: MediaInfo (technical metadata), screenshot generation, spectrogram, or trim.
4. Read the returned metadata; save the spectrogram/screenshots as leads (edits, splices, embedded tones).
5. Corroborate anything important with a local run of `[[mediainfo]]` / `[[exiftool]]` on the original file.

## Inputs → Outputs
- **In:** a media file or link (its embedded `metadata-exif`)
- **Out:** technical `metadata-exif` (codecs/container/duration), screenshots, spectrogram
- **Empty/negative result looks like:** the bot rejects the format/size or returns sparse info — re-run locally; a thin readout doesn't mean the file is clean of metadata.

## Gotchas & OpSec
- **The file leaves your control** — it goes to Telegram and a third-party operator. Never send a subject's private/sensitive media; use only non-sensitive samples, and a sock-puppet Telegram account.
- Requires a Telegram account (human-in-the-loop).
- OpSec: **active** — you are uploading the artifact to a remote party.

## Overlaps ("do both")
- Pairs with `[[exiftool]]` and `[[mediainfo]]` — those are the authoritative *local* metadata tools with no upload risk; use the bot for convenience/spectrograms, then verify locally on the untouched original.

## Trust & verifiability
`trust: community` — open-source and transparent about what it does, but operated by an unaffiliated third party; trust the code, not the handling of whatever you upload.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mediainforobot |
| category | documents-metadata |
| selectorsIn → selectorsOut | metadata-exif → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
