---
id: boatinfoworld
name: BoatInfoWorld
description: Use when you have a `name` (owner or vessel) and want US Coast Guard documented-vessel records — returns owner `name`, `address`, `document-id` (hull ID) and vessel details.
url: https://www.boatinfoworld.com/
category: public-records
path:
- public-records
bestFor: Linking a person to a US Coast Guard documented vessel, or a boat to its owner and hailing port.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- document-id
- associate
status: live
pricing: freemium
costNote: Free to search and view individual vessel records (owner, hull ID, hailing port, specs). Bulk data downloads and some features require an account/payment.
opsec: passive
opsecNote: Aggregates public USCG documentation data; searching is passive and the subject isn't notified. Basic viewing needs no login; only bulk downloads prompt registration.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Republishes US Coast Guard vessel documentation (a public record); the underlying data is authoritative but may lag the official register.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Boat Info World
tags:
- vessel
- boat
- coast-guard
- asset-search
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# BoatInfoWorld

> A searchable mirror of US Coast Guard documented-vessel records: tie a name to a boat, or a boat to its owner, hailing port and hull ID — an asset-and-location angle general people-search misses.

## When to use
You have a subject `name` and suspect they own a documented vessel, or you have a boat name/hull ID and want the owner. Vessel records expose an owner `name`, mailing `address`, hailing port (a location tie), and physical details — useful for asset investigations, corroborating an address, or placing a subject near a marina/port. Covers 400k+ US documented vessels.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.boatinfoworld.com/ and search by owner name, boat name, builder, or location (zip/city/county/state).
2. Open a vessel record: owner name, hull identification number, hailing port, length, year built, builder, and more.
3. Use the owner's mailing `address` and hailing port as pivots; note co-owners as `associate` links.
4. Cross-check against the official USCG documentation database for the authoritative current record.
5. Pivot: run the owner name/address through people-search and property records; the hailing port narrows geography.

## Inputs → Outputs
- **In:** `name` (owner or vessel), or `address`/location
- **Out:** owner `name`, `address`, `document-id` (hull ID), hailing port, vessel specs, co-owners (`associate`)
- **Empty/negative result looks like:** no match — the subject owns no *federally documented* vessel (small/state-registered boats aren't here), or the boat is titled to an LLC/other name; absence doesn't rule out boat ownership.

## Gotchas & OpSec
- Only **USCG-documented** vessels (generally 5+ net tons) — state-registered small craft aren't included.
- Data mirrors the federal register and may be somewhat stale; confirm against the official USCG source for currency.
- Ownership is often held by an LLC/trust — pivot through the entity name.
- US-only.

## Overlaps ("do both")
- Pairs with the official USCG vessel documentation search and state DMV/boat registries — this is the convenient front end; the official source is authoritative and state registries catch smaller boats.

## Trust & verifiability
`trust: community` — republished public USCG records; the data is authoritative in origin but may lag, so verify the current record against the official database before asserting ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | boatinfoworld |
| category | public-records |
| selectorsIn → selectorsOut | name, address → name, address, document-id, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
