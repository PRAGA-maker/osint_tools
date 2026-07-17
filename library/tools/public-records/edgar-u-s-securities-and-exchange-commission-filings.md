---
id: edgar-u-s-securities-and-exchange-commission-filings
name: EDGAR (SEC Filings Full-Text Search)
description: Use when you have a `name` or `employer-org` and want SEC filings that mention them — returns officer/insider `name`s, `employer-org` links and `address`es.
url: https://www.sec.gov/edgar/search/
category: public-records
path:
- public-records
bestFor: Full-text searching US securities filings for people (officers, directors, insiders, beneficial owners) and companies.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free official service of the US Securities and Exchange Commission; no account. (The old commercial edgar-online.com reseller is defunct — use SEC.gov directly.)
opsec: passive
opsecNote: You search the SEC's public filing database; no subject is contacted and the filings are legally public records. No login means only the host's standard logs see your query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US SEC; filings are legally mandated primary-source disclosures — the authoritative record for US public companies and their insiders.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- SEC EDGAR
- EDGAR full-text search
- edgar-online
tags:
- company-research
- financial-disclosure
- public-records
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# EDGAR (SEC Filings Full-Text Search)

> The SEC's public database of US securities filings — full-text searchable, so a person's `name` or a `employer-org` can surface the disclosures that tie executives, directors and major shareholders to companies, addresses and each other.

## When to use
You have a `name` or company (`employer-org`) with a plausible link to a US public company, fund, or securities offering, and you want the official paper trail. Filings name officers, directors, insiders (Forms 3/4/5), 10%+ beneficial owners (SC 13D/G), and often list business `address`es and signatures. This turns a name into corporate roles, co-signatories (`associate`s), and company affiliations — strong for due diligence and for locating people connected to business/finance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.sec.gov/edgar/search/ (full-text search covers filings from 2001 on).
2. Enter the person's `name` (in quotes) or the company name; filter by form type (e.g. `4` for insider trades, `SC 13D` for large stakes, `DEF 14A` proxy for exec bios).
3. Open a hit and read the document: signatory names, titles, business address, related entities and dates.
4. For a company's full history, use the company/CIK browse (`https://www.sec.gov/cgi-bin/browse-edgar`); for automation, EDGAR offers structured APIs/data.
5. Pivot: feed insider `name`s into people search, related `employer-org`s into company registries, and addresses into address lookups.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` affiliations, co-filer/officer `associate` `name`s, business `address`es, roles and dates
- **Empty/negative result looks like:** no filings — the person/company has no US SEC disclosure obligation (most private individuals and private companies don't). Absence says nothing about non-public activity; full-text search also predates 2001 poorly.

## Gotchas & OpSec
- OpSec: **passive** — legally public records; nothing reaches the subject.
- US securities filings only — private companies, non-US entities and ordinary individuals usually don't appear.
- Full-text search starts ~2001; older filings need the company/CIK browse. Common names need a form/company filter to disambiguate.

## Overlaps ("do both")
- Pairs with company registries (Companies House, OpenCorporates) and `[[every-politician]]`-style people databases — EDGAR is authoritative for US securities disclosures; registries cover the broader corporate picture.

## Trust & verifiability
`trust: trusted` — a first-party US government system of legally mandated disclosures; every result is a citable primary document filed under penalty of law.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | edgar-u-s-securities-and-exchange-commission-filings |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
