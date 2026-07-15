---
id: nmc-org-in
name: "Indian Medical Register (National Medical Commission)"
description: Use when you have a doctor's `name` (or registration number) in India and want to verify their medical registration — returns registration number, year, state council, qualification and `employer-org` context.
url: https://www.nmc.org.in/information-desk/indian-medical-register/
category: public-records
path:
- public-records
bestFor: Verifying that a person is a registered medical practitioner in India and pulling their registration details.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- document-id
- employer-org
status: live
pricing: free
costNote: Free official government registry; no account or payment required.
opsec: passive
opsecNote: Passive — you query a public government register; the subject is not notified. It is a first-party official source, so no third-party leakage. Sock-puppet browsing is fine; no login.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by India's National Medical Commission (statutory regulator, successor to the Medical Council of India) — this is the authoritative national register of medical practitioners.
missingPersonsRelevance: high
coverage:
- in
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- IMR
- Indian Medical Register
- NMC doctor search
- Medical Council of India register
tags:
- professionlicensing
- Profession & Licensing Sites
- medical-registration
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Indian Medical Register (National Medical Commission)

> India's official national register of licensed doctors — search by name or registration number to confirm a practitioner is genuinely registered and pull their credentials.

## When to use
You have a `name` (or a claimed medical registration/`document-id`) for someone in India who says they are a doctor, and you want to confirm it and extract registration details. A hit anchors identity to a state medical council, a registration year, and a qualification — strong corroboration for a professional and a route to their training institution and practice location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Indian Medical Register search at the URL (the NMC "Information Desk → Indian Medical Register" page links to the searchable IMR).
2. Search by full name, registration number, state medical council, or year of registration (any combination you have).
3. Solve any CAPTCHA the portal presents and submit.
4. Read the result: doctor's name, registration number, registering state council, year of registration, and qualification/university.
5. Pivot: qualification + university feeds alumni/academic OSINT; the state council and city narrow location; a mismatch flags a false claim.

## Inputs → Outputs
- **In:** `name` and/or registration number (`document-id`)
- **Out:** `name`, registration number (`document-id`), state medical council, registration year, qualification, and institution (`employer-org` context)
- **Empty/negative result looks like:** "no records found" — the person is not in the national register under that name/number. Given the size of the register and name variants, try alternate spellings and the specific state council before concluding the claim is false.

## Gotchas & OpSec
- Human-in-the-loop: the portal uses CAPTCHA and can be slow or intermittently return 5xx errors under load — retry later if it's down.
- Older records migrated from state councils and the former Medical Council of India can have inconsistent spelling/transliteration; search loosely.
- Registration confirms licensure at registration time, not current practice status — a doctor may be registered but no longer practising.

## Overlaps ("do both")
- Pairs with state medical council registers and hospital staff directories — the IMR gives the authoritative registration; local council/hospital sources add current posting and contact details.

## Trust & verifiability
`trust: trusted` — this is the statutory national regulator's own register, so a positive match is authoritative for the fact of registration; verify current practice status separately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nmc-org-in |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
