---
id: hcpc-uk-org
name: HCPC Check the Register (hcpc-uk.org)
description: Use when you have a `name` of a UK health/care professional and want to confirm their registration and status — returns name, profession/registration, and registration number.
url: https://www.hcpc-uk.org/check-the-register/
category: public-records
path:
- public-records
bestFor: Confirming a UK health & care professional (e.g. paramedic, physio, radiographer) is registered, and their status.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free official register maintained by the Health and Care Professions Council; no account.
opsec: passive
opsecNote: A public professional-register lookup; the individual is not notified. Nothing is sent to them. Confirms professional identity, not home/contact details.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the HCPC, the UK statutory regulator for 15 health & care professions; the authoritative source for whether a named person holds current registration.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- HCPC register
- Health and Care Professions Council register
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- verification
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# HCPC Check the Register (hcpc-uk.org)

> The UK regulator's public register for 15 health & care professions — search a surname to confirm someone is (or isn't) a registered professional and their current status.

## When to use
You have a `name` and a claim (or a need to check) that the person is a UK-registered health/care professional — paramedic, physiotherapist, radiographer, dietitian, occupational therapist, arts/speech therapist, etc. Use it to verify a professional identity, spot an impostor, or confirm the profession/registration of a subject who works in one of these fields.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open hcpc-uk.org/check-the-register/.
2. Search by surname (plus select the profession from the dropdown) or by registration number.
3. Read the result: registered name, profession, registration number/status, and any prescribing/medicines entitlement or restrictions.
4. Pivot: a confirmed profession + registration number (`document-id`) corroborates identity and employer context; a *non-match* against a claimed title is itself a finding.

## Inputs → Outputs
- **In:** `name` (surname + profession) or registration number
- **Out:** registered `name`, profession/registration (`employer-org` context), registration `document-id`/number and status, entitlements/restrictions
- **Empty/negative result looks like:** no match — the person isn't HCPC-registered under that name/profession (could be a different UK regulator — GMC for doctors, NMC for nurses, GDC for dentists — or not registered at all, which may itself be significant).

## Gotchas & OpSec
- Wrong regulator: doctors (GMC), nurses/midwives (NMC), dentists (GDC), social workers (Social Work England) are elsewhere — a blank here doesn't mean unregulated.
- Common surnames return several entries; disambiguate by first name, town, or registration number.
- OpSec: passive; confirms professional standing only, not personal contact details.

## Overlaps ("do both")
- Pairs with the other UK professional regulators (GMC/NMC/GDC/SRA) and Companies House — this verifies the health/care credential; the others cover different professions and the person's business links.

## Trust & verifiability
`trust: trusted` — first-party statutory-regulator data; authoritative for HCPC registration status. A match verifies the credential; verify the *person* (right individual) via name/town/registration number before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hcpc-uk-org |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
