---
id: archives
name: Archives.com (Death & Vital Records)
description: Use when you have a `name` and want US death, obituary and vital records to confirm a death, approximate DOB and relatives — returns dob, name, associate.
url: https://www.archives.com/search/death
category: public-records
path:
- public-records
bestFor: Confirming whether a subject has died and pulling DOB, death date, place and named relatives from US death/obituary/vital records.
selectorsIn:
- name
selectorsOut:
- dob
- name
- associate
- address
- document-id
status: live
pricing: freemium
costNote: Searching (name + optional year/state) is free and returns match previews, but viewing full record details requires a paid Archives.com subscription / free-trial signup (Archives.com is an Ancestry-owned service).
opsec: passive
opsecNote: Searching genealogy/death indexes is passive and does not alert anyone. A subscription/trial ties record views to a billing identity — use a dedicated account, not one linked to your real identity, if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Archives.com / Ancestry, a major commercial genealogy provider indexing official death, SSDI, obituary and cemetery records; data provenance is reputable though completeness varies by state and era.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: true
invitationOnly: false
aliases:
- Archives.com
- Archives death search
tags:
- genealogy
- family
- death-records
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Archives.com (Death & Vital Records)

> An Ancestry-owned genealogy service with billions of US death, obituary, SSDI and cemetery records — the go-to free-to-search check for "is this person deceased, and who are their relatives?"

## When to use
You have a `name` and need to establish whether the subject has died — a common branch in missing-person and cold-case work — or you want to anchor a `dob`, death date/place, and named next-of-kin. Death and vital records are among the most reliable identity anchors, and confirming a death redirects the whole investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.archives.com/search/death.
2. Enter last name (required), first name, and optionally death year and state to narrow.
3. Read the free result previews: name, approximate age/DOB, death year and location, record type (SSDI, obituary, cemetery).
4. To see full details (exact dates, relatives named in obituaries, document images) you must start a subscription/free trial — the paywall gates the record body, not the search.
5. Pivot: relatives named in an obituary become new `name`/`associate` leads; a death place/`address` feeds local records; a confirmed death closes or redirects the case.

## Inputs → Outputs
- **In:** `name` (+ optional death year, state)
- **Out:** `dob`/age, death date & place, `name`, `associate` (relatives from obituaries), `address` (last residence/burial), `document-id` (record references)
- **Empty/negative result looks like:** no matching death record — meaning the person isn't in these indexes (may be alive, recent, or outside coverage), NOT proof they are alive; corroborate with SSDI/state records.

## Gotchas & OpSec
- Freemium: the search preview is free but detailed record content is behind the Ancestry/Archives paywall (payment-wall-partial).
- Coverage skews US and varies by state and time period; recent deaths lag.
- Common names return many candidates — disambiguate with year/state before attributing.
- OpSec: passive; only the billing account for a subscription is attributable.

## Overlaps ("do both")
- Pairs with free obituary/newspaper searches and state death indexes — Archives aggregates broadly, while a targeted local obituary confirms specifics and names relatives without a paywall.

## Trust & verifiability
`trust: trusted` — a major commercial genealogy provider (Ancestry-owned) indexing official/published death records; provenance is solid, but completeness varies, so confirm a match against a second source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archives |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, name, associate, address, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
