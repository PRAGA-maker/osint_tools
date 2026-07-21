---
id: youtube-caption-searcher
name: YouTube Caption Searcher
description: Use when you have a YouTube video and a keyword and want to jump to where it's spoken in the captions — returns caption timestamps, surfacing names/places/context mentioned in the audio.
url: https://chromewebstore.google.com/detail/youtube-caption-searcher/aagdogpbnlhfcaaendmehjmdnepolaap
category: social-networks
path:
- social-networks
bestFor: Keyword-searching a YouTube video's subtitles to locate exactly where a term is spoken.
selectorsIn:
- username
selectorsOut:
- name
- geolocation
- associate
status: degraded
pricing: free
costNote: Free Chrome extension; verify it is still listed on the Chrome Web Store before relying on it.
opsec: passive
opsecNote: The extension reads the caption track of a video you are already watching — no interaction with the uploader, nothing disclosed. Passive. Installing any extension grants it browser permissions, so use a dedicated research profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A third-party Chrome extension by an unknown developer; it operates on YouTube's own caption data, which you can verify by reading the captions directly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- YouTube caption search
tags:
- Social Media
- YouTube
- browser-extension
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# YouTube Caption Searcher

> A browser extension that turns a YouTube video's captions into a searchable transcript — find the exact moment a keyword is spoken instead of scrubbing the timeline.

## When to use
You have a long YouTube video tied to a subject (their channel, or one that mentions them) and need to find where a specific term — a name, place, event — is spoken. Manually watching hours of video is impractical; caption search jumps you straight to the relevant timestamps, surfacing spoken names, locations, and references that never appear in the title or description.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "YouTube Caption Searcher" from the Chrome Web Store into a research browser profile (confirm the listing is still live first).
2. Open the target YouTube video (it must have captions — auto-generated or uploaded).
3. Use the extension's search box to enter your keyword.
4. Step through matches (Enter forward, Shift+Enter back) to jump to each caption timestamp.
5. Read/listen around each hit; pivot spoken `name`/`geolocation`/`associate` mentions into people-search and geolocation tools.

## Inputs → Outputs
- **In:** a YouTube video (linked to a `username`/channel) + a keyword
- **Out:** caption timestamps → spoken `name`s, `geolocation`s, mentioned `associate`s
- **Empty/negative result looks like:** no matches, OR the video has no caption track — with no captions there's nothing to search (not the same as "term not mentioned").

## Gotchas & OpSec
- Captions required: no subtitle track (auto or manual) means nothing to search.
- Auto-caption errors: machine captions mangle proper nouns — try phonetic variants, and confirm by listening.
- Extension volatility: Chrome Web Store items get delisted — verify availability (status: degraded reflects this) and prefer a research browser profile for any extension.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with transcript-download tools and general YouTube search — this searches within one video's captions in-browser, while transcript tools export the full text for offline analysis.

## Trust & verifiability
`trust: unverified` — a third-party extension, but it works on YouTube's own caption data, so any hit is verifiable by reading the captions/listening directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-caption-searcher |
| category | social-networks |
| selectorsIn → selectorsOut | username → name, geolocation, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
