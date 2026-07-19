---
id: mapme-com
name: mapme.com
description: Use when a subject or org may publish a public interactive directory/map here — browse Mapme-hosted maps to place people, businesses or points at a `geolocation`/`address`.
url: https://mapme.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Finding and reading public interactive maps/directories (member maps, business locators, project portfolios) that pin a subject or place.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Creating maps is a freemium SaaS; viewing published public maps is free and needs no account.
opsec: passive
opsecNote: Browsing a published public map is read-only and does not notify anyone. If you sign up to build a map you expose an account — for OSINT you only need to view public maps, ideally from a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Mapme is a legitimate no-code map-building platform; the map content itself is created by third parties (orgs/individuals) and is only as accurate and current as those creators made it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Mapme
- mapme.com
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- directory
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# mapme.com

> A no-code interactive-map platform — its OSINT value is the public maps built on it: member directories, business locators and project maps that can pin a subject or place at a location.

## When to use
You suspect a subject, business or organization appears on a public interactive map — a club/member directory, a real-estate or store locator, a community project map, an event map — and you want the underlying `geolocation`/`address`. Mapme hosts many such public maps (at `mapme.com` and `viewer.mapme.com`), each with searchable/filterable pins carrying names, descriptions and contact detail. This is a targeted lookup: it only helps when your subject is on a Mapme-hosted map, which you usually reach via a web search rather than the homepage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Rather than the homepage (a marketing/builder site), search the web for the specific map: e.g. `site:mapme.com "Subject Name"` or `viewer.mapme.com <org> directory`.
2. Open the public map and use its search/filter to find the subject, business or place.
3. Read the pin details — location (`geolocation`/`address`), description, contact info, links.
4. Confirm the pin refers to your subject (names/orgs can collide) before treating the location as established.
5. Pivot: an `address`/`geolocation` feeds mapping and people-search; contact detail feeds phone/email tools.

## Inputs → Outputs
- **In:** `name` / `employer-org` / `address` (whatever the map is keyed on)
- **Out:** `geolocation` / `address` of the matching pin, plus any contact/description the creator added
- **Empty/negative result looks like:** no relevant public map exists, or the subject isn't pinned on it — the common case, and not evidence of anything.

## Gotchas & OpSec
- Human-in-the-loop: none to view public maps; account only needed to build maps (not for OSINT).
- OpSec: **passive** — viewing a published map notifies no one.
- The data is creator-supplied and can be outdated, aspirational, or wrong; verify a pin before relying on the location. The homepage itself is a builder tool, not a searchable people index — go via the specific published map.

## Overlaps ("do both")
- Pairs with general web search (to locate the relevant Mapme map) and with mainstream mapping/geolocation tools that place addresses the map surfaces.

## Trust & verifiability
`trust: unverified` — a legitimate platform hosting third-party-authored maps; the pins are only as reliable as their creators, so corroborate any location before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapme-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | name, employer-org, address → geolocation, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
