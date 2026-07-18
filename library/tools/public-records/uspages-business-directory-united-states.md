---
id: uspages-business-directory-united-states
name: USPages Business Directory (United States)
description: Use when you have an `employer-org` or `name` and want a US business listing — returns company address, category, and contact details.
url: http://www.uspages.com/businessdirectory.htm
category: public-records
path:
- public-records
bestFor: Looking up a US company's category, address, and contact details in a general business directory.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free to browse and search; ad-supported directory, no account needed.
opsec: passive
opsecNote: Passive — you query a public web directory; no business or person is notified. No login, so nothing ties the lookup to you beyond your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A general-purpose commercial business directory of uncertain provenance and freshness; listings are self-submitted/aggregated and not authoritative registration records.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- corporationwiki
- opencorporates
aliases:
- USPages
- uspages.com
tags:
- toddington
- company-search
- business-directory
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# USPages Business Directory (United States)

> A free, ad-supported US business directory — browse by category or search a company to pull its listing and address.

## When to use
You have an `employer-org` (a company name) or a `name` associated with a business and want a quick directory listing: category, location/`address`, and any published contact details. In an investigation this is a lightweight, corroborating lookup — useful to confirm a business exists, locate its address, or find its industry classification — rather than an authoritative source. It complements official registry tools, which carry the legal ownership data this directory lacks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.uspages.com/businessdirectory.htm.
2. Search by company name or browse the industry-category tree.
3. Open a listing to read the business's `address`, category, and any listed phone/website.
4. Cross-check the address/category against a mapping tool and an official registry.
5. Pivot: a confirmed business address feeds people-search and property tools; the company name feeds corporate-registry tools for officers/ownership.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` (matched business), `address` and category/contact details
- **Empty/negative result looks like:** no matching listing — the business may simply not be indexed here (coverage is partial and skewed to businesses that submitted listings), not that it doesn't exist.

## Gotchas & OpSec
- Listings are self-submitted/aggregated with no verification; expect stale addresses, defunct businesses, and gaps.
- Not a legal record — it says nothing authoritative about ownership, registration status, or officers.
- General directories like this overlap heavily; if you get nothing, try another directory or go straight to the state registry.
- OpSec: passive; no notification to the business.

## Overlaps ("do both")
- Pairs with `[[corporationwiki]]` and `[[opencorporates]]` — those carry officer/ownership and registration data from official filings, while USPages is just a quick address/category directory; use the registry tools to establish facts.

## Trust & verifiability
`trust: unverified` — a commercial, self-submission directory; treat every listing as an unconfirmed lead to be verified against an authoritative registry or direct contact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uspages-business-directory-united-states |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
