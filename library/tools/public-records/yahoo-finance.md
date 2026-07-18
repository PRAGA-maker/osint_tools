---
id: yahoo-finance
name: Yahoo Finance
description: Use when you have a company `name`/ticker or an `employer-org` and want its corporate profile — returns HQ `address`, key executives (`name`), sector and filings/news links.
url: https://finance.yahoo.com/
category: public-records
path:
- public-records
bestFor: Pulling a public company's profile — HQ address, executives, sector, and news — from a name or ticker.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free to browse company profiles, quotes and news; a paid tier adds premium research not needed for OSINT profiling.
opsec: passive
opsecNote: Reading a public company profile is passive and unseen by anyone. Nothing about your subject is submitted; standard site logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Yahoo Finance aggregates market data and company-supplied profiles; core facts (HQ, executives, ticker) are reliable for public companies, while it holds little/nothing on private firms or individuals.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- finance.yahoo.com
- Yahoo! Finance
tags:
- toddington
- curated-directory
- company-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Yahoo Finance

> A fast, free window into public-company data — HQ address, executive roster, sector and news for any listed firm, from a name or ticker.

## When to use
Your subject is tied to a **publicly-traded company** — as an executive, employee, director, or the company itself is of interest — and you want its corporate profile. Yahoo Finance's Profile tab lists the **HQ address**, **key executives** (names, titles, sometimes ages/pay), sector/industry, employee count, and website, plus filings and news. Use it to confirm an `employer-org`, find named executives to pivot on, or place a company geographically. It's strongest for public companies and thin on private firms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://finance.yahoo.com/ and search the company `name` or ticker.
2. Open the quote page and the **Profile** tab: read the HQ `address`, website, sector/industry, employee count, and the **Key Executives** table (names + titles).
3. Check the **News** and **SEC filings** links for recent events and primary documents.
4. Pivot: named executives feed people-search and professional-network tools; the HQ address feeds mapping and business-registry work; the ticker feeds regulator filings (SEC EDGAR etc.).

## Inputs → Outputs
- **In:** company `name`/ticker or `employer-org`
- **Out:** `employer-org` profile, HQ `address`, executive `name`s/titles, sector, filings/news links
- **Empty/negative result looks like:** no match or only a quote with no profile — the company is private, delisted, foreign-listed under another ticker, or too small to be covered. Yahoo Finance won't help for private companies or for looking up an individual directly.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — public data; no one is alerted.
- **Public companies only** in practice — private firms and individuals are largely absent; use business registries and people-search for those.
- Executive lists and profiles can lag reorganisations; verify a named officer against the company's own filings/site.

## Overlaps ("do both")
- Do both with official regulator filings (SEC EDGAR / Companies House) for authoritative, dated records, and with business-registry tools — Yahoo Finance is the quick overview, the registries are the primary source.

## Trust & verifiability
`trust: community` — an aggregator with reliable core data for public companies (verify officers/HQ against filings); it asserts little about private entities or people, so don't infer absence of a person from a blank here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yahoo-finance |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
