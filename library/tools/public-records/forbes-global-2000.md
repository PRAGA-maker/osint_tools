---
id: forbes-global-2000
name: Forbes Global 2000
description: Use when you have an `employer-org` and want to verify and size it — returns whether a company is among the world's 2000 largest public firms, with country, industry and financial rank.
url: https://www.forbes.com/global2000/
category: public-records
path:
- public-records
bestFor: Checking whether a company is a top-2000 global public firm and reading its country, sector and financial ranking.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: The ranked list is free to browse on Forbes.com; no account needed (site may show ads/consent prompts).
opsec: passive
opsecNote: Reading a published ranking is fully passive and anonymous; you query Forbes' public list, not any target, so nothing is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Forbes' well-known annual ranking of the world's largest public companies, compiled from reported financials; authoritative for scale/ranking, updated yearly.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- forbes-com
- forbes-magazine
aliases:
- Global 2000
- Forbes 2000
- world's largest public companies
tags:
- company-research
- rankings
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Forbes Global 2000

> Forbes' annual ranking of the 2,000 largest public companies worldwide — a fast way to confirm a company is a major public firm and read its country, sector and financial scale.

## When to use
You have an `employer-org` a subject claims to work for, own, or deal with, and you want an authoritative, quick sense of whether it's a genuine large public company and how big. Being on (or absent from) the Global 2000, plus the listed headquarters country, industry, sales/profit/assets and rank, helps validate an employer, gauge its scale, and spot inflated claims. It profiles companies, not individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.forbes.com/global2000/ and use the list's search/sort/filter to find the company by name, country or industry.
2. Read the company's row: rank, headquarters country, industry, and the reported financials (sales, profit, assets, market value).
3. If the company isn't listed, note that it's either not a top-2000 public firm, privately held, or named differently — a useful signal against an overstated claim.
4. Pivot: the confirmed country/industry feeds business-registry and company-research tools; the scale calibrates how much public reporting (filings, executives) you can expect to find.

## Inputs → Outputs
- **In:** `employer-org` (company name)
- **Out:** `employer-org` verification and profile — rank, country, industry, headline financials
- **Empty/negative result looks like:** the company isn't in the list — it is not among the world's 2000 largest public companies (private, smaller, subsidiary, or newly renamed); this bounds its size, it doesn't prove the company is fake.

## Gotchas & OpSec
- Human-in-the-loop: none; the list is public (dismiss any cookie/consent prompt).
- The list is annual — figures and membership reflect the latest edition's snapshot, so a company can move or drop between years.
- Only large *public* companies qualify; big private firms and subsidiaries legitimately won't appear, so absence alone doesn't discredit an employer.

## Overlaps ("do both")
- Pairs with `[[forbes-com]]` and national business registries — Global 2000 gives scale and ranking, while a registry confirms legal identity, officers and filings; use the registry to tie the company to named people.

## Trust & verifiability
`trust: trusted` — Forbes compiles the ranking from reported company financials; it's an authoritative measure of scale, though always as of the latest annual edition.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forbes-global-2000 |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
