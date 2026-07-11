---
id: docinfo-org
name: docinfo.org
description: Use when you have a doctor's `name` and want to confirm and locate them professionally — returns the states they're licensed in, medical school, city/state (`address`), specialty and any board discipline.
url: https://www.docinfo.org/#/search/query
category: public-records
path:
- public-records
bestFor: Verifying a US physician's licensure, location, and disciplinary history by name.
selectorsIn:
- name
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free consumer lookup operated by the Federation of State Medical Boards (FSMB). No account or payment for a standard name search.
opsec: passive
opsecNote: You query a public professional-licensing database, not the physician. Nothing is disclosed to the subject. Fully passive; standard web hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Federation of State Medical Boards and fed by the ~70 US state medical boards via the Physician Data Center — authoritative licensure and disciplinary data, updated as often as daily.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- npi-registry
aliases:
- DocInfo
- FSMB DocInfo
- Physician Data Center
tags:
- professionlicensing
- Profession & Licensing Sites
- physician
- medical-license
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# docinfo.org

> The Federation of State Medical Boards' public physician-lookup: enter a doctor's name and state and confirm their license, locations, training, specialty, and any board discipline across all US states.

## When to use
You have a `name` that belongs to (or is claimed to belong to) a US physician or physician assistant and want to verify and locate them. DocInfo confirms whether the person is really a licensed doctor, which states they hold active licenses in (a strong `geolocation`/`address` signal), where they trained, their specialty, and — critically — whether any state medical board has disciplined them. Excellent for confirming a subject's profession, catching impersonation, or locating a doctor who has moved between states.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.docinfo.org.
2. Enter the physician's `name` (and state, to disambiguate common names).
3. Select the matching record and read the report: states of active licensure, medical school, city/state (`address`-level location), specialty certification, and disciplinary-action flags.
4. For discipline details, follow the links to the relevant state medical board.
5. Pivot: the states-licensed list narrows geography; the medical school and specialty corroborate identity; cross-check the NPI number and practice address via `[[npi-registry]]`.

## Inputs → Outputs
- **In:** `name` (+ state to narrow)
- **Out:** licensure states, medical school (`employer-org`-style training), city/state `address`, specialty, disciplinary-action indicator, confirmed `name`
- **Empty/negative result looks like:** no matching physician — the person isn't a licensed US MD/DO/PA under that name (possible impersonation, a non-US doctor, a name variant, or a different profession). It confirms the negative for US medical licensure specifically.

## Gotchas & OpSec
- Human-in-the-loop: none; a straightforward public search.
- OpSec: **passive** — a licensing-board database; the physician is never contacted or notified.
- DocInfo flags *that* discipline exists; the detail lives on the individual state board sites — follow through for specifics. Common names need the state filter to avoid conflating two doctors.

## Overlaps ("do both")
- Pairs with `[[npi-registry]]` — DocInfo gives licensure and discipline; the NPI registry gives the practice `address`, taxonomy, and provider identifiers. Run both to fully pin down a US medical professional.

## Trust & verifiability
`trust: trusted` — operated by the FSMB and sourced directly from the state medical boards, so licensure and disciplinary data are authoritative. Confirm ambiguous matches with the state filter and the linked board records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | docinfo-org |
| category | public-records |
| selectorsIn → selectorsOut | name → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
