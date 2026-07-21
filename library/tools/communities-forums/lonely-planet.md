---
id: lonely-planet
name: Lonely Planet
description: Use when you have a `geolocation` and need travel-context — venues, neighbourhoods, transport, and accommodation a subject might use — returns place and address leads for a location.
url: http://www.lonelyplanet.com
category: communities-forums
path:
- communities-forums
bestFor: Building travel-context for a location — notable venues, hostels/hotels, transport hubs, and traveller haunts.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free to read destination guides online; guidebooks and some content are sold, but the web guides are open.
opsec: passive
opsecNote: Reading destination guides is passive and anonymous; nothing reaches any subject. (Its Thorn Tree traveller forum closed in 2021, so the interactive community angle is gone.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A reputable travel publisher; its guides are editorially produced but are travel context, not authoritative records about people.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Lonely Planet
- lonelyplanet.com
tags:
- toddington
- curated-directory
- online-communities-blogs
- travel
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Lonely Planet

> The travel publisher's destination guides, used as background: what a place's traveller-facing venues, lodging, and transport look like when a subject is on the move.

## When to use
A **context** resource for cases with a travel dimension. When a subject is thought to be travelling through or staying in a place, Lonely Planet's guides map the traveller ecosystem there — hostels and hotels, backpacker districts, bus/train hubs, popular sights and cafés. This helps you reason about where someone on a budget or a tourist route might go, and gives named `address`es to check against sightings. It does not find people; it characterizes places.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.lonelyplanet.com and navigate to the destination (`geolocation`).
2. Read the guide's sections: where to stay (hostels/hotels), transport, and popular areas/sights.
3. Note specific venue `address`es and neighbourhoods that fit the subject's profile (budget traveller, tourist, etc.).
4. Cross-reference those places against any sightings, receipts, or social posts.
5. Pivot: candidate venues feed direct enquiries and local records; neighbourhoods narrow imagery/CCTV canvassing.

## Inputs → Outputs
- **In:** a `geolocation` / destination
- **Out:** traveller-oriented `geolocation`/`address` leads — lodging, transport hubs, notable venues
- **Empty/negative result looks like:** thin coverage for a very small or off-route place — the guides prioritize traveller destinations, so obscure locations have little.

## Gotchas & OpSec
- Context, not people: it never returns individuals, only place information.
- The Thorn Tree traveller forum (its old community/Q&A) closed in 2021; don't expect interactive traveller intel here anymore.
- OpSec: passive reference browsing.

## Overlaps ("do both")
- Pairs with mapping tools and hostel/booking sites — Lonely Planet frames *which* traveller venues matter; mapping and booking platforms give live specifics.

## Trust & verifiability
`trust: community` — a credible travel publisher; reliable as place context, but not a record source about any person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lonely-planet |
| category | communities-forums |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
