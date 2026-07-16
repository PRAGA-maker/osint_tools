---
id: gov-im-4
name: Isle of Man Deeds, Probate & Land Registry Search
description: Use when you have a name or property on the Isle of Man and want official deed/probate/land records — returns registered documents including wills, grants of probate and land dealings.
url: https://services.gov.im/deeds-probate-land-registry-document-search/
category: public-records
path:
- public-records
bestFor: Searching official Isle of Man deeds, probate (wills/grants) and land-registry documents by surname or property.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- name
- address
- associate
- document-id
status: live
pricing: freemium
costNote: Searching the index is free; viewing/downloading document images is a paid purchase per document. Images stay in your account for 30 days once bought.
opsec: passive
opsecNote: You query the Isle of Man government registry, not the subject — no notification is sent. The service logs access and requires account/payment to view images; use lawful public-record scope. VPN for sensitive lookups.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Isle of Man Government Deeds & Probate / Land Registry online service; records are authoritative government registrations.
missingPersonsRelevance: high
coverage:
- im
auth: none
api: false
localInstall: false
registration: false
aliases:
- Isle of Man Deeds and Probate Registry
- IoM land registry search
- services.gov.im deeds probate
tags:
- propertysites
- Property Related Sites
- probate
- isle-of-man
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- gov-im
- gov-im-2
- gov-im-3
- gov-im-5
---

# Isle of Man Deeds, Probate & Land Registry Search

> The Isle of Man's official online registry — search deeds, wills/grants of probate, and land dealings by surname or property to tie a person to property, estates and their heirs.

## When to use
Your subject has an Isle of Man connection — property, an estate, a business, or a deceased relative there. This registry lets you search by surname (or property) across three record types: **deeds** (property and other registered dealings), **probate** (grants of probate with the wills and, from 2006, the court application documents), and the **land registry**. A will names executors and beneficiaries; a deed ties a name to a property and often to co-parties — both are strong for confirming identity, family links and assets.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://services.gov.im/deeds-probate-land-registry-document-search/.
2. Choose the record type (Deeds, Probate, or Land) — note that a Deeds search won't return probate documents and vice versa, so run each type separately.
3. Start with a single criterion (usually a **surname**) and only narrow further if you get too many hits — over-specifying can hide relevant records.
4. Review the index of matching documents (parties, dates, `document-id`). Purchase/download the image for the ones you need.
5. Pivot: a will's executors/beneficiaries are `associate`s to chase; a deed's property `address` and co-owners feed people/address lookups.

## Inputs → Outputs
- **In:** `name` (surname), `address`/property, or `employer-org`
- **Out:** registered `document-id`s, party `name`s, property `address`, and `associate`s (executors, beneficiaries, co-parties)
- **Empty/negative result looks like:** no index match. Records run from 1911 onward (pre-1911 are in the Manx Museum archives), so a gap may be an era limit, a spelling variant, or an over-narrowed query — retry with just the surname.

## Gotchas & OpSec
- Search each record type separately; a Deeds query will miss probate and land, and vice versa.
- Index browsing is free but **viewing document images is paid** per document (human-in-the-loop payment step); bought images persist 30 days in your account — download to keep.
- Start broad (surname only); adding fields too early causes you to miss records, per the registry's own guidance.
- Pre-1911 records aren't online — route those to the Manx Museum Library & Archives.

## Overlaps ("do both")
- Pairs with UK-wide probate and Land Registry tools — the Isle of Man is a separate jurisdiction, so a subject's estate/property may split across both.
- Feeds people-search on executors/beneficiaries surfaced from a will.

## Trust & verifiability
`trust: trusted` — this is the first-party Isle of Man Government registry, so the documents are authoritative legal records; the free index is a pointer, and the purchased document image is the verifiable evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-im-4 |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → name, address, associate, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
