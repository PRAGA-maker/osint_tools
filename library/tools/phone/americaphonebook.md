---
id: americaphonebook
name: AmericaPhonebook
description: Use when you have a US phone number or a name and want to resolve it to a person's name, address, or listed number — returns name, address, and phone from public directory records.
url: https://www.americaphonebook.com/
category: phone
path:
- phone
bestFor: Free US reverse-phone and name lookups drawing on white-pages / public directory data, including some unlisted numbers.
selectorsIn:
- phone
- name
selectorsOut:
- name
- address
- phone
status: live
pricing: free
costNote: Free directory lookups; some deeper results funnel to partner paid people-search services. No account for the basic search.
opsec: passive
opsecNote: You query a public directory, not the subject — passive. The site links out to data-broker partners; avoid those affiliate flows if you don't want your query monetized, and use a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing US directory aggregator over public/white-pages records; coverage is broad but stale entries are common, so corroborate.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- America Phone Book
- AmericaPhone
tags:
- phone
- directory
- people-search
source: inteltechniques-tools
lastVerified: '2026-07-23'
enrichment: full
---

# AmericaPhonebook

> A free US white-pages/reverse-phone directory — turn a number into a name and address, or a name into a listed number.

## When to use
You have a US `phone` number and want the subscriber `name`/`address` (reverse lookup), or you have a `name` and want a listed `phone`/`address`. It's a fast, free first pass for US contact resolution — useful early in a case to attach a real identity and location to a number. As directory data it's a starting point to corroborate, not a final source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.americaphonebook.com/ and choose **Reverse Phone** (number → identity) or **People Search** (name → listing).
2. Enter the `phone` or `name` (+ state to narrow) and submit.
3. Read the result: listed `name`, `address`, and any associated `phone` numbers.
4. Watch for "results" that are actually paid-partner upsells; take only the free directory data and verify it elsewhere.
5. Pivot: a `name`+`address` → people-search / voter/property records; a confirmed `phone` → carrier/line lookups.

## Inputs → Outputs
- **In:** a US `phone` number, or a `name` (+ state).
- **Out:** `name`, `address`, and listed `phone`(s) from directory records.
- **Empty/negative result looks like:** "no listing found" — common for mobile-only, unlisted, or recently-changed numbers, or a stale entry pointing to an old address; absence isn't proof the number is invalid.

## Gotchas & OpSec
- US-only, and skewed toward landline/white-pages data — mobiles and younger subjects are under-covered.
- Data can be years out of date; treat an address/name as a lead to confirm, not fact.
- The site pushes affiliate data-broker links; stay on the free lookup and don't feed queries into paid partner flows unless intended.

## Overlaps ("do both")
- Pairs with other US people-search/reverse-phone tools: directory coverage varies per source, so a miss here may hit elsewhere — run more than one.

## Trust & verifiability
`trust: community` — an aggregator over public directory data; useful and free, but corroborate any name/address against a second source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | americaphonebook |
