---
id: search-systems-public-records-us
name: Search Systems Public Records (US)
description: Use when you have a `name` (and rough `geolocation`) and need to find the right official US/county public-records portal — a directory that routes you to courts, property, and vital-records databases.
url: http://publicrecords.searchsystems.net/
category: dark-web
path:
- dark-web
bestFor: Routing to the correct federal/state/county public-records database for a US subject
selectorsIn:
- name
- geolocation
- address
selectorsOut:
- address
- document-id
- associate
status: degraded
pricing: freemium
costNote: Many links to free government databases are free; some aggregated/premium record lookups are paid.
opsec: passive
opsecNote: Browsing the directory and the government portals it links to is passive. The directory is a pointer; OpSec depends on each destination site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-standing public-records link directory; link freshness and current upkeep not independently verified.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- SearchSystems
tags:
- toddington
- curated-directory
- public-records
- deep-web-search
source: toddington-resources
lastVerified: ''
enrichment: full
---

# Search Systems Public Records (US)

> A directory of free and fee-based public-records databases (mis-categorized here as "dark-web"; it is in fact a clearnet deep-web/public-records index) that points you at the right court, property, and vital-records portal for a US locality.

## When to use
Use it when you have a `name` plus an approximate `geolocation`/`address` and you don't know which county or state database to query. Rather than searching records directly, it maps a jurisdiction to its official portals — courts, recorder/property, business filings, professional licenses, and vital records — which then yield `address`, `document-id`, and `associate` links.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://publicrecords.searchsystems.net/ and drill down by state, then county, then record type.
2. Follow the link to the official government portal it indexes.
3. Run your `name`/`address` query on that destination database.
4. Pivot: a hit (e.g. a property deed or court filing) gives a current `address`, related parties (`associate`), and case/`document-id` references to chase next.

## Inputs → Outputs
- **In:** `name`, `geolocation`/`address`
- **Out:** `address`, `document-id`, `associate` (via the linked official databases)
- **Empty/negative result looks like:** a dead or moved link, or a jurisdiction with no online records — fall back to direct county clerk sites.

## Gotchas & OpSec
- Human-in-the-loop: none for the directory; destination sites may require captcha, payment, or login.
- OpSec: passive. This is a link index, so verify each destination is the genuine official source before entering query terms; note the http (not https) directory URL.
- Category note: filed under "dark-web" but it is clearnet public-records — treat accordingly.

## Overlaps ("do both")
- Pairs with national people-search aggregators: this gives authoritative primary sources, aggregators give breadth and speed.

## Trust & verifiability
`trust: unverified` — a well-known public-records link directory surfaced via Toddington, but link rot is likely and current maintenance is unconfirmed; always validate the linked official source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-systems-public-records-us |
| category | dark-web |
| selectorsIn → selectorsOut | name, geolocation, address → address, document-id, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
