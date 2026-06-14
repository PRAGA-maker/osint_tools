---
id: searchalljunk
name: SearchAllJunk
description: Use when you want to query multiple classifieds/marketplace sources from one box — a meta-search front-end for second-hand listings across platforms.
url: https://www.searchalljunk.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: One-box meta-search across several classifieds/marketplace sites to catch a subject's listings without visiting each site.
input: Keywords, location, category
output: Aggregated classified/marketplace listings with links back to the source sites
selectorsIn: [name, phone, geolocation]
selectorsOut: [geolocation, image, social-profile, phone]
status: unknown
pricing: free
costNote: Presents as a free meta-search front-end; no payment indicated by name/category.
opsec: passive
opsecNote: A meta-search front-end is passive — it forwards your query to source sites and returns links. Exposure only occurs if you later contact a poster on a source site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Obscure aggregator known only from its name/URL and the classifieds category; exact source coverage, liveness, and quality are not verified. Confirm it still works before relying on it.
missingPersonsRelevance: high
coverage: [us]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: [classifieds, aggregator, meta-search]
source: arf-seed
lastVerified: ''
enrichment: full
---

# SearchAllJunk

> Classifieds/marketplace meta-search front-end — intended to query several second-hand-listing sites from one box. (Coverage and liveness unverified.)

## When to use
You want a quick first pass across multiple classifieds sources for a subject's `name`/alias, `phone`, or a distinctive item, scoped by `geolocation`, without opening each marketplace individually. Treat results as leads to confirm on the source sites, not as authoritative.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.searchalljunk.com/ and enter keywords (alias, phone, item text) plus a location.
2. Run the search; review aggregated results and follow each link to the original listing on its source site.
3. On the source site, read full listing text, photos, and any contact details.
4. Pivot: take a recurring alias/phone to username/phone OSINT; run listing `image`s through reverse-image search.

## Inputs → Outputs
- **In:** keywords (`name`/alias, `phone`, item), `geolocation`
- **Out:** `geolocation` (posting area), listing `image` and seller page (`social-profile`-like) via source sites, `phone` if posters include it
- **Empty/negative result looks like:** no aggregated hits, or dead/stale links — given the tool is unverified, absence here is weak; confirm directly on Craigslist/OfferUp/etc.

## Gotchas & OpSec
- Human-in-the-loop: none expected for search.
- OpSec: passive meta-search; exposure happens only if you contact a poster on a source site — use a sock puppet then.
- Unverified: the underlying source list and whether the site is still maintained are unknown; do not assume comprehensive coverage.

## Overlaps ("do both")
- Pairs with [[search-tempest]] and [[totalcraigsearch]] for Craigslist-specific depth, which this generic aggregator may not match.

## Trust & verifiability
`trust: unverified` — identified only from name/URL/category; functionality and current availability not confirmed. Validate before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchalljunk |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone, geolocation → geolocation, image, social-profile, phone |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
