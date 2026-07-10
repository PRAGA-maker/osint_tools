---
id: company-information-service-gov-uk-2
name: Companies House – Dissolved Company Search
description: Use when you have a `name`, `employer-org` or `address` and want dissolved/closed UK companies — returns company details, registered address and officer records.
url: https://find-and-update.company-information.service.gov.uk/dissolved-search
category: public-records
path:
- public-records
bestFor: Finding UK companies that have been dissolved/closed and their historical officers, addresses and filings via the official Companies House register.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free official government service; no account or payment to search or view dissolved-company records.
opsec: passive
opsecNote: A public statutory register; the subject is not notified. No login required, so searches are not tied to you. Officer records here are public record by law.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Companies House is the UK's official companies registrar; its register (including dissolved companies) is the authoritative, legally-mandated source.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- ukas-com
aliases:
- Companies House dissolved search
- find-and-update.company-information.service.gov.uk
tags:
- companysites
- Company Related Sites
- uk
- companies-house
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Companies House – Dissolved Company Search

> The official UK register's dissolved-company search: find companies that have closed and recover their historical officers, addresses and filings.

## When to use
You are tracing a UK subject or business and the company you're interested in is no longer active. The live Companies House search hides dissolved companies, so use this dissolved-search to recover them — confirming a person was a director/secretary (`name`), the company's registered `address`, incorporation/dissolution dates, and links to other officers (`associate`). Essential for reconstructing a subject's past business footprint and finding co-directors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://find-and-update.company-information.service.gov.uk/dissolved-search.
2. Search by company `name`/`employer-org` (or use the main register to search officers by `name`).
3. Open a dissolved company: registered office `address`, status/dates, and (via filings) its officers.
4. From an officer record, pivot to other companies that person was involved in.
5. Pivot: co-directors become `associate` leads; a registered address feeds property/people search; officer partial DOB helps disambiguate identity.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or `address`
- **Out:** `employer-org` (company details/status), `address` (registered office), `name` (officers), officer partial DOB and co-director links
- **Empty/negative result looks like:** no match in the dissolved register. The company may still be active (search the live register instead), never have existed, or be registered abroad — absence here is not absence everywhere.

## Gotchas & OpSec
- This endpoint is specifically for **dissolved** companies; active ones are on the main find-and-update search — check both.
- Officer DOBs are shown as month/year only (privacy), useful for disambiguation but not a full DOB.
- Historical addresses may be old registered offices, not personal residences.
- OpSec: passive; an official public-register read.

## Overlaps ("do both")
- Pairs with `[[ukas-com]]` and professional registers to vet a business and its people, and with the live Companies House register — dissolved + active together give the full corporate history.

## Trust & verifiability
`trust: trusted` — Companies House is the statutory UK companies registrar, so its records are authoritative. Note that filings reflect what companies submitted, so an address or officer detail is only as current as the last filing before dissolution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | company-information-service-gov-uk-2 |
</content>
