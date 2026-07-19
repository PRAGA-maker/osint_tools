---
id: nitter
name: Nitter
description: Use when you have an X/Twitter `username` and want to read their tweets without an account or JS — returns the profile's posts, media and any geotags via a privacy front-end.
url: https://nitter.net
category: social-networks
path:
- social-networks
bestFor: Viewing an X/Twitter profile and its tweets/media privately (no login, no tracking) through a Nitter instance.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
status: degraded
pricing: free
costNote: Free and open source; the only "cost" is finding a working instance or self-hosting one.
opsec: passive
opsecNote: Nitter is a privacy front-end — it fetches X content server-side and serves it without JavaScript, login, or the X tracking stack, so viewing a profile through it isn't tied to an X account or logged by X to you. This is its core OpSec advantage over visiting x.com directly. Use a working instance (or self-host); avoid instances you don't trust for sensitive queries.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Reputable open-source project (Zedeus et al.); content mirrors X, but public instances are intermittent, so an unreachable instance is an availability issue, not bad data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- nitter.net
- Twitter front-end
tags:
- twitter
- x
- privacy-frontend
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# Nitter

> An open-source privacy front-end for X/Twitter — read a profile's tweets and media with no login, no JavaScript and no X tracking. As of 2026 the flagship nitter.net is down, but working instances and self-hosting keep it usable.

## When to use
You have an X/Twitter `username` (or a name to search) and want to view their public tweets, replies and media **without** logging into X, being rate-walled by X's login gate, or leaving a trace tied to an X account. Nitter is ideal for covert profile review, pulling media for reverse-image work, and reading geotagged posts. Note its status is **degraded**: you must find a live instance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Don't assume nitter.net works — it's currently down. Check an instance-health tracker (e.g. status.d420.de) for a live instance, or self-host from the project's code.
2. On a working instance, open `https://<instance>/<username>` to view the profile.
3. Read tweets/replies/media; use the RSS feed some instances expose for monitoring; scan for geotagged posts (`geolocation`).
4. If an instance rate-limits or errors, switch to another live instance — this is expected.
5. Pivot: media → `[[imgops]]`/reverse-image; geotags → mapping; linked handles/URLs → other platforms.

## Inputs → Outputs
- **In:** X/Twitter `username` (or `name` to search on a supporting instance)
- **Out:** the `social-profile`'s tweets, replies and media; occasional post `geolocation`; RSS feed for monitoring
- **Empty/negative result looks like:** the instance returns an error, "instance has been rate limited," or a blank profile — almost always an **availability** problem (dead/limited instance), not proof the account is empty; retry on another instance before concluding anything.

## Gotchas & OpSec
- Availability is the main issue — flagship nitter.net is down and public instances are intermittent since X locked down its API; self-hosting is the most reliable route.
- Content is a mirror of X — completeness depends on what the instance can fetch (some features/timelines may be partial).
- Human-in-the-loop: expect rate-limit hops between instances.
- OpSec: strong — no login, no JS, no X-side tracking of you; that privacy is the whole point.

## Overlaps ("do both")
- Pairs with direct X viewing (when you must, via sock puppet) and X-OSINT tools — Nitter is the low-footprint reader; dedicated tools do search/analytics Nitter doesn't. Feed media into `[[imgops]]`.

## Trust & verifiability
`trust: community` — a well-regarded open-source project; the data it shows is genuine X content, and its weakness is uptime, not accuracy. Verify anything critical against the live X profile via a sock puppet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nitter |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
