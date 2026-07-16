---
id: mugshots
name: Mugshots.com
description: Use when you have a `name` and want to check for a US arrest/booking record — returns booking photo, charges, arrest location and date; treat as an unverified lead, not proof.
url: http://mugshots.com/search.html
category: public-records
path:
- public-records
bestFor: A quick check for a booking photo and arrest record on a US subject, to corroborate elsewhere.
selectorsIn:
- name
selectorsOut:
- image
- name
- address
- document-id
status: live
pricing: free
costNote: Free to search and view records. It is an aggregator of public arrest data and news, not an official source.
opsec: passive
opsecNote: Searching is passive and does not alert the subject. Note the site is ethically controversial (it publishes booking photos of people not convicted); handle findings carefully and never treat an arrest as guilt.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial arrest-photo aggregator that explicitly disclaims accuracy/timeliness; records can be stale, mismatched, or reflect dropped charges. Corroborate with the originating county/court.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Mugshots
tags:
- court
- inmate
- arrest-records
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- mugshots-com
---

# Mugshots.com

> A searchable aggregator of US booking photos and arrest records — fast for a lead, but unverified and ethically fraught, so confirm everything at the source.

## When to use
You have a `name` and want to know whether a US subject has a booking record, and to grab the associated arrest photo (`image`) for face/reverse-image work. A hit can corroborate identity, place a person in a jurisdiction at a date, and surface charges. But this is a lead source only: it aggregates from mixed public and news sources with no accuracy guarantee.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://mugshots.com/search.html and search by `name` (add a state to narrow).
2. Review candidate records: booking photo, listed charges, arresting agency, arrest/booking date and location.
3. Note the booking `document-id`/case reference and the county — then **verify at the source**: the county sheriff's booking log, jail roster, or court records.
4. Pivot: the booking photo feeds face search; the arrest county/date frames court-record and `[[vinelink]]` custody checks; charges hint at further records.

## Inputs → Outputs
- **In:** `name` (+ state to disambiguate)
- **Out:** booking `image`, `name`, arrest `address` (agency/location), booking `document-id`, and (sometimes) DOB
- **Empty/negative result looks like:** no matching record. Absence is weak evidence — coverage is patchy, and records are removed/expunged; conversely, common-name matches routinely conflate different people, so a hit is not identity confirmation.

## Gotchas & OpSec
- **Arrest ≠ guilt**, and charges shown may have been dropped or expunged — the site itself disclaims accuracy. Never report a mugshots hit as fact without the source record.
- Ethically controversial (booking-photo publishing / reputation harms); use findings responsibly and lead with the primary source.
- OpSec: **passive**; searching doesn't notify anyone.

## Overlaps ("do both")
- Pairs with `[[vinelink]]` and county jail/booking sites — Mugshots may surface an old arrest photo the official current roster won't, while the official sources give the authoritative, up-to-date record.

## Trust & verifiability
`trust: unverified` — a commercial aggregator with a self-disclaimed accuracy; every hit is a lead to confirm against the originating agency or court, not a fact in itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mugshots |
| category | public-records |
| selectorsIn → selectorsOut | name → image, name, address, document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
