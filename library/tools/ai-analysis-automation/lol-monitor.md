---
id: lol-monitor
name: lol_monitor
description: Use when you have a target's League of Legends Riot ID and want to track when they start/finish matches and log their game activity in real time — returns social-profile, associate and geolocation-timing leads.
url: https://github.com/misiektoja/lol_monitor
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Real-time monitoring of a League of Legends player's online/match activity with CSV activity logs.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: GPL-3.0 open-source Python; free. Requires your own free Riot API key and Python 3.12+.
opsec: passive
opsecNote: Polls Riot's public API using your own API key — you never contact the target, and they get no notification. The monitored player cannot see they are being watched. Keep your Riot API key private; run from an environment you control.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Part of misiektoja's well-regarded family of activity monitors (steam/psn/xbox/spotify/instagram etc.); active open-source project, but data accuracy depends on Riot's API exposing match state.
missingPersonsRelevance: low
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
- psn-monitor
- spotify-monitor
- spotify-profile-monitor
- steam-monitor
- xbox-monitor
aliases:
- lol_monitor
- League of Legends monitor
tags:
- gaming-platforms
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# lol_monitor

> A Python tool that watches a League of Legends player's Riot ID and alerts you the moment they start or finish a match, logging every game with full stats — a passive activity/pattern-of-life sensor.

## When to use
You have a subject's League of Legends Riot ID (`username#tag`) and region, and you want to establish their pattern of life: when they are online and gaming, how long sessions run, and who they play with. Match logs reveal timing (which maps to time zone / waking hours / `geolocation` inference) and team compositions can surface `associate` accounts they consistently queue with. Useful when a person's gaming identity is a live signal even if their other accounts are dark.

## How to use it (`bestInteractionPattern`: cli)
1. Get a free Riot API key from the Riot developer portal.
2. Install: `pip install lol_monitor` (needs Python 3.12+).
3. Run with the target's Riot ID and region, supplying your API key (env var or config).
4. Leave it running: it polls and emits notifications on match start/stop plus CSV logs of kills/deaths/assists, champion, role, lane, team, and bans.
5. Pivot: session timestamps → time-zone/activity-window inference; repeat teammates → `[[psn-monitor]]`/`[[steam-monitor]]`/`[[xbox-monitor]]` to correlate the same social circle across platforms.

## Inputs → Outputs
- **In:** Riot ID (`username#tag`) + region
- **Out:** online/in-match state, per-match stats, timestamped activity CSV (`social-profile` activity, recurring `associate` teammates)
- **Empty/negative result looks like:** no match events over a long window — the account is inactive or the Riot ID/region is wrong; an API error means a bad or rate-limited key, not target inactivity.

## Gotchas & OpSec
- Human-in-the-loop: you must obtain and supply your own Riot API key (registration on Riot's dev portal).
- OpSec: passive — you query Riot's API, never the target; no notification reaches them. Protect your API key.
- Accuracy depends on Riot exposing current-match data; some queue types or privacy states may not report.

## Overlaps ("do both")
- Part of misiektoja's monitor suite — pair with `[[steam-monitor]]`, `[[psn-monitor]]`, `[[xbox-monitor]]`, `[[spotify-monitor]]` and the others to build a cross-platform activity timeline for the same person.

## Trust & verifiability
`trust: community` — active, well-maintained open-source project in a respected monitor family; data is only as complete as Riot's API allows, so treat gaps as API limits, not proof of inactivity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lol-monitor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
