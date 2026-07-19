---
id: bluesky-users-stats
name: BlueSky users stats
description: Use when you're working a Bluesky lead and want ecosystem context — returns platform stats, top-account rankings and a directory of Bluesky OSINT tools.
url: https://vqv.app/stats/chart
category: social-networks
path:
- social-networks
bestFor: Getting a feel for the Bluesky landscape (growth, most-followed and most-blocked accounts) and finding the right Bluesky-specific lookup tools for a target.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free dashboard; no account. Aggregate stats and rankings update hourly; the linked tools directory points to other free Bluesky utilities.
opsec: passive
opsecNote: Viewing aggregate stats and rankings is anonymous and touches no individual account. Any follow-on account lookup should be done with a passive/logged-out method where possible.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run Bluesky analytics site; useful for aggregate ranking/stats and as a tools hub, but it is not an authoritative per-account record.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- vqv.app
- VQV Bluesky Stats
- Top 1000 Bluesky Users
tags:
- Social Media
- Bluesky
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# BlueSky users stats

> A community Bluesky analytics dashboard (VQV) — platform growth, top-1000/most-blocked account rankings, and a directory of Bluesky OSINT tools — best used as an orientation and jump-off point.

## When to use
Your subject may be on Bluesky and you want ecosystem context before diving in: how big/active the platform is, whether a handle ranks among the most-followed (a quick prominence check), and — most useful for OSINT — VQV's **tools directory**, which points to the dedicated Bluesky account-lookup and profile-analysis utilities you'll actually use on an individual. Treat this as a hub, not a per-person lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vqv.app/ (stats at https://vqv.app/stats/, rankings on the homepage, tools at https://vqv.app/tools/).
2. Use the stats/leaderboards to gauge activity and check whether a `username` is a top/most-blocked account.
3. Open the **Tools** directory and pick a per-account analyzer (profile viewer, follower/bot analysis, post history) for your specific target.
4. Pivot: run the actual handle through the linked account-analysis tool, then cross-reference the display name and links to other platforms.

## Inputs → Outputs
- **In:** `username` (for the ranking check) — otherwise aggregate/topic browsing
- **Out:** platform-level stats, account rankings, and links to per-account `social-profile` tools
- **Empty/negative result looks like:** your target simply isn't in the top rankings — which is the normal case for ordinary users and tells you nothing about whether they have an account. For that, use a dedicated profile-lookup tool from the directory.

## Gotchas & OpSec
- **Aggregate, not individual.** Rankings only cover prominent accounts; this won't confirm or locate a specific ordinary user — use the linked tools for that.
- Community-maintained; treat stats as indicative, not authoritative.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with the dedicated Bluesky account-lookup tools it links to — VQV orients you and points the way, those do the actual per-target work.

## Trust & verifiability
`trust: community` — a hobby analytics dashboard. Fine for ecosystem context and tool discovery; verify any specific-account claim with a first-party check on bsky.app itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bluesky-users-stats |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
