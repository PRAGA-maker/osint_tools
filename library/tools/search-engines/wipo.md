---
id: wipo
name: WIPO Global Brand Database
description: Use when you have a `name`, brand, or `employer-org` and want trademark records — returns trademarks, their owners/applicants, and filing details worldwide.
url: https://www3.wipo.int/branddb/en/
category: search-engines
path:
- search-engines
bestFor: Searching global trademark filings to link a brand to its owner/applicant, or find brands owned by a person/company.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- address
status: live
pricing: free
costNote: Free official WIPO database; no account needed.
opsec: passive
opsecNote: Public intellectual-property registry search; the applicant isn't notified. Fully passive, no login.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by WIPO (World Intellectual Property Organization, a UN agency); aggregates authoritative trademark data from national/international registries.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- uspto-tess
- euipo-esearch
aliases:
- WIPO Global Brand Database
- branddb
tags:
- speciality-search-engines
- trademark
- intellectual-property
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# WIPO Global Brand Database

> WIPO's Global Brand Database — search trademarks across dozens of national and international registries to connect a brand to the person or company that owns it.

## When to use
You're investigating a business or a subject who may own a brand. Trademark filings name the applicant/owner (often with an address or agent) and reveal what brands a person/company controls. Use the Global Brand Database to go from a `name`/`employer-org` to their trademarks, or from a brand name to its owner — a solid corporate/identity pivot (low direct missing-persons relevance, higher for business-linked subjects).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www3.wipo.int/branddb/en/.
2. Search by brand/wordmark, or by owner/applicant name; filter by jurisdiction, status, and date.
3. Open a record to read the mark, owner/applicant, representative, filing/registration dates, and goods/services class.
4. Note the applicant address/agent — often a real business address or law firm tied to the subject.
5. Pivot: owner name → corporate-registry and domain lookups; a US mark → `[[uspto-tess]]` for full US file history; EU mark → `[[euipo-esearch]]`.

## Inputs → Outputs
- **In:** a `name`, brand, or `employer-org`
- **Out:** trademark records with owner/applicant `name`/`employer-org`, representative, and often an `address`
- **Empty/negative result looks like:** no marks — the person/company holds no registered trademarks, or filed only in a registry not covered; a null is common for individuals (most people own no trademarks).

## Gotchas & OpSec
- Coverage is broad but not every jurisdiction is included; a national office (USPTO/EUIPO) may hold records WIPO's aggregate misses — check the relevant national DB too.
- Applicant details can be a law firm/agent rather than the real person; the address may be a representative's.
- Owner names get abbreviated/varied across registries — try name variants and the company's legal form.

## Overlaps ("do both")
- Pairs with `[[uspto-tess]]` and `[[euipo-esearch]]` — national databases with deeper file histories; WIPO is the multi-jurisdiction first pass, the national offices give depth.

## Trust & verifiability
`trust: trusted` — an authoritative UN-agency database aggregating official registry data. Records are reliable; confirm ownership/address against the originating national registry when it's decisive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wipo |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
