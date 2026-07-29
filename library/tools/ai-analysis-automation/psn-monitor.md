---
id: psn-monitor
name: psn_monitor
description: Use when you have a subject's PlayStation Network `username`/PSN ID and want to track their online presence — monitors online/offline status, games played, and session times, with alerts.
url: https://github.com/misiektoja/psn_monitor
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Real-time monitoring of a PSN account's online status and gaming activity for pattern-of-life.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (GPLv3), Python. Requires your own PSN account's NPSSO auth token to use the PlayStation API.
opsec: active
opsecNote: You authenticate with your OWN PlayStation account's NPSSO token, so activity is tied to that account — use a dedicated sock-puppet PSN account, never your real one. The target is not directly notified, but you are polling Sony's API about them; keep polling intervals reasonable.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: An actively maintained open-source monitor (misiektoja) using the documented PSN API; the technique is reproducible and the code is auditable.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
invitationOnly: false
relatedTools:
- github-monitor
- instagram-monitor
- lastfm-monitor
- lol-monitor
- spotify-monitor
- spotify-profile-monitor
- steam-monitor
- xbox-monitor
aliases:
- psn_monitor
- PSN Monitor
tags:
- Code
- gaming-osint
- pattern-of-life
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# psn_monitor

> A CLI that watches a PlayStation Network account in real time — online/offline transitions, which game is running, session lengths — turning a PSN `username` into a pattern-of-life signal.

## When to use
You have a subject's PSN ID / online-ID (a `username`, often reused across platforms) and want behavioral intelligence: when are they online, what do they play, how long are sessions? For a missing-person or fugitive case, a still-active PSN account is a live signal that the person (or someone with their credentials) is present and awake at certain hours — a genuine pattern-of-life lead.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `github.com/misiektoja/psn_monitor` and install the Python requirements.
2. Obtain an NPSSO token from a **sock-puppet** PlayStation account (log into the PSN site, retrieve the NPSSO value) and configure it.
3. Run the monitor against the target's PSN ID.
4. Watch the output/log: online/offline changes, game launches/changes, session durations, PS+ status, trophies, recently played. Enable email alerts and/or CSV export for a record.
5. Pivot: activity windows narrow the subject's timezone/awake hours; the same handle feeds cross-platform username enumeration; a linked profile can corroborate identity.

## Inputs → Outputs
- **In:** a PSN online-ID (`username`) / `social-profile`
- **Out:** timestamped online/offline and gameplay activity (a live `social-profile` presence feed)
- **Empty/negative result looks like:** the account is set to "appear offline", is private, or has no activity — you get no presence signal; that is a privacy setting, not proof the person is inactive.

## Gotchas & OpSec
- Human-in-the-loop: you must obtain and supply an NPSSO token (`api-key`) from your own PSN account; tokens expire and need refreshing.
- OpSec: **active** — authentication ties the polling to whatever PSN account you use, so use a burner, never your real account. Poll at sane intervals to avoid rate limits/attention.
- "Appear offline" and privacy settings defeat it entirely; absence of signal is inconclusive.
- Confirm the online-ID actually belongs to your subject — handles are reused and impersonated.

## Overlaps ("do both")
- Pairs with cross-platform username tools and other presence monitors: username enumeration finds *where* the handle exists; psn_monitor gives *live behavioral timing* on PSN specifically. Combine handle discovery with this pattern-of-life feed.

## Trust & verifiability
`trust: community` — actively maintained open-source using the documented PSN API; every observation is timestamped and reproducible, though you should still corroborate that the account is your subject's.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | psn-monitor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
