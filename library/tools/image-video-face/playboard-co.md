---
id: playboard-co
name: playboard.co
description: Use when you have a YouTube channel `social-profile`/`username` and want independent analytics — returns channel stats, rankings, growth, earnings estimates, and related-channel `associate` links.
url: https://playboard.co/en/
category: image-video-face
path:
- image-video-face
bestFor: Third-party YouTube channel analytics — rankings, growth history, live-stream/super-chat data, and comparable channels.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Free browsing of channel stats, rankings, and charts; deeper analytics/exports sit behind paid plans and login. No account needed for basic channel lookups.
opsec: passive
opsecNote: Reading Playboard's analytics is passive and does not touch the target's channel — Playboard, not you, tracks the data. Standard sock-puppet browsing is sufficient; no interaction with the subject occurs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established YouTube analytics platform (24M+ channels tracked); figures are Playboard's own estimates and rankings, useful directionally but not authoritative earnings/audience data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- socialblade
- yasiv-youtube
aliases:
- Playboard
- playboard.co
tags:
- youtube
- YouTube Related Sites
- analytics
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# playboard.co

> A third-party YouTube analytics dashboard — pull rankings, growth history, live-stream/super-chat data, and comparable channels for a creator without touching their channel.

## When to use
Your subject runs or is tied to a YouTube channel and you want context beyond the channel page itself: how it ranks (globally/by country/category), its growth trajectory, live-stream and super-chat activity, estimated earnings, and — usefully for pivoting — related/comparable channels that may reveal collaborators or a network. It corroborates a channel's scale and activity and can surface `associate` links.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://playboard.co/en/ and search the channel `name`, handle, or paste its URL.
2. Read the channel dashboard: subscriber/view trends, rankings, live-stream and super-chat stats, category, and estimated earnings.
3. Use the rankings/related sections to find comparable or connected channels (collaborators, same-network creators).
4. Note that granular exports/history need a paid login — the free view is enough for corroboration.
5. Pivot: a confirmed channel/handle feeds broader username checks; related channels feed further YouTube/social OSINT; cross-check figures against `[[socialblade]]`.

## Inputs → Outputs
- **In:** YouTube channel `username`/handle or `social-profile` URL
- **Out:** channel `social-profile` analytics (stats, rankings, growth), related-channel `associate` links
- **Empty/negative result looks like:** a channel not in Playboard's index (small/new channels) returns no dashboard — absence of analytics, not proof the channel doesn't exist.

## Gotchas & OpSec
- Earnings and audience figures are estimates derived from public signals — directional, not accounts-grade truth.
- Small or brand-new channels may be missing or sparsely tracked.
- OpSec: fully passive; you analyse Playboard's data, never the target's channel directly.
- Limited direct missing-persons value: strongest when the subject is a content creator or you need to map a creator network.

## Overlaps ("do both")
- Pairs with `[[socialblade]]` — both estimate YouTube stats with different models; compare to sanity-check figures.
- Use `[[yasiv-youtube]]` to visualise related-video/channel networks alongside Playboard's rankings.

## Trust & verifiability
`trust: community` — a widely-used analytics platform, but the numbers are its own estimates and rankings. Treat scale/earnings as approximate and confirm channel identity on YouTube itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | playboard-co |
| category | image-video-face |
| selectorsIn → selectorsOut | username, social-profile → social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
