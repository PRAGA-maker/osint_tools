---
id: maldives-sex-offender
name: Maldives Child Sex Offenders Registry
description: Use when you have a `name` linked to the Maldives and want to check the official child sex-offenders registry — returns name, image, dob, address, national ID and conviction details.
url: http://www.offenders.mv/offenders/
category: public-records
path:
- public-records
bestFor: Checking the Maldives government child sex-offenders registry for a named individual.
selectorsIn:
- name
selectorsOut:
- name
- image
- dob
- address
- document-id
- physical-description
status: degraded
pricing: free
costNote: Free public registry published by the Maldives Ministry of Gender, Family & Social Services; no account needed.
opsec: passive
opsecNote: You are reading a public government registry (currently served as a downloadable PDF), so browsing is passive and leaks nothing about the subject. Handle the data carefully — it names convicted offenders with photos and national IDs; do not republish or misattribute.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official registry mandated by Maldives' 2009 child sexual-abuse-prevention law and published by the Ministry of Gender; authoritative but historically updated irregularly.
missingPersonsRelevance: high
coverage:
- mv
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- offenders.mv
- Maldives sex offender registry
tags:
- sex-offender-registry
- maldives
- government
- public-records
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Maldives Child Sex Offenders Registry

> The Maldives government's official public list of convicted child sex offenders — photos, full names, national IDs, DOBs, addresses and conviction/imprisonment details — published at offenders.mv.

## When to use
You have a `name` (or physical description/photo to match) for someone connected to the Maldives and need to know whether they appear on the national child sex-offenders registry. Because each entry carries a photo, national ID number, date of birth and address, a hit is also a rich identity-confirmation record for a Maldives subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.offenders.mv/offenders/.
2. The site is frequently "under maintenance"; when it is, follow the PDF link the page provides — the registry itself is published as a downloadable document.
3. Manually scan/search the list of ~180+ named individuals for your subject (by name, national ID, or by matching the photo).
4. Read the record: full `name`, `image` (mugshot), national identity card number (`document-id`), `dob` and age, `address`, and conviction / imprisonment / release dates plus detention centre.
5. Pivot: the national ID and address feed other Maldives records; the photo feeds face-search tools.

## Inputs → Outputs
- **In:** `name` (or a photo / national ID to match against the list)
- **Out:** `name`, `image`, `dob`, `address`, `document-id` (national ID), `physical-description`, plus conviction dates
- **Empty/negative result looks like:** the subject is absent from the published list — meaning no listed child-sex conviction on this registry, NOT a general clean record (the list is limited to child sexual offences and is known to lag updates).

## Gotchas & OpSec
- Human-in-the-loop: there is no live search box when the site is in maintenance mode — you manually review a PDF, so expect to read/scan rather than query.
- Data currency: the registry has a documented history of irregular updates; a recent conviction may not yet appear.
- OpSec: **passive** — reading a public PDF leaks nothing, but the content is sensitive; do not scrape-and-republish or attach the label to the wrong person.

## Overlaps ("do both")
- Standalone for the Maldives; pair with international sex-offender aggregators only to confirm whether a Maldives subject also appears in another jurisdiction, since this registry is national-only.

## Trust & verifiability
`trust: trusted` — it is the Maldives Ministry of Gender's statutorily-mandated registry, so entries are authoritative court-backed records; the caveat is timeliness (updates have historically been irregular), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maldives-sex-offender |
| category | public-records |
| selectorsIn → selectorsOut | name → name, image, dob, address, document-id, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
