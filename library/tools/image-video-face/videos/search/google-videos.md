---
id: google-videos
name: Google Videos
description: Use when you want to find video clips across the web by keyword (name, place, event) — returns video results from YouTube, news sites, and other hosts with thumbnails and source links.
url: https://www.google.com/videohp
category: image-video-face
path:
- image-video-face
- videos
- search
bestFor: Keyword video search across YouTube, news, and other video hosts.
input: Search keywords (name, place, event)
output: Video results with thumbnails, titles, durations, and source pages
selectorsIn:
- name
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free; no account required.
opsec: passive
opsecNote: Standard keyword query against Google's video index; the target is not contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google product (the Videos vertical of Google Search); reliable, broad index.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- google-images
aliases: []
tags:
- video-search
source: arf-seed
lastVerified: ''
enrichment: full
---

# Google Videos

> Google's video search vertical: keyword-search for clips across YouTube, news outlets, and other hosts in one place.

## When to use
You have a `name`, place, or event and want to find video footage — a missing person's appearance in a livestream, a local news segment, a social video tagged to a location. Broader than searching any single platform because it aggregates many video hosts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.google.com/videohp (or run a normal Google search and click the "Videos" tab).
2. Enter keywords — full name, alias, location plus event terms, or quoted phrases (`selectorsIn`).
3. Use Tools → time filter to narrow by upload date; scan thumbnails, titles, and source domains.
4. Open promising clips for `geolocation`/`social-profile` context; pivot the source channel into platform-specific account searches.

## Inputs → Outputs
- **In:** `name` (plus place/event keywords)
- **Out:** `social-profile` (uploader channels/accounts), `geolocation` (location-tagged footage)
- **Empty/negative result looks like:** only unrelated stock or news clips — refine with aliases, location, or quoted phrases; try platform-native search (YouTube, TikTok).

## Gotchas & OpSec
- Aggregates but does not deeply index every platform (e.g. TikTok/Instagram coverage is partial); also search natively.
- Ranking favors popular/recent content; obscure local footage can be buried — use the date filter and exact phrases.
- OpSec: passive keyword search; no target contact. Use a clean session if your search terms are sensitive.

## Overlaps ("do both")
- Pairs with platform-native video search and with `[[google-images]]` (use a video frame as a reverse-image query).

## Trust & verifiability
`trust: trusted` — first-party Google video vertical; broad and reliable, though coverage of closed/walled platforms is incomplete.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-videos |
| category | image-video-face |
| selectorsIn → selectorsOut | name → social-profile, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
