---
id: gov-cy
name: Cyprus Registrar of Companies (DRCOR)
description: Use when you have a Cyprus `employer-org`/company name (or reg number) and want its official registry record — returns registered `address`, company officers/directors and status.
url: https://efiling.drcor.mcit.gov.cy/DrcorPublic/SearchForm.aspx?sc=0
category: public-records
path:
- public-records
bestFor: Official Cyprus company search — find a registered company, its officers and registered address.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- name
- associate
status: live
pricing: free
costNote: Free public search of the registered-organisations catalogue; certified copies of filings may carry a fee, but the basic search and officer/address view are free.
opsec: passive
opsecNote: Passive lookup of a public government registry; neither the company nor its officers are notified. First-party official source. No account needed; clean session sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Cyprus Department of Registrar of Companies and Intellectual Property (DRCOR), Ministry of Energy, Commerce and Industry — the authoritative Cyprus corporate register.
missingPersonsRelevance: high
coverage:
- cy
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- legalmondo-com
- cyprus
aliases:
- DRCOR
- Cyprus company registry
- efiling.drcor.mcit.gov.cy
tags:
- companysites
- Company Related Sites
- corporate-records
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Cyprus Registrar of Companies (DRCOR)

> Cyprus's official company register — search registered organisations by name or number to pull their officers, registered address and status. Cyprus is a common corporate-vehicle jurisdiction, so this matters in beneficial-ownership work.

## When to use
You have a Cyprus `employer-org` (company name or registration number) or a person you believe is an officer/director of a Cyprus entity, and you want the authoritative record — officers, registered office `address`, and status. Because Cyprus is frequently used for holding companies, a subject linked to a Cypriot entity can be traced through its officer/director listings and address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the DRCOR public search at the URL.
2. Search by organisation name (options include all-words / some-words / phonetic) or by registration number.
3. Open the matching entity to view its status, registered office `address`, and officers/directors (`associate`/`name`).
4. Order a certified copy of filings if you need the underlying documents (may incur a fee).
5. Pivot: named officers feed people-search; a shared registered address links multiple entities; company number feeds cross-jurisdiction corporate tools.

## Inputs → Outputs
- **In:** `employer-org` (company name/number) or an officer `name`
- **Out:** `employer-org` record, registered `address`, officers/directors (`name`/`associate`), status
- **Empty/negative result looks like:** no matching organisation — try name fragments, the phonetic option, or the exact registration number; a nominee-heavy structure may show only nominee officers rather than the true beneficial owner.

## Gotchas & OpSec
- Interface is bilingual (Greek/English); some fields and filings are Greek-only.
- Cyprus entities often use nominee directors/secretaries — listed officers may be professional nominees, not the beneficial owner.
- Basic search is free; full document copies may be paid.

## Overlaps ("do both")
- Pairs with EU company aggregators (OpenCorporates) and the `[[legalmondo-com]]`-style jurisdiction guides — the aggregator gives a fast first pass, DRCOR gives the authoritative Cyprus record.

## Trust & verifiability
`trust: trusted` — the official Cyprus registrar; records are authoritative, though nominee structures can obscure real ownership, so treat listed officers accordingly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-cy |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, name, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
