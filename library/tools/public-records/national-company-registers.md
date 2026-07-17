---
id: national-company-registers
name: National Company Registers (directory)
description: Use when you have an `employer-org` (or a person's directorship) in a specific country and need the official corporate registry — a directory pointing to each nation's authoritative company register.
url: https://en.wikipedia.org/wiki/List_of_company_registers
category: public-records
path:
- public-records
bestFor: Finding the official government company register for a given country to look up a business or its officers.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: The directory (a Wikipedia list) is free; individual national registers vary — many are free to search, some charge per document.
opsec: passive
opsecNote: Reading the directory and most official registers is passive and anonymous. Some registers log searches or require login for documents; use an investigative account where needed.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: A maintained Wikipedia index of official government company registers; the registers it links are the authoritative primary sources, though the list itself is community-maintained.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- opencorporates
aliases:
- List of company registers
tags:
- company-research
- corporate-registry
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# National Company Registers (directory)

> The "which official registry do I use?" index — a country-by-country list linking to each nation's authoritative government company register, where directorships and filings are primary-source.

## When to use
You need to research a company (`employer-org`) or a person's role in one — director, shareholder, registered address — and you want the **official** source for that jurisdiction rather than an aggregator. Company registers are gold for people work: they tie individuals to businesses, list co-directors (`associate`s), give registered/service addresses, and often show a person's whole portfolio of companies. This directory gets you to the correct national register fast, which matters because coverage, language and access rules differ per country.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the list at https://en.wikipedia.org/wiki/List_of_company_registers and find the country you need.
2. Follow the link to that nation's official register (e.g. UK Companies House, France's Infogreffe/RNE, etc.).
3. Search by company name or (where supported) by officer/director `name`.
4. Read the record for officers, registered `address`, incorporation date, filings and status; note co-directors as `associate` leads.
5. Watch for paywalls — many registers show basic data free but charge for full documents/filings (human-in-the-loop budget step).
6. Pivot: officers → people-search; registered addresses → geolocation; a director's other companies → their broader footprint. Cross-check with `[[opencorporates]]`.

## Inputs → Outputs
- **In:** `employer-org` (company) or `name` (officer/director) + the country
- **Out:** official company record — officers/`associate`s, registered `address`, status, filings
- **Empty/negative result looks like:** no match in the national register — the company may be in another jurisdiction, dissolved, or an unregistered trading name. Try `[[opencorporates]]` (which aggregates many registers) and neighbouring countries.

## Gotchas & OpSec
- It's a *directory*, not a search engine — you still go to each national register and learn its quirks (language, ID formats, fees).
- Access varies wildly: some registers are fully open, others require registration or charge per document; a few are only partially online.
- The Wikipedia list is community-maintained and can lag; verify a register's current official URL before trusting it.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` — OpenCorporates aggregates and cross-links many of these registers into one search, but the official national register is the authoritative source for filings/documents. Use OpenCorporates to find, the official register to confirm.

## Trust & verifiability
`trust: trusted` — the registers this indexes are official government primary sources (authoritative). The index page itself is community-maintained, so confirm each register's current official link, and treat any single record's currency against the register's stated update cadence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | national-company-registers |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
