---
id: superpages-com
name: Superpages.com
description: Use when you have a US `address`, `name`, or `phone` and want white/yellow-pages data — returns listed `name`, `phone`, business listings, and neighbors as `associate` leads.
url: http://wp.superpages.com
category: people-search
path:
- people-search
bestFor: US white-pages people/reverse lookups and yellow-pages business search (a Thryv/Dex-family directory).
selectorsIn:
- address
- name
- phone
selectorsOut:
- name
- phone
- associate
status: live
pricing: free
costNote: Free, ad-supported directory; heavier on business (yellow-pages) listings, with white-pages people/reverse lookups. Some detail routes to paid partners.
opsec: passive
opsecNote: A directory query is passive and does not notify the subject. Your query is logged by Superpages and its ad/partner network; use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established US directory (Dex/Thryv family); data is aggregated public-listing/business data and can be stale, with white-pages coverage weaker than dedicated people-search sites.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- white-pages
- allareacodes
- white-pages-people-finder-anywho
aliases:
- Superpages
- superpages.com
tags:
- address
- white-pages
- yellow-pages
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Superpages.com

> A US white/yellow-pages directory — reverse-address and name lookups plus business listings, useful as one more free directory to cross-check identity and locate.

## When to use
You have a US `address`, `name`, or `phone` and want a free directory pass: who's listed at an address (and their neighbors as `associate` leads), a name→phone match, or the business at a location. Superpages skews toward business/yellow-pages listings but includes white-pages people data — a supplementary source to run alongside stronger people-search tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://wp.superpages.com and pick white-pages (people/reverse) or yellow-pages (business).
2. Enter the `address`, `name` (+ city/state), or `phone`.
3. Read the free results: listed `name`, `phone`, business listings, and nearby/associated listings.
4. Treat paid "full report" links as upsells, not new evidence.
5. Pivot: cross-check on `[[white-pages]]`, `[[allareacodes]]`, and `[[white-pages-people-finder-anywho]]`; feed an address into reverse-address people-search for co-residents.

## Inputs → Outputs
- **In:** `address`, `name` (+ location), or `phone`
- **Out:** listed `name`, `phone`, business listings, neighbor/`associate` leads
- **Empty/negative result looks like:** no match or only business results — white-pages coverage is thinner here than on dedicated people-search sites; absence isn't proof.

## Gotchas & OpSec
- Heavier on business than people; for individuals, stronger people-search tools usually outperform it.
- Data can be stale and skews to listed numbers; corroborate addresses.
- OpSec: passive; the subject isn't notified. Use a sock puppet.

## Overlaps ("do both")
- Overlaps with `[[white-pages]]`, `[[allareacodes]]`, and `[[white-pages-people-finder-anywho]]` — different, overlapping directory data; run several and reconcile.

## Trust & verifiability
`trust: community` — an aggregated directory, useful for leads but not authoritative and partly business-focused. Verify specifics against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | superpages-com |
| category | people-search |
| selectorsIn → selectorsOut | address, name, phone → name, phone, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
