---
id: global-security
name: GlobalSecurity.org
description: Use when you have an `employer-org` (military unit/agency) or defense subject and want reference context — returns employer-org and geolocation background on units, facilities, and equipment.
url: https://www.globalsecurity.org
category: dark-web
path:
- dark-web
bestFor: Background reference on military units, bases, weapons systems, and defense/intelligence organizations for context and image identification.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free to read; the site is ad-supported with no paywall on its reference library.
opsec: passive
opsecNote: Reading a public reference/news site; no query touches your subject. Only your own web request is logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running, widely-cited independent defense/intelligence reference (GlobalSecurity.org); credible for background but a secondary source — corroborate specifics.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GlobalSecurity
- globalsecurity.org
tags:
- toddington
- curated-directory
- deep-web-search
- military
- reference-sites
source: toddington-resources
lastVerified: '2026-07-20'
enrichment: full
---

# GlobalSecurity.org

> A deep, free reference library on the world's militaries, weapons, bases, and intelligence agencies — background context, not a person lookup.

## When to use
Your case involves a military or defense angle: a unit, base, weapon system, or agency named in a document, a uniform/vehicle/insignia in a photo, or an organization you need to understand. GlobalSecurity.org provides encyclopedic profiles — unit lineages, facility locations, equipment specs, and defense news — that help you identify what you're looking at and place an `employer-org` in geographic and organizational context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.globalsecurity.org and use the site search or browse (military, intelligence, systems, world).
2. Enter the unit/base/system/agency (`employer-org`) or a defense-related `name`.
3. Read the profile for organizational structure, base `geolocation`, equipment, and history.
4. Use it to interpret imagery (insignia, hardware) or to understand an organization a subject is tied to.
5. Pivot: an identified unit/base narrows geolocation and which official/defense records to pursue; equipment IDs feed imagery analysis.

## Inputs → Outputs
- **In:** `employer-org` (unit/base/agency) or defense-related `name`/keyword
- **Out:** `employer-org` context (structure/history), `geolocation` (base/facility locations), equipment/reference detail
- **Empty/negative result looks like:** no article on a niche or very recent topic — coverage is broad but not exhaustive or fully current; check primary/official sources for the latest.

## Gotchas & OpSec
- It's a reference/context site, not a people-finder — value is identifying and understanding orgs/hardware, not naming individuals.
- Secondary source: some articles are dated; corroborate specifics against official or newer reporting.
- OpSec: passive; you only read public content.

## Overlaps ("do both")
- Pair with official military records (e.g. [[access-to-archival-databases]]) and imagery/geolocation tools: GlobalSecurity explains the org/hardware, those tie it to people and places.

## Trust & verifiability
`trust: community` — a credible, widely-cited independent reference, but secondary and occasionally dated; use it to orient, then verify against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-security |
| category | dark-web |
| selectorsIn → selectorsOut | employer-org, name → employer-org, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
