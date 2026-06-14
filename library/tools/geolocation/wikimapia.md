---
id: wikimapia
name: Wikimapia
description: Use when you need crowd-labeled names and descriptions of buildings, businesses, and landmarks at a location that official maps leave blank.
url: https://wikimapia.org/#lang=en&lat=40.078071&lon=-100.458984&z=5&m=b
category: geolocation
path:
- geolocation
bestFor: Reading user-contributed place labels, outlines, and notes overlaid on satellite imagery.
input: Location query
output: User-labeled geographic features and notes
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: degraded
pricing: free
costNote: Free crowd-sourced map; ad-supported.
opsec: passive
opsecNote: Browsing a public crowd-mapped layer; no contact with the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced and lightly maintained; labels are user-supplied and can be wrong, outdated, or vandalized — verify anything load-bearing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- yandex-maps
- view-in-google-earth
aliases: []
tags:
- crowdsourced-map
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Wikimapia

> A "Wikipedia of maps" — user-drawn outlines and labels over satellite imagery, useful for naming the unnamed when official maps fall short.

## When to use
You have a `geolocation` (often from a photo or satellite view) and an official map shows the building/business/landmark unlabeled. Wikimapia's crowd layer may name it, outline its footprint, and add notes — helping you turn "that grey building" into an identifiable `address` or place name. Treat it as a lead generator, not authoritative ground truth.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wikimapia.org/ and pan/zoom to the area, or paste coordinates into the URL/search.
2. User-outlined objects appear as shaded shapes; hover/click to read the community-supplied name and description.
3. Note alternative/local names that other maps don't carry — useful for follow-up searches.
4. Corroborate any label against a second source before trusting it.
5. Pivot: take a resolved place name into a search engine or a stronger regional map like [[yandex-maps]]; verify the footprint in [[view-in-google-earth]].

## Inputs → Outputs
- **In:** `geolocation` / area of interest.
- **Out:** user-supplied place names, outlines, and notes (can yield an `address`/place name).
- **Empty/negative result looks like:** sparse or no labels in the area (common outside well-mapped cities), or obviously stale/incorrect entries.

## Gotchas & OpSec
- Status **degraded**: the site is dated and lightly maintained; expect old imagery and stale labels.
- Labels are crowd-sourced — wrong, outdated, joke, or vandalized entries occur. Always corroborate.
- No login or captcha for browsing; passive.

## Overlaps ("do both")
- Pairs with [[yandex-maps]] (strong regional POI/labels) and [[view-in-google-earth]] for verifying the actual footprint and imagery date.

## Trust & verifiability
`trust: community` — entirely user-generated; valuable for leads but never authoritative. Verify every load-bearing label against an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikimapia |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
