---
id: jahs-ie
name: Insolvency Service of Ireland — Public Register
description: Use when you have an Irish subject's `name` and want to check whether they hold an insolvency/debt arrangement — returns `address`, `dob` and court-record `document-id`.
url: https://isi.jahs.ie/public/cases
category: financial-crypto
path:
- financial-crypto
bestFor: Confirming whether a named Irish person is on the statutory insolvency/bankruptcy registers, with address and year of birth.
selectorsIn:
- name
selectorsOut:
- address
- dob
- document-id
status: live
pricing: free
costNote: Free public statutory register; no account or payment needed to search.
opsec: passive
opsecNote: A public statutory register — searching a name is passive and generates no notice to the subject. Only the ISI portal's own server logs your query. No login, so nothing ties the search to you beyond your IP; use a clean session for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official register maintained by the Insolvency Service of Ireland, an independent statutory body (est. 2013); entries are authoritative legal records.
missingPersonsRelevance: medium
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- ISI public register
- Insolvency Service of Ireland register
- isi.jahs.ie
tags:
- insolvency
- public-records
- financial
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Insolvency Service of Ireland — Public Register

> Ireland's official, free, name-searchable register of statutory debt solutions and bankruptcies — an authoritative address/DOB corroboration source for an Irish subject.

## When to use
You have an Irish subject's `name` and want to know whether they are (or were) subject to a formal insolvency process. A positive hit is doubly useful: it confirms a financial-distress event on a date, and — critically for tracing — the register entry publishes the debtor's **address** and **year of birth** alongside the court and record number. That address/DOB pairing is strong corroboration when placing or distinguishing a same-named person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://isi.jahs.ie/public/cases (the portal is a JavaScript app — allow it to finish loading past the "ISI Portal Loading…" splash).
2. Search jointly by first name and surname; the register covers Debt Relief Notices (DRN), Debt Settlement Arrangements (DSA), Personal Insolvency Arrangements (PIA), Protective Certificates (PC) and bankruptcies.
3. Read a positive result: debtor name, address, year of birth, the relevant court and the court record/case number.
4. Pivot: the published `address` feeds electoral-roll/directory checks; the `dob` disambiguates common names; the case number feeds court-record follow-up.

## Inputs → Outputs
- **In:** `name` (first name + surname)
- **Out:** `address`, `dob` (year of birth), `document-id` (court record number), arrangement type and court
- **Empty/negative result looks like:** "no records found" for that exact name — the person is not on the insolvency registers (searches are confined strictly to the name entered, so spelling/variants matter).

## Gotchas & OpSec
- Searches match the name as typed — try known variants, maiden names and spellings; an absent record is not proof of solvency, only that the exact name isn't registered.
- Entries can age off / change status as arrangements complete; the current view reflects live status.
- Fully passive and public; no subject notification.

## Overlaps ("do both")
- Pairs with the Irish Companies Registration Office and electoral-roll/directory tools — insolvency gives address+DOB, those confirm current residence and business roles for the same person.

## Trust & verifiability
`trust: trusted` — the first-party statutory register operated by the Insolvency Service of Ireland; entries are legally authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jahs-ie |
| category | financial-crypto |
| selectorsIn → selectorsOut | name → address, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
