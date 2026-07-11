---
id: 411directoryassistance-ca
name: 411 Directory Assistance (Canada)
description: Use when you have a Canadian `name` or `phone` and want listed directory details — returns addresses and phone numbers from Canadian white/yellow-pages listings.
url: https://www.411directoryassistance.ca
category: people-search
path:
- people-search
bestFor: Canadian phone-book style lookup — resolving a name to a listed address/number, or a number to a listed name (reverse), across Canada.
selectorsIn:
- name
- phone
selectorsOut:
- address
- phone
- name
status: live
pricing: free
costNote: Free directory-assistance style lookups; results are limited to publicly listed white/yellow-pages entries, so unlisted mobiles won't appear.
opsec: passive
opsecNote: Directory lookups are passive and do not notify the subject. It only returns listings the person chose to make public, so it reveals nothing beyond a phone book — but log queries through a clean browser as a matter of habit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A Canadian directory-assistance/white-pages aggregator; useful for landline-era listed numbers but of unverified freshness and no authority over unlisted or mobile data.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- 411 Canada
- 411directoryassistance.ca
tags:
- people-search
- canada
- directory
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# 411 Directory Assistance (Canada)

> A Canadian phone-book on the web — forward (name→number/address) and reverse (number→name) lookups over publicly listed Canadian directory entries.

## When to use
Your subject has a Canadian footprint and you have a `name` (to find a listed address and landline) or a `phone` number (to reverse-resolve who it's listed to). Reach for this as the Canadian equivalent of a white/yellow-pages check: quick corroboration that a listed number or address ties to a name, especially for older/landline listings that aggregators sometimes miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.411directoryassistance.ca.
2. For a forward lookup, enter the `name` and a province/city to narrow; for a reverse lookup, enter the `phone` number.
3. Read the listing: `name`, listed `address`, and `phone`.
4. Cross-check against a second Canadian source, since directory data can be stale.
5. Pivot: a confirmed address feeds Canadian property/municipal records; a confirmed name+city feeds broader people search and social lookups.

## Inputs → Outputs
- **In:** `name` (+ province/city) or `phone`
- **Out:** `address`, `phone`, `name` from listed directory entries
- **Empty/negative result looks like:** no listing — extremely common now, since most mobiles and many households are unlisted; absence tells you almost nothing about whether the person lives in Canada.

## Gotchas & OpSec
- Coverage skew: only *publicly listed* numbers appear, heavily weighted to landlines — the modern mobile-only population is largely invisible here.
- Freshness unknown: listings can lag years behind reality; treat as a lead to corroborate.
- OpSec: passive — nothing is sent to the subject.

## Overlaps ("do both")
- Pairs with `[[canada411]]`/other Canadian directories — different aggregators carry different listings, so run several.
- Pairs with `[[ufind-name]]` for broader (US-leaning) aggregation when the Canadian directory comes up empty.

## Trust & verifiability
`trust: community` — a directory aggregator with no authority over unlisted/mobile data and unverified freshness; a listing is a corroborating lead, not proof of current residence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 411directoryassistance-ca |
