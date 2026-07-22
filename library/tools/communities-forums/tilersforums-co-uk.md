---
id: tilersforums-co-uk
name: Tilers Forums (UK)
description: Use when you have a `username` and want a UK tiling-trade professional's forum footprint — returns `social-profile`, reused `username` and disclosed location/employer detail.
url: https://www.tilersforums.co.uk/forums/
category: communities-forums
path:
- communities-forums
bestFor: Tracing a UK tiler/construction tradesperson's posts, handle reuse and disclosed trade details on a niche trade forum.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to read most threads; a free account is needed to post or view members-only areas.
opsec: passive
opsecNote: Reading and Google-dorking public threads is passive. Registering or messaging a member is active and visible — use a sock puppet only if you must interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established UK trade community forum; posts are user self-report, valuable mainly for handle reuse and volunteered trade/location detail.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Tilers Forums
- tilersforums.co.uk
tags:
- forums
- trade-community
- construction
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Tilers Forums (UK)

> A niche UK tiling/construction trade forum — narrow, but a good hit if your subject is a tradesperson, exposing handle reuse and volunteered business/location detail.

## When to use
You have a `username` (or a `name`) and reason to think the subject works in tiling, building or the trades in the UK. Trade forums like this are where professionals discuss jobs, tools, suppliers and their own businesses — posts often leak a trading name, service area/town, business phone, supplier relationships and years in the trade. Best used to confirm an occupation, recover a reused handle, or geolocate a tradesperson by their stated service area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use the forum search, or Google-dork it: `site:tilersforums.co.uk "<username>"`.
2. Open the member's profile (join date, post count, sometimes location field) and their post history.
3. Read posts for volunteered detail — trading name, region worked, business contact, supplier/merchant mentions.
4. Pivot: a reused `username` feeds cross-platform enumeration; a trading name feeds Companies House / directory checks; a service area narrows `geolocation`.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (forum profile + post history), reused `username`, volunteered location/employer/trade detail
- **Empty/negative result looks like:** no profile or dork hits — the handle isn't used here (the common case unless the subject is in the trade); members-only areas may hide some content without a login.

## Gotchas & OpSec
- Very niche: expect nothing unless the subject is a UK tradesperson.
- Self-reported content — corroborate any business/location claim.
- Passive to read; posting/DMing is attributable — sock puppet only.

## Overlaps ("do both")
- Pairs with Companies House, trade-directory and cross-platform username tools — the forum reveals the human/handle; those confirm the registered business behind it.

## Trust & verifiability
`trust: community` — a legitimate long-running trade forum; content is user self-report, so treat individual claims as leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tilersforums-co-uk |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
