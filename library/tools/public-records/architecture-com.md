---
id: architecture-com
name: architecture.com (RIBA Members Directory)
description: Use when you have a `name` and think the person is a UK architect — returns their RIBA chartered status, practice/employer-org, and professional location.
url: https://members.architecture.com/directory/default.asp?dir=3
category: public-records
path:
- public-records
bestFor: Confirming and locating a UK Chartered architect by surname via the official RIBA members directory.
selectorsIn:
- name
- geolocation
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free public directory of consenting RIBA Chartered Members; no account or payment required.
opsec: passive
opsecNote: A first-party professional-registry lookup; searching by surname raises no notice to the individual. No login needed, so the query is anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Royal Institute of British Architects (RIBA); an authoritative membership register, though it lists only ~28,000 members who consented to appear.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- RIBA Members Directory
- architecture.com directory
tags:
- professionlicensing
- Profession & Licensing Sites
- professional-register
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# architecture.com (RIBA Members Directory)

> The official RIBA register of ~28,000 consenting UK Chartered Members — a name-in, practice-and-location-out professional identity check.

## When to use
You have a `name` and a hint that the subject is (or claims to be) a UK architect, and you want to confirm the professional identity and place them at a firm. The directory turns a surname into a verified Chartered Member record: full name, the practice/`employer-org` they're attached to, and its `address`/location — useful for corroborating a career claim or finding a current work location for someone in the architecture field.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the directory URL and choose the member/architect search.
2. Enter the surname; pick a match mode (contains / starts with / exact) and, to narrow, add a location or postcode (`geolocation`).
3. Read the returned records: member name, chartered status, and associated practice with its address/contact.
4. Cross-check the practice against Companies House or the firm's own site for current employment.
5. Pivot: the practice (`employer-org`) feeds corporate-registry and staff-page searches; the location feeds local records.

## Inputs → Outputs
- **In:** `name` (surname), optional `geolocation` (location/postcode)
- **Out:** confirmed `name` + chartered status, `employer-org` (practice), practice `address`
- **Empty/negative result looks like:** "no members found" — means either the person isn't RIBA-chartered, isn't UK-registered, or (importantly) did not consent to appear in the public directory. Absence is not proof they aren't an architect.

## Gotchas & OpSec
- Coverage is opt-in: only members who consented are listed, so a real architect can be legitimately absent.
- The directory "may not be used for commercial purposes" per RIBA — keep use investigative/personal.
- OpSec: passive and anonymous; no login, no notification to the subject.

## Overlaps ("do both")
- Pairs with a UK company registry (Companies House) — RIBA confirms the professional credential and current practice, the registry confirms the firm's directors/officers and filings.

## Trust & verifiability
`trust: trusted` — a first-party register maintained by RIBA; membership entries are authoritative, with the only caveat being consent-based coverage gaps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | architecture-com |
| category | public-records |
| selectorsIn → selectorsOut | name, geolocation → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
