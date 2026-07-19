---
id: nonprofit-explorer
name: Nonprofit Explorer
description: Use when you have an `employer-org` or a person's `name` and want their US nonprofit ties and pay — returns officer/director names, compensation and Form 990 filings.
url: https://projects.propublica.org/nonprofits/
category: public-records
path:
- public-records
bestFor: Finding a US nonprofit's officers, directors and their reported compensation, and full-text-searching Form 990 filings for a person's name.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- employer-org
- address
- document-id
status: live
pricing: free
costNote: Free and open; no account required for search or to view/download Form 990 PDFs.
opsec: passive
opsecNote: Read-only public IRS data via a ProPublica web app. No login, no query attribution. Names and pay of real individuals appear; treat as sensitive though it is already public record.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by ProPublica directly from IRS Form 990 filings and audit records; sourcing and coverage windows are documented. Reputable newsroom.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- 527-explorer
- coronavirus-bailouts-search-every-company-approved-for-federal-loans-over-150k
- credibly-accused
- nursing-home-inspect
- parler-capitol-videos
- police-protest-videos
- the-nypd-files
aliases:
- ProPublica Nonprofit Explorer
- Form 990 search
tags:
- public-records
- nonprofits
- us
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Nonprofit Explorer

> ProPublica's searchable index of US tax-exempt organizations and their Form 990 filings — a fast way to tie a person to a nonprofit's leadership and see reported pay.

## When to use
You have an `employer-org` (a US charity, foundation or 501(c) group) or a `name` you suspect sits on a nonprofit board, and you want officer/director listings, executive compensation, addresses, and the underlying Form 990 documents. Because 990s list named officers and highest-paid staff, full-text search can surface a subject's affiliation, role and salary — useful for confirming employment, associates, and geographic ties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://projects.propublica.org/nonprofits/ .
2. Search by organization name to reach an org page (EIN, category, location, revenue/expenses, filing history), or use the full-text filing search to hunt a person's `name` across scanned 990s.
3. Open a filing to read Part VII (officers, directors, trustees, key employees) and their reported compensation; download the source PDF if needed.
4. Note the org's principal `address` and any related entities.
5. Pivot: an officer `name` feeds people-search; an org address and EIN feed business-registry and grant tools like [[527-explorer]].

## Inputs → Outputs
- **In:** `employer-org` or `name`
- **Out:** officer/director `name`s, `employer-org` detail (EIN, category), `address`, compensation figures, `document-id` (990 filing IDs / PDFs)
- **Empty/negative result looks like:** no matching org or no filing mentioning the name — the entity may be too small to file a full 990, dissolved, or outside the processed window. Absence is not proof of no affiliation.

## Gotchas & OpSec
- Human-in-the-loop: none — fully public, no login. An API is available for bulk use.
- OpSec: **passive**; the subject is never notified.
- Filing data lags real time by 1–2 years and tiny nonprofits (990-N postcard filers) carry little detail. Confirm a person match by cross-referencing the org and role, since common names recur.

## Overlaps ("do both")
- Pairs with [[527-explorer]] (political orgs) and [[coronavirus-bailouts-search-every-company-approved-for-federal-loans-over-150k]] — same ProPublica data family, each covering a different funding/entity dataset.

## Trust & verifiability
`trust: community` — authoritative newsroom republishing official IRS filings with documented methodology; the primary-source 990 PDFs are downloadable for verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nonprofit-explorer |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → name, employer-org, address, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
