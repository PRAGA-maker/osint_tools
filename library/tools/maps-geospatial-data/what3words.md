---
id: what3words
name: what3words
description: Use when you have a three-word what3words code (or a `geolocation`/`address`) and want to resolve it to precise lat/long — returns a 3-metre `geolocation`.
url: http://what3words.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Resolving a what3words three-word address to exact coordinates (and vice versa) at 3-metre resolution.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to look up and share locations on the web map and apps; paid plans exist only for the developer API at volume.
opsec: passive
opsecNote: Looking up a code on the public map is passive — nothing is sent to the subject. If you resolve a code the subject shared themselves (e.g. in a message or emergency call), you are only decoding data you already hold.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by what3words Ltd; the grid is a fixed, published geocoding system used by emergency services in several countries, so a resolved code is authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- what3words-2
- convert-geographic-units
aliases:
- w3w
- three word address
tags:
- bellingcat-toolkit
- maps
source: bellingcat-toolkit
lastVerified: '2026-07-22'
enrichment: full
---

# what3words

> A global geocoding grid that maps every 3×3-metre square on Earth to a unique three-word label — used to decode a location a subject gave you, or to pin one precisely.

## When to use
You have a what3words code (three dot-separated words like `filled.count.soap`) that a subject, witness, or emergency dispatcher provided, and you need the exact `geolocation` it points to. Also useful in reverse: you have a `geolocation` or rough `address` and want the compact three-word label to share unambiguously with a search team.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://what3words.com/ in a browser.
2. Type the three words into the search box (or paste `///filled.count.soap`) and submit.
3. The map recenters on the exact 3m square; read the lat/long shown in the panel or the URL.
4. Reverse lookup: drop the map pin on a `geolocation`/`address` and read the three-word label it returns.
5. Pivot: feed the resolved coordinates into a mapping tool or coordinate converter (`[[convert-geographic-units]]`) for UTM/DMS forms other systems expect.

## Inputs → Outputs
- **In:** a three-word what3words code, or a `geolocation` / `address`
- **Out:** precise `geolocation` (lat/long) for that 3m square
- **Empty/negative result looks like:** a mistyped or non-existent word triplet returns "no matches" or suggests nearby valid combinations — every valid code resolves to exactly one square worldwide, so there is no partial match.

## Gotchas & OpSec
- Words are language-specific: the same square has different triplets in each of 60+ languages, and similar-looking codes can be far apart — confirm the language and double-check spelling.
- No human-in-the-loop or login needed for lookups.
- OpSec: passive; decoding a code reveals nothing to the subject.

## Overlaps ("do both")
- Pairs with `[[convert-geographic-units]]` — what3words gives you decimal lat/long, that tool reshapes it into UTM/DMS/NATO formats other datasets and responders use.
- See `[[what3words-2]]` for the same provider's alternate entry.

## Trust & verifiability
`trust: trusted` — the grid is a deterministic, published system maintained by what3words Ltd and adopted by emergency services, so a resolved square is authoritative, not a crowd estimate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | what3words |
