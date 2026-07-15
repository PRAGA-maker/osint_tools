---
id: personlookup-co-nz
name: personlookup.co.nz
description: Use when you have a New Zealand `phone` (or `name`/`address`) and want to identify the person behind it — returns a name, residential address and related property/valuation data.
url: https://personlookup.co.nz/
category: phone
path:
- phone
bestFor: Reverse phone lookup and name/address search across New Zealand residential data.
selectorsIn:
- phone
- name
- address
selectorsOut:
- name
- address
- phone
status: live
pricing: freemium
costNote: Basic search is free; the site advertises a database of 4.5M+ New Zealanders and added real-estate valuation/sale-history features that may sit behind fuller/paid detail — confirm gating before relying on a "free" full record.
opsec: passive
opsecNote: A reverse lookup queries the site's own aggregated dataset, not the subject's phone or accounts, so it is passive — the person is not alerted. You disclose the searched number to the site operator; use a sock-puppet browser if the number's sensitivity warrants.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial NZ data-aggregator scraping/compiling residential, phone and property data; not an official register and data currency/accuracy are unverified.
missingPersonsRelevance: high
coverage:
- nz
auth: none
api: false
localInstall: false
registration: false
aliases:
- Person Lookup NZ
- NZ reverse phone lookup
tags:
- mobilephone
- Mobile & Phone Related
- new-zealand
- reverse-lookup
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# personlookup.co.nz

> "The fastest search for New Zealand residential data" — a reverse phone / name / address lookup over a claimed 4.5M+ NZ residents, now bundled with property valuation and sale-history data.

## When to use
You have a New Zealand `phone` number (landline or listed mobile), or a `name`/`address`, and want to identify the person, their household, or last-known address. Reverse phone → name is the headline use; forward name → address and address → occupant also work. Strong for locating NZ subjects where electoral-roll access is restricted.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://personlookup.co.nz/.
2. Enter the `phone` number (for reverse lookup), or a `name` / `address` for forward search.
3. Read the result: matched name(s), residential address, and — for property searches — valuation and sale-price history.
4. Pivot: a name feeds NZ people/social searches; an address feeds property records and neighbor mapping; a confirmed number feeds messaging-app account checks.

## Inputs → Outputs
- **In:** `phone` / `name` / `address` (NZ)
- **Out:** `name`, residential `address`, associated `phone`; property valuation/sale history for address searches
- **Empty/negative result looks like:** "no match" — common for unlisted mobiles, ex-directory numbers, or recent movers. Absence is weak evidence given the dataset only covers listed/aggregated residential data.

## Gotchas & OpSec
- **Coverage bias:** built largely from listed/residential and property data — unlisted mobiles and privacy-suppressed entries won't appear.
- **Currency unknown:** aggregated data lags reality; treat addresses as leads and corroborate.
- **Freemium gating:** basic hits may be free while fuller detail is gated — don't assume a partial result is the whole record.
- OpSec: passive; no notification to the subject.

## Overlaps ("do both")
- Pairs with the NZ Companies Office / property (LINZ-derived) records and international reverse-phone tools — those confirm business/property links, while this is optimized for fast residential reverse lookup.

## Trust & verifiability
`trust: unverified` — a commercial aggregator, not an official source. Any name/address it returns should be confirmed against a second source (electoral, property, or direct) before action.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | personlookup-co-nz |
| category | phone |
| selectorsIn → selectorsOut | phone, name, address → name, address, phone |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
