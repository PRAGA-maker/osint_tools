---
id: infospace
name: InfoSpace
description: Use when you have a US `name` or `phone` and want a free white-pages/metasearch lookup — returns address, phone and related directory listings via an ad-supported search portal.
url: https://infospace.com
category: people-search
path:
- people-search
bestFor: Free white-pages people/reverse-phone lookups through an ad-supported metasearch portal.
selectorsIn:
- name
- phone
selectorsOut:
- address
- phone
- associate
status: live
pricing: free
costNote: Free and ad-supported; the white-pages and reverse-phone panels are usable without payment, though "full report" buttons hand off to paid brokers.
opsec: passive
opsecNote: You query a directory portal, not the subject — no notification is sent. No login required, so exposure is limited to the site/ad networks. Use a clean browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing directory/metasearch brand (historically powered MSN white pages); now an ad-supported portal aggregating third-party directory data — broad but not authoritative, and heavy on upsell.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- InfoSpace white pages
- infospace.com
tags:
- people-search
- white-pages
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# InfoSpace

> A veteran ad-supported white-pages/metasearch portal: run a free name or reverse-phone lookup for address and directory listings before paying a broker.

## When to use
You have a US subject's `name` (or a `phone` for reverse lookup) and want a free first pass for address and directory listings. InfoSpace aggregates third-party directory data and offers people-search and reverse-phone panels; use it to scope leads and decide whether a paid source is worth it. Do not treat it as authoritative — it repackages directory data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://infospace.com in a clean browser (no account needed). Navigate to the white-pages / people search, or the reverse-phone panel.
2. Enter the `name` (add city/state to disambiguate) or the `phone` number.
3. Read the free listing: `address`, listed `phone`, and any related/household names (`associate` leads).
4. Ignore "full background report" buttons that hand off to paid brokers unless you intend to pay.
5. Pivot: an address feeds reverse-address/mapping; household names feed a fresh name search; a phone feeds carrier/reverse-phone tools.

## Inputs → Outputs
- **In:** `name` (+ optional city/state) or `phone`
- **Out:** `address`, `phone`, `associate`/household names
- **Empty/negative result looks like:** no directory listing, or several conflated same-name entries — for a common name expect noise, not a clean single hit.

## Gotchas & OpSec
- Human-in-the-loop: none for the free panels; only the broker upsells require registration/payment.
- Data quality: aggregated third-party directory data lags reality; corroborate before relying.
- OpSec: passive, no login; still use a compartmentalized session to avoid ad-tracking bleed.

## Overlaps ("do both")
- Pairs with `[[usa-official-com]]` and other free US people-search aggregators — coverage and freshness differ, so cross-check addresses/phones across two before trusting a value.

## Trust & verifiability
`trust: community` — a real, long-lived directory brand, but now an ad-supported reseller of third-party data with heavy upsell, so its output is corroboration-grade rather than authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infospace |
| category | people-search |
| selectorsIn → selectorsOut | name, phone → address, phone, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
