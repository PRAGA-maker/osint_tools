---
id: findmypast-ie
name: findmypast.ie
description: Use when you have a `name` and Irish ancestry/context and want historical records (census, BMD, church, migration) to build family and identity links — returns associate, dob and address history.
url: https://www.findmypast.ie/
category: public-records
path:
- public-records
bestFor: Irish and UK genealogy record research — census, births/marriages/deaths, church, and migration records to reconstruct family trees and confirm identities.
selectorsIn:
- name
- dob
selectorsOut:
- associate
- dob
- address
status: live
pricing: freemium
costNote: Searching the record indexes is free; viewing full record images/transcripts requires a paid subscription or pay-as-you-go credits.
opsec: passive
opsecNote: You search a historical-records archive, not the living subject; no target-facing signal is sent. Register a sock-puppet account for the paid tier to keep research off a personal identity.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Findmypast is a major, established commercial genealogy provider digitising official and institutional records; transcriptions can contain errors but sources are authoritative.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- ancestry
- findmypast-co-uk
aliases:
- Findmypast Ireland
- findmypast.ie
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- ireland
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# findmypast.ie

> The Irish edition of Findmypast — a large commercial genealogy archive for census, BMD, church, and migration records to reconstruct family and identity links.

## When to use
You have a `name` (and ideally an approximate `dob`/era and Irish or UK context) and need to build out a family tree, confirm relatives, or trace a historical identity. Genealogy records are a powerful missing-persons lever: they surface `associate` links (parents, siblings, spouses), birth/death dates, and past `address` history that living-person databases lack — especially for older or cold cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.findmypast.ie/ and register (a sock-puppet account for paid access).
2. Search a record set (census, births/marriages/deaths, church, passenger/migration) by `name` + place/date.
3. Read the free index result; unlock the full record image/transcript with a subscription or credits.
4. Cross-reference across record sets to confirm a person and their family.
5. Pivot: relatives feed associate mapping; a confirmed `dob`/birthplace anchors other records; migration records tie Irish and diaspora identities together.

## Inputs → Outputs
- **In:** `name` (+ approximate `dob`/place)
- **Out:** `associate` (family members), `dob` (birth/death dates), `address` (historical residences)
- **Empty/negative result looks like:** no matching record — the event may predate/postdate the digitised sets, be mis-transcribed, or simply not survive. Try spelling variants before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: index search is free but record images sit behind a paywall and login.
- Transcriptions carry OCR/indexing errors and name variants — search fuzzily and verify against the source image.
- OpSec: passive; a historical archive, not the living subject.

## Overlaps ("do both")
- Pairs with `[[ancestry]]` and `[[findmypast-co-uk]]` — record coverage differs by collection and country, so a record missing on one is often present on another.

## Trust & verifiability
`trust: trusted` — an established provider digitising official/institutional records; the underlying sources are authoritative even though transcriptions should be checked against the original images.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findmypast-ie |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → associate, dob, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
