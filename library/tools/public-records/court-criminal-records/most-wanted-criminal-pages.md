---
id: most-wanted-criminal-pages
name: FBI Most Wanted / Fugitives
description: Use when you have a `name`, `image` or `physical-description` and want to check the FBI's wanted lists — returns fugitive profiles with photos, aliases, physical details and known associates.
url: https://www.fbi.gov/wanted/fugitives
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Checking whether a person appears on the FBI's wanted/fugitive lists and pulling their profile.
selectorsIn:
- name
- physical-description
selectorsOut:
- name
- image
- physical-description
- associate
status: live
pricing: free
costNote: Free official U.S. government resource; no account.
opsec: passive
opsecNote: Browsing the FBI's public wanted pages is passive and anonymous; nothing is sent to any subject. If you recognize a fugitive, use the official tip channels rather than approaching anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official FBI publication; profiles are authoritative U.S. law-enforcement records, though wanted status changes as cases resolve.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- most-wanted
- sex-offender-registry-websites
- vault-fbi-gov
- fbi-common-fraud-schemes-united-states
- fbi-information-technology-united-states
- federal-bureau-of-investigations-value
aliases:
- FBI Most Wanted
- FBI Fugitives
- FBI Ten Most Wanted
tags:
- fbi
- wanted
- fugitives
- law-enforcement
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# FBI Most Wanted / Fugitives

> The FBI's official wanted and fugitive listings — authoritative profiles with photos, aliases, physical descriptors and case details for people sought by U.S. law enforcement.

## When to use
You have a `name`, alias, `image`, or `physical-description` and need to check whether the person is a wanted fugitive, or you're working a case where a subject may intersect with FBI-sought individuals (fugitives, missing persons, kidnapping/ViCAP, seeking-information). Each profile carries photos, aliases, DOB, physical characteristics (height, weight, eyes, scars/marks), last-known locations and sometimes named associates — directly useful for identification and for corroborating an identity against an official record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.fbi.gov/wanted and browse categories (Ten Most Wanted, Fugitives, Kidnappings/Missing Persons, Seeking Information) or use the site search.
2. Search or scan by `name`/alias; open a profile to read photos, physical descriptors, aliases, reward, and case narrative.
3. Compare photos and physical details against your subject; note aliases and locations as new leads.
4. Pivot: aliases feed username/name enumeration; named associates feed `associate` mapping; the field office/jurisdiction narrows geography. Report genuine matches via the official FBI tip line — do not act on them yourself.

## Inputs → Outputs
- **In:** `name`/alias or `physical-description` (and a photo to compare)
- **Out:** `name`/aliases, `image` (wanted photos), `physical-description`, and `associate`/location details from the profile
- **Empty/negative result looks like:** no match — the person isn't on FBI wanted lists (they may be sought by state/local agencies or Interpol instead); absence here is not a clearance.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; report matches through official channels only.
- Scope is FBI/federal — state, local and international wanted persons appear on other registries (state DOJ, Interpol Red Notices), so check those too.
- Wanted status is a snapshot; profiles are removed as fugitives are captured or cases close, so verify currency and never treat a listing as a substitute for law-enforcement contact.

## Overlaps ("do both")
- Pairs with `[[sex-offender-registry-websites]]`, state most-wanted lists and Interpol notices — the FBI list covers federal cases; running the others catches subjects wanted at other jurisdictional levels.

## Trust & verifiability
`trust: trusted` — an authoritative official FBI resource; profiles are reliable, but confirm current status (captured/removed) and defer to law enforcement for any action.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | most-wanted-criminal-pages |
| category | public-records |
| selectorsIn → selectorsOut | name, physical-description → name, image, physical-description, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
