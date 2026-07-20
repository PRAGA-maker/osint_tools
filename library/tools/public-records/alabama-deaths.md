---
id: alabama-deaths
name: Alabama Deaths
description: Use when you have a `name` and want an Alabama death record (1908–1974) — returns dob, address, and associate (next-of-kin) links from the FamilySearch collection.
url: https://familysearch.org/search/collection/1307888
category: public-records
path:
- public-records
bestFor: Confirming an Alabama death and pulling dates, residence, and family links for genealogy timelines.
selectorsIn:
- name
- dob
selectorsOut:
- dob
- address
- associate
status: live
pricing: free
costNote: Free to search and view; requires a free FamilySearch account to see full record details.
opsec: passive
opsecNote: Searching indexed historical death records; the deceased and living relatives are not notified. You must be logged into a FamilySearch account to view full images, so those queries tie to your account — use a research/sock-puppet account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by FamilySearch (a non-profit run by the LDS Church); the collection indexes official Alabama state death records.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- family-search
- familysearch
- familysearch-org
- familysearch-research-wiki
- colorado-statewide-marriage-index
- familysearch-2
- familysearch-births-and-baptisms-1972-1981-australia
- familysearch-deaths-and-burials-1816-1980-australia
- familysearch-free-family-trees-and-genealogy-archives-familysearch-org
- familysearch-guessing-a-name-variation
aliases:
- FamilySearch Alabama Deaths
- Alabama Deaths 1908-1974
tags:
- toddington
- curated-directory
- specialty-search
- genealogy
- vital-records
source: toddington-resources
lastVerified: '2026-07-20'
enrichment: full
---

# Alabama Deaths

> A FamilySearch index of Alabama state death records, 1908–1974 — a vital-records source for confirming a death and mapping family connections.

## When to use
You have a `name` for someone who may have died in Alabama between 1908 and 1974 and want to confirm the death, fix the date and place, and surface next-of-kin. This is a genealogy/vital-records tool: it closes out a subject's timeline and pivots to living relatives via the informant, spouse, or parents named on the record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://familysearch.org/search/collection/1307888 and sign in with a free FamilySearch account.
2. Enter the target `name`; narrow with an approximate death year, birth year, or county if known.
3. Read the indexed fields: name, death date, death place, age/birth date, and — depending on the record — parents' names, spouse, or informant.
4. Open the record detail (and image where available) to capture `associate` links (family members) and residence.
5. Pivot: relatives' names feed people-search on the living; a confirmed death date closes a missing-person timeline or redirects to descendants.

## Inputs → Outputs
- **In:** `name` (+ optional death/birth year, county)
- **Out:** `dob`, `address` (death/residence place), `associate` (family/informant names)
- **Empty/negative result looks like:** "No results" — the person isn't in this Alabama 1908–1974 index; they may have died elsewhere, in another year range, or the name is transcribed differently. Try spelling variants.

## Gotchas & OpSec
- Human-in-the-loop: a free FamilySearch **account login** is required to view full details/images.
- Scope is strictly Alabama, 1908–1974 — a common cause of false negatives; check adjacent FamilySearch collections for other states/years.
- Older indexes carry transcription errors; verify names/dates against the record image.
- OpSec: passive research; only your FamilySearch account activity is logged.

## Overlaps ("do both")
- Pairs with the broader [[familysearch-org]] / [[family-search]] search and [[colorado-statewide-marriage-index]] — do both to cross-state a person whose life events span jurisdictions.

## Trust & verifiability
`trust: trusted` — FamilySearch is a reputable non-profit indexing official Alabama state vital records; the underlying data is authoritative, subject only to indexing/transcription error.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alabama-deaths |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → dob, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
