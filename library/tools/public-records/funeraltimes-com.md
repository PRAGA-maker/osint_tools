---
id: funeraltimes-com
name: Funeral Times
description: Use when you have a `name` and want Northern Ireland / Ireland death and funeral notices — returns name, dob (death date), address, associate.
url: https://www.funeraltimes.com/
category: public-records
path:
- public-records
bestFor: Finding a subject's death/funeral notice across Northern Ireland and Ireland — death date, funeral location and named relatives.
selectorsIn:
- name
selectorsOut:
- name
- dob
- address
- associate
status: live
pricing: free
costNote: Free to search and read; free optional registration only adds alerts, condolences and a personal diary.
opsec: passive
opsecNote: Reading published death notices is passive and does not alert anyone. Only register (free) with a sock-puppet identity if you want alerts; posting a condolence would be an attributable, visible action — don't.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely used Northern Ireland/Ireland funeral-notice aggregator; notices are submitted by families/funeral directors, so details are generally reliable but self-published and unverified.
missingPersonsRelevance: high
coverage:
- gb
- ie
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- FuneralTimes
- funeraltimes.com death notices
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- death-notices
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Funeral Times

> The go-to death- and funeral-notice board for Northern Ireland and Ireland — search a name to confirm a death and pull the funeral date/place plus family named in the notice.

## When to use
You have a `name` tied to Northern Ireland or the Republic of Ireland and need to establish whether the person has died, when and where the funeral is/was, and who their relatives are. Death and funeral notices are a rich, free source for confirming a death, anchoring a death date, and enumerating next-of-kin — a common branch in missing-person and genealogy work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.funeraltimes.com/death-notices.
2. Search by `name`, and/or filter by county (Belfast, Antrim, Armagh, Down, Fermanagh, Derry/Londonderry, Tyrone, Dublin and other Irish counties).
3. Read the notice: name, date of death, address/townland, funeral service location and time (often with a map), and family members named (spouse, children, siblings).
4. Pivot: named relatives become `associate`/`name` leads; the townland/address is a `geolocation`; the death date anchors record searches elsewhere.

## Inputs → Outputs
- **In:** `name` (optionally + county)
- **Out:** `name`, `dob` (death date, sometimes age), `address` (residence/townland, funeral venue), `associate` (relatives named in the notice)
- **Empty/negative result looks like:** no notice — meaning none was published here (person alive, elsewhere, or notice placed only in print/another site), NOT proof of anything; check RIP.ie and local funeral directors too.

## Gotchas & OpSec
- Regional scope: strong for Northern Ireland and Ireland, thin elsewhere.
- Notices are family/undertaker-submitted and self-published — names/relationships are generally accurate but unverified.
- OpSec: passive for reading; do not post condolences or use a real-name account.

## Overlaps ("do both")
- Pairs with RIP.ie and individual funeral-director notice pages — coverage overlaps only partly, so a death missing here may appear on another; run both.

## Trust & verifiability
`trust: community` — a real, well-used notice aggregator, but entries are self-submitted by families/funeral directors, so corroborate the death and relationships against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | funeraltimes-com |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
