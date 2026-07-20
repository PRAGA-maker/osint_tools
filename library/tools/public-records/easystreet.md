---
id: easystreet
name: StreetEasy
description: Use when you have an NYC `address` or building and want listing, price, and agent history — returns real-estate records that yield `address`, `name` (agents/sellers), and unit details.
url: https://streeteasy.com
category: public-records
path:
- public-records
bestFor: Pulling New York City real-estate listing history (sales, rentals, prices, agents) for an address or building.
selectorsIn:
- address
- name
selectorsOut:
- address
- name
status: live
pricing: freemium
costNote: Browsing listings, building pages, and past-listing history is free; some agent/market tools and contacting listers may prompt registration.
opsec: passive
opsecNote: Browsing public listing and building pages is passive. Do NOT submit inquiry forms or contact agents about a target's unit — that is active and creates a footprint. Use a sock-puppet account if you must interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: StreetEasy is a major, established NYC real-estate marketplace (owned by Zillow Group); listing data is operator-published and generally reliable for NYC.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- streeteasy.com
- StreetEasy
tags:
- property
- real-estate
- nyc
source: metaosint
lastVerified: '2026-07-20'
---

# StreetEasy

> The dominant NYC real-estate marketplace — an address/building lookup for listing history, prices, unit specifics, and the agents behind them.

## When to use
You have a New York City `address`, building, or unit and want its real-estate footprint: current and past sale/rental listings, asking prices, listing dates, unit layout, and the listing agents/brokerages. This corroborates that a subject lives (or lived) at an address, reveals when a unit turned over (a move-out timeline), and surfaces `name`s of agents/sellers to pivot on. Note: id/name in the library was mis-harvested as "EasyStreet"; the tool is **StreetEasy** (streeteasy.com).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://streeteasy.com (may block automated fetchers; use a real browser).
2. Search the `address` or building name; open the building page for a unit-by-unit history.
3. Read past listings for asking prices, listing/sold dates (→ move timeline), and the listing agent's `name`/brokerage.
4. Cross-reference unit turnover dates with other residence records to confirm/deny a subject's tenure at the address.
5. Pivot: agent names feed people-search; confirmed address + timeline feeds property-record and voter/utility checks.

## Inputs → Outputs
- **In:** `address` / building (NYC), or an agent `name`
- **Out:** listing history, prices, dates, unit details, agent/broker `name`
- **Empty/negative result looks like:** no listings for the address — means the unit simply hasn't been listed on StreetEasy, not that no one lives there; absence is weak evidence.

## Gotchas & OpSec
- NYC-only — useless outside the five boroughs (and immediate metro); don't apply it elsewhere.
- Listings name *agents/sellers*, not necessarily the current occupant — don't assume the lister is the resident.
- OpSec: browse passively; never send inquiry forms about a target's unit.

## Overlaps ("do both")
- Pairs with county property-record and people-search tools — StreetEasy gives listing/market history and agents; deed/tax records give legal ownership.

## Trust & verifiability
`trust: trusted` — an established Zillow-owned marketplace with reliable NYC listing data; still confirm occupancy against ownership/residence records, since a listing agent isn't the resident.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | easystreet |
| category | public-records |
| selectorsIn → selectorsOut | address, name → address, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
