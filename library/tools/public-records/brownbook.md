---
id: brownbook
name: BrownBook
description: Use when you have a business `name`/`employer-org` and want its listing — returns address, phone, and contact details from a global crowd-sourced business directory.
url: https://www.brownbook.net/
category: public-records
path:
- public-records
bestFor: Looking up a business worldwide in a free, crowd-editable directory for address, phone, and category.
selectorsIn:
- employer-org
- name
selectorsOut:
- address
- phone
- employer-org
status: live
pricing: free
costNote: Free to search and view listings; businesses can claim/edit their own entries for free. No account to browse.
opsec: passive
opsecNote: Searching a public business directory is passive and notifies no one. Because entries are crowd-editable, treat any single listing as an unverified lead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A global, openly crowd-sourced business directory; anyone can add/edit listings, so data quality is uneven — corroborate before relying on a detail.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Brownbook.net
tags:
- company-research
- business-directory
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# BrownBook

> A free, worldwide crowd-sourced business directory — a quick way to pull a company's listed address, phone, and category, and to spot a subject tied to a small business.

## When to use
You have a business `name`/`employer-org` (an employer, a company a subject runs, a name on a document) and want contact and location detail — especially for small businesses that don't appear in formal registries. BrownBook's global, open coverage can surface a phone, address, and category, and sometimes an owner's name, feeding both employer verification and a person's locate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open brownbook.net and search the business `name` (optionally by location/category).
2. Open the listing: registered/listed `address`, `phone`, website, category, and any contact person.
3. Because listings are crowd-editable, cross-check the details against the business's own site or an official registry.
4. Pivot: a listed phone/address feeds reverse-phone and people-search; a named owner feeds people lookups; the business links to a subject's employment.

## Inputs → Outputs
- **In:** business `name`/`employer-org` (+ optional location)
- **Out:** `address`, `phone`, website, category, and sometimes owner/contact for the `employer-org`
- **Empty/negative result looks like:** no listing — the business isn't in BrownBook (common for very small or new firms), or the name/location differs; try other directories.

## Gotchas & OpSec
- Crowd-editable and unverified — entries can be stale, wrong, or self-promotional; corroborate every detail.
- Duplicate/spam listings exist for the same business.
- Coverage is broad but shallow — good for a lead, weak as proof.
- OpSec: passive search.

## Overlaps ("do both")
- Pairs with official company registries and other directories (Yellow Pages-style) — BrownBook gives a fast global lead; a registry confirms the legal entity and officers.

## Trust & verifiability
`trust: community` — open crowd-sourced data; useful for leads and contact points, but verify against an authoritative source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | brownbook |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → address, phone, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
