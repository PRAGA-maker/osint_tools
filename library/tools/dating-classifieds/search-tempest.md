---
id: search-tempest
name: Search Tempest
description: Use when you need to sweep Craigslist (and eBay) across many cities at once for a subject's listings, alias, or distinctive item — instead of searching one city at a time.
url: https://www.searchtempest.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Nationwide/multi-city Craigslist (plus eBay) search to find where a subject is posting without manually checking each city board.
input: Keywords, ZIP/city, radius (up to nationwide), category, price range
output: Aggregated Craigslist (and eBay) listings across all cities in the chosen radius, linking back to source posts
selectorsIn: [name, phone, geolocation]
selectorsOut: [geolocation, phone, image, social-profile]
status: live
pricing: freemium
costNote: Free for standard aggregated Craigslist searches; an optional paid tier adds wider radius/eBay/auto features. Free tier is sufficient for most OSINT sweeps.
opsec: passive
opsecNote: Passive meta-search; it queries Craigslist on your behalf and returns links. You leak nothing to the subject unless you then contact a poster on the source site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, well-known Craigslist aggregator listed in many OSINT directories; entry reasoned from known function, not re-verified.
missingPersonsRelevance: high
coverage: [us, ca]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: [SearchTempest, CrazedList]
tags: [classifieds, craigslist, aggregator, meta-search]
source: arf-seed
lastVerified: ''
enrichment: full
---

# Search Tempest

> Multi-city Craigslist (and eBay) meta-search — sweeps every Craigslist board in a chosen radius at once, so a subject's posting surfaces even if you don't know which city they used.

## When to use
You have a subject's likely region (`geolocation`), a `phone`/`name`/alias they might include in a post, or a distinctive item they may be selling, and you want to find Craigslist activity across many cities without checking each board manually. Useful for catching relocations and cross-city posting patterns.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.searchtempest.com/ and enter keywords (alias, phone, distinctive item text).
2. Set the center ZIP/city and expand the radius up to nationwide; pick the category.
3. Run the search; results aggregate matching Craigslist posts across all covered cities, each linking to the original post.
4. Open source posts on Craigslist for full text, photos, and any contact info. Pivot: a recurring phone/alias → phone/username OSINT; listing `image`s → reverse-image search; posting cities → movement timeline.

## Inputs → Outputs
- **In:** keywords (`name`/alias, `phone`, item text), `geolocation` (ZIP + radius)
- **Out:** `geolocation` (which cities the subject posts in), `phone`, listing `image` (via source post), seller post page (`social-profile`-like)
- **Empty/negative result looks like:** no aggregated hits — does not prove the subject never posted (Craigslist posts expire quickly), only that nothing is live now.

## Gotchas & OpSec
- Human-in-the-loop: none for search.
- OpSec: passive; it only queries Craigslist. Exposure happens only if you reply to a poster on Craigslist — use a sock-puppet email if so.
- Craigslist anonymizes contact via relay emails; phone numbers appear only when posters include them in text.

## Overlaps ("do both")
- Pairs with [[totalcraigsearch]] (another Craigslist multi-city tool) — run both, coverage and freshness differ.

## Trust & verifiability
`trust: community` — established aggregator with a documented function; entry reasons from known behavior rather than fresh verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-tempest |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone, geolocation → geolocation, phone, image, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
