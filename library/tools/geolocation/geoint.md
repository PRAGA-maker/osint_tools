---
id: geoint
name: GEOINT (start.me dashboard)
description: Use when you have an `image` or `geolocation` to place and want a curated hub of geolocation/GEOINT tools and datasets in one board — returns links to imagery, mapping and verification resources.
url: https://start.me/p/W1kDAj/geoint
category: geolocation
path:
- geolocation
bestFor: A one-page curated launchpad of GEOINT/geolocation tools when you need to pick the right imagery or mapping resource.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free start.me board; the linked tools vary (mostly free, some freemium).
opsec: passive
opsecNote: Browsing the dashboard leaks nothing. OpSec considerations begin on whichever downstream tool you open — apply each tool's own guidance.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-curated start.me page; a useful index whose quality depends on the curator's upkeep and the linked tools.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GEOINT start.me
- geoint dashboard
tags:
- tool-collection
- start-me
- geolocation
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- cse-utopia
- osint-assassin
- socmint
- start-me
---

# GEOINT (start.me dashboard)

> A curated start.me board of geolocation and GEOINT resources — a single launchpad to the imagery, mapping and verification tools you need to place an image or point.

## When to use
You have an `image` to geolocate or a `geolocation` to verify and want a vetted menu of the right tools — satellite/aerial imagery, street-level, chronolocation, terrain, and verification aids — without hunting piecemeal. This board organizes GEOINT resources so you can jump straight to the appropriate tool for the pivot in front of you. It routes; it does not itself analyse imagery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://start.me/p/W1kDAj/geoint.
2. Scan the grouped tiles for the capability you need (imagery, maps, shadows/sun position, weather, webcams, verification).
3. Open the tool that fits your case and run the actual geolocation there.
4. Chain several: e.g. narrow region with satellite imagery, then confirm with street-level or webcams.
5. Pivot: a confirmed `geolocation` feeds mapping, property, and local-records tools.

## Inputs → Outputs
- **In:** an `image` or candidate `geolocation` you want to resolve
- **Out:** links to imagery/mapping/verification tools that produce a refined `geolocation`
- **Empty/negative result looks like:** the board lacks a tool for your exact need — fall back to a broader OSINT tool directory or another GEOINT dashboard.

## Gotchas & OpSec
- It is an index, not an analyser — no imagery processing happens here; you still run the linked tools.
- Curated boards can drift: verify a linked tool is live before relying on it.
- OpSec: passive at the board; real footprint is on the downstream tools.

## Overlaps ("do both")
- Pairs with other curated dashboards ([[start-me]], [[socmint]]) and specific geolocation tools — this board points you to them; run the actual analysis in the destination tool.

## Trust & verifiability
`trust: community` — a community-curated start.me page; trustworthy as a launchpad, but vet each linked tool and confirm findings against an authoritative map source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geoint |
| category | geolocation |
| selectorsIn → selectorsOut | image, geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
