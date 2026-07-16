---
id: twitch-overlap
name: Twitch Overlap
description: Use when you have a Twitch channel `username` and want to see which other channels share its audience — returns associate/community links to other social-profile handles.
url: https://stats.roki.sh/
category: social-networks
path:
- social-networks
bestFor: Finding which other Twitch channels a streamer's chatters also watch, to map their community and likely associates.
selectorsIn:
- username
selectorsOut:
- associate
- social-profile
status: live
pricing: free
costNote: Free public site; no account or payment. Open-source backend (snoww/TwitchOverlap on GitHub).
opsec: passive
opsecNote: You only browse pre-computed aggregate stats; you never touch the target's channel or chat, so nothing is logged against you and the target is not alerted. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent hobby project (roki/snoww) computing overlap from public Twitch chatter lists every 30 minutes; unofficial but transparent and open-source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Twitch Viewer Overlap
- stats.roki.sh
tags:
- twitch
- social-media
- audience-overlap
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Twitch Overlap

> A Twitch audience-overlap map: for any tracked channel, it shows which other channels share the most chatters — a proxy for who a streamer's community also follows.

## When to use
You have a subject tied to a Twitch channel `username` and want to understand their community and co-streamers — who their viewers also watch, which collaborators share an audience, and which adjacent channels to check for the same people. Useful for pivoting from one streamer to a cluster of `associate` channels and their linked `social-profile` handles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stats.roki.sh/.
2. Search or click a channel name (only channels that regularly exceed ~1,000 concurrent viewers are tracked).
3. Read the overlap table: it lists the other channels whose chatters most intersect with this one, ranked by shared-viewer count/percentage.
4. Pivot: treat the top overlapping channels as candidate `associate`s or communities the subject participates in; open those channels and cross-check for the same usernames.

## Inputs → Outputs
- **In:** Twitch channel `username`
- **Out:** ranked list of overlapping channels (`associate` / community `social-profile` leads) with shared-audience metrics.
- **Empty/negative result looks like:** "No data" / channel not listed — the channel is too small (under the ~1,000-viewer threshold) or inactive, so no overlap is computed.

## Gotchas & OpSec
- Only large channels are tracked; small or private streamers will not appear at all.
- Overlap is a *statistical audience* signal, not proof two streamers know each other — treat it as a lead, not a relationship.
- Data updates every ~30 minutes and reflects recent activity, so a dormant channel's overlap may be stale.

## Overlaps ("do both")
- Pairs with `[[twitch-recover]]` — this maps the community around a channel, while Twitch Recover pulls the channel's own (even deleted) VOD content.

## Trust & verifiability
`trust: community` — an unofficial open-source project deriving overlap from public Twitch chatter data; the method is transparent but not endorsed by Twitch, so verify any specific claim by inspecting the channels directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-overlap |
| category | social-networks |
| selectorsIn → selectorsOut | username → associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
