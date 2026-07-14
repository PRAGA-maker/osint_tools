---
id: mastogizmos-com
name: MastoGizmos
description: Use when you have a username, hashtag or topic and want to search across the decentralised Mastodon fediverse — returns matching profiles, posts and linked accounts.
url: https://mastogizmos.com/
category: social-networks
path:
- social-networks
bestFor: Searching hashtags, verified users and topics across many Mastodon instances at once (which native Mastodon search can't do).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- domain
status: live
pricing: free
costNote: Free web tools; no account required. Some gizmos hit instance APIs that rate-limit, and results depend on which instances are reachable.
opsec: passive
opsecNote: Queries run against MastoGizmos and public Mastodon instance APIs, not against the target's own account, so viewing is passive. Instance admins can see API/read traffic; use a VPN for sensitive searches. Do not follow or interact from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A hobbyist collection of client-side Mastodon utilities; useful and low-risk but not an official or audited service, and coverage is best-effort across a decentralised network.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MastoGizmos
- mastogizmos.com
- Mastodon gizmos
tags:
- mastodon
- Mastodon Related Sites
- fediverse
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# MastoGizmos

> A toolbox of small web utilities for searching Mastodon/the fediverse across many instances at once — filling the gap left by Mastodon's deliberately limited native search.

## When to use
You have a `username` or `name` you suspect is active on Mastodon, or a `hashtag`/topic to track, and you need to search *across* instances — because Mastodon's own search only sees the local instance plus what it has federated. MastoGizmos bundles cross-instance hashtag search, verified-user search (find posts from users with a specific profile link), user-directory browsing by linked domain, and Google-backed Mastodon search, so it turns a decentralised, hard-to-query network into something searchable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mastogizmos.com/ and pick the gizmo that fits your goal:
   - **Big Mastodon Hashtag Search** — cross-instance hashtag hunting with filters.
   - **Mastodon Custom Verified User Search** — find posts from verified users whose profile links to a given site/domain.
   - **David's Dex** — browse user directories by their linked `domain`.
   - **Mastodon Web Search** — a Google dork wrapper to search Mastodon instances.
2. Enter your `username`, `name`, hashtag or `domain` and run it.
3. Read the results: profile handles are `@user@instance.tld` — note both the handle and its home instance.
4. Pivot: a home `domain`/instance and verified profile link feed cross-platform lookups; a hashtag's active contributors feed `associate` mapping.

## Inputs → Outputs
- **In:** `username`, `name`, hashtag, or a linked `domain`
- **Out:** `social-profile` (fediverse handles), `name`, home instance `domain`
- **Empty/negative result looks like:** no matching handle or an instance that won't respond to the API. Because coverage is best-effort across a federated network, absence is weak evidence — retry a different gizmo/instance before concluding the subject isn't on Mastodon.

## Gotchas & OpSec
- No login/CAPTCHA on MastoGizmos itself, but underlying instance APIs rate-limit and some instances block cross-instance queries, so coverage is patchy and never exhaustive.
- A handle is only unique *per instance* — always capture the full `@user@instance` form; the same username on two instances is two different people.
- Passive against the target, but instance admins can see read traffic; VPN for sensitive work.

## Overlaps ("do both")
- Pairs with reverse-image/face search on the profile avatar to link the fediverse account to accounts on other networks.
- Complements a general `[[github-io-2]]`/Google dork for the same handle — cross-check what federation misses.

## Trust & verifiability
`trust: community` — an independent hobby toolset; the data it returns comes straight from public Mastodon APIs (authoritative for that instance), but coverage and uptime of the gizmos themselves are not guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mastogizmos-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
