---
id: citizen-audit
name: CitizenAudit
description: Use when you have a US nonprofit `employer-org` or a `name` and want to search Form 990 filings — returns officers, salaries, grants, and connections buried in nonprofit tax documents.
url: https://www.citizenaudit.org/
category: search-engines
path:
- search-engines
bestFor: Full-text search of US nonprofit Form 990 tax filings to surface people, pay, and grant relationships.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- associate
- employer-org
status: live
pricing: freemium
costNote: Limited free searching/preview; full-text search, document access, and exports require a paid subscription. Basic lookups can be done free.
opsec: passive
opsecNote: Searching filed public tax documents is read-only and alerts no one. CitizenAudit sees your account/IP if you register. The data is public IRS filings, but it names living individuals (officers, top earners) — handle responsibly.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Indexes authoritative IRS Form 990 filings; the underlying documents are official public records, though OCR/extraction can occasionally misread figures.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- propublica-nonprofit-explorer
- guidestar-candid
- opencorporates
aliases:
- citizenaudit.org
tags:
- toddington
- curated-directory
- specialty-search
- nonprofit
- form-990
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# CitizenAudit

> A full-text search engine over millions of US nonprofit Form 990 tax filings — the way to find a person's board seats, salary, grants, and organizational ties hidden inside nonprofit paperwork.

## When to use
You have a US nonprofit `employer-org` you want to dissect, or a `name` you suspect sits on nonprofit boards, draws nonprofit salaries, or moves money through grants. Form 990s disclose officers/directors, the highest-paid employees and their compensation, and grants given/received — a rich map of a person's affiliations and financial relationships. CitizenAudit's full-text index finds a name *inside* the documents, catching connections that org-name-only databases miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.citizenaudit.org/ and search the `employer-org` or `name`.
2. For an org: open its filings to read officers/directors, top earners and salaries, and grants made/received (each grant names another `employer-org`/`associate`).
3. For a person: use full-text search to find every 990 that names them — board memberships, compensation, or as a grant contact.
4. Note that deep full-text search and document downloads sit behind a subscription; do the high-value lookups within the free preview or a paid plan.
5. Pivot: named officers → people-search; connected orgs → corporate registries (`[[opencorporates]]`); cross-check figures on `[[propublica-nonprofit-explorer]]`.

## Inputs → Outputs
- **In:** `employer-org` (US nonprofit) or `name`
- **Out:** `name` (officers/earners), `associate` (co-directors, grant partners), `employer-org` (connected nonprofits), compensation and grant figures
- **Empty/negative result looks like:** no filings/no name hits — the org isn't a 990-filing US nonprofit (small orgs file the 990-N postcard with little detail), or the person has no nonprofit role indexed. Absence isn't proof of no involvement, especially for tiny orgs.

## Gotchas & OpSec
- Coverage is US 990-filing nonprofits; small orgs filing the 990-N reveal almost nothing, and filings lag a year or two.
- Figures are OCR-extracted from scanned forms and can be misread — verify a critical salary/grant against the source PDF.
- The most useful features (full-text search, exports) are paid; plan your queries.
- OpSec: **passive** — public filings; but respect the privacy of named individuals.

## Overlaps ("do both")
- Pairs with `[[propublica-nonprofit-explorer]]` and `[[guidestar-candid]]` — each indexes 990s differently (ProPublica is free), so cross-check a name/org across them for fuller coverage and to confirm figures.

## Trust & verifiability
`trust: trusted` — built on authoritative IRS filings; the records are official, with the only caveat being occasional OCR/extraction errors you should confirm against the original document.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | citizen-audit |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, name → name, associate, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
