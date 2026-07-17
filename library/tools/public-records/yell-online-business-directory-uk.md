---
id: yell-online-business-directory-uk
name: Yell Online Business Directory (UK)
description: Use when you have a UK business `name`/`employer-org` (or a trade + area) and want its contact details — returns `address`, `phone`, website, and category.
url: https://www.yell.com
category: public-records
path:
- public-records
bestFor: Finding a UK business's address, phone, and website, or identifying tradespeople/firms by trade and area.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- phone
status: live
pricing: free
costNote: Free to search and view business listings (Yell is the online successor to the UK Yellow Pages). Businesses pay for enhanced/advertised placement, but searching is free to the public.
opsec: passive
opsecNote: You search a public business directory, not the business owner. No subject-side footprint unless you use a "contact this business" form — avoid that on a target. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A legitimate, well-known UK directory; listings are business-submitted and advertising-driven, so details are usually current but not authoritative — confirm against Companies House or the firm's own site.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- scoot
- companies-and-orgs-search-engine
aliases:
- Yell
- Yell.com
- Yellow Pages UK
tags:
- toddington
- company-search
- uk-business
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Yell Online Business Directory (UK)

> The online UK Yellow Pages: turn a business name (or a trade + location) into its address, phone, website, and category — a quick contact-details and small-trader lookup.

## When to use
Your subject runs or works at a UK business, or a lead references a trade name/sole trader you need to place. Yell resolves an `employer-org`/`name` to a listing with `address`, `phone`, website, opening hours, and category — and, searching by trade + area, surfaces small operators (builders, cleaners, taxi firms) who never appear in formal company registers. Useful for confirming a business exists, getting a contact address, or identifying a self-employed tradesperson.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.yell.com and search by business name, or by trade/keyword plus a town/postcode.
2. Open the listing: business name, address, phone, website, category, reviews, and sometimes photos/hours.
3. For sole traders, use the address/phone as a person-linking lead (a home-based business often lists a residential area).
4. Cross-check the entity against Companies House (for limited companies) or the firm's own site — Yell is self-submitted advertising data.
5. Pivot: the website feeds domain/WHOIS; the address feeds property/people search; the phone feeds phone OSINT.

## Inputs → Outputs
- **In:** `employer-org`/`name`, or a trade + UK location
- **Out:** `employer-org`, `address`, `phone`, website, category
- **Empty/negative result looks like:** no listing — the business isn't advertised on Yell (many aren't), has closed, or trades under another name; absence is not proof it doesn't exist. Check Companies House and general search.

## Gotchas & OpSec
- Advertising-driven: listings are business-submitted and ranking reflects paid placement, not authority — details can be stale or promotional.
- UK-only, business-only: not a person directory; it links to people only via the businesses they run.
- Confirm elsewhere: verify a limited company via Companies House and a sole trader's address via a second source before relying on it.
- OpSec: passive; don't use the contact form on a target.

## Overlaps ("do both")
- Pairs with `[[scoot]]` (another UK business directory) and `[[companies-and-orgs-search-engine]]` — cross-check listings across directories, and go to Companies House for the authoritative registration behind a limited company.

## Trust & verifiability
`trust: unverified` — a reputable directory but built on self-submitted, advertising-funded listings; treat contact details as good leads and confirm the underlying entity against authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yell-online-business-directory-uk |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, phone |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
