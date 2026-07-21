---
id: twitch-stream-filter
name: Twitch Stream Filter
description: Use when you want to find live Twitch streams by criteria — title, game, language, viewer count, broadcaster type — returns `social-profile`.
url: https://twitch-tools.rootonline.de/channel_previews.php
category: social-networks
path:
- social-networks
bestFor: Filtering the live Twitch stream directory by title/game/language/viewers to surface specific channels.
selectorsIn:
- username
- geolocation
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free web tool (part of CommanderRoot's twitch-tools suite); no login required.
opsec: passive
opsecNote: Queries Twitch's public directory via a third-party tool; you don't interact with any channel, so it's passive. Use a sock-puppet browser for hygiene; watching a live stream from your own account could reveal you in chat/viewer signals, so browse listings here rather than joining.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by CommanderRoot (a known Twitch-tools developer); it reads Twitch's public API, so results are as accurate as Twitch's live data at query time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- twitch-tools
- twitch-tools-rootonline-de
- removetweets
aliases:
- Twitch channel previews
- rootonline twitch filter
tags:
- social-networks
- twitch
- live-streams
- filtering
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Twitch Stream Filter

> A filterable window on Twitch's live directory — slice currently-live streams by title, game, language, viewers, broadcaster type and uptime to find the channel you're after.

## When to use
Twitch's own directory is hard to search precisely. This tool lets you filter *currently live* streams on many attributes at once — title/game/category, spoken language, min/max viewers, broadcaster type (partner/affiliate), account age, uptime, and even the streaming datacenter/region. Useful when you know your subject streams (a game they play, their language, a title keyword) but not the exact handle, or when you want to catch them while live, or to narrow a region via language/datacenter clues.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://twitch-tools.rootonline.de/channel_previews.php.
2. Set filters: title/keyword, game, language, viewer range, broadcaster type, uptime, and region as needed.
3. Read the sortable results: channel name, game, tags, viewers, "online since," and broadcaster language.
4. Open a promising channel (`social-profile`) on Twitch to confirm identity via bio, panels, linked socials and past clips.
5. Pivot: take the Twitch handle into username-search tools to find matching accounts elsewhere; use linked socials from the channel's panels.

## Inputs → Outputs
- **In:** filter criteria (title/game keyword, language, viewers) or a suspected `username`; language/region as a `geolocation` proxy
- **Out:** `social-profile` — matching live Twitch channels with metadata
- **Empty/negative result looks like:** no live streams match your filters right now — because it only covers *currently live* streams; an offline subject simply won't appear, so retry at their usual streaming hours.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — reads the public directory; you don't touch the channel. Don't *join* a small stream from an identifying account (you may show in viewer/chat).
- Live-only: the tool sees only streams online at query time, so absence isn't evidence the person doesn't stream — it just isn't live now.

## Overlaps ("do both")
- Part of the rootonline `[[twitch-tools]]` suite — pair with its other utilities (VOD/follower tools) and with cross-platform username search to confirm a channel belongs to your subject and to find their other accounts.

## Trust & verifiability
`trust: community` — a well-known third-party tool reading Twitch's public API; results mirror Twitch's live data at the moment you query, so re-check the channel directly to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-stream-filter |
| category | social-networks |
| selectorsIn → selectorsOut | username, geolocation → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
