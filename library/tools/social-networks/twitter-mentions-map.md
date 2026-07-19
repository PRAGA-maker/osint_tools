---
id: twitter-mentions-map
name: Twitter Mentions Map
description: Use when you have access to a Twitter/X account and want a world map of where the users mentioning it are located — returns `geolocation` clustering of an account's mentioners.
url: https://www.twitonomy.com/mentions-map.php
category: social-networks
path:
- social-networks
bestFor: Visualising, on a map, the self-reported locations of users who mention a given Twitter/X account.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: freemium
costNote: Twitonomy has a free tier; the mentions map requires signing in with a Twitter/X account via OAuth. Post-2023 X API restrictions make results incomplete or intermittently broken.
opsec: active
opsecNote: Using it requires OAuth-connecting a Twitter/X account to Twitonomy, which grants a third party access to that account — never connect a real/personal account; use a dedicated sock-puppet. Locations shown are users' self-reported profile locations, not verified geodata.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Twitonomy is a third-party Twitter-analytics service. Location data is derived from profile self-reports and is degraded by X's API changes; treat output as approximate.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- twitonomy
aliases:
- Twitonomy Mentions Map
tags:
- Social Media
- Twitter
- geolocation
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Twitter Mentions Map

> A Twitonomy visualisation plotting, on a world map, the self-reported locations of accounts that mention a given Twitter/X handle.

## When to use
You have a Twitter/X handle of interest and want a quick geographic sense of who engages with it — clusters of mentioners can hint at where an account's audience or contacts are based. This is a soft, aggregate signal (interest/community geography), not a locator for any one person, and its usefulness has dropped sharply since X restricted its API.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.twitonomy.com/mentions-map.php.
2. Sign in via Twitter/X OAuth using a dedicated sock-puppet account (never a personal one).
3. Provide the handle whose mentions you want mapped.
4. Read the map: pins/clusters mark the self-reported profile locations of accounts that mentioned the handle.
5. Pivot: use dense clusters as regional leads to corroborate elsewhere; individual pins are weak evidence.

## Inputs → Outputs
- **In:** a Twitter/X handle (audience `geolocation` question)
- **Out:** map clustering of mentioners' self-reported `geolocation`s
- **Empty/negative result looks like:** a blank/sparse map or an auth/API error — often means X's API returned nothing rather than that no one mentions the account. Do not read absence as fact.

## Gotchas & OpSec
- Status is degraded: X's 2023+ API restrictions frequently break or thin out results.
- Locations are self-reported profile strings ("Earth", "everywhere", a joke city) — not GPS; geocoding is approximate and gameable.
- Human-in-the-loop: requires connecting a Twitter/X account — use a sock-puppet; connecting grants Twitonomy access.
- OpSec: active — you authenticate a third-party app; isolate it from any real identity.

## Overlaps ("do both")
- Pairs with `[[twitonomy]]` — the mentions map is one view; the broader Twitonomy profile covers an account's tweets, engagement, and activity patterns.

## Trust & verifiability
`trust: unverified` — a third-party analytics tool over self-reported data, degraded by API limits. Treat the map as a rough audience-geography hint and verify any lead independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-mentions-map |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
