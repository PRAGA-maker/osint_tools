---
id: biblio
name: Biblio
description: Use when a subject deals in used/rare/antiquarian books and you want to find their seller listings or a specific book's sellers — returns `social-profile`, `address`, `associate`.
url: https://www.biblio.com
category: search-engines
path:
- search-engines
bestFor: Searching a global used/rare-book marketplace for a seller's listings or a specific title's vendors.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- address
- associate
status: live
pricing: free
costNote: Free to search and browse listings and seller pages; buying is transactional but the OSINT lookups are free.
opsec: passive
opsecNote: Browsing listings and seller pages is passive; the subject/seller is not notified. Contacting a seller through the site is active and attributable — use a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established used/rare-book marketplace aggregating independent booksellers; seller-provided info is self-reported and should be corroborated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Biblio.com
tags:
- toddington
- curated-directory
- specialty-search
- marketplace
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Biblio

> A global marketplace of independent used- and rare-book sellers — a niche pivot when a subject is a bookseller/collector, or when a distinctive title itself is the lead.

## When to use
Your subject buys or sells used, rare, or antiquarian books, or you have a specific book (edition, inscription, provenance) that ties to them. Biblio aggregates thousands of independent booksellers, each with a storefront page that often lists a business name, location, and contact route. So it works two ways: search a `name`/`employer-org` to find a seller's storefront and inventory, or search a distinctive title to find which sellers hold it. Low general relevance — a specialist tool for book-trade subjects or object-provenance work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.biblio.com.
2. To profile a seller: search the bookseller/business `name` and open their storefront (bookstore page) — note location, stated business details, and inventory patterns.
3. To trace a book: search the title/author (add edition/keywords) and review the sellers offering it and their locations.
4. Read the output: a storefront page (`social-profile`), a stated business `address`/location, and — via a distinctive inventory — links to the same seller elsewhere (`associate`).
5. Pivot: a bookstore name/address feeds business-registry and mapping tools; a seller's inventory fingerprint feeds cross-marketplace searches (AbeBooks, etc.).

## Inputs → Outputs
- **In:** `name` (seller/collector) or `employer-org` (bookstore); or a distinctive title as the query
- **Out:** `social-profile` (seller storefront), `address` (stated business location), `associate` (same seller across listings/marketplaces)
- **Empty/negative result looks like:** no matching seller or listing — the subject/title isn't on Biblio; check sister marketplaces before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none for search/browse; contacting a seller is active — use a sock puppet.
- OpSec: passive browsing.
- Seller-provided details are self-reported; a stated location/name is a lead to corroborate against business records, not a verified fact.

## Overlaps ("do both")
- Pairs with AbeBooks/other book marketplaces and business-registry tools — Biblio finds the storefront and inventory, while registries confirm the underlying business and address. Do both to tie a bookseller persona to a real entity.

## Trust & verifiability
`trust: community` — an established marketplace aggregating independent sellers; listings are authentic but seller details are self-reported, so verify names/addresses against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | biblio |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → social-profile, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
