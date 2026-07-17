---
id: us-securities-and-exchange-commission
name: US Securities & Exchange Commission (EDGAR)
description: Use when you have a company or person `name` and want SEC filings naming them — returns officers/insiders, addresses, ownership stakes, and `employer-org` links via EDGAR full-text search.
url: http://www.sec.gov/
category: search-engines
path:
- search-engines
bestFor: Finding a person or company in SEC filings — executives, directors, insiders, and beneficial owners of US public companies.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
- document-id
status: live
pricing: free
costNote: Free US government system (EDGAR); no account, no limits for normal use.
opsec: passive
opsecNote: Searching EDGAR is passive — you query the SEC's public database, nothing reaches any subject. All disclosures are legally public. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US SEC filing system; filings are legally-mandated disclosures signed under penalty of law — authoritative primary-source records.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- SEC EDGAR
- sec.gov
- EDGAR full-text search
tags:
- corporate-records
- filings
- financial-disclosure
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
relatedTools:
- edgar
- edgar-u-s-securities-and-exchange-commission-filings
- sec-company-search
- sec-gov
- sec-gov-edgar
---

# US Securities & Exchange Commission (EDGAR)

> The SEC's EDGAR database: every public-company filing, full-text searchable — a primary source for tying a person to companies as an officer, director, insider, or beneficial owner.

## When to use
You want to connect a `name` or company to US public-company activity: is a subject an executive/director, do they own a reportable stake, what companies are they tied to, and what addresses/associates appear alongside them? EDGAR full-text search scans the actual filings (10-K, 8-K, DEF 14A proxies, Forms 3/4/5 insider transactions, Schedules 13D/G) so a name search surfaces the person's corporate roles, co-officers (`associate`s), business `address`es, and ownership — a rich, authoritative professional footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://efts.sec.gov/LATEST/search-index?q= (EDGAR full-text search) via sec.gov → "Search filings" → "Full-Text Search".
2. Search the person's `name` (in quotes) or a company/`employer-org`; filter by form type and date.
3. Open matching filings: for a person, look at Forms 3/4/5 (insider holdings/trades) and proxy statements (bios, compensation, other directorships); for a company, the 10-K cover and exhibits list officers and addresses.
4. Pivot: co-officers and related entities feed `associate`/company mapping; a CIK number (`document-id`) pins the exact filer; a business address feeds registry/map checks.

## Inputs → Outputs
- **In:** person `name` or `employer-org`.
- **Out:** corporate roles, co-officers (`associate`), business `address`, ownership stakes, filing/CIK identifiers (`document-id`).
- **Empty/negative result looks like:** no filings mention the name — the person isn't tied to a US public company (most people aren't). Absence is not proof of no business activity (private companies don't file here).

## Gotchas & OpSec
- Covers US public companies only — private firms, most small businesses, and non-US entities won't appear.
- Name collisions: common names recur across filers; confirm via CIK, company, and role before attributing.
- Full-text search covers filings from 2001 onward; older filings need the classic EDGAR browse.

## Overlaps ("do both")
- Pair with state business-registry searches (for private companies) and OpenCorporates to complete the corporate picture; feed insider addresses into people-search.

## Trust & verifiability
`trust: trusted` — official primary-source regulatory filings. Highly reliable; the main risk is misattributing a common name, not data quality — always confirm the filer identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-securities-and-exchange-commission |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
