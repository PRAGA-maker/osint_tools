---
id: corporate-information
name: Corporate Information
description: Use when you have a company `name` and want a consolidated financial/company profile — returns employer-org details, address and executive names.
url: http://www.corporateinformation.com
category: public-records
path:
- public-records
bestFor: Pulling a consolidated company profile (financials, address, executives) for a business tied to your subject.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: freemium
costNote: Free company snapshots (profiles across ~46,000 companies worldwide); a free registration and paid research reports unlock deeper financials. Basic profile browsing is free.
opsec: passive
opsecNote: Querying a company-research portal, not the subject — passive, no notification. A free login may be prompted for fuller data; use a sock-puppet email.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Wright Investors' Service (a long-running financial-data firm); company data is compiled from filings/providers — reliable at the profile level, corroborate specifics.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- corporateinformation.com
- Wright Investors Service
tags:
- company-research
- financials
- business-registry
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Corporate Information

> A company-research portal (Wright Investors' Service) with consolidated profiles on tens of thousands of companies worldwide — a quick way to get a business's financial snapshot, address and executives from its name.

## When to use
You have a company `name` (or an `employer-org` tied to your subject) and want a one-page picture: what the company is, where it's based, its financial snapshot, and named executives/officers. Good for corroborating an employer, sizing up a business someone owns or works for, and surfacing executive `name`s to pivot on — especially for larger/public companies across many countries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.corporateinformation.com and search the company `name`.
2. Open the company profile: business description, headquarters `address`, sector, financial snapshot, and executives/officers.
3. For deeper financials you may hit a free-registration or paid-report wall — take the free profile data and note what's gated.
4. Cross-check against official registries (SEC EDGAR for US public companies, OpenCorporates, national registries).
5. Pivot: executive `name`s → people-search and other companies; HQ `address` → location OSINT; ticker/registry ID → EDGAR/registry filings.

## Inputs → Outputs
- **In:** company `name` / `employer-org`
- **Out:** company profile — `employer-org` details, HQ `address`, executive `name`s, financial snapshot
- **Empty/negative result looks like:** no profile or a thin stub — small/private/local companies may be absent (coverage skews to larger and public firms); try a national registry or OpenCorporates instead.

## Gotchas & OpSec
- Coverage favors larger/public companies — small private businesses are often missing.
- Deeper financials sit behind registration/paid reports; the free profile is the OSINT layer.
- Data is compiled from third-party providers — treat as a summary to corroborate against primary filings.
- OpSec: passive; use a sock-puppet email if a login is required.

## Overlaps ("do both")
- Pairs with SEC EDGAR, OpenCorporates and national company registries — Corporate Information gives a fast consolidated snapshot; those give authoritative, primary filings.

## Trust & verifiability
`trust: community` — a long-standing financial-data firm's portal; profile-level data is generally reliable, but confirm specific financials/officers against official registry filings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | corporate-information |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
