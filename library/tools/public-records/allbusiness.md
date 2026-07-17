---
id: allbusiness
name: AllBusiness
description: Use when you have an `employer-org` or `name` and want a US business directory profile — returns `employer-org`, `address`, and business-context leads.
url: https://www.allbusiness.com
category: public-records
path:
- public-records
bestFor: Looking up a company's directory profile and small-business context alongside a large library of business news and guides.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free to read articles and browse the business directory; no account required.
opsec: passive
opsecNote: Reading a public directory/news site is passive and leaks nothing to any subject. Standard web-tracking applies; a clean browser is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial business-content site with a self-listed company directory; directory entries are largely self-submitted, so treat them as leads, not verified records.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- allbusiness.com
tags:
- toddington
- curated-directory
- company-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# AllBusiness

> A US small-business content site whose company directory and profiles give a light, free first pass on an employer — best paired with an authoritative register for anything you'll rely on.

## When to use
You have a company `employer-org` (or a `name` you're trying to tie to a business) and want a quick, free directory read: a company profile, category, and any listed contact/`address` details, plus surrounding business context. Useful early in employer research to confirm a company exists and gather leads, before moving to a state Secretary of State or a paid corporate database for authoritative filings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.allbusiness.com and go to the "Business Directory" section.
2. Search the company name (or browse by category); open the company profile.
3. Read the profile for listed `address`, contacts, category, and description; use the site search for any articles mentioning the company or person.
4. Pivot: confirm the entity and officers against a state business register; feed an address into mapping/records and a person's name into people-search.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` (directory profile), `address` and contact leads, plus business-context articles.
- **Empty/negative result looks like:** no directory entry — the business never self-listed here (very common); fall back to a Secretary of State register or a broader company-search tool.

## Gotchas & OpSec
- Directory listings are largely self-submitted and can be stale or promotional — corroborate the address/entity against an official register before trusting it.
- Coverage skews US small-business; large or non-US entities may be absent.
- OpSec: passive public browsing; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with an authoritative company register — AllBusiness gives a fast, free lead and context; the register gives the legal entity, officers, and filing history to confirm it.

## Trust & verifiability
`trust: community` — a commercial content site with a self-serve directory; profiles are unverified user/business submissions, so use them as starting points and confirm elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | allbusiness |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
