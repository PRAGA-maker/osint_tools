---
id: blueskymeter-com
name: blueskymeter.com
description: Use when you have a Bluesky `username` (handle) and want public account analytics — returns follower/engagement metrics and profile activity as a social-profile.
url: https://blueskymeter.com/
category: social-networks
path:
- social-networks
bestFor: Pulling quick public analytics (followers, activity trend) for any Bluesky handle without logging in.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free; no account or payment required to look up a handle.
opsec: passive
opsecNote: You query a third-party analytics site, not Bluesky directly, so the target is not notified. The lookup is logged by blueskymeter, not by the subject. Use a sock-puppet browser if you want to avoid tying the query to your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent third-party analytics site (not operated by Bluesky). Metrics are derived from Bluesky's public AT Protocol data, so figures are reproducible but not officially blessed.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- bsky-app
aliases:
- Bluesky Meter
- bluesky analytics
tags:
- bluesky
- BlueSky / BSky Related Sites
- social-analytics
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# blueskymeter.com

> A no-login analytics dashboard for any Bluesky handle: followers, engagement, and activity trend at a glance.

## When to use
You have a Bluesky `username`/handle (e.g. `andrei.blue`) and want a fast read on the account's size and activity — follower count, posting cadence, engagement — to gauge whether the profile is active, dormant, or a bot, and to establish a baseline before deeper enumeration. Bluesky offers no native analytics, so this fills that gap.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://blueskymeter.com/ in a clean/sock-puppet browser session.
2. Enter the target handle (with or without the `.bsky.social` suffix — custom-domain handles like `alice.example.com` also work).
3. Read the dashboard: follower/following counts, a "Daily Activity" trend, and engagement figures.
4. Pivot: confirm the account is live and current, then move to the profile itself on `[[bsky-app]]` to read posts, replies, and the follow graph for associate links.

## Inputs → Outputs
- **In:** `username` (Bluesky handle)
- **Out:** `social-profile` (public metrics: followers, following, activity/engagement over time)
- **Empty/negative result looks like:** "handle not found" or zeroed metrics — the handle is misspelled, was renamed, or the account was deleted; try resolving the handle on Bluesky directly first.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a direct handle lookup.
- OpSec: **passive** — the subject is not notified. You are trusting a third party with your query and IP; use a sock puppet if attribution matters.
- Only public AT Protocol data is exposed; nothing here reveals private DMs, email, or IP.

## Overlaps ("do both")
- Pairs with `[[bsky-app]]` — this gives the numbers, the native app gives the actual posts and follow graph you pivot on.

## Trust & verifiability
`trust: community` — independent site built on Bluesky's public firehose data. Cross-check any surprising metric against the raw profile, since third-party counts can lag or cache.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blueskymeter-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
