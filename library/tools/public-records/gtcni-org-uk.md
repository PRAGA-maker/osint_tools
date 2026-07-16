---
id: gtcni-org-uk
name: GTCNI Register of Teachers (Northern Ireland)
description: Use when you have a `name` and want to confirm whether someone is a registered teacher in Northern Ireland — returns registration status, last known employer, GTCNI number.
url: https://iregistration.gtcni.org.uk/search-teachers
category: public-records
path:
- public-records
bestFor: Confirming a person's status on the statutory register of teachers in Northern Ireland and their last known school/employer.
selectorsIn:
- name
selectorsOut:
- employer-org
- name
- document-id
status: live
pricing: free
costNote: Free public register lookup; any member of the public may check a teacher's registration status with no account or fee.
opsec: passive
opsecNote: Searching the statutory register is passive and anonymous — the teacher is not notified. No login is required, so a clean browser is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The General Teaching Council for Northern Ireland is the statutory regulator; the register is the authoritative record of who may teach in NI.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- General Teaching Council for Northern Ireland
- GTCNI register
- search.gtcni.org.uk
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# GTCNI Register of Teachers (Northern Ireland)

> The statutory register of Northern Ireland teachers — confirm a person teaches, and pull their last known school.

## When to use
You have a `name` and a claim (or suspicion) that the person is or was a teacher in Northern Ireland, and you want to verify it and get an employment anchor. A hit confirms registration status, gives the last known employer (`employer-org` — usually a named school), and returns the person's GTCNI registration number (`document-id`) — all corroboration for identity and a lead toward a workplace/location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the public "Search the Register" tool (current endpoint: `search.gtcni.org.uk`; the legacy `iregistration.gtcni.org.uk` path also routes here).
2. Enter the subject's `name` (surname is the key field; add given name to narrow).
3. Read the result:
   - A registered teacher shows their name, GTCNI number, registration status, and last known employer (school).
   - No match means they are not (currently) on the NI register under that name.
4. Pivot: the named school (`employer-org`) feeds workplace/location research; the confirmed identity + GTCNI number corroborates other findings.

## Inputs → Outputs
- **In:** `name`
- **Out:** `employer-org` (last known school), `name` (registered spelling), `document-id` (GTCNI number), plus registration status
- **Empty/negative result looks like:** "no teacher found" — meaning not registered in Northern Ireland under that name (they may teach in England/Scotland/Wales, whose registers are separate, or not at all). Not proof the person isn't a teacher elsewhere.

## Gotchas & OpSec
- NI only. England has no comparable open teacher register; Scotland (GTCS) and Wales (EWC) have their own — check those separately.
- The register confirms *status and employer only*; it does not give home address or contact details.
- OpSec: fully passive and anonymous.

## Overlaps ("do both")
- Pairs with the GTCS (Scotland) and EWC (Wales) teacher registers and with Companies House for any private-tutoring business — each covers a different jurisdiction or facet of the same person.

## Trust & verifiability
`trust: trusted` — the statutory regulator's own register; registration status is authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gtcni-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
