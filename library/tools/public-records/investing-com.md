---
id: investing-com
name: Investing.com
description: Use when you have a public company or ticker and want its profile — returns business description, key executives, financials and filings context for a company tied to your subject.
url: https://www.investing.com/
category: public-records
path:
- public-records
bestFor: Pulling a publicly-traded company's profile, executives and financials to corroborate a subject's corporate links.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free to view quotes, company profiles and news; an ad-free "Pro"/premium tier and some data are paid, but the company-profile and executives info is free.
opsec: passive
opsecNote: Reading public market data is passive and reveals nothing about your target. The site sets ad/analytics cookies and nags for account creation; use a clean browser profile and you never need to log in for the profile pages.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Large commercial financial-data portal (Investing.com); good for a quick public-company overview, but a third-party aggregator — verify anything evidential against primary filings (SEC/registry).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- investing.com
tags:
- Company information search
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Investing.com

> A free financial-data portal used in OSINT to profile a publicly-traded company — its business, executives and numbers — when your subject links to a listed firm.

## When to use
Your subject is connected to a **publicly-traded** company (as an executive, board member, employee, investor, or counterparty) and you want a fast overview: what the company does, who its named executives are, its ticker/exchange, financial summaries, and recent news. It's a quick corroboration layer — confirm a claimed employer is a real listed entity, surface the exec team a person might belong to, and get news that dates a person's association. It covers listed companies, not private individuals or small private firms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.investing.com/ and search the company name or ticker (`employer-org`).
2. Open the equity's page and the **Company Profile** tab: read the business description, sector, exchange, and the **key executives / management** list.
3. Check the news and financials tabs to date the subject's likely association and spot related parties.
4. Pivot: named executives (`associate`) → people-search and cross-registry checks; the confirmed ticker/entity → primary filings (SEC EDGAR / national registry) and `[[opencorporates]]`-style lookups for authoritative officer data.

## Inputs → Outputs
- **In:** `employer-org` (company name or ticker)
- **Out:** company profile, sector/exchange, `associate` (listed executives/management), financials and news context
- **Empty/negative result looks like:** no matching listed company — the firm is private, delisted, or too small to be covered here; use company registries, `[[opencorporates]]`, or filings databases instead.

## Gotchas & OpSec
- Human-in-the-loop: none; you can read profiles without an account (dismiss the sign-up prompts).
- OpSec: passive — no target lookup is performed; only your own browsing is logged.
- Aggregated data can lag or omit; executive lists show current management, not historical officers — go to primary filings for evidential detail.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` and SEC/registry filings — Investing.com is fast for a public-company snapshot and current execs, while registries/filings give authoritative, historical officer and ownership records.

## Trust & verifiability
`trust: community` — a commercial aggregator, reliable for a quick overview but not a primary source; corroborate any name, role, or figure against official filings before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | investing-com |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
