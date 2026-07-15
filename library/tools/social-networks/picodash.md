---
id: picodash
name: Picodash
description: Use when you have a `username`/`name` and want Instagram search/analytics — formerly a location & hashtag search engine, now a paid analytics tool whose OSINT-grade location search was gutted by Instagram's API changes.
url: https://www.picodash.com
category: social-networks
path:
- social-networks
bestFor: Instagram account/hashtag analytics and content curation; historically, searching Instagram posts by location.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- geolocation
status: degraded
pricing: freemium
costNote: Now a subscription analytics/marketing service (formerly Gramfeed). The free/OSINT-useful location & hashtag search that made it valuable was curtailed after Instagram deprecated its public API in 2018; full features require a paid plan.
opsec: passive
opsecNote: Querying Picodash's own index is passive against the subject — no signal to their Instagram. You do disclose the account/location of interest to Picodash and must create an account for most features; use a sock-puppet login.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial third-party Instagram tool dependent on Instagram's API; its capabilities have shrunk as Instagram restricted access, so current OSINT yield is uncertain.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Gramfeed
- picodash.com
tags:
- instagram
- analytics
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Picodash

> Once a go-to Instagram *location and hashtag search engine* (as Gramfeed), now a paid Instagram analytics/marketing tool — its OSINT edge blunted by Instagram's 2018 API lockdown.

## When to use
You want to search or analyze Instagram beyond the native app — historically, "who posted from this place / under this hashtag," plus account analytics. That location-search capability is exactly what made it valuable for missing-persons and event work. Reach for it knowing the OSINT-grade features are diminished and gated; if the location search still returns results for your target area, it's a useful supplement, but don't rely on it as the primary Instagram-by-location tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.picodash.com and create an account (most features are login-gated now).
2. Search an Instagram `username` for account analytics, or try the hashtag/location search for posts tied to a place or tag.
3. Read the output: matched posts, images, and any geotag/location context that survives Instagram's restrictions.
4. Pivot: poster handles feed username OSINT; a surviving geotag feeds geolocation; images feed reverse-image/face tools.

## Inputs → Outputs
- **In:** `username` / `name` / hashtag / location
- **Out:** `social-profile` (accounts), `image` (posts), `geolocation` (where still available)
- **Empty/negative result looks like:** thin or empty location/hashtag results, or a paywall — increasingly the norm since Instagram cut off the public API. Treat an empty location search as a tooling limitation, not proof no one posted there.

## Gotchas & OpSec
- **Degraded by design:** the 2018 Instagram API deprecation removed much of the open location/hashtag search; what remains is partial and subscription-gated.
- **Login required** (`account-login`) for most features — use a sock-puppet account.
- Analytics are estimates; verify any concrete lead on the live Instagram profile.
- OpSec: passive against the subject; you expose your interest to Picodash.

## Overlaps ("do both")
- Pairs with current Instagram-by-location approaches and general Instagram viewers — since Picodash's location search is unreliable now, cross-check with tools that still resolve geotags, and confirm on Instagram directly.

## Trust & verifiability
`trust: unverified` — a commercial tool whose OSINT capabilities depend on Instagram's shifting API access. Confirm anything it surfaces against the live platform; do not assume its coverage is complete or current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | picodash |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
