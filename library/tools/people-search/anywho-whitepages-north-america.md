---
id: anywho-whitepages-north-america
name: AnyWho Whitepages (North America)
description: Use when you have a `name` or `phone` in the US and want a listed address, landline and household associates — returns address, phone and associate leads.
url: http://www.anywho.com/whitepages
category: people-search
path:
- people-search
bestFor: Quick free US whitepages lookup — name-to-address/phone and reverse-phone-to-name for listed (mostly landline) numbers.
selectorsIn:
- name
- phone
selectorsOut:
- address
- phone
- associate
status: degraded
pricing: free
costNote: Free to search; results skew to older listed/landline data and route some detail to paid partner reports.
opsec: passive
opsecNote: You query a public directory, not the subject; nothing target-facing is sent. Use a sock-puppet browser out of habit, but a lookup does not notify anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-standing but aging US whitepages aggregator; data is often stale and US-only, so treat results as leads to confirm.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- anywho
- white-pages-people-finder-anywho
aliases:
- AnyWho
- anywho.com whitepages
tags:
- toddington
- curated-directory
- people-search
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# AnyWho Whitepages (North America)

> A free US whitepages directory — name-to-address/phone and reverse-phone lookups, strongest for older listed landline records.

## When to use
You have a `name` (optionally a US city/ZIP to disambiguate) or a `phone` and want a fast, free first pass at a listed address, landline number, and household associates. Best for confirming an older or landline-listed US individual; weak for young, mobile-only, or non-US subjects.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the whitepages URL.
2. Search by `name` + city/state/ZIP, or run a reverse lookup by `phone`.
3. Read the listing: address, associated household members, and phone. Some fuller detail hands off to paid partner reports — treat those as optional.
4. Pivot: an address feeds property/neighbour records; a household associate feeds relationship mapping; a landline feeds reverse-phone corroboration.

## Inputs → Outputs
- **In:** `name` (+ location) or `phone`
- **Out:** `address`, `phone`, `associate` (household/relatives)
- **Empty/negative result looks like:** "no results" — very common for mobile-only, unlisted, young, or non-US people. Absence here is not evidence the person doesn't exist.

## Gotchas & OpSec
- Data is frequently outdated and US-only; verify any hit against a second source before relying on it.
- No batch search and no international coverage — narrow, single-lookup tool.
- OpSec: passive; a public directory query.

## Overlaps ("do both")
- Pairs with other US people-search sources (Whitepages, TruePeopleSearch, FastPeopleSearch) — coverage differs, so cross-check the address/associates each returns.

## Trust & verifiability
`trust: unverified` — an aggregator of public/listed records with no freshness guarantee; use for leads, confirm elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | anywho-whitepages-north-america |
| category | people-search |
| selectorsIn → selectorsOut | name, phone → address, phone, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
