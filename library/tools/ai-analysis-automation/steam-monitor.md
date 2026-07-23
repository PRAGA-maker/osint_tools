---
id: steam-monitor
name: steam_monitor
description: Use when you have a Steam account (`username`/Steam64 ID) and want to track its activity over time — a CLI that logs online/offline, game played, and profile changes with timestamps.
url: https://github.com/misiektoja/steam_monitor
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Continuously monitoring a known Steam account's online status and gaming activity to infer patterns/timezone.
selectorsIn:
- username
- device-id
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (GPL-3.0); Python CLI. Requires a free Steam Web API key.
opsec: passive
opsecNote: Passive — it polls Steam's public Web API for a profile's status; the target is not contacted directly and receives no notification. Your Steam API key ties the queries to your Steam account, so use a sock-puppet Steam account/key. Only monitors data the profile exposes publicly (private profiles reveal little).
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: One of a family of activity-monitor scripts by misiektoja; open source and actively maintained, but it only sees what Steam's API exposes for that profile.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- github-monitor
- instagram-monitor
- lastfm-monitor
- lol-monitor
- psn-monitor
aliases:
- steam_monitor
- misiektoja steam_monitor
tags:
- gaming-platforms
- activity-monitoring
- steam
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# steam_monitor

> A CLI that watches a Steam account and logs its activity — when it goes online/offline, what game it's playing, and profile changes — building a timestamped picture of behaviour over time.

## When to use
You have a confirmed Steam account (a Steam64 ID or a community URL/`username`) and want longitudinal behaviour, not a one-off snapshot: activity hours (which hint at timezone/routine), which games the person plays and when, and changes to their display name or friends list. Reach for steam_monitor to run passive surveillance of a *public* Steam profile over hours or days — useful for pattern-of-life analysis on a known target.

## How to use it (`bestInteractionPattern`: cli)
1. Get a free Steam Web API key and install the tool: `pip install steam_monitor` (Python).
2. Resolve the target to a Steam64 ID (the tool accepts a community URL and resolves it).
3. Run `steam_monitor <steam64_id> -u "<api_key>"`; it polls status and logs changes.
4. Collect the output — console logs, CSV activity history, JSON status, optional email alerts on changes.
5. Pivot: online/offline patterns suggest timezone and routine; games and name/friends changes are leads; a friends list (if public) exposes `associate`s to pursue elsewhere.

## Inputs → Outputs
- **In:** a Steam account — Steam64 ID or resolvable community `username`/URL
- **Out:** timestamped activity log (online/offline, current game, profile/name/friends changes) as CSV/JSON
- **Empty/negative result looks like:** a private/friends-only profile yields little or nothing (status hidden) — you'll see it exists but not its activity; a public profile that's simply idle logs long offline stretches.

## Gotchas & OpSec
- Human-in-the-loop: needs a Steam Web API key (free) tied to a Steam account — use a sock puppet.
- Only sees what the profile makes public; private profiles defeat it.
- OpSec: passive; polling the API doesn't alert the target. Don't over-poll (respect rate limits).

## Overlaps ("do both")
- Part of a monitor family — pair with `[[psn-monitor]]`, `[[instagram-monitor]]`, `[[lastfm-monitor]]`, etc., to build cross-platform pattern-of-life on the same person. Combine with a Steam-profile OSINT lookup to first confirm and enrich the account.

## Trust & verifiability
`trust: community` — an open-source, maintained monitor; its data is straight from Steam's API, so it's reliable for what Steam exposes, and every inferred pattern (timezone, routine) should be corroborated across enough observations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steam-monitor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, device-id →  |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
