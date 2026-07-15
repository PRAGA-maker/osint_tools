---
id: 4sqmap
name: 4sqmap
description: Use when you have a Foursquare/Swarm `username` and want to plot that account's check-ins, venues and photos on a map — returns `geolocation` history and place `social-profile` data, subject to Foursquare API limits.
url: http://www.4sqmap.com/
category: social-networks
path:
- social-networks
bestFor: Visualising a Foursquare/Swarm user's public check-in history and venue photos on an interactive map.
selectorsIn:
- username
selectorsOut:
- geolocation
- social-profile
status: degraded
pricing: free
costNote: Free web app. Relies on the Foursquare/Swarm API, which has been repeatedly restricted — expect partial or empty results; not a paid product but functionally throttled.
opsec: passive
opsecNote: Reading public Foursquare data through a third-party viewer does not notify the target. The 4sqmap operator and Foursquare see your queries, not the subject — but do not connect/authorise your own Foursquare account against a target's profile, which could create a follow signal.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party visualiser of Foursquare data, provenance and current maintenance unclear; the source data is Foursquare's, but this front-end is unvetted and its uptime is unreliable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- foursquare
aliases:
- 4sqmap
- foursquare map
tags:
- toddington
- curated-directory
- social-media
- geo-location-mapping-tools
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# 4sqmap

> A map overlay for a Foursquare/Swarm account — turns a user's public check-ins into a plotted movement history, when the Foursquare API still lets it through.

## When to use
Your subject has (or had) a public Foursquare/Swarm presence and you want their location pattern rather than a flat feed: the venues they check into, how often, where photos were taken, and any mayorships/badges that anchor them to specific places. That check-in history is high-value `geolocation`: it can reveal a home neighbourhood, a workplace, a gym, a regular bar, and time-of-day patterns — directly useful for narrowing where a person spends time. Reach for it only when you already have a Foursquare `username`/profile from another lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.4sqmap.com/ in a clean/sock-puppet browser.
2. Point it at the target Foursquare/Swarm user (via the account/handle it accepts).
3. Explore the map layers it offers — venues, check-ins, mayorships, badges, photos — and note clustered locations and repeat visits.
4. Record the geolocated venues and any timestamps/photos.
5. Pivot: recurring venues become physical-surveillance/address leads; venue photos feed reverse-image; the Foursquare profile itself feeds `[[foursquare]]` and broader username enumeration.

## Inputs → Outputs
- **In:** Foursquare/Swarm `username`/profile
- **Out:** mapped `geolocation` history (venues, check-ins, photos), place `social-profile` metadata
- **Empty/negative result looks like:** a blank map, an API/error message, or "no data" — usually because Foursquare's API restrictions block the pull or the account's check-ins are private; a miss here is very often the tool, not the subject.

## Gotchas & OpSec
- Human-in-the-loop: expect **rate-limit**/API failures — Foursquare has tightened its API repeatedly, so the viewer is frequently degraded or empty; retry later or fall back to the profile directly.
- OpSec: **passive** for reading public data. Do not authenticate your own Foursquare account against the target or "follow" them — that leaks your interest.
- Data can be stale: many users abandoned Foursquare/Swarm years ago, so check-ins may be old — good for historical pattern-of-life, weak for current location.

## Overlaps ("do both")
- Pairs with `[[foursquare]]` — pull the raw profile/feed there for authoritative venue and timestamp detail, and use 4sqmap purely for the map visualisation; if 4sqmap is down, the native profile still gives you the check-ins.

## Trust & verifiability
`trust: unverified` — an unvetted third-party front-end whose maintenance and uptime are uncertain. The underlying check-ins are genuine Foursquare data, so confirm any critical location against the native Foursquare profile rather than relying on the map alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 4sqmap |
| category | social-networks |
| selectorsIn → selectorsOut | username → geolocation, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
