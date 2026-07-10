---
id: company-information-service-gov-uk
name: UK Companies House (Find & Update Company Information)
description: Use when you have a person `name`, company `name`/number or `address` in the UK and want official corporate records — returns directorships (`employer-org`), registered/service `address`es and officer `name`s.
url: https://find-and-update.company-information.service.gov.uk/advanced-search
category: public-records
path:
- public-records
bestFor: Searching the UK's official company register to link a person to their directorships, registered addresses, and co-officers via free advanced/officer search.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free to search companies, officers, and filings and to download most filed documents. No account or payment required. A bulk data API and product are also free.
opsec: passive
opsecNote: Public statutory register; neither company nor officer is notified. Queries hit a UK government service — use a puppet browser/IP if you don't want your address tied to the search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Companies House, the UK's official registrar of companies — authoritative for incorporation, directorship, and filing data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Companies House
- find-and-update.company-information.service.gov.uk
- UK company search
tags:
- companysites
- company-related-sites
- public-records
- corporate-registry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# UK Companies House (Find & Update Company Information)

> The UK's official, free company register — the authoritative way to tie a person to directorships, registered/service addresses, and co-officers.

## When to use
You have a `name` and a UK nexus and want to establish corporate footprint: which companies the subject directs or has controlled, the addresses they've filed (registered office and, revealingly, personal **service addresses**), and who they run companies with. Companies House is one of the richest free people-locating sources for the UK because directors must file a correspondence address and often a partial DOB and nationality. Also use to research a company `name` or number directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://find-and-update.company-information.service.gov.uk/ (use **Advanced search** for filters, or the **Officers** search to find a person).
2. Search the person's `name` under officer search, or a company `name`/number. Advanced search filters by company type, status, incorporation date, and registered-office location.
3. Open an officer record to see every appointment, each with role, appointed/resigned dates, partial DOB (month/year), nationality, and **correspondence/service `address`**.
4. Open a company to read registered office `address`, filing history, People with Significant Control (PSC), and co-officers (`associate`s).
5. Pivot: service address → people-search/property; co-directors/PSC → `associate` graph; partial DOB + name → electoral roll and other UK records. Bulk work → the free Companies House API.

## Inputs → Outputs
- **In:** `name` (officer/PSC), company `name`/number, or `address`
- **Out:** `employer-org` (appointments), `address` (registered office + service address), `name` (co-officers/PSC), plus partial DOB, nationality, and dates
- **Empty/negative result looks like:** no officer/company match — the person may hold no UK directorships, use a middle name/initial differently, or be recorded under a variant spelling. Common names over-match; disambiguate with DOB and address.

## Gotchas & OpSec
- Directors can use a company/agent address as their service address, so a listed address may be an accountant's office, not a home — corroborate.
- DOB is shown as month/year only (day is redacted) — enough to narrow, not confirm alone.
- OpSec: **passive** — public statutory record, no notification.

## Overlaps ("do both")
- Pairs with `[[cyprus]]`/`[[asic-gov-au]]` and OpenCorporates for cross-jurisdiction directorships, and with UK electoral-roll/people-search to turn a service address into a residence.

## Trust & verifiability
`trust: trusted` — first-party UK government registrar; incorporation and appointment data are authoritative. The one caveat is that filed addresses/DOB are self-declared by directors, so verify identity where it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | company-information-service-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
