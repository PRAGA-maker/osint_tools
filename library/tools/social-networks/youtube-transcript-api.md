---
id: youtube-transcript-api
name: youtube-transcript-api
description: Use when you have a YouTube video ID and want its spoken content as text — returns the transcript/subtitles, including auto-generated and translated.
url: https://github.com/jdepoix/youtube-transcript-api
category: social-networks
path:
- social-networks
bestFor: Programmatically pulling a YouTube video's transcript (manual or auto-generated, any language) for keyword search and analysis.
selectorsIn:
- social-profile
selectorsOut:
- name
- associate
- geolocation
status: live
pricing: free
costNote: Free and open source (MIT); install via pip. No API key or Google account required for public videos.
opsec: passive
opsecNote: Fetches publicly available captions from YouTube from your machine — requests come from your IP, so use a VPN for volume. It does not require logging in and touches only public transcript endpoints; the uploader is not notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Widely used, well-maintained open-source Python library; it reads YouTube's own caption data, so transcript accuracy is YouTube's (auto-captions can misspell names/places).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- get-text-from-video
- eightify
aliases:
- jdepoix youtube-transcript-api
tags:
- Social Media
- YouTube
- transcript
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# youtube-transcript-api

> A Python library that pulls any public YouTube video's transcript — including auto-generated and translated captions — so you can search spoken content at scale.

## When to use
You have a subject's YouTube channel/videos (a `social-profile`) and need to mine what is actually said: names dropped, places mentioned, relationships and plans described, dates referenced. Watching hours of video by hand is impractical — this turns each video into searchable text, letting you grep across a channel for a `name`, `geolocation`, or `associate`. Ideal when a person of interest vlogs, streams, or is discussed in others' videos.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install youtube-transcript-api`.
2. Grab the video ID from the URL (the `v=` parameter) and call the API in a short script to fetch the transcript; it also lists available languages and can translate.
3. Save transcripts and search them for names, places, dates, and relationships; batch across a channel's video IDs.
4. Pivot: a name/place found in speech feeds people- and location-search; timestamps let you jump back to the video to verify context.

## Inputs → Outputs
- **In:** YouTube video ID (from a `social-profile`/channel)
- **Out:** transcript text yielding `name`, `associate`, `geolocation` mentions
- **Empty/negative result looks like:** the library raises "transcripts disabled" or "no transcript found" — captions are off for that video; try another video or an audio-to-text tool like `[[get-text-from-video]]`.

## Gotchas & OpSec
- Auto-generated captions misspell proper nouns and lack punctuation — treat extracted names/places as approximate leads to verify by ear.
- YouTube periodically changes its endpoints and rate-limits scraping; pin a current library version and throttle batch jobs (use a VPN for volume).
- OpSec: passive; the uploader is not notified.

## Overlaps ("do both")
- Pairs with `[[get-text-from-video]]` (audio→text when no captions exist) and `[[eightify]]` (AI summary of a transcript) — this one is best for exact keyword search across many videos.

## Trust & verifiability
`trust: community` — a popular, actively maintained open-source library that reads YouTube's own caption data; accuracy is bounded by YouTube's captions, and you should confirm key names against the actual audio.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-transcript-api |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → name, associate, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
