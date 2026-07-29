---
id: twitchtracker
name: TwitchTracker
description: Use when you have a Twitch `username`/channel and want its detailed analytics — stream history, games played, follower/viewer trends and schedule — returns social-profile and pattern-of-life leads.
url: https://twitchtracker.com/
category: social-networks
path:
- social-networks
bestFor: Deep Twitch channel analytics: historical stream log, games/categories, follower and viewer trends, and streaming schedule.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to view channel statistics and history in the browser; no account needed. Some advanced/removed-ads features may be paid.
opsec: passive
opsecNote: Passive — TwitchTracker aggregates public Twitch data; viewing a channel's stats never touches the target. No login required, so nothing ties the lookup to you beyond your IP; use a sock-puppet browser to be safe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established third-party Twitch analytics site; figures are derived from Twitch's public data and periodic sampling, so historical stats are estimates, not official counts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- twitchtracker.com
tags:
- streaming
- gaming-platforms
- analytics
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# TwitchTracker

> Third-party Twitch analytics — a channel's full streaming history, the games it plays, its follower/viewer trends, and, crucially, when it typically goes live.

## When to use
You have a subject's Twitch `username`/channel and want a pattern-of-life and interest profile: their historical stream log (dates/times/durations), what games and categories they stream, how their following has grown, and their usual streaming schedule. Stream timestamps map to a person's active hours and time zone; the games and titles reveal interests and possible cross-platform handles. A strong enrichment step when Twitch is a live identity for the subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://twitchtracker.com/ and search the channel name (or go to `twitchtracker.com/<channel>`).
2. Review the **stream history**: each session's date/time, duration, game, peak/average viewers.
3. Check the **games/categories** breakdown and the **followers/viewers over time** charts.
4. Read the inferred **schedule** (which days/hours they stream).
5. Pivot: stream times → time-zone/activity-window inference; game titles/usernames → search the same handle on Steam/Discord/YouTube; peak dates → correlate with events.

## Inputs → Outputs
- **In:** Twitch `username`/channel name
- **Out:** historical stream log, games played, follower/viewer trends, typical schedule (`social-profile` activity + pattern of life)
- **Empty/negative result looks like:** "channel not found" or a near-empty history — the channel is new, tiny, renamed, or banned; sparse data means little streaming activity, not necessarily an inactive person.

## Gotchas & OpSec
- Stats are sampled estimates, not Twitch's official numbers — treat viewer/follower figures as approximate.
- Only reflects public streaming activity; subscriber-only or deleted content won't appear.
- OpSec: passive; no login needed — use a clean browser anyway.

## Overlaps ("do both")
- Pairs with `[[twitch-tools]]` (follower/following rosters) and `[[lol-monitor]]`/other activity monitors — TwitchTracker gives the historical analytics; those give the social graph and real-time activity.

## Trust & verifiability
`trust: community` — well-known analytics site derived from Twitch's public data; historical figures are estimates, so verify decisive numbers against Twitch itself where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitchtracker |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
