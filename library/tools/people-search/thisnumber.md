---
id: thisnumber
name: ThisNumber
description: Use when you have a `name` or `phone` in a specific country and need that country's phone directory — a gateway to national white/yellow-pages that return `name`, `address`, and `phone`.
url: https://sur.ly/o/numberway.com/AA000014
category: people-search
path:
- people-search
bestFor: Finding the right national telephone directory (white/yellow pages) for a given country, then searching it.
selectorsIn:
- name
- phone
selectorsOut:
- name
- address
- phone
status: degraded
pricing: free
costNote: Free directory-of-directories; it routes you to national phone books (each with its own free/paid model). The listed URL is a redirect wrapper — availability of the underlying portal varies.
opsec: passive
opsecNote: Browsing a list of directories is passive. OpSec exposure begins on the destination national directory, where a query may be logged — apply that site's precautions there.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A curated portal linking to national phone directories worldwide; it holds no data itself and destination quality/coverage varies widely by country.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- numberway
- phone-book-of-the-world
- infobel
aliases:
- ThisNumber
- thisnumber.com
tags:
- bellingcat-toolkit
- people
- phone-directory
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
---

# ThisNumber

> A directory-of-directories for phones — pick a country and it points you to that nation's white/yellow-pages, so you search the right local phone book instead of a US-centric one.

## When to use
Your subject is abroad and you have a `name` or `phone` number in a specific country. Rather than guessing which national directory to use, ThisNumber indexes phone books by country, routing you to the local white/yellow-pages that can return a `name`, `address`, and `phone`. It's a navigation aid — the actual lookup happens on the destination directory.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the portal and browse to the subject's country.
2. Follow the link to that country's white-pages / yellow-pages / directory-enquiries service.
3. On the destination, search by `name` (people) or `phone` (reverse lookup) per that site's interface/language.
4. Read the local result: listed `name`, `address`, `phone`.
5. Pivot: cross-check the same details on `[[numberway]]`, `[[phone-book-of-the-world]]`, or `[[infobel]]`, which also aggregate international directories.

## Inputs → Outputs
- **In:** `name` or `phone` + the target country
- **Out:** (via the destination directory) listed `name`, `address`, `phone`
- **Empty/negative result looks like:** the country has thin/no online directory, or the destination returns nothing — coverage varies enormously by country, and many mobiles aren't listed anywhere.

## Gotchas & OpSec
- Holds **no data itself** — it only routes you; judge coverage/reliability on the destination directory.
- The listed URL is a redirect wrapper; if it's down, reach the same national directories via `[[numberway]]` or `[[phone-book-of-the-world]]`.
- Destination sites are often non-English — expect localized interfaces.
- OpSec: passive at the portal; adopt the destination's precautions once you search there.

## Overlaps ("do both")
- Overlaps with `[[numberway]]`, `[[phone-book-of-the-world]]`, and `[[infobel]]` — all aggregate international directories; use several since each links a different set of national phone books.

## Trust & verifiability
`trust: community` — a useful curated gateway, but only an index. The reliability of any number/name is a property of the destination national directory, judged separately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thisnumber |
| category | people-search |
| selectorsIn → selectorsOut | name, phone → name, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
