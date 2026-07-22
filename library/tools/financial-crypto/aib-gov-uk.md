---
id: aib-gov-uk
name: Accountant in Bankruptcy — Register of Insolvencies (Scotland)
description: Use when you have a `name` and want to check Scotland's statutory insolvency register — returns `address`, `dob` and case `document-id` for bankruptcies/protected trust deeds.
url: https://roi.aib.gov.uk/roi/Security/Home/Landing
category: financial-crypto
path:
- financial-crypto
bestFor: Confirming whether a named person has a Scottish bankruptcy or protected trust deed, with address and date of birth.
selectorsIn:
- name
selectorsOut:
- address
- dob
- document-id
status: live
pricing: free
costNote: Free public statutory register run by Accountant in Bankruptcy (a Scottish Government agency); no payment to search.
opsec: passive
opsecNote: A public statutory register — a name search is passive and generates no notice to the subject. Only the AiB server logs your query; no login, so use a clean session for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Register of Insolvencies maintained by Accountant in Bankruptcy, an agency of the Scottish Government; entries are authoritative legal records.
missingPersonsRelevance: medium
coverage:
- gb-sct
auth: none
api: false
localInstall: false
registration: false
aliases:
- Accountant in Bankruptcy
- Register of Insolvencies
- AiB ROI
- roi.aib.gov.uk
tags:
- insolvency
- public-records
- scotland
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Accountant in Bankruptcy — Register of Insolvencies (Scotland)

> Scotland's official, free, name-searchable register of bankruptcies (sequestrations) and protected trust deeds — an authoritative address/DOB corroboration source for a Scottish subject.

## When to use
You have a `name` for a subject with a Scottish connection and want to confirm a formal insolvency event. Scotland runs a separate insolvency system from England & Wales, so a person absent from the English Individual Insolvency Register may appear here. A positive entry publishes the debtor's **address** and **date of birth** with the case type and reference — strong corroboration for placing or disambiguating a same-named individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://roi.aib.gov.uk/ and enter the register search.
2. Search by `name` (try known variants/maiden names); the register covers sequestrations (bankruptcies), protected trust deeds and related awards.
3. Read a positive result: debtor name, address, date of birth, case type and AiB case reference, plus the appointed trustee.
4. Pivot: the `address` feeds electoral-roll/directory checks; the `dob` disambiguates common names; the trustee/case reference feeds insolvency follow-up.

## Inputs → Outputs
- **In:** `name`
- **Out:** `address`, `dob`, `document-id` (case reference), case type and trustee
- **Empty/negative result looks like:** "no records" for that name — the person has no Scottish insolvency on the register (try England & Wales and Ireland registers separately); spelling/variants matter.

## Gotchas & OpSec
- Scotland only — cross-check the England & Wales Individual Insolvency Register and Ireland's ISI for full UK/IE coverage.
- Entries can age off as cases discharge; the live view reflects current status.
- Fully passive and public; no subject notification.

## Overlaps ("do both")
- Pairs with `[[jahs-ie]]` (Ireland ISI) and the England & Wales insolvency register, plus Companies House — insolvency gives address+DOB, those confirm residence and directorships.

## Trust & verifiability
`trust: trusted` — the first-party statutory register of a Scottish Government agency; entries are legally authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aib-gov-uk |
| category | financial-crypto |
| selectorsIn → selectorsOut | name → address, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
