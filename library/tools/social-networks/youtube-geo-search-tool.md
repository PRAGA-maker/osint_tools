---
id: youtube-geo-search-tool
name: Youtube Geo Search Tool
description: Use when you have a `geolocation` (and optional keyword/timeframe) and want YouTube videos tagged near that spot — returns geo-tagged videos and their channels.
url: https://youtube.github.io/geo-search-tool/search.html
category: social-networks
path:
- social-networks
bestFor: Finding YouTube videos filmed/tagged within a radius of a location and time window — eyewitness footage discovery.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
- geolocation
status: degraded
pricing: free
costNote: Free, hosted by YouTube on GitHub Pages; uses YouTube Data API v3 via in-browser Google sign-in (no separate paid key needed for normal use).
opsec: passive
opsecNote: You query YouTube's public API, not any uploader, so no target is notified. The tool authenticates with your Google account, though — sign in with a research Google profile, never a personal one, since your API queries are tied to that account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published under YouTube's own GitHub org, but explicitly "not an official Google product." It depends on videos being geo-tagged and on YouTube's location search parameters, which YouTube has deprecated/degraded over time — coverage is now partial and shrinking.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: false
relatedTools:
- geo-search-tool
aliases:
- YouTube Geo Search
tags:
- youtube
- geolocation
- eyewitness
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Youtube Geo Search Tool

> A YouTube-hosted browser tool that queries the Data API for videos tagged within a radius of a location and time window — built for finding eyewitness footage near a place and moment.

## When to use
You have a `geolocation` — where a subject was last seen, an incident site, a location in a photo — and want video shot near there, optionally filtered to a date range and keyword. For missing-persons and event work, geo-tagged uploads can put a camera at the right place and time, potentially capturing the person, a vehicle, or context. Use it when a specific place/time is your anchor and you want footage rather than text.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://youtube.github.io/geo-search-tool/search.html and sign in with a Google account when prompted (use a research profile).
2. Set the **location** (place name or coordinates) and the **radius** (1–1000 km).
3. Set the **timeframe** (date range) and optional **keywords**; optionally restrict to specific channels or Creative-Commons/embeddable results.
4. Run the search — results are geo-tagged videos with thumbnails, upload times, and channel links, plottable on a map.
5. Open promising videos on YouTube to inspect content and the uploader's channel.
6. Pivot: an uploader's channel → `social-profile` enumeration; a video's frames → geolocation/reverse-image analysis to confirm the place and time.

## Inputs → Outputs
- **In:** `geolocation` (+ optional timeframe, keyword, channel filter)
- **Out:** geo-tagged videos, upload times, uploader channels (`social-profile`), mapped `geolocation`s
- **Empty/negative result looks like:** few or no results even for a busy location — because only a small (and shrinking) share of uploads carry geo-tags and YouTube has degraded location search, an empty result does NOT mean no footage exists; treat coverage as partial.

## Gotchas & OpSec
- Relies on uploaders having geo-tagged their videos AND on YouTube's location search parameters, which Google has deprecated/limited over the years — expect sparse, incomplete results.
- Human-in-the-loop: requires a Google sign-in; use a dedicated research account since queries hit the API under your identity.
- Passive toward uploaders (no one is notified). It is community tooling on YouTube's org, "not an official Google product," so don't assume long-term stability.

## Overlaps ("do both")
- Pairs with `[[geo-search-tool]]` and other geo-video finders (e.g. channel/topic-based YouTube location search) — run more than one, since each surfaces different geo-tagged uploads and none is comprehensive.

## Trust & verifiability
`trust: trusted` — hosted under YouTube's own GitHub organization and querying the official Data API, so the mechanism is legitimate; results are still limited by geo-tag availability and API deprecation, so absence is not evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-geo-search-tool |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → social-profile, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
