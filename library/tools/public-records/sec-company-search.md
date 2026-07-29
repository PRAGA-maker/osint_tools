---
id: sec-company-search
name: SEC Company Search
description: Use when you have a `name` or `employer-org` and want US securities filings tying a person to a public company — returns `employer-org`, `associate`, and `address` links.
url: https://www.sec.gov/edgar/searchedgar/companysearch.html
category: public-records
path:
- public-records
bestFor: Confirming whether a person is an officer, director, or major shareholder of a US-listed company and pulling their disclosed filings.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Fully free US government service (EDGAR); no account or API key required for the web search.
opsec: passive
opsecNote: You are querying the SEC's public EDGAR database, not the target. Searches are anonymous and leave no trace to the subject; no sock puppet needed, though route through a clean IP if you prefer to keep your investigation off SEC access logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the U.S. Securities and Exchange Commission; EDGAR filings are legally mandated primary-source disclosures.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- edgar
- sec-gov
- sec-gov-edgar
- us-securities-and-exchange-commission
- edgar-u-s-securities-and-exchange-commission-filings
aliases:
- EDGAR company search
- SEC EDGAR
tags:
- corporate
- public-records
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# SEC Company Search

> The front door to EDGAR — search US public-company filings by company name, ticker, or the name of an insider.

## When to use
You have an `employer-org` (a US-listed company) or a person's `name` and want to establish their corporate role, disclosed compensation, share ownership, or connections to other people. Officers, directors, and >10% shareholders must file with the SEC, so a person tied to a public company leaves a durable paper trail of business addresses, co-officers (`associate`), and dated disclosures.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sec.gov/edgar/searchedgar/companysearch.html.
2. To find a company, enter its name or ticker; to find a person, use the full-text search (efts.sec.gov) for filings that mention them by name.
3. Open the entity's filing history and read the relevant forms:
   - **DEF 14A (proxy statement)** — names directors/officers, compensation, and biographical detail.
   - **Forms 3/4/5** — insider ownership and transactions (ties a `name` to a company).
   - **10-K / 8-K** — business `address`, subsidiaries, key personnel.
4. Pivot: officer names feed people-search; a business `address` feeds property/corporate-registry lookups; co-signers on filings are `associate` leads.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` confirmation, `associate` (co-officers/directors), disclosed business `address`
- **Empty/negative result looks like:** "No matching companies/filings" — means no US public-company filing under that name, not that the person has no corporate ties (private companies don't file here).

## Gotchas & OpSec
- Covers **US public companies only** — private firms, foreign issuers, and small businesses are absent; use a state corporate registry for those.
- Full-text search (EFTS) only indexes filings from 2001 onward; older filings need the browse-by-company view.
- Names are self-reported; a common name may collide, so corroborate with the CIK (Central Index Key) number.

## Overlaps ("do both")
- Pairs with `[[edgar]]`, `[[sec-gov-edgar]]`, and `[[edgar-u-s-securities-and-exchange-commission-filings]]` — same underlying database via different entry points; run full-text search alongside this company-name search to catch person mentions the name index misses.

## Trust & verifiability
`trust: trusted` — EDGAR is the SEC's official filing system; the documents are legally required primary sources, so the data is authoritative (subject only to what filers disclosed).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sec-company-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
