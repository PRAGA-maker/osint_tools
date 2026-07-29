---
id: lastfm-monitor
name: lastfm_monitor
description: Use when you have a Last.fm `username` and want to track their listening in real time — returns now-playing/online-activity signals and a listening timeline.
url: https://github.com/misiektoja/lastfm_monitor
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Passively monitoring a target's Last.fm account to infer when they are active/online from their music scrobbles.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open source (Python). Requires your own free Last.fm API key to run; no payment.
opsec: passive
opsecNote: It only reads the target's PUBLIC Last.fm scrobbles via the API — you never interact with the target, and Last.fm shows them your API key's activity, not your identity. Still, long-term monitoring builds a behavioral profile (sleep/wake patterns, timezone) that is sensitive; run it from your own API key on infrastructure you control and handle the derived pattern-of-life data responsibly.
humanInLoop: false
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Part of misiektoja's well-known family of OSINT "monitor" tools (Spotify, Steam, Xbox, Instagram, GitHub, etc.); open source and auditable, actively maintained, community-trusted for account activity tracking.
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
- lol-monitor
- psn-monitor
- spotify-monitor
- spotify-profile-monitor
- steam-monitor
- xbox-monitor
aliases:
- lastfm_monitor
tags:
- music-streaming-services
- account-monitoring
- pattern-of-life
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# lastfm_monitor

> A Python tool that watches a Last.fm user's scrobbles in real time — turning "what they're listening to" into an online-activity and pattern-of-life signal.

## When to use
You have a subject's Last.fm `username` and want a low-noise **activity indicator**: Last.fm logs ("scrobbles") each track a user plays, often the moment they play it. Monitoring that stream tells you when the person is awake, at their computer/phone, and active — useful for establishing pattern-of-life, timezone, and online/offline status when other accounts are quiet. It also yields taste/interest data. Part of a broader suite of per-platform monitors you can run in parallel.

## How to use it (`bestInteractionPattern`: cli)
1. Get a free Last.fm API key and install the tool from GitHub (Python + requirements).
2. Configure it with your API key and the target `username`.
3. Run it; it polls the user's recent-tracks feed and alerts on now-playing/started-listening events (and can log a timeline).
4. Read the signal: active listening ≈ the person is online now; gaps and clusters reveal daily rhythm and likely timezone.
5. Pivot: run sibling monitors (`[[spotify-monitor]]`, `[[steam-monitor]]`, `[[github-monitor]]`, etc.) on the same subject and correlate activity windows across platforms.

## Inputs → Outputs
- **In:** Last.fm `username`
- **Out:** real-time listening/online-activity events and a behavioral timeline (`social-profile` activity)
- **Empty/negative result looks like:** no recent scrobbles — the account is inactive, private, or the person simply isn't scrobbling; silence isn't proof they're offline everywhere.

## Gotchas & OpSec
- Requires your own Last.fm API key (`api-key`); the key's usage, not your identity, is what Last.fm sees.
- Only public scrobbles are visible; users can hide/disable scrobbling.
- Long-term monitoring produces sensitive pattern-of-life data — collect only what your investigation justifies and store it responsibly.

## Overlaps ("do both")
- Pairs with the rest of the monitor family — `[[spotify-monitor]]`, `[[spotify-profile-monitor]]`, `[[steam-monitor]]`, `[[psn-monitor]]`, `[[xbox-monitor]]`, `[[lol-monitor]]`, `[[instagram-monitor]]`, `[[github-monitor]]` — correlating activity across platforms sharpens the pattern-of-life picture.

## Trust & verifiability
`trust: community` — a maintained, auditable open-source tool from a respected author of similar monitors; it faithfully relays Last.fm's own API data, so reliability tracks the account's public scrobble stream.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lastfm-monitor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
