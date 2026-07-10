---
id: offender-tracking-information-system-otis
name: Michigan OTIS (Offender Tracking Information System)
description: Use when you have a `name` of someone possibly in the Michigan corrections system and want their status, photo, physical description and location — returns image, physical-description, address and dob.
url: https://mdocweb.state.mi.us/OTIS2/otis2.aspx
category: public-records
path:
- public-records
bestFor: Looking up Michigan prisoners, parolees, probationers and absconders by name — status, mugshot, physical description, offense and current facility/supervision.
selectorsIn:
- name
selectorsOut:
- image
- physical-description
- address
- dob
status: live
pricing: free
costNote: Free public service of the Michigan Department of Corrections; no account or payment required.
opsec: passive
opsecNote: You query the state corrections database, not the subject, so nothing is disclosed to the person. Fully passive; standard state web-server logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Michigan Department of Corrections system; the offender status, location and identifying data are authoritative first-party government records.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- OTIS
- Michigan OTIS
- MDOC Offender Search
tags:
- court
- inmate
- corrections
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Michigan OTIS (Offender Tracking Information System)

> The Michigan Department of Corrections' public offender lookup — search by name to confirm whether a person is a prisoner, parolee, probationer or absconder, with photo, physical description and current location.

## When to use
You have a `name` and want to know whether the subject is (or has been) in the Michigan corrections system, and if so, where they are and their status. This is a strong missing-person branch: incarceration or supervision explains a disappeared trail, and the record supplies a mugshot (`image`), physical identifiers, offense, sentence dates, and a current facility or supervision `address`. Absconder status is directly relevant when someone has gone missing from supervision.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the OTIS search at the URL.
2. Enter the subject's last name and first name; optionally narrow with sex, race, age, or "marks, scars & tattoos".
3. Set the offender-status filter (Active, Prisoner, Parolee, Probationer, Discharged, Parole/Probation Absconder) — or leave broad to catch any status.
4. Open a matching record: photo (`image`), height/weight/eye/hair and identifying marks (`physical-description`), date of birth (`dob`), current facility or supervising office (`address`), offense(s) and dates.
5. Pivot: a discharge/absconder date anchors a timeline; a facility feeds visitation/records angles; identifying marks corroborate other sightings.

## Inputs → Outputs
- **In:** `name` (optionally sex/race/age/marks)
- **Out:** `image` (mugshot), `physical-description` (height/weight/eyes/hair/tattoos), `address` (facility/supervision location), `dob`
- **Empty/negative result looks like:** "no offenders found" — meaning no Michigan corrections record under that name/filter; it says nothing about other states' systems.

## Gotchas & OpSec
- **Michigan only** — for other states use their equivalent DOC lookup or the federal BOP inmate locator; absence here is not absence everywhere.
- Names can be spelled/aliased differently; try alternate spellings and loosen filters if a known subject doesn't appear.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with the Federal BOP inmate locator and other state DOC search tools, plus court-record tools like `[[the-courts-of-british-columbia-home]]`-style portals — check the corrections system alongside court judgments to build the full legal picture.

## Trust & verifiability
`trust: trusted` — authoritative first-party data from the Michigan Department of Corrections.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | offender-tracking-information-system-otis |
| category | public-records |
| selectorsIn → selectorsOut | name → image, physical-description, address, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
