---
id: sortedbyname-com
name: SortedByName.com
description: Use when you have a `name` and want genealogy/vital-record leads (births, marriages, deaths) indexed by surname — returns links to public records exposing `dob`, `address` and relatives (`associate`).
url: https://sortedbyname.com/
category: public-records
path:
- public-records
bestFor: Surname-first discovery of births, marriages, divorces and death records aggregated from public sources.
selectorsIn:
- name
selectorsOut:
- dob
- address
- associate
status: live
pricing: free
costNote: Free; a static, browsable/downloadable index (2M+ pages) linking to public genealogy and vital-record sources.
opsec: passive
opsecNote: Static pages of links to already-public records; nothing is submitted about your subject beyond the name you browse to, and there is no login. Use a clean session for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A one-person curated index (430M+ entries) pointing to public records (e.g. Texas state data, New York marriages via FOI); the underlying records are authoritative but the index is unofficial and coverage is uneven.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- cancelthesefunerals-com
- legacy-com
aliases:
- Sorted By Name
- sortedbyname
tags:
- genealogy
- vital-records
- death-records
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# SortedByName.com

> A surname-indexed gateway to public genealogy and vital records — 430M+ entries pointing at births, marriages, divorces, and deaths.

## When to use
You have a `name` and want to pull vital-record leads: a date of birth, a marriage/divorce, a death record, or the relatives that link a person to a family. Because it is organised by surname across millions of lightweight pages (and even allows downloading the files), it's a fast way to enumerate everyone with a given name and triangulate the right individual via associated relatives and dates — valuable for both confirming a death and mapping family for a missing person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sortedbyname.com/ and browse by first letter → surname.
2. Locate the surname page and scan entries for your subject; each links out to the underlying public record (state data, marriage indexes, etc.).
3. Follow the links to the source records for `dob`, `address`, marriage/death details, and relatives (`associate`).
4. Corroborate any death or vital event against a second source before relying on it.
5. Pivot: relatives (`associate`) feed people-search; a death lead feeds `[[cancelthesefunerals-com]]` and `[[legacy-com]]`.

## Inputs → Outputs
- **In:** `name` (surname-first)
- **Out:** links to public records → `dob`, `address`, marriage/divorce/death events, `associate` (relatives)
- **Empty/negative result looks like:** the surname page absent or no matching entry — coverage is uneven (US-heavy, e.g. Texas/New York), so absence means "not in this index," not "no record exists."

## Gotchas & OpSec
- Coverage is patchy and skewed to certain US states with strong public-records access; treat it as one index among many.
- It links to third-party records — verify at the source, and be aware some linked sites may be stale or moved.
- OpSec: **passive** — browsing a static index of public data.

## Overlaps ("do both")
- Pairs with `[[cancelthesefunerals-com]]` (Death Master File) and `[[legacy-com]]` (obituaries) — SortedByName surfaces the vital-record lead; the DMF confirms a federal death record and obituaries add the human/family detail.

## Trust & verifiability
`trust: community` — an unofficial curated index over authoritative public records; the records are real but coverage is incomplete, so corroborate every hit at its source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sortedbyname-com |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
