---
id: social-stats
name: Social Stats
description: Use when you have a VK community/user `username` or `name` and want engagement and activity statistics for that VKontakte page — returns social-profile activity metrics.
url: http://socialstats.ru
category: social-networks
path:
- social-networks
bestFor: Pulling wall-post, audience and activity statistics for a VKontakte community or user to gauge how active/real a Russian-speaking profile is.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free VK statistics service; no payment required. Russian-language interface.
opsec: passive
opsecNote: You query the analytics site about a public VK page, not VK directly, so the target is not notified. It is a third-party Russian service — use a research browser/connection and do not enter any VK credentials into it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party Russian SMM analytics site with no transparency about data sourcing; treat metrics as approximate. Availability is intermittent.
missingPersonsRelevance: medium
coverage:
- ru
auth: none
api: false
localInstall: false
registration: false
aliases:
- socialstats.ru
- SocialStats VK
tags:
- vk
- russia
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
---

# Social Stats

> A Russian VKontakte analytics site that reports posting/engagement statistics for a VK community or user — a "is this profile active and real" check.

## When to use
Your subject is tied to a VKontakte page (community or personal) and you want a quick read on how active it is: posting frequency, audience, engagement patterns. Useful to distinguish a live, real Russian-speaking profile from a dormant or bot page before investing in deeper VK OSINT.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://socialstats.ru (Russian interface; use a translator).
2. Enter the VK community/user identifier (`username` / short name) or the display `name`.
3. Read the returned statistics: wall-post activity, audience size, popularity, and interest/overlap groups.
4. Use the activity profile to judge whether the page is worth pivoting on.
5. Pivot: take the confirmed VK identity into a native VK profile view or a dedicated VK OSINT tool (e.g. `[[vk-city4me-com]]`) for friends, photos and history.

## Inputs → Outputs
- **In:** VK `username`/short name or `name`
- **Out:** `social-profile` activity/engagement statistics (posts, audience, popularity)
- **Empty/negative result looks like:** no data for the identifier, or a site error — meaning the page isn't indexed, the handle is wrong, or the service is temporarily down.

## Gotchas & OpSec
- The service is intermittently reachable (`status: degraded`) and Russian-only; expect downtime and machine-translate the UI.
- It profiles VK **communities/pages** primarily; personal-profile depth is limited.
- Metrics are unverified third-party estimates — corroborate against the live VK page.

## Overlaps ("do both")
- Pairs with `[[vk-city4me-com]]` — this gives activity statistics, while city4me and native VK give the actual friends, photos and post content.

## Trust & verifiability
`trust: unverified` — an opaque third-party Russian analytics site with no sourcing disclosure; use its numbers as a rough activity signal, not as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-stats |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
