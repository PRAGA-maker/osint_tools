---
id: ratemyemployer-canada
name: RateMyEmployer (Canada)
description: Use when you have an `employer-org` in Canada and want employee reviews and context — returns workplace ratings, location/industry and reviewer-disclosed detail about the company.
url: http://www.ratemyemployer.ca/
category: search-engines
path:
- search-engines
bestFor: Reading Canadian employee reviews of a company to understand a workplace, its locations and its industry.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free to browse and search reviews; no account required to read.
opsec: passive
opsecNote: Browsing published reviews of a company transmits nothing about your subject. Fully passive. Do not post a review or register from an investigative machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: User-generated employer reviews (~10k companies, ~36k ratings); anonymous and unverified, subject to bias and fake entries. Treat as sentiment/leads, not fact.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- RateMyEmployer.ca
- ratemyemployer canada
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# RateMyEmployer (Canada)

> A Canadian employer-review site — Glassdoor-style anonymous ratings of workplaces, useful for context on a company a subject is tied to.

## When to use
You have identified an `employer-org` connected to your subject (from a resume, LinkedIn, or a document) and want a feel for that workplace: where its offices are, its industry, and what employees say about it. Occasionally a review discloses a location, a department, or a detail that corroborates or extends what you already know about the company — and by extension the person's likely work location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ratemyemployer.ca/ and search the company name, or browse by province / industry category.
2. Open the employer page to read the aggregate score and individual reviews; note stated locations, departments, and industry classification.
3. Scan reviews for concrete, verifiable detail (office city, size, business lines) — ignore purely subjective sentiment for factual purposes.
4. Corroborate the company's existence/details against a business registry or the company's own site.
5. Pivot: a confirmed office location narrows a subject's likely work city; industry/size detail feeds business-registry and LinkedIn searches.

## Inputs → Outputs
- **In:** `employer-org` (company name)
- **Out:** `employer-org` context (industry, size), `address` (office locations disclosed in reviews), employee sentiment
- **Empty/negative result looks like:** the company is not listed, or has only a handful of reviews — coverage is limited to ~10k mostly larger Canadian employers; small firms are usually absent.

## Gotchas & OpSec
- Reviews are anonymous, unverified, and can be biased, promotional, or fake in both directions — never treat a single review as fact.
- Canada-only and skewed to larger employers; a small or foreign employer likely won't appear.
- Fully passive: reading reviews leaks nothing. Do not register or post from an investigative identity.

## Overlaps ("do both")
- Pairs with a Canadian business registry and LinkedIn company pages — those give the authoritative corporate record and current staff, while this adds unofficial insider sentiment and occasional location detail.

## Trust & verifiability
`trust: unverified` — crowd-sourced anonymous reviews with no vetting; use for leads and sentiment only, and confirm any factual detail against a primary corporate source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ratemyemployer-canada |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → employer-org, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
