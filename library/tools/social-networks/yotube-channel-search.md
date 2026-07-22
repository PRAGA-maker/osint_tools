---
id: yotube-channel-search
name: YouTube Channel Search (YTDT)
description: Use when you have a `name`/keyword and want to enumerate YouTube channels matching it with their IDs, creation dates and stats as a table — returns social-profile, name.
url: https://tools.digitalmethods.net/netvizz/youtube/mod_channels_search.php
category: social-networks
path:
- social-networks
bestFor: Keyword-to-channels enumeration on YouTube, returning channel IDs, creation dates and subscriber/view counts in one table.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free academic tool (YouTube Data Tools / Digital Methods Initiative); no login. Runs on the maintainer's YouTube API quota, so heavy use can be throttled.
opsec: passive
opsecNote: Queries go to the YTDT server (which calls the YouTube Data API), not to any channel owner — no target notification. Nothing beyond your keyword is submitted; a neutral browser session is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Bernhard Rieder / Digital Methods Initiative (University of Amsterdam) as YouTube Data Tools; results come straight from the YouTube Data API.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- YTDT channel search
- YouTube Data Tools channel search
tags:
- youtube
- social-media
- channel-search
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- google-autocomplete-scraper
- internet-archive-wayback-machine-link-ripper
- tools-digitalmethods-net
- wikipedia-cross-lingual-image-analysis
- youtube-comments-analyze
- youtube-data-tools
- ytdt-digitalmethods-net
- ytdt-digitalmethods-net-2
---

# YouTube Channel Search (YTDT)

> Part of Bernhard Rieder's YouTube Data Tools: type a keyword/name and get back every matching channel as a table of IDs, creation dates and audience stats.

## When to use
You have a person's `name`, handle, or a keyword and want to find their (or candidate) YouTube channels and compare them at a glance — channel ID, description, creation date, subscriber/view/upload counts. Good for discovering a subject's channel when you only have a name, or for spotting the real account among impersonators by creation date and size.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tool (the URL 301-redirects to its current home at `ytdt.digitalmethods.net/mod_channels_search.php`).
2. Enter the keyword/name and run the search.
3. Read the results table: each row is a channel with its **channel ID**, title, description, creation date, and subscriber/view/video counts — download as CSV if needed.
4. Triage: use creation date + subscriber/upload counts to distinguish an established real channel from a recent impersonator.
5. Pivot: take a channel ID into `[[youtube-channel-id]]`-style lookups or the YouTube Data API, or into Wayback for historical channel snapshots.

## Inputs → Outputs
- **In:** `name` / keyword (or a `username`/handle as the keyword)
- **Out:** `social-profile` (matching channels + IDs + stats), `name` (channel titles)
- **Empty/negative result looks like:** an empty table (no channels match the keyword) or a quota/error message if the shared API allowance is temporarily exhausted — retry later.

## Gotchas & OpSec
- It's keyword search over channel titles/metadata, not a resolver — you may get many candidates and must disambiguate by stats/creation date.
- Runs on the maintainer's shared YouTube API quota; expect occasional throttling on heavy use.
- OpSec: passive; queries hit YTDT/YouTube, never the channel owner.

## Overlaps ("do both")
- Pairs with `[[youtube-channel-id]]` — this enumerates candidate channels from a name, while the ID finder resolves a specific channel URL/handle to its canonical ID; use them in sequence.

## Trust & verifiability
`trust: trusted` — a long-standing academic tool (Digital Methods Initiative) pulling directly from the YouTube Data API, so the channel data is authoritative; only the shared quota limits it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yotube-channel-search |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
