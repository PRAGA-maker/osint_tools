---
id: ahpra-gov-au
name: ahpra.gov.au
description: Use when you have a `name` and want to verify/locate an Australian health practitioner — returns registration status, profession, qualifications and principal practice location (`address`/`employer-org`) from the national register.
url: https://www.ahpra.gov.au/Registration/Registers-of-Practitioners.aspx
category: public-records
path:
- public-records
bestFor: Verifying an Australian doctor, nurse, or other health practitioner and finding their practice location.
selectorsIn:
- name
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free official national register search. No account or payment.
opsec: passive
opsecNote: You search a public statutory register; the practitioner is not contacted or notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Australian Health Practitioner Regulation Agency's official national register, covering 15+ regulated health professions — authoritative registration and conditions/notation data.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- docinfo-org
- rcvs-org-uk
aliases:
- AHPRA
- Register of Practitioners Australia
tags:
- professionlicensing
- Profession & Licensing Sites
- health-practitioner
- australia
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# ahpra.gov.au

> Australia's national register of health practitioners — confirm whether a person is a registered doctor, nurse, dentist, psychologist (and more), and find their profession, registration status, and practice location.

## When to use
You have a `name` claimed to be an Australian health practitioner and want to verify and locate them. AHPRA's register covers 15+ regulated professions and returns registration status, registration number, profession/division, qualifications, any conditions or reprimands (notations), and the principal place of practice (a location `address`/`employer-org` signal). Ideal for confirming a subject's profession, catching false medical claims, and locating a practitioner through their registered practice.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the register at https://www.ahpra.gov.au/Registration/Registers-of-Practitioners.aspx.
2. Search by practitioner `name` (narrow by profession/registration number if you have it).
3. Open the matching record: profession, registration status/type, registration number, qualifications, conditions/notations, and principal practice location.
4. Note the practice location and any conditions on registration.
5. Pivot: the practice `address` narrows `geolocation`; the profession/qualifications corroborate identity; compare methodology with equivalent registers abroad (`[[docinfo-org]]` US physicians, `[[rcvs-org-uk]]` UK vets).

## Inputs → Outputs
- **In:** `name` (+ profession/registration number to narrow)
- **Out:** registration status/type, registration number, profession, qualifications, conditions/notations, principal practice location (`address`/`employer-org`), confirmed `name`
- **Empty/negative result looks like:** no match — the person isn't currently registered under that name in any AHPRA-regulated profession (a variant, lapsed/cancelled registration, or a non-regulated role). A confident negative for *current AHPRA registration*.

## Gotchas & OpSec
- Human-in-the-loop: none; a public register search.
- OpSec: **passive** — a statutory register; nobody is notified.
- Reflects current registration; a suspended/cancelled practitioner shows a status/notation — read it carefully. Common names need the profession or registration number to disambiguate.

## Overlaps ("do both")
- Methodologically parallel to `[[docinfo-org]]` (US physicians) and `[[rcvs-org-uk]]` (UK vets) — when a subject's claimed profession spans jurisdictions, run the register for each country. AHPRA is the authoritative source for Australia.

## Trust & verifiability
`trust: trusted` — the official national regulator's register, so registration and conditions data are authoritative. Confirm the right individual (common names) via registration number and practice details before acting on a match.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ahpra-gov-au |
| category | public-records |
| selectorsIn → selectorsOut | name → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
