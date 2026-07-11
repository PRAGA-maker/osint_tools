---
id: what3words-2
name: what3words
description: Use when you have a `geolocation`/`address` or a three-word address and want to convert between them — returns the precise 3m-square location (coordinates/map) or its unique three-word address.
url: https://what3words.com
category: geolocation
path:
- geolocation
bestFor: Converting a three-word address to exact coordinates (and back) to pin a location to a 3m square.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free to use on the web/app for lookups; the developer API has paid tiers, but manual conversion is free.
opsec: passive
opsecNote: Converting a location is a passive lookup against what3words' own grid — no subject is contacted. Requests go to what3words; use a sock-puppet browser if you'd rather not log the location you're resolving. It reveals nothing about who is at a location — only where a 3m square is.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: what3words is the official operator of the global three-word geocoding grid; conversions are deterministic and authoritative. Beware near-identical word combinations that map to distant squares — verify the exact words.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- what3words
- w3w
- three word address
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- geocoding
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# what3words

> The official three-word geocoding grid: every 3m×3m square on Earth has a unique three-word address, and this converts between those words and coordinates.

## When to use
Someone gives (or you find) a three-word address — `///filled.count.soap` — in a message, a rescue call, an app share, or an EXIF/geotag, and you need the exact `geolocation`. Or you have coordinates/an `address` and want the three words to communicate a precise spot unambiguously. Widely used by emergency services and increasingly in missing-person and field-search coordination, where a 3m-precise location beats a vague place name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://what3words.com (or the app).
2. To resolve words → location: enter the three words (with or without the `///`) in the search; the map shows the exact 3m square and coordinates.
3. To go the other way: search coordinates or an address, or drop a pin, and read the assigned three-word address.
4. Verify the words carefully — a single wrong/plural word maps to a completely different square.
5. Pivot: the resolved `geolocation` feeds `[[maps-app-by-apple]]`/`[[google-street-view]]` for imagery and a full `address`; a three-word address found in a message becomes a concrete search location.

## Inputs → Outputs
- **In:** a three-word address, OR `geolocation`/`address`
- **Out:** the exact 3m-square `geolocation` (coordinates + map) or its three-word `address`
- **Empty/negative result looks like:** "no match" or a location in an unexpected country — usually a typo, a plural/singular slip, or a similar-sounding word combination. The tool won't error meaningfully; sanity-check the resolved square against the expected region.

## Gotchas & OpSec
- Similar word combinations map to far-apart squares — always confirm the exact spelling/order; a near-miss looks valid but points elsewhere.
- It only converts locations; it says nothing about who or what is there.
- Some inputs need the country/language context; the default word list is English but localized grids exist.

## Overlaps ("do both")
- Pairs with `[[maps-app-by-apple]]`, Google Maps and coordinate tools — what3words gives the precise square from three words; those give imagery, routing and the conventional address around it.

## Trust & verifiability
`trust: trusted` — the authoritative first-party operator of the grid; conversions are deterministic. The only real pitfall is human word-entry error, not data reliability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | what3words-2 |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
