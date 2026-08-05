---
id: spotify-profile-monitor
name: spotify_profile_monitor
description: Use when you have a target's public Spotify profile/username and want to monitor changes over time — playlists, followers/following, and (where visible) listening activity — returns username/social-profile activity leads.
url: https://github.com/misiektoja/spotify_profile_monitor
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Tracking a public Spotify user's playlists, follows, and activity changes over time.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free, open-source Python tool; you supply your own Spotify API credentials (free developer account) to run it.
opsec: passive
opsecNote: It reads a target's PUBLIC Spotify data via the API, so it doesn't friend or notify them — passive. Your Spotify developer app/account is what makes the calls; use a sock-puppet developer account, and remember polling frequently still queries Spotify (which logs your app), not the target.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: An open-source monitoring tool by an independent developer (misiektoja); it uses Spotify's official API, so the data is authoritative, but the tool itself is community-maintained.
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
- spotify-monitor
- steam-monitor
- xbox-monitor
aliases:
- spotify profile monitor
tags:
- music-streaming-services
- socmint
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# spotify_profile_monitor

> A Python watcher for a public Spotify profile — get alerted when a target's playlists, follows, or activity change, building a behavioural timeline from their music footprint.

## When to use
SOCMINT on a subject known to use Spotify with a public profile. Given a Spotify `username`/profile, this tool periodically checks it and reports changes — new/edited playlists, follower/following changes, and activity where Spotify exposes it. Playlists and their timing can hint at mood, events, location cues (city-named playlists), and social connections (shared/collaborative playlists, followed friends).

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/misiektoja/spotify_profile_monitor and install its Python deps.
2. Create a Spotify developer app (sock-puppet account) and configure the tool with the API credentials.
3. Point it at the target's public profile/username and set a polling interval and alerting (email/console).
4. Let it run; review reported changes over time.
5. Pivot: collaborators/followed accounts → `social-profile` links; playlist names/timing → location/event leads; a linked display name → people-search.

## Inputs → Outputs
- **In:** a public Spotify `username`/profile
- **Out:** change alerts on playlists, follows, and activity (`username`/`social-profile` leads)
- **Empty/negative result looks like:** a private profile or no changes — private accounts expose almost nothing, and a static public profile yields no signal.

## Gotchas & OpSec
- **Public data only** — private profiles/activity are invisible; most casual users share little.
- Requires Spotify API credentials (human-in-the-loop) — use a sock-puppet developer account.
- Respect rate limits and Spotify's ToS; aggressive polling can get your app throttled.

## Overlaps ("do both")
- Complements cross-platform username tools and social-profile monitors — this covers the Spotify surface specifically; combine to build a fuller activity picture.

## Trust & verifiability
`trust: community` — an independent tool over Spotify's official API: the underlying data is authoritative, but verify the tool's behaviour and treat inferred leads (mood/location from playlists) as soft signals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spotify-profile-monitor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
