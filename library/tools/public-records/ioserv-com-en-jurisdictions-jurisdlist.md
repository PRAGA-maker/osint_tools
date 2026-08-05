---
id: ioserv-com-en-jurisdictions-jurisdlist
name: IOS Jurisdiction List (ioserv.com)
description: Use when you have an `employer-org` structured offshore and want a reference on its jurisdiction — returns jurisdiction/company-type context to guide where to pull `employer-org` records.
url: https://ioserv.com/en/jurisdictions/jurisdlist
category: public-records
path:
- public-records
bestFor: A reference list of offshore incorporation jurisdictions and company types to orient corporate-structure research.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: degraded
pricing: free
costNote: The jurisdiction reference pages are free to read; IOS's actual incorporation/consulting services are paid, but you never need those to use the reference.
opsec: passive
opsecNote: Reading a public reference page leaks nothing about a subject. Do NOT submit an inquiry/contact form — that would engage a corporate-services provider and is unnecessary for OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A marketing/reference site for the International Overseas Services (IOS) network of independent incorporation agents; useful as orientation, not as an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- company-search-tool
- company-check
aliases:
- International Overseas Services jurisdictions
- IOS jurisdiction list
tags:
- corporate
- offshore
- reference
source: metaosint
lastVerified: '2026-08-05'
enrichment: full
---

# IOS Jurisdiction List (ioserv.com)

> The jurisdiction directory of International Overseas Services, an offshore-incorporation consultancy — a reference on which offshore jurisdictions offer what kind of company, to help you decide where to hunt for a corporate record.

## When to use
You've traced an `employer-org` to an offshore structure (a shell, holding company, or trust) and need orientation before pulling records: which jurisdictions offer which entity types, what each is typically used for, and therefore which registry or corporate-search tool to query next. This is a reference/orientation page, not a searchable registry — it will not return a specific company, only jurisdiction context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ioserv.com/en/jurisdictions/jurisdlist (if it returns a temporary 503, retry later — the site is intermittently up).
2. Browse the list of jurisdictions the IOS network covers and open one to read its company types, typical uses, and disclosure/KYC characteristics.
3. Use that to choose the right primary source: for the actual entity, pivot to the jurisdiction's official registry or a corporate-search aggregator.
4. Feed the `employer-org` name into `[[company-search-tool]]` / `[[company-check]]` scoped to that jurisdiction.

## Inputs → Outputs
- **In:** `employer-org` (an offshore entity whose jurisdiction you're researching)
- **Out:** `employer-org` context — jurisdiction/company-type reference to direct the next lookup
- **Empty/negative result looks like:** the page lists no jurisdiction matching your entity, or is temporarily unavailable (503). It never returns company-specific records — for those you must go to a registry.

## Gotchas & OpSec
- This is a consultancy's marketing/reference site, not a public register; do not treat its descriptions as legal authority.
- The site is intermittently unavailable (observed 503s); if it's down, offshore-jurisdiction reference is also available from other guides.
- OpSec: passive for reading only. Never submit the contact/inquiry form.

## Overlaps ("do both")
- Use it to *decide where to look*, then do the actual lookup in `[[company-search-tool]]` and `[[company-check]]`, which return real entity records the reference page cannot.

## Trust & verifiability
`trust: unverified` — it is promotional material from a network of independent incorporation agents; rely on it only for orientation and confirm every entity fact against the official registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ioserv-com-en-jurisdictions-jurisdlist |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
