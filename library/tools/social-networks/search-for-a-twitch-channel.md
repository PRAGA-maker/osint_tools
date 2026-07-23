---
id: search-for-a-twitch-channel
name: Search for a Twitch channel
description: Use when you have a Twitch `username`/channel and want streaming stats, schedule and activity history — returns social-profile plus behavioural pattern data.
url: https://sullygnome.com/channelsearch
category: social-networks
path:
- social-networks
bestFor: Profiling a Twitch streamer's activity — when they stream, what they play, growth and audience.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free hobby-project analytics site; no account or payment. Historical windows (7/30/90/180/365 days) all open.
opsec: passive
opsecNote: SullyGnome reads Twitch's public API and its own historical archive; it never contacts the streamer. The target gets no signal. Only your own browsing is exposed to SullyGnome.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent Twitch analytics tracker; figures are estimates derived from periodic API polling, not official Twitch numbers, so treat as directional.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- sully-gnome
aliases:
- SullyGnome channel search
- SullyGnome
tags:
- twitch
- social-networks
- streaming-analytics
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Search for a Twitch channel

> SullyGnome's channel search — find a Twitch streamer and pull their streaming history, schedule, games played and audience trends without touching the account.

## When to use
You have a Twitch `username` (or a partial name / game + language filter) and want to understand a streamer's *behaviour*: what hours and days they go live, which games they play, whether activity has grown or lapsed, and rough audience size. This is a pattern-of-life source for a subject known to stream — useful for corroborating timezone, routine, and interests.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://sullygnome.com/channelsearch .
2. Type the Twitch `username` (or filter by game, language, follower/viewer range, partner/affiliate status) and open the matching channel.
3. On the channel page, review the stats cards and pick a time window (7 / 30 / 90 / 180 / 365 days): stream time, average/peak viewers, follower growth, games played, and a per-day/per-hour streaming heatmap.
4. Read the streaming-time heatmap for routine — recurring live hours suggest the streamer's local timezone and daily schedule.
5. Pivot: the confirmed Twitch handle feeds cross-platform username search; the schedule/timezone corroborates other pattern-of-life findings.

## Inputs → Outputs
- **In:** `username` (Twitch handle) or search filters
- **Out:** confirmed `social-profile` (Twitch channel), `username`, plus derived stream schedule, games, and audience/growth estimates
- **Empty/negative result looks like:** no channel matches, or a channel with a flat "no recent streams" history — meaning the account is dormant or SullyGnome stopped tracking it, not necessarily that it never existed.

## Gotchas & OpSec
- Numbers are third-party estimates from API polling; they diverge from Twitch's official counts and can miss short or unlisted streams.
- Only public channels are covered; banned/deleted channels may linger with stale data or vanish.
- OpSec: **passive** — SullyGnome sits between you and Twitch's public data; the streamer is never contacted.

## Overlaps ("do both")
- Pairs with `[[sully-gnome]]` (the same site's broader analytics entry) — use this channel search to land on the profile, then the wider tool for game/leaderboard context.

## Trust & verifiability
`trust: community` — an independent, well-established Twitch analytics project. Reliable for *relative* patterns (when/what/trend) but treat absolute viewer/follower figures as estimates and confirm the handle against Twitch itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-for-a-twitch-channel |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
