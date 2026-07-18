---
id: canadian-trademarks-database
name: Canadian Trademarks Database
description: Use when you have a `name`, brand, or `employer-org` and want Canadian trademark filings tied to them — returns the owner's name, `address` and agent from official CIPO records.
url: https://ised-isde.canada.ca/cipo/trademark-search/srch
category: public-records
path:
- public-records
bestFor: Searching Canada's official trademark register to link a brand/name to its owner, address and filing history.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free official service from the Canadian Intellectual Property Office (CIPO); no account needed to search or view records.
opsec: passive
opsecNote: You search a public government register; nothing about your subject is submitted beyond your query terms, and no owner is notified. CIPO may log queries/IP. Fully passive; use a clean session for sensitive research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party CIPO register covering 140+ years and 1.4M+ Canadian trademarks; owner and filing data are authoritative public records.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- opencorporates
- uspto-trademark-search
- canadian-business-research
- canadian-department-of-finance
- canadian-intellectual-property-office
- completed-access-to-information-requests
- federal-corporation-search-canada
- gov-data-canada
- government-of-canada-open-data
- canadian-importers-database
aliases:
- CIPO Trademarks
- Canadian Trademarks Database
- ic.gc.ca trademarks
tags:
- trademarks
- canada
- business
- public-records
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
---

# Canadian Trademarks Database

> Canada's official trademark register (CIPO) — link a brand or name to the person/company that owns it, with their address and filing history.

## When to use
You have a brand, product name, business name, or a personal `name`/`employer-org` and want to find associated Canadian trademark filings. Trademark records name the **owner** (individual or company), their **address** (as filed), and often an agent — a durable public link between a mark and a real party. Use it to attribute a brand to a person/company, to find a subject's business interests, to confirm an address on record, or to establish a timeline from filing dates. (Note: the old `ic.gc.ca` URL has migrated to the CIPO `ised-isde.canada.ca` database.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ised-isde.canada.ca/cipo/trademark-search/srch.
2. Search by trademark text, or by owner/applicant `name`/`employer-org` (use the searchable-fields options to target the owner field).
3. Open a matching record: registered/pending status, owner name, owner `address`, agent, goods/services, and key dates.
4. Cross-check the owner address and dates against what you already know.
5. Pivot: an owner `employer-org` feeds corporate-registry tools like `[[opencorporates]]`; an owner `address` and name feed people/property searches; filing dates anchor a timeline.

## Inputs → Outputs
- **In:** `name`, brand text, or `employer-org`
- **Out:** owner `name`, owner `address`, `employer-org`, agent, filing/status dates
- **Empty/negative result looks like:** no matching marks — the party holds no Canadian trademark (many individuals/small businesses don't), or the name is spelled/entered differently. Absence isn't evidence of no business activity.

## Gotchas & OpSec
- Canada-only: for other jurisdictions use the equivalent office (e.g. `[[uspto-trademark-search]]` for the US).
- The address is the one filed with CIPO — it may be an agent's/business address rather than a home, and can be dated.
- OpSec: fully passive; a public-register search touches nothing about the subject.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` (map the owner company to directors/filings) and `[[uspto-trademark-search]]` — a party active in both countries may file marks in each, so check both registers.

## Trust & verifiability
`trust: trusted` — the authoritative CIPO register; owner names, addresses, and dates are official public records. The only caveats are match precision and that the filed address may be an agent's, not a residence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-trademarks-database |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
