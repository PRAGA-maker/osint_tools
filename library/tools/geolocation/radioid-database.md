---
id: radioid-database
name: RadioID Database
description: Use when you have a DMR ID or ham-radio `username`/callsign and want the operator's real `name`, city and country — returns identity and coarse `geolocation` from radio registrations.
url: https://radioid.net/database/search
category: geolocation
path:
- geolocation
bestFor: Resolving a DMR radio ID or amateur callsign to the registered operator's name and location.
selectorsIn:
- username
- name
selectorsOut:
- name
- geolocation
status: live
pricing: free
costNote: Free public database; no account needed to search.
opsec: passive
opsecNote: You query RadioID's own dataset, not the operator, so the lookup is passive and leaves no trace with the subject. The data is self-registered by amateur operators and derived from public licensing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run registry (radioid.net) tying DMR IDs to callsigns; callsign→name is backed by national licensing, but city/location is operator-supplied and can be stale.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- radioid.net
- DMR ID database
tags:
- geolocation
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# RadioID Database

> The community registry that maps DMR radio IDs to amateur-radio callsigns and operator identities — a callsign or DMR ID resolves to a real name, city, and country.

## When to use
You have a DMR ID (a numeric radio identifier) or a ham-radio callsign (`username`) — seen in radio traffic, a hotspot log, a forum profile, or on equipment — and want to identify the operator behind it. Amateur licensing ties a callsign to a real `name` and licensing region, so this can turn a radio handle into an identity and a coarse location. Relevant when a subject is a radio hobbyist.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://radioid.net/database/search.
2. Search by DMR ID, callsign, `name`, city, state, or country.
3. Read the result rows: DMR ID, callsign, operator `name`, city/state/country.
4. Cross-check the callsign against the national licensing authority (e.g. FCC ULS in the US, QRZ.com) to confirm the name and get the licensed address.
5. Pivot: a confirmed callsign feeds QRZ/FCC lookups for the licensed `address`; the name feeds people-search.

## Inputs → Outputs
- **In:** `username` (DMR ID / callsign) or `name`
- **Out:** `name` (registered operator), `geolocation` (city/state/country)
- **Empty/negative result looks like:** no matching row — the ID/callsign isn't registered in the DMR database (many licensed hams never register a DMR ID), which does NOT mean the callsign is invalid; check the licensing authority directly.

## Gotchas & OpSec
- City/location is **operator-supplied** and often just their licensing region, not a precise address — treat as coarse.
- Coverage is limited to operators who registered a DMR ID; absence here isn't proof the person has no callsign.
- Passive: the subject is never contacted.

## Overlaps ("do both")
- Pairs with QRZ.com and the national licensing databases (FCC ULS, etc.) — do both, because those give the authoritative licensed name/address while RadioID links the DMR ID to the callsign in the first place.

## Trust & verifiability
`trust: community` — a volunteer-run registry; the callsign linkage is solid (backed by licensing), but confirm identity and any address against the official licensing authority before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radioid-database |
| category | geolocation |
| selectorsIn → selectorsOut | username, name → name, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
