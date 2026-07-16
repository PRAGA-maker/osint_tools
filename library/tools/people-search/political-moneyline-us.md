---
id: political-moneyline-us
name: Political MoneyLine (CQ)
description: Use when you have a `name` and want US political-donation and lobbying records tied to that person — returns the donor's home address, employer-org, occupation, and associate links from contribution filings.
url: https://www.politicalmoneyline.com
category: people-search
path:
- people-search
bestFor: Pulling a US individual's federal campaign-contribution and lobbying history — including the home address and employer disclosed on donation filings.
selectorsIn:
- name
selectorsOut:
- address
- employer-org
- associate
status: degraded
pricing: freemium
costNote: The Political MoneyLine brand is now CQ "Capitol Hill Access" under FiscalNote — a paid subscription with no meaningful free public search. The SAME underlying data (FEC filings) is free at FEC.gov and OpenSecrets; use those unless you already have CQ access.
opsec: passive
opsecNote: Querying campaign-finance filings is passive and leaves no trace against the subject — this is disclosed public record. No sock puppet needed for the data itself; if logging into a CQ subscription, use investigative-context credentials.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running campaign-finance tracker (FECInfo → PoliticalMoneyLine → CQ MoneyLine), now part of CQ Roll Call / FiscalNote; data is sourced from FEC/IRS/House/Senate filings and is reliable, but the standalone free product is effectively gone.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- opensecrets-org
- fec-gov
- politicalmoneyline
aliases:
- PoliticalMoneyLine
- CQ MoneyLine
- Capitol Hill Access
tags:
- people-search
- campaign-finance
- lobbying
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Political MoneyLine (CQ)

> A veteran US campaign-finance and lobbying database — valuable because donation filings disclose a donor's home address, employer, and occupation. Now folded into CQ's paid "Capitol Hill Access," with free equivalents at FEC.gov and OpenSecrets.

## When to use
You have a `name` and suspect the person has made federal political contributions or done lobbying work. Campaign-finance filings are an OSINT goldmine: each itemised contribution discloses the donor's name, **home address**, **employer**, and **occupation** as of the donation date — a rare public source of a residential address plus workplace. Use it to place a person geographically and professionally at a point in time, and to surface `associate` links (shared employers, co-donors, PACs).

## How to use it (`bestInteractionPattern`: web-manual)
1. Be aware the free politicalmoneyline.com now routes to CQ "Capitol Hill Access" (paid). If you lack CQ access, go straight to the free equivalents in step 4.
2. With CQ access: log in and search contributions/lobbying by donor `name` (narrow by state/employer for common names).
3. Read each itemised record: contribution amount and date, recipient committee, and the donor's disclosed **address**, **employer**, **occupation**.
4. Free path (recommended default): run the same name on `[[fec-gov]]` (official filings) and `[[opensecrets-org]]` (enriched, cross-referenced) — they expose the same address/employer fields at no cost.
5. Pivot: the disclosed address feeds reverse-address people-search; the employer feeds workplace OSINT; co-donors feed `associate` mapping.

## Inputs → Outputs
- **In:** `name`
- **Out:** `address` (home address on filing), `employer-org`, occupation, `associate` (co-donors / PAC ties), contribution amounts & dates
- **Empty/negative result looks like:** no itemised contributions found — the person may never have donated above the itemisation threshold (small donors aren't individually disclosed), not that they don't exist.

## Gotchas & OpSec
- **Degraded as a free tool:** the standalone free PoliticalMoneyLine is gone; it's a paid CQ product now. Default to FEC.gov / OpenSecrets for the same data free.
- Addresses/employers are as-of the donation date — potentially years stale.
- Only itemised contributions (above the reporting threshold) name the donor; small donations are invisible.
- Fully passive — this is disclosed public record.

## Overlaps ("do both")
- Pairs with `[[opensecrets-org]]` and `[[fec-gov]]` — same source filings, but OpenSecrets adds cross-referencing and OpenSecrets/FEC are free. Always run the free pair; only use CQ's version if you have a subscription and need its extra tooling.

## Trust & verifiability
`trust: community` — the data derives from authoritative FEC/IRS/congressional filings via a long-established tracker now under CQ/FiscalNote. The records are reliable; the caveat is access (paywalled) and staleness of disclosed contact fields.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | political-moneyline-us |
| category | people-search |
| selectorsIn → selectorsOut | name → address, employer-org, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
