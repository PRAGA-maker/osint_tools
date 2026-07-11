---
id: skyzoo-blue
name: skyzoo.blue
description: Use when you have a Bluesky `username` (handle) and want account statistics, starter-pack membership, and network rankings — returns social-profile and name context.
url: https://skyzoo.blue/stats
category: social-networks
path:
- social-networks
bestFor: Bluesky analytics — per-account stats, starter-pack membership, top-account rankings, and post permalink extraction.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free and open source (donation-supported via Ko-fi/GitHub Sponsors); no login or payment to view stats.
opsec: passive
opsecNote: Reads the public Bluesky (AT Protocol) network via skyzoo's own tooling, not the target's account, so the subject is not notified. Only the site operator sees your IP; use a VPN/sock-puppet browser for sensitive lookups. Do not authenticate.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source community project by jycouet; data derives from the public AT Protocol and is verifiable against Bluesky itself.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- clearsky-app
aliases:
- Sky Zoo
- skyzoo
tags:
- bluesky
- BlueSky / BSky Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# skyzoo.blue

> A free, open-source Bluesky analytics site — per-account stats, starter-pack browsing, network rankings, and post-permalink extraction.

## When to use
You have a Bluesky `username` (handle) and want quantitative context on the account and its place in the network: activity stats, which starter-packs it belongs to (a strong `associate`/community signal), and how it ranks among followed accounts. Complements block-focused tools when you want reach/community context rather than moderation relationships.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://skyzoo.blue/ (or go straight to a profile by prefixing a handle: `skyzoo.blue/<handle>`).
2. For a specific account, enter the Bluesky handle to pull its stats page.
3. Use the sub-tools as needed: **Wolf** (starter-packs browser), **Whale** (global stats), **Lion** (top-followed accounts), **Turtle** (post-URL → permalink extractor).
4. Read the output: the account's stats, starter-pack memberships, and ranking context.
5. Pivot: starter-pack co-members are `associate` leads; feed the handle to [[clearsky-app]] for block/handle-history data skyzoo doesn't emphasize.

## Inputs → Outputs
- **In:** `username` (Bluesky handle); a `name` resolved to a handle
- **Out:** `social-profile` stats/metadata, starter-pack `associate` context, network ranking
- **Empty/negative result looks like:** handle not found or blank stats — the account may be new, deleted, or mistyped; not proof of absence from Bluesky.

## Gotchas & OpSec
- Overlaps heavily with [[clearsky-app]]; skyzoo leans toward stats/rankings/starter-packs while ClearSky leans toward blocks/handle-history — use both for full coverage.
- Rankings/global stats reflect the whole network, not your target; don't confuse network-wide "top accounts" with the subject.
- OpSec: passive — no notification to the subject; only your IP is exposed to the operator.

## Overlaps ("do both")
- Pairs with [[clearsky-app]] because the two Bluesky analytics sites emphasize different dimensions (stats/starter-packs vs. blocks/handle-history) of the same public AT Protocol data.

## Trust & verifiability
`trust: community` — open-source, community-run, built on the public AT Protocol. Outputs are checkable directly against Bluesky, so data-quality risk is low; it is not an official Bluesky service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skyzoo-blue |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
