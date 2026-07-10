---
id: medicalcouncil-ie
name: Irish Medical Council – Check the Register
description: Use when you have a doctor's `name` and want to verify Irish medical registration — returns registration status, specialty/qualifications and registration number.
url: https://www.medicalcouncil.ie/Public-Information/Check-the-Register/
category: public-records
path:
- public-records
bestFor: Verifying that a doctor is registered to practise in Ireland and confirming their specialty, qualifications and registration status.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free official public register maintained by the statutory regulator; no account or payment to check a doctor.
opsec: passive
opsecNote: A public statutory-register lookup; the subject is not notified and no login is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Medical Council is Ireland's statutory medical regulator; its register is the authoritative record of who may practise medicine in Ireland.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mpts-uk-org
aliases:
- Irish Medical Council register
- medicalcouncil.ie
tags:
- professionlicensing
- Profession & Licensing Sites
- ireland
- medical
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Irish Medical Council – Check the Register

> Ireland's statutory medical register: confirm a doctor is legally registered to practise, and read their specialty, qualifications and registration status.

## When to use
You have a `name` claiming to be (or presented as) a doctor in Ireland and need to verify it. The Medical Council register confirms whether the person is registered, on which division (general, specialist, trainee), their recognised specialty and qualifications, and their registration number (`document-id`). Use it to validate a medical credential (an unregistered "doctor" is a serious red flag), disambiguate same-name individuals, or corroborate a subject's stated profession.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.medicalcouncil.ie/Public-Information/Check-the-Register/.
2. Search by the doctor's `name` (add registration number if you have it to disambiguate).
3. Read the entry: registration status, division/type of registration, recognised specialty, qualifications, and registration number.
4. Match the claimed credential to the register — presence and "registered" status confirm the right to practise; absence or a lapsed status contradicts a practising claim.
5. Pivot: a confirmed specialty/`employer-org` corroborates the subject's professional life; a registration number anchors identity across records.

## Inputs → Outputs
- **In:** `name` (± registration number)
- **Out:** `name`, registration status, specialty/qualifications (`employer-org` context), registration number (`document-id`)
- **Empty/negative result looks like:** no match. Meaningful in itself — someone practising or claiming to be a doctor in Ireland who is absent from the register is a discrepancy worth flagging (they may be registered in another country instead).

## Gotchas & OpSec
- Covers Ireland only; a doctor may be registered in the UK (GMC) or elsewhere — check the right regulator for the jurisdiction claimed.
- Registration status and specialty are point-in-time; a lapsed or restricted registration matters.
- OpSec: passive; a public-register read with no login.

## Overlaps ("do both")
- Pairs with `[[mpts-uk-org]]` and the UK GMC register when a doctor's history spans jurisdictions — registration in one country plus fitness-to-practise history in another gives a fuller picture.

## Trust & verifiability
`trust: trusted` — the Medical Council is Ireland's statutory regulator, so its register is authoritative for the right to practise. Just ensure you're checking the correct national regulator for where the person claims to work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | medicalcouncil-ie |
</content>
