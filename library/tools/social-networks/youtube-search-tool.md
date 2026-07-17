---
id: youtube-search-tool
name: YouTube search tool
description: Use when you have a `name`, keyword, or place and want targeted YouTube results — a query-builder that filters videos, channels, and playlists by type and upload date.
url: https://www.aware-online.com/en/osint-tools/youtube-search-tool/
category: social-networks
path:
- social-networks
bestFor: Building precise YouTube searches (by keyword, type, upload date) to find a subject's videos, channel, or footage of a place.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free web query-builder from Aware Online; it constructs and hands off searches to YouTube (no account needed).
opsec: passive
opsecNote: It only builds a YouTube search URL/query — passive. Running the search on YouTube while logged out avoids tying it to your Google account; use a clean/sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aware Online is a reputable OSINT-training provider offering free tool helpers; this is a convenience query-builder over YouTube's own search, which does the actual work.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- youtube-metadata
- search-youtube-by-location
aliases:
- Aware Online YouTube search tool
tags:
- youtube
- video-search
- osint-search
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# YouTube search tool

> Aware Online's YouTube search-query builder — construct precise, filtered YouTube searches (type, exact phrase, upload date) to find a subject's videos or footage of a place.

## When to use
YouTube's default search is imprecise. This builder lets you compose exact-phrase, type-specific (video/channel/playlist/live), and date-filtered queries, which is how you find a subject's own channel, videos mentioning them, or user-uploaded footage from a location/event. Useful for confirming an online presence, recovering statements, or hunting eyewitness video around a place and time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.aware-online.com/en/osint-tools/youtube-search-tool/.
2. Enter your term and choose the mode: general keywords, exact phrase, video/channel/playlist/live/movie, etc.
3. Run the built search (it may hand off to YouTube) — ideally in a logged-out/sock-puppet browser.
4. On YouTube, further filter by upload date and sort to narrow footage to the relevant window.
5. Pivot: a found video → `[[youtube-metadata]]` for exact publish time and any geotag; a location angle → `[[search-youtube-by-location]]`; a channel → the subject's other content and links.

## Inputs → Outputs
- **In:** a `name`, `username`, keyword, or place
- **Out:** targeted YouTube videos/channels/playlists → `social-profile` and possible `geolocation` (via footage/geotags)
- **Empty/negative result looks like:** no relevant results — the term isn't in YouTube titles/metadata, or filters are too tight; broaden the query or try exact-phrase vs. keyword modes.

## Gotchas & OpSec
- It's a convenience layer — the real search happens on YouTube, subject to YouTube's ranking/limits.
- YouTube search matches titles/descriptions/tags, not spoken content, so relevant footage with vague titles can be missed.
- Run logged out to avoid personalizing results and linking the search to your Google identity.

## Overlaps ("do both")
- Pairs with `[[youtube-metadata]]` — find a video here, then extract its precise timestamp/geotag/thumbnails there.
- Pairs with `[[search-youtube-by-location]]` for finding videos filmed near a place rather than by keyword.

## Trust & verifiability
`trust: community` — a helper from a reputable OSINT trainer; it just builds queries, and YouTube returns the real results. Verify any specific video's details with metadata tooling.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-search-tool |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
