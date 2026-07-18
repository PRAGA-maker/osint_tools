---
id: kelkoo-shopping-search-engine-europe
name: Kelkoo (Shopping Search, Europe)
description: Use when you have a product or seller and want European retail listings — returns where an item is sold, by which merchants, and at what price.
url: https://www.kelkoo.com
category: search-engines
path:
- search-engines
bestFor: Finding which European merchants sell a given product, and comparing sellers/prices for a listing.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free shopping comparison engine; funded by merchant affiliate links.
opsec: passive
opsecNote: You search a product-comparison index — no subject is involved and nothing is signalled. A retail tool with only incidental OSINT use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial shopping-comparison engine; listings are merchant-supplied affiliate feeds, accurate for products but not an investigative data source.
missingPersonsRelevance: low
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
aliases:
- Kelkoo
- kelkoo.com
tags:
- toddington
- curated-directory
- shopping
- europe
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Kelkoo (Shopping Search, Europe)

> A European shopping-comparison engine — its OSINT use is marginal: identifying which merchants sell a product, or which sellers are behind a listing.

## When to use
Rarely, and only for retail-adjacent questions. If a case touches a specific product or an online seller — tracing where an item is available in Europe, comparing the merchants offering it, or corroborating that a seller/merchant (`employer-org`) exists and lists particular goods — Kelkoo can help. It has no people-search function; treat it as a last-resort commercial-context tool, not a core OSINT resource.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.kelkoo.com and select the relevant European country/site.
2. Search the product (or browse a category) to see merchant listings and prices.
3. Note which merchants (`employer-org`) carry the item and their listing details.
4. Pivot: a merchant identified as a seller feeds corporate-registry and website/WHOIS checks to profile the business behind it.

## Inputs → Outputs
- **In:** a product name/category (and, incidentally, a seller `employer-org`)
- **Out:** merchant listings, prices, and which sellers carry the product
- **Empty/negative result looks like:** no listings — the product isn't in Kelkoo's merchant feeds for that country; says nothing beyond retail availability.

## Gotchas & OpSec
- **Not an OSINT database** — it indexes products/merchants, not people; expect no personal data.
- Listings are merchant-supplied affiliate feeds and skew to mainstream retail; niche/second-hand sellers won't appear.
- Coverage is European and product-centric.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with corporate registries and WHOIS/website-analysis tools when you need to profile a merchant found here — Kelkoo only tells you a seller lists a product; those tell you who the seller is.

## Trust & verifiability
`trust: community` — a commercial comparison engine with merchant-supplied data. Fine for retail facts, but it's not an investigative source; anything about a seller should be confirmed via business registries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kelkoo-shopping-search-engine-europe |
