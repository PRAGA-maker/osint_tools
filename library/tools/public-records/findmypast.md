---
id: findmypast
name: FindMyPast
description: Use when you have a `name` and want genealogy/vital records — returns census, birth/marriage/death, military and newspaper matches exposing relatives (`associate`), `dob` and historical `address`es.
url: https://search.findmypast.com/search-world-records
category: public-records
path:
- public-records
bestFor: Deep UK/Ireland-focused family-history research — census, BMD, military, and newspaper records.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- address
status: live
pricing: freemium
costNote: Free to search and see record counts/previews; viewing full record images/transcripts requires a paid subscription or pay-per-view credits.
opsec: passive
opsecNote: Read-only genealogy search; the subject is not notified. Registration and payment expose your identity to the operator (DC Thomson) — use a sock-puppet account and billing hygiene.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A major, reputable genealogy service; official records (census, BMD, military) are authoritative, but user-submitted trees and hints are unverified.
missingPersonsRelevance: high
coverage:
- uk
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- genesreunited-co-uk
- gro-gov-uk
- sortedbyname-com
aliases:
- Find My Past
- findmypast world records
tags:
- genealogy
- family
- family-history
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# FindMyPast

> A major genealogy service, strongest on UK/Ireland — census, BMD, military, and newspaper archives to map a subject's relatives, dates, and historical addresses.

## When to use
You have a `name` and want to build the family and historical picture: census entries (placing a household at an `address` in a given year), birth/marriage/death records (`dob`/dates), military service records, and even newspaper mentions. For a missing-persons case this identifies next of kin (`associate`), prior addresses, and family context that disambiguates namesakes and opens contact routes. Coverage is broad, with particular depth for the UK and Ireland.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search.findmypast.com/search-world-records and register (use a **sock-puppet** account).
2. Search by `name`, narrowing with approximate year, place, and record type.
3. Free tier: see match counts and limited previews. Full record images/transcripts require a subscription or PPV credits.
4. Read the records: census households (relatives + historical `address`), BMD dates (`dob`), military and newspaper hits.
5. Corroborate user-tree hints against primary records before relying on them.
6. Pivot: relatives (`associate`) feed people-search; a UK death feeds `[[gro-gov-uk]]`; cross-check via `[[genesreunited-co-uk]]` / `[[sortedbyname-com]]`.

## Inputs → Outputs
- **In:** `name` (+ approximate year/place/record type)
- **Out:** census (relatives + historical `address`), BMD (`dob`/dates), military/newspaper records, family trees (`associate`)
- **Empty/negative result looks like:** zero match counts (the name isn't in the indexed records, or is spelled differently), or matches locked behind the paywall. Free counts tell you whether anything exists before you pay.

## Gotchas & OpSec
- Human-in-the-loop: **account required**, full records **paywalled** (subscription/PPV).
- User-submitted trees/hints are **unverified** — official census/BMD/military are authoritative.
- Living-person detail is limited by data-protection; strongest for historical records.
- OpSec: **passive** toward the subject; your account/billing is visible to the operator.

## Overlaps ("do both")
- Pairs with `[[genesreunited-co-uk]]` (overlapping UK census/tree data), `[[gro-gov-uk]]` (official UK BMD index), and `[[sortedbyname-com]]` — different indexes and record sets, so run several and cross-confirm family links.

## Trust & verifiability
`trust: community` — authoritative official records plus unverified user trees; corroborate any tree-derived link against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findmypast |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
