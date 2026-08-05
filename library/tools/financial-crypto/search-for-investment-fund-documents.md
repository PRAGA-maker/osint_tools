---
id: search-for-investment-fund-documents
name: SEDAR+ Investment Fund Document Search
description: Use when you have a Canadian investment/mutual fund or its manager (`employer-org`) and want its official filings — returns prospectuses, financials and `document-id` from Canada's SEDAR+ system.
url: https://www.sedar.com/search/search_form_mf_en.htm
category: financial-crypto
path:
- financial-crypto
bestFor: Pulling the public regulatory filings of a Canadian investment fund (prospectus, financial statements, fund facts) and identifying the manager behind it.
selectorsIn:
- employer-org
- name
selectorsOut:
- document-id
- employer-org
- associate
status: live
pricing: free
costNote: Free public access. Note the legacy sedar.com form now redirects to SEDAR+ at sedarplus.ca — use the SEDAR+ investment-fund search there.
opsec: passive
opsecNote: You query a public securities regulator's filing database with a fund/company name — no target individual is alerted and nothing about your investigation leaks beyond the query. The site uses bot-protection, so search manually in a normal browser; automated scraping may be blocked.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: SEDAR+ is the official electronic filing system of the Canadian Securities Administrators; documents are authoritative primary-source regulatory filings, not third-party scrapes.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- search-for-company-documents
- xbrl-voluntary-filing-program
aliases:
- SEDAR
- SEDAR+ fund search
- sedarplus.ca investment funds
tags:
- companies-finance
- regulatory-filings
- canada
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# SEDAR+ Investment Fund Document Search

> Canada's official securities-filing system (SEDAR+): search a Canadian investment or mutual fund by name and get its authoritative public filings — prospectuses, fund facts, financial statements — plus the management company behind it.

## When to use
You're investigating a Canadian investment/mutual fund, an asset manager, or a financial product marketed in Canada, and you want the primary-source regulatory record: who manages the fund, its official documents, its filing history. Because filings name the fund manager, trustee, and auditors, this also pivots a fund into the corporate `employer-org`/`associate` entities running it — useful for financial due diligence and network mapping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to SEDAR+ at https://www.sedarplus.ca/ (the legacy https://www.sedar.com/ investment-fund form redirects here).
2. Choose the investment-fund search and enter the fund name or the fund-group/manager `employer-org`.
3. Open the results to read the filed documents (prospectus, fund facts, annual/interim financials, material change reports).
4. Pivot: the prospectus/financials name the manager, trustee, and auditor (`employer-org`, `associate`); take those into a corporate registry and `[[search-for-company-documents]]` for the issuing companies.

## Inputs → Outputs
- **In:** `employer-org` (fund/manager/group name) or `name` (a named fund)
- **Out:** `document-id` (filed documents), `employer-org` (manager/trustee), `associate` (auditors, related entities)
- **Empty/negative result looks like:** no filings for the name — the fund may be non-Canadian (try the US EDGAR or the relevant national regulator), wound up, or filed under a different legal name; try the manager's name instead.

## Gotchas & OpSec
- Canada-only: for US funds use SEC EDGAR, for UK use the FCA register — match the regulator to the fund's jurisdiction.
- The legacy sedar.com system was fully replaced by SEDAR+ (sedarplus.ca) in 2023; always work from SEDAR+ for current and historical filings.
- Bot-protection is in place — search by hand rather than scripting.

## Overlaps ("do both")
- Pairs with `[[search-for-company-documents]]`: this covers the *fund* filings, that covers the *company* (reporting-issuer) filings — together they give the full SEDAR+ picture of an entity.

## Trust & verifiability
`trust: trusted` — SEDAR+ is the CSA's official filing system, so its documents are authoritative primary sources. Verify facts directly in the filed PDFs rather than any summary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-for-investment-fund-documents |
| category | financial-crypto |
| selectorsIn → selectorsOut | employer-org, name → document-id, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
