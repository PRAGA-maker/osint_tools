---
id: aarya
name: aarya
description: Use when you have an `email` and want its digital footprint — which platforms it's registered on plus Google Maps contributions/reviews — returns linked accounts, places reviewed, and account-creation hints.
url: https://github.com/forshaur/aarya
category: email
path:
- email
bestFor: Mapping which platforms an email is registered on and extracting Google Maps reviews/contributions tied to it.
selectorsIn:
- email
selectorsOut:
- social-profile
- name
- geolocation
status: live
pricing: free
costNote: Free and open-source; installable via PyPI (`pip install aarya`) or from source. No paid tier.
opsec: active
opsecNote: aarya makes live requests to each platform (Instagram, Amazon, Spotify, Google Maps, etc.) from your host to test the email — that traffic originates from your IP and can be logged by those services. Run behind a VPN/sock-puppet network; some checks may brush against platform terms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A modest but active community tool (~35 stars). Platform checks and Maps extraction depend on volatile endpoints, so validate hits and expect breakage over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- forshaur/aarya
tags:
- email-osint
- account-enumeration
- google-maps
source: gh-topic-footprinting
lastVerified: '2026-07-11'
enrichment: full
---

# aarya

> An email-to-footprint CLI: it checks where an address is registered across platforms and, crucially, pulls the target's Google Maps reviews and contributions — which double as a map of places they've been.

## When to use
You have an `email` and want its wider footprint: which services it's registered on (Instagram, Wattpad, Duolingo, Amazon, Spotify, and more) and any Google Maps reviews/contributions linked to it. The Maps angle is the standout for missing-person work — reviews reveal `geolocation`s the subject has physically visited, plus a display `name`. Also surfaces ProtonMail account-creation dates.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install aarya` (or clone the repo and install from source).
2. Run: `aarya target@example.com` (add `-o results.json` to save output).
3. Read the results: platforms where the email is registered, plus extracted Google Maps contributions/reviews (place names, coordinates, the reviewer's display name).
4. Note account-creation hints (e.g. ProtonMail) as account-age signals.
5. Pivot: registered platforms feed account enumeration; Maps places feed `[[mapillary-2]]`/geolocation to build a movement map; a display name feeds people-search.

## Inputs → Outputs
- **In:** `email`
- **Out:** linked `social-profile`s across platforms, Google Maps reviews/contributions (`geolocation` + `name`), account-age hints
- **Empty/negative result looks like:** no platform hits and no Maps data — the email is little-used, the checks broke (endpoints change), or the account has no public Maps activity. An empty run is often tooling drift, not absence — spot-check manually.

## Gotchas & OpSec
- Volatile checks: platform-existence and Maps extraction rely on endpoints that change; verify hits and expect occasional breakage.
- OpSec: **active** — live requests from your IP to each platform; isolate behind a VPN/sock puppet.
- Maps gold: the Google Maps contributions are the highest-value output for location work — prioritise them.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]`/`[[protonmail-users]]` (provider existence oracles) and `[[blackbird]]` — aarya adds the Google Maps location angle those lack; run together for both account footprint and physical-location leads.

## Trust & verifiability
`trust: community` — a small active tool over volatile endpoints; treat platform hits and Maps data as leads to verify, but the Maps places are strong, checkable location evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aarya |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, name, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
