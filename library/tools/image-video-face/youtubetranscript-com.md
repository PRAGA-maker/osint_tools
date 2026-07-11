---
id: youtubetranscript-com
name: YouTube Transcript
description: Use when you have a YouTube video (a `social-profile` URL) and want its full spoken transcript to mine for names, places and details — returns name, associate and geolocation leads mentioned on-camera.
url: https://youtubetranscript.com/
category: image-video-face
path:
- image-video-face
bestFor: Pulling the full text transcript of a YouTube video so it can be read, searched, and mined for entities.
selectorsIn:
- social-profile
selectorsOut:
- name
- associate
- geolocation
status: live
pricing: free
costNote: Free; no account. Works on videos that have captions/auto-captions available.
opsec: passive
opsecNote: Fetches the public transcript server-side — it does not add a view from your session, subscribe, or comment, so the uploader is not alerted. Only your IP touches the transcript site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple utility that surfaces YouTube's own caption track; accuracy of the text depends on whether captions are human-made or auto-generated (auto-captions mis-hear names/places).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- YouTube Transcript
- youtubetranscript.com
tags:
- youtube
- YouTube Related Sites
- transcript
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# YouTube Transcript

> Turns any captioned YouTube video into readable, searchable text — so you can mine what was said for names, places, and corroborating detail.

## When to use
You have a YouTube video tied to your subject (their own channel, or one that features them) and you need the spoken content as text: to search a long video for a name or address, to extract people and places mentioned on-camera, or to quote/timestamp a statement. Reading the transcript is far faster than watching, and lets you grep hours of footage for the detail you care about.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://youtubetranscript.com/.
2. Paste the YouTube video URL (the `social-profile`/video link) and submit.
3. Read the returned transcript (often timestamped). Use in-page/browser find to search for candidate `name`s, place names (`geolocation`), organisations, or handles.
4. Pivot: names/associates mentioned become new subjects; a place named on-camera becomes a geolocation lead; a timestamped claim can be corroborated against other sources or the video itself.

## Inputs → Outputs
- **In:** a YouTube video URL (`social-profile`/video)
- **Out:** full transcript text → extracted `name`, `associate`, `geolocation` leads
- **Empty/negative result looks like:** "no transcript available" — the video has captions disabled and no auto-captions (or is private/removed); nothing to mine there.

## Gotchas & OpSec
- Auto-generated captions frequently mis-transcribe proper nouns — verify any name/place before relying on it, and check the audio at that timestamp.
- Only works on videos that expose a caption track; live streams and caption-disabled uploads may return nothing.
- Passive: pulling the transcript does not register as a view or notify the uploader.

## Overlaps ("do both")
- Pairs with a metadata/frame-analysis pass on the same video — the transcript captures what was *said*, while frame grabs and description/metadata capture what was *shown* and *tagged*; together they cover the whole video.

## Trust & verifiability
`trust: community` — a thin wrapper over YouTube's caption data. The text is trustworthy where captions are human-authored; treat auto-caption output as approximate, especially for names and locations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtubetranscript-com |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → name, associate, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
