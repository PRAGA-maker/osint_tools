---
id: sec-gov-edgar
name: SEC.gov - EDGAR
description: Use when you have a `name` or `employer-org` and want US securities filings tying a person to a public company as officer, director or major shareholder — returns employer-org, address and associate leads.
url: https://www.sec.gov/cgi-bin/browse-edgar
category: public-records
path:
- public-records
- general-info-and-news
bestFor: Finding a person's ties to US public companies via SEC filings — insider roles, ownership stakes, and signatures.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free official SEC database; no account or payment. Full-text search and a public API (EDGAR full-text / data.sec.gov) are also free.
opsec: passive
opsecNote: A US government public database; searching does not notify anyone and reveals nothing about you to the subject. All data here is legally public filing information.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US Securities and Exchange Commission; filings are the authoritative primary source, submitted under legal penalty for falsehood.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- EDGAR
- SEC EDGAR
- SEC full-text search
tags:
- corporate
- securities
- filings
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- edgar
- sec-company-search
- sec-gov
- us-securities-and-exchange-commission
- edgar-u-s-securities-and-exchange-commission-filings
---

# SEC.gov - EDGAR

> The SEC's filing database: search a person or company and read the authoritative US securities filings — 10-Ks, proxy statements, and insider Forms 3/4/5 — that connect people to public companies.

## When to use
Your subject may be an officer, director, major shareholder, or signatory of a US public company (or a fund). EDGAR ties a `name` to an `employer-org` through filings: proxy statements list executives and directors with compensation and sometimes addresses; insider Forms 3/4/5 show who holds/trades a company's stock; and any filing's signature block and exhibits can name `associate`s and business relationships. Strong for corporate/financial-angle investigations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Company path: use the company search at https://www.sec.gov/cgi-bin/browse-edgar to find a firm by name/ticker/CIK, then browse its filings (proxy DEF 14A for people, 10-K for the business).
2. Person path: use EDGAR **full-text search** (https://efts.sec.gov/LATEST/search-index?q=) — search the person's name in quotes to find every filing mentioning them.
3. Insider path: search a person in the "insider transactions" view to pull their Forms 3/4/5 across companies.
4. Read the document: names, titles, ownership, addresses, and related parties.
5. Pivot: `employer-org` → corporate registries; co-signers/directors → `associate`s; disclosed address → location lead; for automation use the `data.sec.gov` JSON API.

## Inputs → Outputs
- **In:** `name`, company/`employer-org`, ticker, or CIK
- **Out:** filings revealing `employer-org` ties, roles, ownership, `associate`s, and occasionally an `address`.
- **Empty/negative result looks like:** no filings for the name — the person isn't (and wasn't) an insider/filer of a US-registered issuer; that's a meaningful negative, not a tool error.

## Gotchas & OpSec
- Covers only US SEC registrants — private companies and non-US firms mostly won't appear.
- Common-name collisions: confirm identity via the associated company/CIK, not the name alone.
- Filings can be historical; a role listed may have ended — check filing dates.

## Overlaps ("do both")
- Pairs with `[[sec-company-search]]` and corporate registries (OpenCorporates, Companies House) — EDGAR gives the authoritative US securities filings, registries add incorporation/officer data across jurisdictions.

## Trust & verifiability
`trust: trusted` — a US government primary source; filings are legally binding disclosures, so the data is authoritative (mind only date-staleness and name ambiguity).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sec-gov-edgar |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
