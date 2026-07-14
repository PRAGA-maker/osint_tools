---
id: teachingcouncil-ie
name: teachingcouncil.ie
description: Use when you have a `name` you believe belongs to an Irish teacher and want to confirm their registration status and registration number — returns name, employer-org (registration), document-id.
url: http://www.teachingcouncil.ie/en/Registration/Register-of-Teachers/Search-the-Register/
category: public-records
path:
- public-records
bestFor: Confirming a person is a registered teacher in Ireland and retrieving their registration details.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free, public statutory register maintained by the Teaching Council of Ireland; no account needed.
opsec: passive
opsecNote: A read-only query against an official public register; the subject is not notified and nothing is disclosed to them. No login, so no attribution beyond ordinary web-server logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Teaching Council, Ireland's statutory regulator for the teaching profession; the register is authoritative for registration status.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- Teaching Council of Ireland Register
- Search the Register of Teachers
tags:
- professionlicensing
- Profession & Licensing Sites
- register
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# teachingcouncil.ie

> Ireland's official, searchable Register of Teachers — confirm whether a named person is a registered teacher and pull their registration number and status.

## When to use
You have a `name` and a claim (or suspicion) that the person is or was a teacher in Ireland, and you want an authoritative check: are they registered, under what registration number, and in good standing? Useful for verifying employment claims, corroborating identity, or confirming a professional link in a broader profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Search the Register page at teachingcouncil.ie (Registration → Register of Teachers → Search the Register).
2. Enter the teacher's `name` (or registration number if known) and submit.
3. Read the result: registered name, registration number (`document-id`), registration route/status, and the categories/subjects they're registered to teach.
4. Match carefully — common names may return multiple entries; use the registration number to disambiguate.
5. Pivot: a confirmed registration corroborates the person's profession and can be cross-checked against school/employer (`employer-org`) records and other professional registers.

## Inputs → Outputs
- **In:** `name` (or registration number)
- **Out:** `name`, registration number (`document-id`), registration status/category, `employer-org` (professional context)
- **Empty/negative result looks like:** no matching registrant — meaning they are not on the Irish register (not registered, registered elsewhere, or lapsed), not proof they never taught.

## Gotchas & OpSec
- Coverage is Ireland only — an unregistered result says nothing about teaching in other jurisdictions.
- Registration can lapse; status reflects the current register, not full history.
- OpSec: fully passive query of an official public register.

## Overlaps ("do both")
- Pairs with other national professional/licensing registers (e.g. UK GTC-style bodies) and with employer/school directories to place the teacher at a specific institution.

## Trust & verifiability
`trust: trusted` — the statutory regulator's own register; registration status here is authoritative, subject only to the register being current.
