---
id: filmot
name: Filmot
description: Use when you have a `name`, phrase, or keyword and want to find the exact YouTube videos and timestamps where it is spoken — returns videos, channels and jump-to timecodes from subtitle text.
url: https://filmot.com/
category: image-video-face
path:
- image-video-face
bestFor: Full-text searching YouTube's spoken subtitles/transcripts to find where a name or phrase is said and by whom.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Core subtitle and metadata search is free; logged-in/Patreon supporters get premium features (higher limits, extra filters). No account needed for basic searching.
opsec: passive
opsecNote: You search Filmot's index, not YouTube directly, so neither the subject nor a channel owner is notified. Filmot may log queries; opening the resulting YouTube links is a normal (logged-out) video view. Use a clean session if the topic is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent, widely-used YouTube subtitle search engine indexing 1.5B+ videos. Results are drawn from actual YouTube captions, so they are verifiable by opening the linked video.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- youtube-data-viewer
- google-video-search
aliases:
- filmot.com
- YouTube subtitle search
tags:
- video-search
- youtube
- transcripts
- subtitles
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Filmot

> A full-text search engine over YouTube's captions — find the exact video and second where a name, phrase, or phone number is spoken, across 1.5B+ videos.

## When to use
You want to find YouTube content by what is *said* in it, not just titles/descriptions. Search a subject's `name`, a username, a place, a phone number, or a distinctive phrase and Filmot returns the videos (with jump-to timestamps) where those words appear in the subtitles. Excellent for surfacing a person being named or speaking on video, for locating a specific clip, or for finding a subject's own channel via things they've said. The video's channel is a direct pivot to a `social-profile`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://filmot.com/.
2. Enter the search term(s) — use quotes for exact phrases; boolean AND/OR, channel filters (up to 200 channels), date ranges, and manual-vs-auto subtitle filters are available.
3. Review results: each hit shows the video, channel, and the matching subtitle line with a timestamp.
4. Click a result to open the YouTube video at that exact moment and confirm the context.
5. Pivot: the channel behind a match is a `social-profile`/handle to run through username and cross-platform tools; a name spoken on video corroborates other findings and can reveal associates in the same clip.

## Inputs → Outputs
- **In:** `name`, `username`, phrase, or keyword
- **Out:** matching YouTube videos + timestamps, the `social-profile` (channel) of each, `name` mentions in speech
- **Empty/negative result looks like:** no subtitle matches — the term may only appear in videos without captions, or not on YouTube at all. Absence is not proof it was never said on video.

## Gotchas & OpSec
- Only searches videos that have subtitles (auto-generated or manual); un-captioned videos are invisible to it.
- Auto-captions mis-transcribe names/uncommon words — try phonetic variants if an exact spelling returns nothing.
- OpSec: passive; searching Filmot doesn't touch the target. Open linked videos logged-out to avoid tying views to your account.

## Overlaps ("do both")
- Pairs with `[[youtube-data-viewer]]` (metadata/geolocation of a specific video you found) and `[[google-video-search]]` — Filmot finds videos by spoken content, those enrich or broaden a specific video once located.

## Trust & verifiability
`trust: community` — an independent index of real YouTube captions; every result is verifiable by opening the linked video at the given timestamp, so false positives are easy to check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | filmot |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
