---
id: deceasedonline-com
name: deceasedonline.com
url: https://www.deceasedonline.com/servlet/GSDOSearch
category: public-records
path:
- public-records
description: Use when you have a `name` and want UK burial/cremation records — returns death/burial dates, cemetery or crematorium, grave details and family in the same plot.
bestFor: Locating UK burial and cremation register entries (and grave-map/family links) for a named deceased person.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- dob
- address
- associate
status: live
pricing: freemium
costNote: Searching by name and seeing that a record exists is free; viewing the full digitised register scan, grave details or maps is pay-per-view (voucher/credit) after free registration.
opsec: active
opsecNote: The name search itself is a passive archive query, but viewing full records requires creating an account and paying, which ties the lookup to your identity/payment method. Register with a sock-puppet account and dedicated payment if attribution matters. No notification ever reaches the (deceased) subject.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official digitised burial/cremation registers supplied under agreement with UK local authorities and cemetery/crematoria operators; this is primary-source data, not scraped aggregation.
missingPersonsRelevance: high
coverage:
- uk
auth: account
api: false
localInstall: false
registration: true
aliases:
- Deceased Online
- UK burial and cremation records
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- burial-records
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# deceasedonline.com

> The central digitised database of UK burial and cremation registers — free to confirm a record exists, pay-per-view to see the scanned register, grave and family detail.

## When to use
You have a `name` for someone who may have died in the UK and need to confirm the death and locate the burial/cremation. A free name search tells you whether an official register entry exists; paying opens the digitised register page, which typically names others in the same grave (spouses, parents, children) — high-value next-of-kin leads in a missing-person or estate trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.deceasedonline.com/servlet/GSDOSearch.
2. Enter the surname (required) plus optional first name and death-year range; you can filter for children/stillborn or illegible entries.
3. Run the free search: matching results show name, year and burial authority — enough to confirm a record exists.
4. To see the scanned register, grave map or co-buried family, register (free) and spend a pay-per-view credit on that record.
5. Pivot: co-buried `associate` names and the burial authority feed probate/electoral searches and `[[interment]]` for cross-checking.

## Inputs → Outputs
- **In:** `name` (+ optional death-year `geolocation`/range)
- **Out:** `name`, `dob` (death/burial dates), cemetery/crematorium `address`, `associate` (others in the same grave)
- **Empty/negative result looks like:** no matching register rows. Coverage is authority-by-authority, so an absent record can mean that council's registers aren't digitised here yet — not that no death occurred.

## Gotchas & OpSec
- Coverage is partial and expanding: many UK authorities are included but not all. A miss is inconclusive.
- The valuable family/grave detail is behind the paywall; budget credits before you start.
- OpSec: registration + payment link the search to you. Use a sock-puppet account and dedicated payment method for sensitive work. The subject is deceased, so there is no owner-notification risk.

## Overlaps ("do both")
- Pairs with `[[interment]]` — DeceasedOnline is authoritative for UK burial/cremation registers, while Interment covers US and other cemeteries; run both when nationality is uncertain.

## Trust & verifiability
`trust: trusted` — records are digitised primary-source registers licensed from UK local authorities and crematoria, so entries are authoritative; the main limitation is coverage breadth, not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deceasedonline-com |
| category | public-records |
| selectorsIn → selectorsOut | name, geolocation → name, dob, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (payment-wall-partial, account-login) |
