---
id: public-register-online
name: Public Register Online
description: Use when you have a company name and want its published annual reports — returns employer-org financial/annual reports to read directors, addresses, and performance.
url: https://www.annualreportservice.com/
category: public-records
path:
- public-records
- annual-reports
bestFor: Finding and requesting/downloading participating public companies' annual reports in one place.
input: Company name
output: Annual report listings with request or download links
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free to browse and request annual reports; funded by participating companies/advertising rather than user fees.
opsec: passive
opsecNote: Browsing and requesting reports goes through the service; the target company is not directly contacted by you. If you request a mailed hard copy you'd supply a delivery address — use a non-attributable one, or just take the digital/download option.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing annual-report aggregation service; the reports themselves are the companies' own published filings.
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
- annualreportservice.com
- Annual Report Service
tags:
- public-records
- annual-reports
- company-research
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Public Register Online

> A one-stop aggregator of participating public companies' annual reports — read a firm's own financial narrative, board, and registered address without hunting each investor-relations site.

## When to use
You have an `employer-org` (a public company) and want its annual reports for corporate intelligence: the board and officers (`associate` links to named people), the registered/HQ `address`, financial performance, and business narrative. Faster than tracking down each company's IR page, and useful for building a picture of a firm a subject runs, works for, or is invested in.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.annualreportservice.com/ and search the company name (or browse by industry/exchange).
2. Open the company entry to see available annual reports; choose the digital/download option (or request a hard copy).
3. Read the report: directors and executives, registered/head-office address, financial statements, and the narrative sections.
4. Pivot: named directors/officers are `associate` leads for people searches; the registered address and subsidiaries feed corporate-registry cross-checks; financials contextualise the subject's finances.

## Inputs → Outputs
- **In:** `employer-org` (public company name)
- **Out:** `employer-org` (annual reports/financials), `address` (registered/HQ), `associate` (named directors/officers)
- **Empty/negative result looks like:** company not listed / no report available — private companies and small firms won't be here, and not every public company participates; use the company's own IR site or a securities regulator's filings instead.

## Gotchas & OpSec
- Human-in-the-loop: none for digital reports; a mailed hard-copy request would need a delivery address.
- OpSec: passive — the company isn't directly contacted by you. Prefer the download option; if requesting a physical copy, don't use an attributable address.
- Coverage is limited to participating public companies; for authoritative filings use the relevant regulator (SEC EDGAR, Companies House, etc.).

## Overlaps ("do both")
- Pairs with SEC EDGAR / Companies House and `[[crunchbase]]` — this gives the company's own polished annual reports, while regulators give the raw statutory filings and aggregators add funding/leadership context.

## Trust & verifiability
`trust: community` — a useful aggregator, but the authoritative source is the company's regulator filing; verify figures and board details against official filings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | public-register-online |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
