---
id: bearpanther-com
name: Bearpanther Instamap
description: Use when you have a `geolocation` (a point or area on a map) and want to surface public Instagram posts tagged there — returns social-profile, username, and image leads.
url: http://bearpanther.com/instamap
category: social-networks
path:
- social-networks
bestFor: Plotting geotagged public Instagram posts for a location onto a map to find who was there.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
- username
- image
status: degraded
pricing: free
costNote: Free, open-source tool (code on GitHub as bearpanther/instamap). No account or payment; hosted demo has historically been intermittently offline.
opsec: passive
opsecNote: You are not contacting the target directly, but the tool queries Instagram's public endpoints on your behalf. Run the self-hosted version behind a sock-puppet IP if you want to avoid tying the queries to your own address; the hosted demo logs are outside your control.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Community-built hobby project by an independent developer (bearpanther); not a maintained commercial service.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Instamap
- Instagram Map
tags:
- instagram
- geolocation
- socmint
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Bearpanther Instamap

> A map-first Instagram search: drop a pin and see public posts geotagged near it, to answer "who was at this place?"

## When to use
You have a `geolocation` — a last-known location, a venue, a street, an area of a search grid — and you want to know which Instagram users posted publicly from there. This is a place-to-people pivot: rather than starting from a username, you start from the map and work back to accounts, images, and timestamps that put a person at a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://bearpanther.com/instamap (or self-host from the `bearpanther/instamap` GitHub repo if the hosted demo is down).
2. Navigate/zoom the map to the target `geolocation`, or search for the place name.
3. Trigger the search for posts tagged in that area.
4. Read the pins: each represents a public post — click through to the `username`, the `image`, and the post's own location tag.
5. Pivot: feed a promising `username` into `[[findme-0xsaikat]]` or a username-search tool; feed the `image` into reverse-image/face search.

## Inputs → Outputs
- **In:** `geolocation` (map area or place)
- **Out:** `social-profile` / `username` of posters, `image` content, refined `geolocation` (per-post tags)
- **Empty/negative result looks like:** no pins in the area, or an error/timeout. Because Instagram has heavily restricted programmatic access to location feeds, an empty map often means the endpoint is blocked, NOT that nobody posted there — do not treat emptiness as evidence of absence.

## Gotchas & OpSec
- Human-in-the-loop: Instagram rate-limits and has repeatedly removed public location-search endpoints, so this class of tool is fragile; the hosted demo is frequently offline (observed HTTP 503). Self-hosting is the more reliable path.
- OpSec: **passive** toward the target, but the tool hits Instagram on your behalf — use a sock-puppet IP/session, especially when self-hosting.
- Treat this as degraded: verify any hit directly on Instagram before relying on it, and cross-check timestamps.

## Overlaps ("do both")
- Pairs with `[[instahunt]]` and other Instagram map/geo tools — coverage of the same location endpoints varies by tool and by date, so run more than one before concluding a location is quiet.

## Trust & verifiability
`trust: community` — an open-source hobby project, not a vetted service. The underlying data is Instagram's public posts, so a confirmed hit is verifiable by opening the post itself; the tool is just the finder.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bearpanther-com |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → social-profile, username, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
