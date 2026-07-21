---
id: us-government-printing-office
name: US GPO govinfo
description: Use when you have a `name` and want to find them in official US federal publications — congressional hearings, court opinions, the Federal Register, reports and directories — returns `employer-org`, `document-id`, `associate`.
url: https://www.govinfo.gov/
category: search-engines
path:
- search-engines
bestFor: Full-text searching authoritative US federal government publications (Congressional Record, hearings, bills, court opinions, Federal Register, GAO reports) for a person or organization.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- document-id
- associate
status: live
pricing: free
costNote: Free official US Government Publishing Office service; no account required.
opsec: passive
opsecNote: A public government archive; searching it discloses nothing to the subject. Standard sock-puppet hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US Government Publishing Office platform (govinfo.gov); the authoritative, authenticated source for federal documents — it replaced the retired GPO FDsys system.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- court-electronic-records-pacer
aliases:
- govinfo.gov
- GPO FDsys
- Government Publishing Office
tags:
- search-engines
- public-records
- government-documents
- us-federal
- toddington
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# US GPO govinfo

> The US Government Publishing Office's official full-text archive — where a person's name can surface in hearings, court opinions, the Federal Register, reports and official directories.

## When to use
You have a `name` or `employer-org` and want to check whether they appear in the official record of the US federal government. govinfo full-text-searches Congressional hearings and reports, the Congressional Record, bills and laws, the U.S. Code and CFR, the Federal Register (rules, notices, nominations, grants), GAO reports, the Congressional Directory, and U.S. court opinions. It's strong for people connected to government, litigation, regulation, testimony, federal grants, or official appointments — turning a name into documents, dates, roles, and co-named parties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.govinfo.gov/ and use the search box (or "Advanced Search" to scope by collection, date, author, or committee).
2. Search the `name` in quotes; narrow by collection (e.g. "Congressional Hearings", "Court Opinions", "Federal Register") if results are noisy.
3. Open matching documents — each is an authenticated PDF/HTML with a citation and `document-id` — and read for the person's role, affiliation, dates, and other named parties.
4. Record the `employer-org`/title context and any co-named `associate`s (co-witnesses, co-defendants, colleagues, nominating officials).
5. Pivot: federal court references lead to `[[court-electronic-records-pacer]]` for the full docket; a stated employer/agency feeds org-focused searches.

## Inputs → Outputs
- **In:** `name` (or `employer-org`)
- **Out:** `employer-org` / role context, `document-id` (official citation), `associate` (co-named parties in the same document)
- **Empty/negative result looks like:** zero documents for the name — meaning the person doesn't appear in the *federal* published record (very common for private individuals); it says nothing about state/local records.

## Gotchas & OpSec
- Human-in-the-loop: none. A public API is also available for bulk/programmatic queries.
- OpSec: passive — an official archive; nothing reaches the subject.
- Coverage is US **federal** only and skewed toward government, legal, and regulatory contexts; most ordinary people never appear. Name collisions are common — confirm identity from the document's context, not the name alone.

## Overlaps ("do both")
- Pairs with `[[court-electronic-records-pacer]]` — govinfo carries selected federal court *opinions*, while PACER holds the full docket and filings; use govinfo to find the case, PACER to work it.

## Trust & verifiability
`trust: trusted` — it is the GPO's authenticated, first-party publication system (successor to FDsys); documents are official and citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-government-printing-office |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
