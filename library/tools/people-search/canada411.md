---
id: canada411
name: Canada411
description: Use when you have a Canadian `phone`, `name`, or `address` and want free white-pages data — returns listed `name`, `address`, and `phone` from Canada's national directory.
url: http://www.canada411.ca
category: people-search
path:
- people-search
bestFor: Free Canadian white-pages people search, reverse phone lookup, and reverse address lookup.
selectorsIn:
- phone
- name
- address
selectorsOut:
- name
- address
- phone
status: live
pricing: free
costNote: Free, ad-supported national directory operated by Yellow Pages Canada; core people/phone/address searches need no account.
opsec: passive
opsecNote: A directory query is passive and does not notify the subject. You disclose the query to Yellow Pages/YP.ca and its ad network; use a sock-puppet browser. No interaction reaches the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Canada's established national telephone directory, operated by Yellow Pages Digital & Media Solutions with data from Canadian telecom providers; strong for listed landlines, thinner for mobiles.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- allareacodes
- white-pages
aliases:
- Canada 411
- canada411.ca
tags:
- people-investigations
- white-pages
- canada
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Canada411

> Canada's national white-pages directory (Yellow Pages Canada) — free people search, reverse phone, and reverse address lookup across the country.

## When to use
Your subject is in Canada and you have a `phone` number, a `name`, or an `address`. Canada411 resolves listed numbers to a subscriber `name` and `address`, finds people by name + city, and does reverse-address lookups to see who is listed at a location — the Canadian counterpart to US white-pages tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.canada411.ca in a sock-puppet browser.
2. Choose the search type: People (name + city/province), Reverse Phone, or Reverse Address/Postal Code.
3. Enter the selector and search.
4. Read the result: listed entries show `name`, `address`, and `phone`; unlisted/mobile numbers often return little or nothing.
5. Pivot: a returned address feeds reverse-address searches for co-residents (`associate`); cross-check numbers against `[[allareacodes]]` and names against broader `[[white-pages]]`.

## Inputs → Outputs
- **In:** `phone` (best for landlines), `name` (+ location), or `address`
- **Out:** listed `name`, `address`, `phone`
- **Empty/negative result looks like:** "no results" — common for mobiles and unlisted numbers; absence is not proof the person isn't in Canada.

## Gotchas & OpSec
- Coverage favours listed landlines; mobile and unlisted numbers frequently don't resolve.
- Directory data can be stale; treat an address as a lead to confirm against a second source.
- OpSec: passive; the subject isn't alerted. Use a sock puppet to avoid tying queries to you.

## Overlaps ("do both")
- Pairs with `[[allareacodes]]` (which also covers Canada) — run the same number through both, and feed name/address hits into `[[white-pages]]`.

## Trust & verifiability
`trust: trusted` — the recognised national directory operated by Yellow Pages Canada with telco-sourced data. Listed results are reliable but can lag reality; verify currency of any address.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canada411 |
| category | people-search |
| selectorsIn → selectorsOut | phone, name, address → name, address, phone |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
