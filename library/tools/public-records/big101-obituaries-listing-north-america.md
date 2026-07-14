---
id: big101-obituaries-listing-north-america
name: Big101 Obituaries Listing (North America)
description: Use when you have a `name` (and a US state/Canadian region) and want to find an obituary/death notice — a meta-directory of newspaper obituary pages and death indexes returning death date, locality and family.
url: http://www.big101.com/OBITUARIES101.htm
category: public-records
path:
- public-records
bestFor: Locating a deceased subject's obituary via a state-by-state directory of North American newspaper death notices and indexes.
selectorsIn:
- name
selectorsOut:
- dob
- name
- associate
status: live
pricing: free
costNote: Free directory of links. The obituary pages it points to are mostly free, though some newspaper archives may paywall older notices.
opsec: passive
opsecNote: Passive — you follow public obituary links; nothing about the subject is submitted to any monitored system and no alert is generated.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party link directory (not a data source itself); usefulness depends on the linked newspapers and whether their links are still live. Some links may be dead.
missingPersonsRelevance: high
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- sysoon-deceased-database
aliases:
- Obituaries101
- big101 obituaries
tags:
- toddington
- curated-directory
- specialty-search
- deceased
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Big101 Obituaries Listing (North America)

> A meta-directory that consolidates hundreds of North American newspaper obituary pages and death indexes by state/province — a jumping-off point for finding a death notice from a name.

## When to use
You suspect a subject may be deceased and you know roughly where (a US state or Canadian province). This page routes you to the local newspaper obituary sections and national death sources for that area, plus historical indexes and the Social Security Death Index — useful for confirming a death, its date, funeral home, and surviving family (associate leads). It's a directory of links, not a single searchable database.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.big101.com/OBITUARIES101.htm.
2. Use the state/province navigator to jump to the subject's likely location; pick a local newspaper's obituary section (or a national source / SSDI link).
3. Search that newspaper's obituaries for the subject `name`.
4. Read the output: an obituary giving death date (and often `dob`/age), locality, funeral home, and surviving relatives' names (`associate`). Confirm identity with location and family details.
5. Pivot: death date/DOB feeds official death-record confirmation; surviving-family names feed people-search and next-of-kin contact; funeral home/locality corroborate geography.

## Inputs → Outputs
- **In:** `name` (+ approximate US state / Canadian region)
- **Out:** `dob`/death date, `name` (full/aliases), `associate` (surviving family)
- **Empty/negative result looks like:** no obituary in the linked papers — inconclusive (small/local deaths may go unpublished online, or the link is dead), NOT proof the person is alive.

## Gotchas & OpSec
- It's a link hub — some links rot, and coverage skews to papers that publish obituaries online. A miss isn't conclusive.
- Older notices may be paywalled in newspaper archives.
- OpSec: fully passive; public obituary data.

## Overlaps ("do both")
- Pairs with [[sysoon-deceased-database]] and official death indexes — this routes you to primary newspaper obituaries by locality, those provide aggregated/searchable death records. Run both to confirm a death.

## Trust & verifiability
`trust: unverified` — a third-party directory, not an authoritative source; the value lies in the primary obituaries it links to. Confirm any death against the actual obituary and an official record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | big101-obituaries-listing-north-america |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, name, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
