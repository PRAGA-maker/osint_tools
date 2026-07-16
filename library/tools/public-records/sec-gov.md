---
id: sec-gov
name: sec.gov (EDGAR)
url: http://www.sec.gov/edgar/searchedgar/companysearch.html
category: public-records
path:
- public-records
description: Use when you have a `name` or `employer-org` and want US securities filings — returns officer/director names, business `address`, company affiliations and `associate` links.
bestFor: Tracing a person through US SEC filings — the companies they run, direct, or hold insider stakes in, plus their business address.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- name
- employer-org
- address
- associate
status: live
pricing: free
costNote: Fully free US government service; no account, no payment, no rate-limit for normal interactive use.
opsec: passive
opsecNote: Passive read of official public filings; the subject is not notified and no login is required. Queries are as anonymous as any web request — clean-browser hygiene is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The US Securities and Exchange Commission's own filing system; documents are legally-mandated primary-source disclosures, so data is authoritative.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- SEC EDGAR
- EDGAR full-text search
tags:
- companysites
- Company Related Sites
- securities-filings
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- edgar
- sec-company-search
- sec-gov-edgar
- us-securities-and-exchange-commission
---

# sec.gov (EDGAR)

> The SEC's EDGAR system — legally-mandated US securities filings, used to tie a person to the public companies they run, direct or hold insider positions in.

## When to use
You have a `name` or `employer-org` tied to US public markets and want authoritative corporate links: who signs the filings, who sits on the board, who owns insider stakes, and the business addresses involved. Strongest when a subject is a company officer, director, or major shareholder — insider forms (3/4/5) name individuals directly, and proxy statements list executives, compensation and related parties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open EDGAR company search (sec.gov/edgar) or the full-text search (efts.sec.gov / "Search EDGAR full text").
2. For a company, enter the `employer-org` to list its filings; for a person, use full-text search on the `name` to find filings that mention them.
3. Open insider forms (3/4/5) and proxy/DEF 14A filings for officer/director names, addresses and holdings.
4. Read the filing for related parties, signatures and business `address`.
5. Pivot: co-signers/directors feed `associate` mapping; a business `address` feeds property/registration searches; company links feed `[[northdata-com]]`/other registries.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or `address`
- **Out:** officer/director/insider `name`s, `employer-org` affiliations, business `address`, `associate` (co-signers, related parties)
- **Empty/negative result looks like:** no filings mention the person/company — very common, since only US-registered public issuers and their insiders file. A miss means "not an SEC-registered entity/insider," not that the person has no business footprint.

## Gotchas & OpSec
- Coverage is US public markets only: private companies and non-US entities are absent.
- Common names collide in full-text search; disambiguate by company, address, or filing role.
- OpSec: fully passive government data — no login, no subject notification.

## Overlaps ("do both")
- Pairs with `[[northdata-com]]` (European registers) and OpenCorporates — EDGAR covers US securities filings, those cover general company registration elsewhere.

## Trust & verifiability
`trust: trusted` — EDGAR is the SEC's primary-source disclosure system, so filings are authoritative; the caveat is scope (US public issuers/insiders only), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sec-gov |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → name, employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
