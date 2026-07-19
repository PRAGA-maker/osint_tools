---
id: github-monitor
name: github_monitor
description: Use when you have a GitHub `username` and want to watch their activity over time — returns real-time alerts on new events, follows, stars and profile changes.
url: https://github.com/misiektoja/github_monitor
category: social-networks
path:
- social-networks
bestFor: Real-time monitoring of a GitHub user's activity and profile changes, with notifications and CSV export.
selectorsIn:
- username
selectorsOut:
- username
- associate
status: live
pricing: free
costNote: Free and open-source (GPLv3), installable via `pip install github_monitor`. A free GitHub token raises rate limits.
opsec: passive
opsecNote: It polls GitHub's public API for the target's public activity — it does not interact with or notify the user. Run it with a token from a sock-puppet GitHub account, not a personal one.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: An open-source monitoring tool by misiektoja (part of a family of *-monitor tools), actively maintained on GitHub; it only surfaces public GitHub data.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- instagram-monitor
- lastfm-monitor
- spotify-monitor
- steam-monitor
- lol-monitor
- psn-monitor
- spotify-profile-monitor
- xbox-monitor
tags:
- github
- monitoring
- cli
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# github_monitor

> A Python CLI that watches a GitHub user in real time — new pushes, PRs, issues, forks, releases, follows, and profile changes — and alerts you, turning a static profile into a live activity feed.

## When to use
Your subject has a GitHub `username` and their ongoing activity matters: what they're building, who they follow/are followed by (relationship signals), when they're active (routine/timezone), and when their profile changes. Instead of manually re-checking, github_monitor tracks it continuously and notifies you, which is ideal for a developer subject or when a repo/account is central to a case.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install github_monitor` (Python 3.10+).
2. Generate a GitHub personal access token from a sock-puppet GitHub account to raise API rate limits.
3. Run the tool against the target username, configuring email/notification settings.
4. Let it poll: it reports new events (pushes, PRs, issues, forks, releases), added/removed followers and followings, newly starred repos, and profile/visibility changes.
5. Export activity to CSV for timeline analysis.
6. Pivot: new followings/followers → `associate`s; commit times → activity pattern/timezone; new repos → interests and possible other handles/emails in commits.

## Inputs → Outputs
- **In:** a GitHub `username`
- **Out:** a running feed of the user's public activity, follower/following changes (`associate` signals), and profile changes
- **Empty/negative result looks like:** no activity during the monitoring window, or a profile that goes private/blocks — meaning the user is inactive or has restricted visibility, not that the account is gone. Commit emails may also be privacy-masked.

## Gotchas & OpSec
- Public data only: it surfaces what GitHub exposes; private repos and activity aren't visible.
- Needs a token to avoid harsh API rate limits — use a sock-puppet account's token.
- It's a monitor, so value comes from running it over time, not a one-shot check.
- OpSec: passive — polling the public API does not notify the target; keep the token tied to a sock puppet.

## Overlaps ("do both")
- Part of a family with `[[instagram-monitor]]`, `[[spotify-monitor]]`, `[[steam-monitor]]` and others — run the matching monitor per platform where your subject is active for a cross-platform activity picture.

## Trust & verifiability
`trust: community` — an open-source tool that only relays public GitHub API data, so the activity it reports is authoritative to GitHub; corroborate identity inferences (e.g. commit-email → person) separately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-monitor |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
