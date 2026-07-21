---
id: international-white-pages
name: International White Pages (WAYP)
description: Use when you have a `name`/`phone` in a specific country and want directory listings — returns `address` and `phone` from national white/yellow-pages directories worldwide.
url: https://www.wayp.com/
category: public-records
path:
- public-records
- general-info-and-news
bestFor: A gateway/directory to national telephone directories worldwide for personal and business contact lookups by country.
selectorsIn:
- name
- phone
selectorsOut:
- address
- phone
status: degraded
pricing: free
costNote: Free to use; it mainly routes you to each country's own directory service, some of which may have their own limits or fees.
opsec: passive
opsecNote: Passive — you query directory listings, with no contact to the listed person. Queries go through WAYP and the linked national directories under your IP; use research infrastructure. Directory results are public listings, so there is no subject-alerting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: WAYP (World Area Yellow Pages) is a long-standing directory aggregator; coverage and freshness vary widely by country and it links to third-party national directories of mixed quality — treat listings as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- WAYP
- World Area Yellow Pages
- wayp.com
tags:
- phone-directory
- white-pages
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# International White Pages (WAYP)

> A country-by-country gateway to the world's telephone directories — the starting point when a `name` or `phone` lead sits in a country whose national white/yellow pages you don't know.

## When to use
You have a `name` or `phone` for someone in a specific country and want a landline/business directory listing (`address`, `phone`). WAYP is most useful for its **country index**: it points you to each nation's own white/yellow-pages service, which is often the authoritative local directory. Best for landlines, businesses, and older listings; weak for mobiles and people who avoid directories.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.wayp.com/ and pick the target country from the continent/country index.
2. Follow through to that country's directory and search the `name`/business, or reverse-search the `phone`.
3. Read the listing — `address`, `phone`, sometimes email/business detail.
4. Repeat across neighbouring countries if the subject may have relocated.
5. Pivot: an `address` → local property/records and mapping; a business listing → company records.

## Inputs → Outputs
- **In:** `name` / business name / `phone`, plus the country
- **Out:** directory listing(s) — `address`, `phone`, occasionally email
- **Empty/negative result looks like:** no listing — extremely common for mobiles, ex-directory numbers, and younger people; absence tells you little. Coverage and data age vary hugely by country.

## Gotchas & OpSec
- It is largely a **link hub** to national directories; quality/freshness depends entirely on each country's service.
- Skewed toward landlines and businesses; mobile and unlisted numbers won't appear.
- Fully passive; no login.

## Overlaps ("do both")
- Complements country-specific people-search and reverse-phone tools — WAYP finds *which* national directory to use; those give deeper or fresher results within one country.

## Trust & verifiability
`trust: community` — a useful directory aggregator, but non-authoritative and uneven; verify any listing against the national directory it links to and a second source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-white-pages |
| category | public-records |
| selectorsIn → selectorsOut | name, phone → address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
