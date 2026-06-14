---
id: totalcraigsearch
name: TotalCraigSearch
description: Use when you want to search Craigslist across many cities/states at once for a subject's listings, alias, or distinctive item — without checking each city board manually.
url: https://www.totalcraigsearch.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Nationwide/multi-city Craigslist search to find where a subject is posting and surface their listings and any included contact info.
input: Keywords, state(s), category
output: Aggregated Craigslist listings across selected states/cities, linking back to source posts
selectorsIn: [name, phone, geolocation]
selectorsOut: [geolocation, phone, image, social-profile]
status: unknown
pricing: free
costNote: Free Craigslist meta-search; no payment indicated.
opsec: passive
opsecNote: Passive meta-search — it queries Craigslist and returns links. You leak nothing to the subject unless you then reply to a poster on Craigslist.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A Craigslist multi-city search front-end identified from name/URL/category; one of several such tools whose current liveness varies. Verify it still returns results before relying on it.
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
tags: [classifieds, craigslist, aggregator, meta-search]
source: arf-seed
lastVerified: ''
enrichment: full
---

# TotalCraigSearch

> Craigslist multi-city/state search front-end — sweeps Craigslist boards beyond a single city so a subject's post surfaces even if you don't know which city they used. (Liveness varies; verify.)

## When to use
You have a subject's likely region (`geolocation`), an alias/`name`/`phone` they might include in a post, or a distinctive item, and you want to find Craigslist activity across multiple cities/states at once. Useful for catching relocations and cross-city posting patterns.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.totalcraigsearch.com/ and enter keywords (alias, phone, distinctive item text).
2. Select the state(s)/scope and category; run the search.
3. Review aggregated Craigslist hits and follow each link to the original post for full text, photos, and contact info.
4. Pivot: recurring phone/alias → phone/username OSINT; listing `image`s → reverse-image search; posting cities → movement timeline.

## Inputs → Outputs
- **In:** keywords (`name`/alias, `phone`, item text), `geolocation` (state/scope)
- **Out:** `geolocation` (which cities the subject posts in), `phone` (if in post text), listing `image` and post page (`social-profile`-like) via source posts
- **Empty/negative result looks like:** no aggregated hits or dead links — Craigslist posts expire fast and this tool's liveness varies, so absence is weak evidence; cross-check with [[search-tempest]].

## Gotchas & OpSec
- Human-in-the-loop: none for search.
- OpSec: passive; it only queries Craigslist. Exposure happens only if you reply to a poster — use a sock-puppet email then.
- Craigslist relays contact via anonymized emails; phone numbers appear only when posters include them.

## Overlaps ("do both")
- Pairs with [[search-tempest]] — run both, as coverage, freshness, and current availability differ.

## Trust & verifiability
`trust: unverified` — identified from name/URL/category as a Craigslist meta-search; current functionality not confirmed. Validate before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | totalcraigsearch |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone, geolocation → geolocation, phone, image, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
