---
id: creditrisk-monitor
name: CreditRiskMonitor Directory
description: Use when you have a company `name`/`employer-org` and want a public-company profile — a free worldwide directory of listed firms by country, industry and active/inactive status.
url: https://www.crmz.com/Directory
category: public-records
path:
- public-records
bestFor: Confirming a public company exists and browsing peers by country/industry; deep credit-risk data is paid.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: freemium
costNote: The public-company directory (browse by country/state/SIC industry, active vs inactive) is free; CreditRiskMonitor's actual financial-risk reports and ratings require a paid subscription.
opsec: passive
opsecNote: Read-only browsing of a public directory; nothing is attributed to your subject and no login is needed for the directory. It covers public (listed) companies only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: CreditRiskMonitor is an established commercial credit-research firm (crmz.com). The free directory is a straightforward index of public companies; the value-add risk analytics are the paid product.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CreditRiskMonitor
- crmz.com directory
tags:
- toddington
- curated-directory
- company-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# CreditRiskMonitor Directory

> CreditRiskMonitor's free worldwide directory of public companies — browse listed firms by country, US state and industry (SIC) to confirm an `employer-org` exists and find its peers.

## When to use
You have a company `name`/`employer-org` a subject claims to work for or own and want to confirm it is a real publicly-traded company and see its basic classification and location. The directory indexes tens of thousands of active and inactive public companies by country (e.g. ~14,000 active US firms), US state and industry code — good for validating a corporate affiliation before digging deeper. The detailed financial-risk analytics CreditRiskMonitor sells are separate and paid; the free directory is the OSINT-useful part.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.crmz.com/Directory (redirects to CreditRiskMonitor's info directory).
2. Drill down by country/US state, or by SIC industry (2/3/4-digit), or search the company name.
3. Read the company entry — official `employer-org` name, industry classification, country/location (`address`), and active vs inactive status.
4. Treat "inactive" as a lead that the company was delisted/dissolved; verify timing elsewhere.
5. Pivot: a confirmed public company feeds SEC/registry filings, [[nonprofit-explorer]] (for non-profits), and officer lookups; the location feeds address checks.

## Inputs → Outputs
- **In:** `name` / `employer-org` (a company)
- **Out:** `employer-org` (official name, industry), `address` (country/state), active/inactive status
- **Empty/negative result looks like:** no match — the company may be private (not covered here), too small, or named differently. Absence only rules out a *public-company* listing, not the company's existence.

## Gotchas & OpSec
- Human-in-the-loop: none for the directory; the risk reports/ratings are paywalled.
- OpSec: **passive**; browsing notifies no one.
- Coverage is public/listed companies only — private firms, sole traders and non-profits won't appear; use company registries or [[nonprofit-explorer]] for those.

## Overlaps ("do both")
- Pairs with national company registries and [[nonprofit-explorer]] — this covers listed public companies; those cover private entities and non-profits.

## Trust & verifiability
`trust: community` — an established commercial credit-research firm; the free directory is a reliable index of public companies, though the substantive risk analytics sit behind its paid subscription.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | creditrisk-monitor |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
