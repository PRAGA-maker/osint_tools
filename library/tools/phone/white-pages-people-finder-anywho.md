---
id: white-pages-people-finder-anywho
name: White Pages | People Finder - AnyWho
description: Use when you have a US `phone` number or a `name` and want free white-pages data — returns the listed `name`, `address`, and phone from public directory records.
url: https://www.anywho.com/reverse-lookup
category: phone
path:
- phone
bestFor: Free US white-pages reverse phone lookup and name/address people search, strongest for landlines.
selectorsIn:
- phone
- name
selectorsOut:
- name
- address
- phone
status: live
pricing: freemium
costNote: Free reverse lookup and people search on public white-pages data; cell numbers and detailed reports push you to paid partner services (AnyWho is part of the Intelius/PeopleConnect family). Ad-supported.
opsec: passive
opsecNote: Querying a directory is passive — the subject is not notified. You do disclose the number/name to AnyWho and its ad/partner network; use a sock-puppet browser and expect heavy advertising and paid-service upsells.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running US white-pages directory (formerly AT&T-affiliated) now under PeopleConnect; data is aggregated from public phone-book records and can be stale, especially for mobiles.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- allareacodes
- thatsthem-phone-search
- white-pages
aliases:
- AnyWho
- AnyWho reverse lookup
- AnyWho white pages
tags:
- phone
- white-pages
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# White Pages | People Finder - AnyWho

> A free US white-pages directory for reverse-phone and name lookups — best at putting a name and address to a landline before you reach for paid data.

## When to use
You have a US `phone` number (ideally a landline) or a `name` and want a quick, free identity/address check. AnyWho draws on public white-pages listings, so a listed number often returns the subscriber `name` and `address` at no cost — a fast first pass before spending on a paid people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.anywho.com/reverse-lookup in a sock-puppet browser.
2. For a number, enter the `phone` in the reverse-lookup box; for a person, use the name/people-search tab with `name` (+ city/state to narrow).
3. Read the result: a listed landline typically returns `name` and `address`; a mobile or unlisted number usually returns only carrier/region and an upsell to a paid partner.
4. Don't pay the partner upsell reflexively — note the free result and pivot.
5. Pivot: cross-check the same number on `[[allareacodes]]` and `[[thatsthem-phone-search]]`, and feed a returned name/address into `[[white-pages]]` or people-search tools.

## Inputs → Outputs
- **In:** `phone` (best for landlines) or `name` (+ location)
- **Out:** listed `name`, `address`, and associated `phone`
- **Empty/negative result looks like:** "no results" or only carrier/city with a "get full report" upsell — common for cell/unlisted numbers; absence here is not proof, just that the number isn't in the free white-pages set.

## Gotchas & OpSec
- Free data skews to landlines and can be years out of date; mobiles rarely resolve to a name for free.
- Heavy advertising and repeated prompts to buy a "full report" from paid partners — treat those as upsells, not new evidence.
- OpSec: passive; the subject isn't alerted, but your query and any purchase are logged by AnyWho/PeopleConnect. Use a sock puppet.

## Overlaps ("do both")
- Pairs with `[[allareacodes]]` and `[[thatsthem-phone-search]]` — each has different white-pages coverage; run the number through all three and reconcile.
- Feed name/address hits into `[[white-pages]]` for a broader people-search view.

## Trust & verifiability
`trust: community` — an established directory sourced from public phone-book records, but aggregated and sometimes stale. Treat a hit as a lead to corroborate (especially the address's currency) rather than confirmed present-day fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | white-pages-people-finder-anywho |
| category | phone |
| selectorsIn → selectorsOut | phone, name → name, address, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
