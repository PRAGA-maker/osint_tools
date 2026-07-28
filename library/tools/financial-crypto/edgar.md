---
id: edgar
name: EDGAR
description: Use when you have a `name` or company (`employer-org`) and want US SEC filings — returns officers, insiders, ownership and `associate` links from corporate disclosures.
url: https://www.sec.gov/edgar/search/
category: financial-crypto
path:
- financial-crypto
bestFor: Full-text searching US public-company filings for people, companies, and their relationships.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free and official; no account. A public JSON/REST API is available for automation.
opsec: passive
opsecNote: Passive query against a US-government public database — the subject receives no signal. Filings are public record, so there is no intrusion, but treat personal details (home addresses in some filings) responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US Securities and Exchange Commission; filings are legally-mandated primary-source records.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- sec-company-search
- sec-gov
- sec-gov-edgar
- us-securities-and-exchange-commission
- edgar-u-s-securities-and-exchange-commission-filings
aliases:
- SEC EDGAR
- EDGAR full-text search
tags:
- bellingcat-toolkit
- companies-finance
- corporate-records
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# EDGAR

> The SEC's public database of US corporate filings — a primary source that ties people to companies, insider ownership, and each other through legally-required disclosures.

## When to use
You have a `name` (executive, director, major shareholder) or an `employer-org` and want the paper trail: who runs a US public company, who owns stakes, who the affiliated persons and entities are, and where they're registered. EDGAR's full-text search covers filings back to 2001 and indexes the actual documents.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sec.gov/edgar/search/ (EDGAR full-text search).
2. Search a person's `name`, a company, or any phrase; filter by filing type and date.
3. Read the high-signal forms:
   - **DEF 14A** (proxy) — officers, directors, compensation, bios.
   - **Forms 3/4/5** — insider ownership and transactions (names + relationships).
   - **SC 13D/G** — beneficial owners of >5%.
   - **10-K/S-1** — subsidiaries, risk factors, related-party deals.
4. Use the API (`https://efts.sec.gov/LATEST/search-index?q=...`) for bulk/automated queries.
5. Pivot: named officers → other filings they appear in (`associate` mapping); registered `address`es → corporate-registry lookups.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** officers/insiders, ownership, related entities (`associate`), business `address`es, filing history
- **Empty/negative result looks like:** no filings — the person/company isn't a US SEC registrant (private companies, non-US entities, and small firms won't appear); absence isn't evidence of nonexistence.

## Gotchas & OpSec
- US public-company scope only — private firms, most non-US entities, and individuals with no securities role are absent.
- Full-text search starts at 2001; older filings need the classic EDGAR browse.
- Names in filings can be common — confirm identity via cross-referenced roles/addresses, not name alone.
- Several near-duplicate SEC entries exist in this library; this is the canonical full-text-search entry point.

## Overlaps ("do both")
- Pairs with [[sec-company-search]] and general corporate-registry tools — EDGAR gives the filings and insider relationships, while registries give incorporation details and non-SEC companies.

## Trust & verifiability
`trust: trusted` — authoritative US-government primary source; filings carry legal accountability, making them among the most reliable person↔company links available.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | edgar |
| category | financial-crypto |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
