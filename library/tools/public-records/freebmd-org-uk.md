---
id: freebmd-org-uk
name: freebmd.org.uk
description: Use when you have a `name` and want English & Welsh birth, marriage, or death registrations — returns the registration event with quarter/year (`dob` lead), district (`address`), and marriage links (`associate`).
url: https://www.freebmd.org.uk/
category: public-records
path:
- public-records
bestFor: Finding historic England & Wales birth/marriage/death index entries by name to build a family/timeline.
selectorsIn:
- name
selectorsOut:
- name
- dob
- address
- associate
status: live
pricing: free
costNote: Free volunteer-transcribed index of the England & Wales civil registration index. Free registration lets you run more searches; no payment for the index itself (ordering the actual certificate from the GRO costs money).
opsec: passive
opsecNote: You search a historic public-records index; nothing reaches any living subject. Fully passive. Registering ties an email to your searches — use a sock-puppet address if you prefer.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-running charitable project transcribing the official GRO index for England & Wales. Highly regarded, but transcription is volunteer-driven and coverage is strongest ~1837–1992 and not 100% complete — verify against the GRO for certainty.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: true
relatedTools:
- gro-gov-uk
- ancestry
aliases:
- FreeBMD
- freebmd.org.uk
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- vital-records
- uk
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# freebmd.org.uk

> A free, searchable transcription of the England & Wales civil-registration index — births, marriages, and deaths from 1837 onward — for placing a person and reconstructing their family.

## When to use
You have a `name` connected to England or Wales and want to anchor a person in the civil record: a birth registration (giving a birth quarter/year — a `dob` lead — and registration district `address`), a marriage (linking spouses as `associate`s), or a death (quarter/year and district). Invaluable for tracing family relationships, confirming a historic identity, distinguishing people with the same name by district/date, and building the genealogical backbone of a missing-person or heir investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register (free) and sign in at https://www.freebmd.org.uk/.
2. Choose the type (Births / Marriages / Deaths) and search by surname + forename, narrowing by date range and registration district.
3. Read the index hits: name, quarter/year, registration district, and (for later years) mother's maiden name on births or age on deaths.
4. For marriages, note the same volume/page shared by spouses to link partners; for births, the mother's maiden surname links to a marriage.
5. Pivot: use the index reference to order the full GRO certificate (`[[gro-gov-uk]]`) for exact dates/addresses; corroborate the family tree in `[[ancestry]]`.

## Inputs → Outputs
- **In:** `name` (+ date range, district)
- **Out:** civil-registration index entries → `name`, birth/death quarter+year (`dob` lead), registration district (`address`), spouse links (`associate`)
- **Empty/negative result looks like:** no index entry — the event may be outside the transcribed coverage/date range, spelled differently, or not yet transcribed (FreeBMD is incomplete). Absence is not proof the event didn't occur; check the GRO index.

## Gotchas & OpSec
- Human-in-the-loop: none beyond the free login; be patient with transcription gaps and name variants.
- OpSec: **passive** — historic public records; no living subject is contacted.
- The index gives the *reference*, not the full detail — dates are only to the quarter and addresses to the district until you order the certificate. Coverage thins toward the most recent decades.

## Overlaps ("do both")
- Pairs with `[[gro-gov-uk]]` (order the actual certificate for exact date/place/parents) and `[[ancestry]]` (broader records + trees) — FreeBMD is the free index to *find* the reference; the others turn a reference into full, verified detail.

## Trust & verifiability
`trust: trusted` — a respected charitable transcription of the official index. Reliable as a finding aid, but volunteer-transcribed and incomplete, so treat entries as pointers to confirm against the GRO before relying on a specific date or relationship.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | freebmd-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
