---
id: iaea-online-org
name: iaea-online.org
description: Use when you need to find or verify a UK/international independent automotive engineer assessor by location/specialty — returns a matching professional's name, area and contact details.
url: https://www.iaea-online.org/find-an-engineer
category: public-records
path:
- public-records
bestFor: Locating or verifying a member automotive engineer assessor (e.g. for vehicle forensics/valuations) by area and type of work.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- name
- address
- social-profile
status: live
pricing: free
costNote: Free public "find an engineer" directory run by a professional body; no account needed. You contract directly with the independent member, not the IAEA.
opsec: passive
opsecNote: Passive — you browse a public professional directory; no subject is contacted through the lookup itself. If you then phone/email a listed assessor you are contacting that professional directly, which is overt.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Institute of Automotive Engineer Assessors (IAEA), a UK learned society and registered charity; membership listings are authoritative for verifying an assessor's professional standing.
missingPersonsRelevance: high
coverage:
- uk
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Institute of Automotive Engineer Assessors
- IAEA find an engineer
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# iaea-online.org

> The Institute of Automotive Engineer Assessors' member directory — find or verify an independent automotive engineer assessor by location and specialty.

## When to use
Two cases: (1) your subject is (or claims to be) an automotive engineer assessor and you want to **verify** that professional identity and find their listed area/contact; or (2) you need to *engage* an independent vehicle expert — pre-purchase inspection, valuation, forensic/accident investigation — as part of a wider trace (e.g. tying a vehicle to a person). It's a niche professional-licensing source: narrow, but authoritative for this trade.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.iaea-online.org/find-an-engineer.
2. Filter by type of work (pre-purchase, valuation, forensic investigation, etc.), and by postcode/town and country (UK, Ireland, and several other countries).
3. Read the returned member listing: assessor `name`, coverage area, and contact details.
4. To verify a claimed membership, search the person's name/area and confirm they appear.
5. Pivot: a confirmed member `name`/area feeds people-search and professional-background checks; contact details corroborate a business identity.

## Inputs → Outputs
- **In:** type of work + location (`address`), or a `name`/`employer-org` to verify
- **Out:** matching member `name`, coverage area (`address`), contact (`social-profile`)
- **Empty/negative result looks like:** no members for that area/specialty (coverage is thin outside the UK), or a claimed name not appearing — the latter is a useful negative for membership verification, though absence could also mean lapsed/non-membership.

## Gotchas & OpSec
- Narrow scope: only IAEA member automotive assessors — not a general engineer or people directory.
- Best coverage is UK; other countries have sparse listings.
- OpSec: **passive** to browse; contacting a listed assessor is overt, direct outreach.

## Overlaps ("do both")
- Pair with general people-search and UK company/registry tools — this confirms the *professional* credential/area; those add personal address, employer and history the directory omits.

## Trust & verifiability
`trust: trusted` — a professional body's own membership directory, authoritative for verifying an assessor's standing. Just note it only covers its members, so treat non-appearance as "not an IAEA member," not "not an engineer."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iaea-online-org |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → name, address, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
