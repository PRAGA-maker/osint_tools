---
id: spotify-monitor
name: spotify_monitor
description: Use when you have a Spotify `username`/user URI and want to track a subject's listening in near-real-time — returns social-profile activity, playlists, and online/active patterns.
url: https://github.com/misiektoja/spotify_monitor
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Continuously monitoring a public Spotify user's activity (now-playing, playlists, followers) for pattern-of-life signals.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free and open source (Python). Requires your own Spotify credentials/token (a free Spotify account) to poll the API.
opsec: active
opsecNote: The tool polls Spotify's API for a specific user on an interval using YOUR account/token, creating a sustained, attributable query pattern tied to your credentials. Use a dedicated sock-puppet Spotify account, never your personal one. Only a target's PUBLIC activity is visible; monitoring is passive toward the subject (they aren't notified) but is a deliberate, ongoing collection you should scope and time-limit.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Part of the actively-maintained misiektoja "*_monitor" OSINT suite on GitHub; community tool, code is open and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- github-monitor
- instagram-monitor
- lastfm-monitor
- lol-monitor
- psn-monitor
- spotify-profile-monitor
- steam-monitor
- xbox-monitor
aliases:
- spotify_monitor
- misiektoja/spotify_monitor
tags:
- spotify
- activity-monitoring
- pattern-of-life
- music-streaming-services
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# spotify_monitor

> A Python watcher for a single Spotify user — polls their public activity so you can see what they're listening to, when they're active, and how their playlists/follows change over time.

## When to use
You have a Spotify `username`/user URI for a subject and want ongoing pattern-of-life data rather than a one-off snapshot. It tracks now-playing tracks, playlist changes, and follower/following shifts, which reveal when the person is online/active (a rough activity clock) and surface musical interests and connected accounts. One of the misiektoja "*_monitor" suite covering Spotify, Instagram, Steam, Xbox, PSN, Last.fm, GitHub, and LoL.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/misiektoja/spotify_monitor and install Python requirements.
2. Provide your own Spotify credentials/token in the config (a free, dedicated sock-puppet account).
3. Run it against the target's Spotify `username`/URI; set the polling interval.
4. Read the logged output/alerts: currently-playing tracks, activity times, playlist and follow changes (`selectorsOut`), and pivot the linked accounts/followers as `associate` leads.

## Inputs → Outputs
- **In:** `username` / `social-profile` (Spotify user URI or profile)
- **Out:** `social-profile` activity (now-playing, playlists, active times), `associate` (followers/following, linked accounts)
- **Empty/negative result looks like:** no activity captured — the user may keep listening private, be inactive, or not expose now-playing; you learn about visibility, not absence of a person.

## Gotchas & OpSec
- Human-in-the-loop: you must supply Spotify API credentials/token (`api-key`).
- OpSec: **active** — sustained polling under your token; use a puppet account, time-box the monitoring, and scope it to what's justified.
- Only public/exposed activity is visible; private-session or hidden listening won't appear.

## Overlaps ("do both")
- Pairs with its sibling monitors [[instagram-monitor]], [[steam-monitor]], [[lastfm-monitor]] and [[spotify-profile-monitor]] — run several against the same subject to cross-time activity across platforms and build a fuller routine.

## Trust & verifiability
`trust: community` — an open-source tool in a maintained suite; the code is auditable and the data comes straight from Spotify's API, so it's accurate for public activity but bounded by the target's privacy settings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spotify-monitor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, social-profile → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
