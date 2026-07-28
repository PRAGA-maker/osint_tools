---
id: twitchmetrics-net
name: Twitchmetrics.net
description: Use when you have a Twitch `username` and want their channel stats, growth history, games played and rankings — returns social-profile context.
url: https://www.twitchmetrics.net/
category: social-networks
path:
- social-networks
bestFor: Profiling a Twitch streamer's audience, activity history, games and ranking without logging into Twitch.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to view channel profiles, rankings and historical stats; no account required.
opsec: passive
opsecNote: Passive third-party analytics; you view aggregated public data, so the streamer isn't notified you looked. Passive — no need to touch the target's Twitch page directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Twitch analytics aggregator; figures are derived estimates from public Twitch data, not official Twitch numbers.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Twitch Metrics
tags:
- twitch
- streaming
- analytics
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Twitchmetrics.net

> A third-party Twitch analytics site: enter a streamer's handle and get their audience size, growth history, games played and rankings — a passive read of an active Twitch identity.

## When to use
You have a Twitch `username` (or suspect a subject streams) and want to understand that channel without logging into or interacting with Twitch: how big and active it is, when it grew, what games it plays, and how it ranks. Streaming activity is a strong signal of when someone is online and where their community is — useful for pattern-of-life, corroboration, and finding linked accounts referenced on stream.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.twitchmetrics.net/ and search the Twitch `username`, or browse category/game rankings.
2. Open the channel profile to read follower/viewer history, average viewers, games streamed, and rank over time.
3. Note activity timing (peak days/hours) as a pattern-of-life signal.
4. Cross-reference the display name/handle against other platforms for the same person.
5. Pivot: the confirmed Twitch `social-profile` links out to the streamer's other socials (often in their bio/panels).

## Inputs → Outputs
- **In:** Twitch `username`
- **Out:** `social-profile` context — audience size, growth history, games, rankings, activity timing
- **Empty/negative result looks like:** no profile or a stale/near-zero channel — the account may be tiny, renamed, or inactive; a missing profile isn't proof they don't stream.

## Gotchas & OpSec
- OpSec: passive; the streamer isn't notified you viewed their metrics here.
- Numbers are third-party estimates from public data, not official Twitch figures — treat magnitudes, not exact counts.
- Handles change; verify the profile is the same person via linked socials before relying on it.

## Overlaps ("do both")
- Pairs with cross-platform username tools — Twitchmetrics profiles the Twitch presence, username enumeration maps the same handle onto other sites for a fuller identity picture.

## Trust & verifiability
`trust: community` — a third-party analytics aggregator; useful for scale and history, but confirm identity and exact figures against Twitch itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitchmetrics-net |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
