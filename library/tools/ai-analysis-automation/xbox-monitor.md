---
id: xbox-monitor
name: xbox_monitor
description: Use when you have an Xbox Live `username` (gamertag) and want to monitor their online status, games played, and profile over time — returns `social-profile` activity and presence patterns.
url: https://github.com/misiektoja/xbox_monitor
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Real-time monitoring of an Xbox Live gamertag's online/offline status, played games, and profile changes.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Open source (GPLv3); free to run. Requires your own (free) Azure AD app registration to authenticate against the Xbox/Microsoft API.
opsec: passive
opsecNote: Polls Microsoft's Xbox APIs for a public gamertag — you never contact the target, and even "appear offline" presence can be inferred. Authenticate with a dedicated Microsoft/Azure identity, not your personal one; running it ties activity to whatever credentials you use.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained open-source monitor (misiektoja) with a family of similar platform monitors; community-grade but current.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- xbox_monitor
tags:
- gaming-platforms
- presence-monitoring
source: awesome-osint
lastVerified: '2026-07-23'
relatedTools:
- github-monitor
- instagram-monitor
- lastfm-monitor
- lol-monitor
- psn-monitor
- spotify-monitor
- spotify-profile-monitor
- steam-monitor
---

# xbox_monitor

> A Python monitor for Xbox Live: track a gamertag's online/offline transitions, the games they play, and profile details over time, with logging and email alerts.

## When to use
You have an Xbox Live `username` (gamertag) tied to a subject and want a temporal picture of their activity: when they come online/offline (a strong routine/timezone signal), which games they play, and changes to their profile, gamerscore, and friends. Establishing an active-presence pattern is valuable in missing-person and lifestyle work — it can show an account is still in use and when.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install dependencies; register a free Azure AD application to get API credentials (OAuth2).
2. Configure the target gamertag and your credentials.
3. Run the monitor; it polls Xbox presence and logs online/offline events, played games, and profile data — optionally emailing on changes and writing CSV.
4. Read the timeline: activity windows (day/hour → likely timezone), game list, and profile changes.
5. Pivot: an activity pattern corroborates a timezone/routine; a gamertag feeds cross-platform username search; friends/profile details feed `associate` mapping.

## Inputs → Outputs
- **In:** `username` (Xbox gamertag) + your API credentials
- **Out:** `social-profile` activity — online/offline events, games, gamerscore, friends, profile changes over time
- **Empty/negative result looks like:** no presence changes over a long run (dormant account) or an unresolved gamertag — dormancy is itself a finding; a bad gamertag/credentials error is a setup issue.

## Gotchas & OpSec
- Human-in-the-loop: you must create an Azure AD app for API access — a one-time setup step.
- "Appear offline" users can still be inferred as active, but privacy settings can hide games/friends; missing detail is a settings artefact, not proof.
- OpSec: **passive** toward the target, but tied to your Microsoft/Azure identity — use a dedicated one.

## Overlaps ("do both")
- Pairs with `[[steam-monitor]]`, `[[psn-monitor]]`, and `[[steam-id-finder]]` — the same subject often games across platforms; monitor each and correlate activity windows.

## Trust & verifiability
`trust: community` — an actively maintained open-source monitor; the presence data comes from Microsoft's own APIs, so it's reliable, but interpret activity patterns as behavioural signals, not certainties.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xbox-monitor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
