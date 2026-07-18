---
id: mugshots-com
name: Mugshots.com
description: Use when you have a `name` (+ US location) and want to check for a booking record — returns arrest mugshot `image`, charges, and booking details, all needing careful verification.
url: https://mugshots.com
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Checking whether a name has a publicly-posted US arrest/booking record with photo and charges.
selectorsIn:
- name
- geolocation
selectorsOut:
- image
- physical-description
- document-id
status: live
pricing: free
costNote: Free to search and view arrest listings; the site states it does not charge for removal.
opsec: passive
opsecNote: Browsing public arrest listings is passive and unseen by the subject. Ethically and legally sensitive: an arrest is not a conviction, records may be expunged or wrong, and these aggregators are widely criticised — treat any hit as an unverified lead, protect the subject's presumption of innocence, and confirm against the official court/sheriff source before relying on or repeating it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party aggregator that re-publishes booking data scraped from many jurisdictions; coverage is patchy, records go stale (no update after charges are dropped/expunged), and the site is a commercial re-publisher, not an authoritative source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mugshots
aliases:
- Mugshots.com
tags:
- court-criminal-records
- arrest-records
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Mugshots.com

> A US arrest-record aggregator — searchable booking photos and charges scraped from many jurisdictions. Useful as a lead, but low-trust and ethically fraught: verify everything at the source.

## When to use
You have a `name` (ideally with a US state/county) and want to check whether there's a publicly-posted **arrest/booking record** — a mugshot, listed charges, booking date, and physical descriptors (age, height). This can corroborate identity, surface a location at a point in time, or flag an event to investigate further. Because these aggregators are unreliable and often out of date, use a hit only to point you at the **authoritative** record (the county sheriff/court), never as the finding itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://mugshots.com and search the `name` (add state/county to disambiguate).
2. Open a matching record and read: the mugshot `image`, listed **charges**, booking date/agency, and any physical descriptors (age/DOB, height, weight).
3. **Verify at source:** take the county, booking date and charges to the relevant sheriff's booking log or court records system and confirm — this is essential.
4. Check the current disposition: an arrest may have led to no charge, dismissal, acquittal, or expungement not reflected here.
5. Pivot: a confirmed booking gives a location + date and physical description; the official court record gives the reliable detail.

## Inputs → Outputs
- **In:** `name` (+ `geolocation`)
- **Out:** mugshot `image`, `physical-description` (age/height/weight), charges and booking `document-id` details
- **Empty/negative result looks like:** no listing — the person has no booking record *that this site scraped and kept* (many jurisdictions aren't covered, and records can be removed). Absence here is weak evidence of anything; it is not a clean-record check.

## Gotchas & OpSec
- Human-in-the-loop: none technically, but **exercise judgement**: an arrest is not a conviction, and misidentification is common with shared names.
- OpSec: **passive** — the subject isn't alerted.
- **Low trust / ethical care:** mugshot aggregators are notorious for stale, incomplete, and sometimes wrongly-attributed data, and for reputational harm. Do not treat a listing as fact, do not republish it, and always confirm against the official record.
- US-only and jurisdiction-patchy; coverage gaps are large.

## Overlaps ("do both")
- Always do both with the **authoritative** source — the county sheriff booking log and the state/county court records system — which give verified, current dispositions. Cross-check identity with people-search tools to avoid same-name misattribution.

## Trust & verifiability
`trust: unverified` — a commercial re-publisher of scraped booking data; useful only as a pointer to the official record, which is where verification and current disposition must come from.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mugshots-com |
| category | public-records |
| selectorsIn → selectorsOut | name, geolocation → image, physical-description, document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
