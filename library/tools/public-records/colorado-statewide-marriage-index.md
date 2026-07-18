---
id: colorado-statewide-marriage-index
name: Colorado Statewide Marriage Index
description: Use when you have a `name` and want to find their Colorado marriage record (1953–2006) — returns spouse `name`/`associate` and marriage `dob` (date) and county.
url: https://familysearch.org/search/collection/1932434
category: public-records
path:
- public-records
bestFor: Confirming a marriage in Colorado (1953–2006) and identifying the spouse and date/county.
selectorsIn:
- name
selectorsOut:
- name
- associate
- dob
status: live
pricing: free
costNote: Free to search and view via FamilySearch; requires a free FamilySearch account to see full record details.
opsec: passive
opsecNote: Passive — you search a historical vital-records index; no living subject is notified. FamilySearch requires a (free) login, so your searches are tied to that account; use a research/sock-puppet account if attribution matters.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hosted by FamilySearch (operated by the nonprofit that runs the largest genealogy archive); indexed from official Colorado state vital records.
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
- familysearch-2
- familysearch-research-wiki
- alabama-deaths
- familysearch-births-and-baptisms-1972-1981-australia
- familysearch-deaths-and-burials-1816-1980-australia
- familysearch-free-family-trees-and-genealogy-archives-familysearch-org
- familysearch-guessing-a-name-variation
aliases:
- Colorado Marriage Index 1953-2006
tags:
- toddington
- curated-directory
- specialty-search
- vital-records
- marriage
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Colorado Statewide Marriage Index

> A free FamilySearch index of Colorado marriages from 1953 to 2006 — tie a name to a spouse, date, and county.

## When to use
You have a `name` and reason to think the person married in Colorado between 1953 and 2006, and you want to confirm the marriage, identify the spouse (`associate`), and get the date and county. Marriage records are strong pivots: a spouse's `name` opens a new identity to research, maiden/married-name links resolve name changes, and the county gives a `geolocation` anchor for a period of the person's life.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the collection at FamilySearch (collection 1932434) and sign in with a free account.
2. Search by the subject's `name` (try maiden and married surnames); optionally filter by year range or county.
3. Review matches: bride/groom names, marriage date, and county.
4. Open a record for full indexed detail and note the spouse (`associate`) and date (`dob`-style event date).
5. Pivot: the spouse's name feeds people-search and other vital-records lookups; the county/date anchors a residence timeline.

## Inputs → Outputs
- **In:** `name` (maiden and/or married surname), optional year/county.
- **Out:** matched marriage record(s) with both spouses' `name`s (`associate`), marriage date, and county.
- **Empty/negative result looks like:** no matching index entry — meaning no Colorado marriage in 1953–2006 under that name (or a spelling/date outside the index), not proof the person never married.

## Gotchas & OpSec
- Bounded coverage: **Colorado only, 1953–2006** — marriages elsewhere or outside those years won't appear.
- Login required: FamilySearch needs a free account to view records.
- Index, not image: it's a transcribed index; verify against the original certificate for legal/critical use, watch for transcription errors and name variants.
- OpSec: passive; searches are tied to your FamilySearch login.

## Overlaps ("do both")
- Pairs with the broader `[[familysearch]]` / `[[family-search]]` collections and other state vital-records indexes — this is the Colorado marriage slice; combine with death/birth indexes to build a full life timeline.

## Trust & verifiability
`trust: trusted` — FamilySearch-hosted and indexed from official Colorado vital records; authoritative as an index, with original-image verification recommended for evidentiary use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | colorado-statewide-marriage-index |
| category | public-records |
| selectorsIn → selectorsOut | name → name, associate, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
