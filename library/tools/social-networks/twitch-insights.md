---
id: twitch-insights
name: Twitch Insights
description: Use when you have a Twitch `username` (or numeric ID) and want to confirm the account exists, when it was created, and whether it is a known bot — returns `social-profile` confirmation and account age.
url: https://twitchinsights.net/
category: social-networks
path:
- social-networks
bestFor: Verifying a Twitch handle, dating the account, and screening it against Twitch's known-bot lists.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, ad-supported analytics site; no account or payment required.
opsec: passive
opsecNote: You query TwitchInsights' own aggregated data, not the target's channel, so there is no notification to the account owner. Standard sock-puppet browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent third-party project (not affiliated with Twitch); stats are refreshed roughly every 15 minutes and are generally reliable but unofficial.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- twitchinsights.net
- Twitch Insights bot list
tags:
- Social Media
- Twitch
- account-existence
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Twitch Insights

> A free, unofficial Twitch analytics site whose most OSINT-useful feature is confirming a handle exists, dating the account, and checking it against a maintained list of known Twitch bots.

## When to use
You have a Twitch `username` (or numeric user ID) surfaced from a cross-platform username search and want to (a) confirm it is a real, live account, (b) estimate how long the person has been on Twitch (account creation date corroborates or contradicts a claimed timeline), or (c) rule the handle out as an automated bot before you invest in it as a person of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://twitchinsights.net/ in a sock-puppet browser.
2. Use the "Check user" / username-to-ID lookup to enter the target handle; it resolves the `username` to a numeric Twitch ID and account status.
3. Read the account creation date and status. Cross-reference the "Twitch Bots" list to see whether the handle is a known chat/view bot rather than a human.
4. Browse game/streamer rankings only if you're profiling an active streamer's audience or activity.
5. Pivot: a confirmed handle + creation date feeds a cross-platform username sweep (e.g. `[[sherlock]]`/`[[whatsmyname]]`) and a timeline; the numeric ID is the stable identifier to carry forward even if the display name changes.

## Inputs → Outputs
- **In:** Twitch `username` or numeric user ID
- **Out:** account existence/`social-profile` confirmation, account creation date, bot-or-not classification
- **Empty/negative result looks like:** "user not found" or no resolution — the handle is unclaimed, banned, renamed, or deleted; try the numeric ID if you have it.

## Gotchas & OpSec
- Data is a ~15-minute-lagged snapshot and unofficial, so treat it as corroborating, not authoritative — verify anything critical against twitch.tv directly.
- OpSec: passive; no owner notification. It is not affiliated with Twitch.
- The site's headline features (viewer counts, game rankings, extension stats) are audience analytics, not people-search — the person-relevant value is the username/ID/creation-date/bot check.

## Overlaps ("do both")
- Pairs with cross-platform username finders — they tell you a handle exists on Twitch, and this confirms it, dates it, and screens out bots.

## Trust & verifiability
`trust: unverified` — a well-known independent project, but third-party and unofficial. The username→ID resolution and creation date are reliable; audience metrics are best-effort estimates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-insights |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
