---
id: pharmacyregulation-org
name: pharmacyregulation.org (GPhC register)
description: Use when you have a `name` or registration number and want to verify a GB pharmacist/pharmacy technician — returns registration status, number, town and any fitness-to-practise decisions.
url: https://www.pharmacyregulation.org/registers
category: public-records
path:
- public-records
bestFor: Verifying whether someone is a registered pharmacist/pharmacy technician in Great Britain and their standing.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free official register search operated by the General Pharmaceutical Council (GPhC); no account or payment.
opsec: passive
opsecNote: An official professional-register lookup — you query the GPhC, not the subject, and nobody is notified. The register is public by statute. Routine sock-puppet browsing hygiene is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the General Pharmaceutical Council, the statutory regulator for pharmacists, pharmacy technicians and pharmacies in Great Britain — an authoritative first-party register.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- GPhC register
- General Pharmaceutical Council register
- pharmacyregulation.org
tags:
- professionlicensing
- Profession & Licensing Sites
- pharmacist
- gphc
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# pharmacyregulation.org (GPhC register)

> The statutory register of Great Britain's pharmacists and pharmacy technicians — confirm a person is registered, in good standing, and where they practise.

## When to use
You want to confirm whether a subject really is a registered pharmacist or pharmacy technician in Great Britain, check their registration status (current/lapsed/removed), or find the town/pharmacy they are associated with. Professional registers are strong identity-verification and location signals — they tie a `name` to a verified profession, a registration `document-id`, and a practising area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.pharmacyregulation.org/registers.
2. Choose the register: pharmacist, pharmacy technician, or pharmacy (premises).
3. Search by `name`, or go straight to a record with a registration number (`document-id`).
4. Read the entry: registrant `name`, registration number and status, town/area, and any published Fitness to Practise decisions.
5. Pivot: a confirmed town/pharmacy (`employer-org`/`address`) narrows geography and workplace; a registration number corroborates identity; an FtP decision links to hearing records.

## Inputs → Outputs
- **In:** `name` or registration number (`document-id`)
- **Out:** registration status, number, town/area, associated pharmacy (`employer-org`/`address`), fitness-to-practise history
- **Empty/negative result looks like:** no matching registrant — the person isn't GPhC-registered (may be unregistered, in a different profession, or registered in a different UK healthcare register). Absence doesn't disprove the person, only the pharmacy registration.

## Gotchas & OpSec
- **Great Britain only** — Northern Ireland pharmacists are regulated separately (PSNI). Other healthcare professions have their own registers (GMC, NMC, HCPC).
- Common names return multiple registrants; use town/registration number to disambiguate.
- OpSec: **passive**, authoritative first-party register; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with other UK professional registers (GMC for doctors, NMC for nurses, `[[psa-gov-ie]]` for Irish security licences) and with company/electoral records — the register verifies the profession and area; other sources add contact and address detail.

## Trust & verifiability
`trust: trusted` — the official GPhC statutory register, kept current; registration status and FtP decisions are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pharmacyregulation-org |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
