---
id: europa-press-releases
name: Europa Press Releases (Press Corner)
description: Use when you have a `name` or `employer-org` and want EU institutional mentions — searches official EU press releases, statements, and speeches by keyword and date.
url: https://ec.europa.eu/commission/presscorner/
category: search-engines
path:
- search-engines
bestFor: Searching the official EU press-release archive for mentions of a person, company, policy, or event across statements, speeches, and Q&As.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free official EU service; searchable archive with email/RSS notifications. No account needed.
opsec: passive
opsecNote: Passive — you search a static official archive; nobody is notified and nothing leaks. Fully OpSec-safe; ordinary clean-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The European Commission's official press service (Press Corner, successor to europa.eu/rapid); entries are authoritative primary-source EU communications.
missingPersonsRelevance: low
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- e-justice-europa-eu
- eu-consolidated-corporate-registers
- eu-sanctions-tool
- europa-eu
- european-commission-home-affairs
- european-union-open-data-portal
- eurostat
- frontex-migratory-map
- inspire-geoportal
- vat-number-validation
aliases:
- europa.eu/rapid
- EU Press Corner
- RAPID
tags:
- toddington
- curated-directory
- eu
- press-releases
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Europa Press Releases (Press Corner)

> The European Commission's official press archive — search decades of releases, statements, speeches, and Q&As for authoritative EU mentions of a person, organization, or policy.

## When to use
You have a `name`, `employer-org`, policy, or event with an EU dimension and want to find where official EU communications reference it. Because it's the Commission's primary-source press record, a hit is authoritative — useful for placing an official, a company, or a matter in the EU institutional record, dating when something was announced, or gathering official statements. Best when a subject intersects EU policy, funding, appointments, sanctions, or enforcement.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ec.europa.eu/commission/presscorner/ (the successor to europa.eu/rapid).
2. Use search to query a name, organization, or keyword; filter by date, type (press release, statement, speech, Q&A), and policy area.
3. Read matching items for official mentions, quotes, dates, and named officials/entities.
4. Set an email/RSS alert to monitor future mentions of a term.
5. Pivot: an official's `name` feeds EU transparency/appointment research; a company mention feeds `[[eu-consolidated-corporate-registers]]`; a sanctions/enforcement reference feeds `[[eu-sanctions-tool]]`.

## Inputs → Outputs
- **In:** a `name`, `employer-org`, or keyword (EU context)
- **Out:** official EU press items mentioning the term — with named `name`/`employer-org` references, dates, and quotes
- **Empty/negative result looks like:** no results means the term isn't referenced in EU press communications — most people/companies never are, so absence says little except that there's no EU-institutional footprint.

## Gotchas & OpSec
- **Institutional scope:** it indexes EU *communications*, not a people directory — it surfaces those the EU has publicly mentioned, not the general public.
- Multilingual; some items exist only in certain languages — try key terms in more than one language.
- The old `europa.eu/rapid` URL now redirects here; bookmark the Press Corner host.

## Overlaps ("do both")
- Sits within the EU-tools cluster — pair with `[[eu-consolidated-corporate-registers]]`, `[[eu-sanctions-tool]]`, and `[[e-justice-europa-eu]]`; Press Corner supplies the official narrative/announcement, and those supply the structured registry/sanctions/legal records.

## Trust & verifiability
`trust: trusted` — the official European Commission press service; its entries are authoritative primary-source communications, citable by date and reference number.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | europa-press-releases |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
