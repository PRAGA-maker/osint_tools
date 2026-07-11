---
id: libsyn
name: Libsyn
description: Use when you have a `name`, `username` or podcast title and want to find a subject's podcast, its episodes and host details — returns `social-profile`, `name`, `metadata-exif` (episode dates/descriptions).
url: https://libsyn.com
category: image-video-face
path:
- image-video-face
bestFor: Locating a subject's self-hosted podcast, its back catalogue, show notes and host bios.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
- metadata-exif
status: live
pricing: freemium
costNote: Hosting is a paid service for creators, but listening to and browsing published shows/episode pages is free and needs no account.
opsec: passive
opsecNote: Browsing a public show page or episode is passive; you view a hosted site, not the target. Following links from show notes to the host's other socials should use sock-puppet accounts as usual.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Libsyn is a long-established, legitimate podcast host; content is publisher-supplied, so accuracy depends on the podcaster, not Libsyn.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Liberated Syndication
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- podcast
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Libsyn

> One of the oldest podcast hosts; useful in OSINT as a place a subject may self-publish audio, exposing their voice, routine, associates and show-note links.

## When to use
You suspect the subject produces or appears on a podcast, or you have a show name / host `username` and want the episode archive, show notes and host bio. Podcasts are a rich, under-checked source: episode descriptions leak locations, employers, associates and event dates, and the audio itself gives a voice sample and physical/behavioural detail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Find the subject's Libsyn-hosted show — usually via a Google search like `site:libsyn.com "subject name"` or by following a "powered by Libsyn" link from a podcast platform, since Libsyn's own directory search is limited.
2. Open the show page to see the episode list, descriptions and publication dates.
3. Read show notes for pivots: names of co-hosts/guests (`associate`), mentioned locations, employer references, and links to the host's other social profiles.
4. Play or download episodes if a voice sample or spoken detail matters.
5. Pivot: feed host/guest names into people-search, and any linked handles into username enumeration.

## Inputs → Outputs
- **In:** `name`, `username`, or a show title
- **Out:** `social-profile` (the show + linked host socials), `name` (hosts/guests), `metadata-exif`-style episode dates and descriptions
- **Empty/negative result looks like:** no Libsyn-hosted show for the subject — they may host elsewhere (Anchor/Spotify, Buzzsprout, self-hosted), so check other hosts before concluding they have no podcast.

## Gotchas & OpSec
- Libsyn's on-site search/directory is weak; discovery is better via a search engine `site:` query or from the podcast's distribution page.
- Show notes are author-written and may be promotional or stale — corroborate any claim.
- Distribution means the same show is often mirrored on Apple/Spotify; those copies may carry extra reviews/comments worth reading.

## Overlaps ("do both")
- Pairs with mainstream podcast directories (Apple Podcasts, Spotify) — Libsyn is the host, those are the discovery/engagement layer where listener comments and ratings live.

## Trust & verifiability
`trust: community` — Libsyn is a legitimate, long-running host, but everything you read is publisher-supplied content, so treat episode claims as leads to verify, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | libsyn |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile, name, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
