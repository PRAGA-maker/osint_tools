---
id: arrests
name: Arrests.org
description: Use when you have a `name` and want to check for a US arrest record or mugshot — returns booking photos, arrest dates, charges, and county, indexed by state.
url: http://www.arrests.org
category: public-records
path:
- public-records
bestFor: Finding US arrest/booking records and mugshots for a subject, browsable by state and county.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: freemium
costNote: Browsing recent bookings and mugshots is free; full detailed reports (charges, court dates, background) are upsold to paid partner reports (commonly ~$20–40).
opsec: passive
opsecNote: A public-records aggregator query that does not notify the subject. Beware of the many near-identical clone/scam domains imitating "arrests.org" — stick to the known site and never pay a clone. Use a clean browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Popular US booking-photo aggregator republishing county arrest data; coverage is uneven, records can be stale or misattributed, and numerous copycat domains exist — verify against the source county.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Arrests.org
- Arrests Org
tags:
- court
- inmate
- mugshot
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- facesearch-arrests-org
---

# Arrests.org

> A national aggregator of US booking photos and arrest records — use it to check whether a subject has a recent arrest, and to pull the mugshot, date, charge, and county to chase in the primary source.

## When to use
You have a `name` and want a quick, cross-jurisdiction check for a US arrest or booking. An arrest record anchors a person to a specific county and date, yields a mugshot for face/reverse-image work, and often surfaces a middle name, age/DOB, and charges — all strong locate and identity leads when a trail has gone cold. Reach for it as a broad first sweep before going to individual county sheriff/court sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site and select the relevant **state**, then narrow by county if offered.
2. Search the subject's `name` (or browse recent bookings for a locality).
3. Read the result list: name, mugshot, booking/arrest date, and county; open a record for charges.
4. **Verify in the primary source** — take the county + date to that county's sheriff/jail/court site to confirm the record is real and correctly attributed.
5. Pivot: the mugshot feeds face/reverse-image tools; a confirmed county anchors location; an age/DOB corroborates identity elsewhere.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name`, `dob` (age), `document-id` (booking reference), plus mugshot, charge, county, date
- **Empty/negative result looks like:** no match — coverage is uneven county-to-county, so absence is weak evidence; check the county source directly and other arrest/inmate sites before concluding no record.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; detailed reports are **paywalled** and often just repackage free public data — go to the county source instead.
- **Clone-site risk is high:** dozens of copycat domains mimic "arrests.org" to harvest payments; do not pay unknown clones. Always confirm records at the originating county.
- Records can be stale, expunged, or misattributed to a namesake — never treat a hit as proof without primary-source confirmation.
- OpSec: passive; the subject is not notified.

## Overlaps ("do both")
- Pairs with state offender/inmate locators like `[[west-virginia]]` and county court portals — this is the broad net; those are the authoritative confirmations for a specific jurisdiction.

## Trust & verifiability
`trust: community` — a popular aggregator, not an authoritative source; every hit must be re-verified in the originating county's official records, and payment prompts/clones treated with suspicion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arrests |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
