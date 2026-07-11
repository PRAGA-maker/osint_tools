---
id: jailbase
name: JailBase
description: Use when you have a `name` and want to check for a recent US arrest — returns booking records with mugshot, charges, booking date and county across hundreds of jurisdictions.
url: http://www.jailbase.com/en/search
category: public-records
path:
- public-records
bestFor: Searching aggregated US county arrest/booking records and mugshots by name to establish whether a subject was recently arrested and where.
selectorsIn:
- name
selectorsOut:
- name
- dob
- image
- document-id
- address
status: live
pricing: freemium
costNote: Browsing recent arrests, the inmate search and county mugshots is free; older/archived records and extra details are sold per-record, and arrest alerts are a paid feature.
opsec: passive
opsecNote: Searching is passive — the arrestee is not notified. Bear in mind arrest ≠ conviction; these are booking records, and mugshot-aggregator data can be outdated or wrongly matched, so treat a hit as a lead to verify against the county's own records.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial aggregator of public arrest data from hundreds of US counties; coverage is broad but incomplete and freshness varies — it is a secondary index, not the authoritative source.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- jailbase.com
- JailBase arrests and mugshots
tags:
- court
- inmate
- arrest-records
- mugshots
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# JailBase

> A nationwide index of US county booking records and mugshots — a fast way to check whether a subject surfaced in a jail intake, and in which jurisdiction.

## When to use
You have a subject `name` and want to know if they've been arrested recently in the US. JailBase aggregates booking data from hundreds of county/city jails, so a hit gives you a mugshot (`image`), charges, booking date, booking/`document-id`, approximate age/`dob`, and the arresting county — which itself places the person in a location at a point in time. Reach for it when tracing a missing or evasive person who may have entered the justice system, or to corroborate an identity via a booking photo.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.jailbase.com/en/search.
2. Search the subject `name`; optionally browse recent arrests filtered by county, date, gender or race.
3. Open a matching record: mugshot, listed charges, booking date, county, and booking number.
4. Confirm against the county sheriff's / jail's own roster (JailBase is a mirror, not the source of truth).
5. Pivot: the county locates the person geographically and temporally; charges/booking numbers feed court-record searches; the mugshot feeds face search (`[[pimeyes]]`).

## Inputs → Outputs
- **In:** `name`
- **Out:** booking `name`, mugshot `image`, approximate `dob`/age, booking `document-id`, charges, and county/jail `address`
- **Empty/negative result looks like:** no matching booking — the person hasn't been arrested in a covered jurisdiction, the arrest predates coverage/was archived (paid), or the county isn't indexed; absence is NOT proof of no record.

## Gotchas & OpSec
- Coverage gaps: JailBase doesn't cover all US counties and adds them over time — a miss can be a coverage hole.
- Arrest ≠ guilt: these are intake records; charges may be dropped — never present an arrest as a conviction.
- Data hygiene: aggregated mugshot data can be stale or mis-matched to a same-name person — verify at the county source.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with county court-record and inmate-locator tools — JailBase flags the arrest; those confirm charges/status and current custody.
- Pairs with `[[pimeyes]]` — the mugshot anchors a face search across other imagery.

## Trust & verifiability
`trust: community` — a commercial aggregator of genuine public records; broad but incomplete and variably fresh, so a JailBase hit should always be confirmed against the originating county's official system.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jailbase |
