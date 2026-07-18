---
id: ytgrep
name: YtGrep
description: Use when you have one or more YouTube video URLs and want to grep their captions for a word/phrase — returns matching subtitle lines with timestamps.
url: https://pypi.org/project/ytgrep/
category: social-networks
path:
- social-networks
bestFor: Keyword/regex searching the closed captions of one or many YouTube videos from the command line.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source (MIT) Python package on PyPI; no account or API key.
opsec: passive
opsecNote: It fetches public caption tracks from YouTube's servers, not from the target — the video owner is not notified. The requests originate from your IP; use a VPN if you don't want YouTube's logs to tie the caption pulls to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: A small open-source CLI by developer alexkohler; it reads genuine YouTube captions, so results are as accurate as the video's subtitle track (auto-generated captions can be imperfect).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- ytgrep CLI
tags:
- youtube
- captions
- cli
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# YtGrep

> A grep-for-YouTube-subtitles CLI: point it at video URLs and a search term, and it returns the caption lines (with timecodes) where that term is spoken.

## When to use
You are working a subject's YouTube presence and need to know *whether and where* something is said inside their videos — a name, a place, a phone number, an admission — without watching hours of footage. Feed the videos a channel posts (or that mention the subject) and grep the spoken content. Especially useful across many videos at once when scanning a channel for a keyword.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install ytgrep` (Python ≥ 3.5; ensure pip's bin dir is on your PATH).
2. Run against one or more videos:
   `ytgrep 'search_term' https://youtu.be/VIDEO1 https://youtu.be/VIDEO2`
3. Use options as needed:
   - `-e` to match a **regular expression** instead of a literal term.
   - `--links` to include jump-to-timestamp links for each hit.
   - `-v` for verbose/debug output.
4. Read the output: caption lines containing the term, each with the video and timecode.
5. Pivot: a matched timecode sends you straight to the relevant moment; content in captions (names, handles, locations) becomes new selectors.

## Inputs → Outputs
- **In:** one or more YouTube video URLs + a keyword/regex (videos usually gathered from a `social-profile`/channel)
- **Out:** matching subtitle lines with video + timestamp; optional deep-links
- **Empty/negative result looks like:** no matches printed — either the term isn't spoken, or the video has **no caption track** (ytgrep can only search videos that have subtitles/auto-captions).

## Gotchas & OpSec
- Videos without any caption track (no manual subs, no auto-captions) can't be searched — a null result there means "no transcript", not "term absent".
- Auto-generated captions mis-transcribe names and jargon; try phonetic variants and use `-e` regex for fuzzy matches.
- OpSec: passive. You pull public captions; nothing signals the channel owner.

## Overlaps ("do both")
- Pairs with [[hadzy-com]] — ytgrep searches what's *spoken* in a video's captions, Hadzy searches what's *written* in its comments; run both to cover a video's full text footprint.

## Trust & verifiability
`trust: community` — an open-source hobby CLI. It surfaces authentic YouTube caption data, so verification is easy (open the timestamped link and listen), but auto-caption errors mean you should confirm any critical hit against the actual audio.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ytgrep |
