---
id: mpts-uk-org-2
name: mpts-uk.org
description: Use when you have a doctor's `name` (or GMC number) and want to check for UK fitness-to-practise tribunal hearings/decisions against them — returns `name`, GMC `document-id`, `employer-org` and published misconduct outcomes.
url: https://www.mpts-uk.org/hearings-and-decisions
category: public-records
path:
- public-records
bestFor: Checking whether a UK doctor has been before a Medical Practitioners Tribunal and reading the published decision.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free public register of hearings and decisions; no account needed. Operated by the MPTS (part of the GMC).
opsec: passive
opsecNote: You read a public tribunal register; the doctor is not notified. Only the MPTS site sees your visit. No sock puppet needed for casual lookups, though use one if the investigation is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Medical Practitioners Tribunal Service, the statutory adjudication body for UK doctors — an authoritative first-party register, not a third-party aggregator.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- gmc-register
aliases:
- MPTS
- Medical Practitioners Tribunal Service
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# mpts-uk.org

> The UK's official register of doctor fitness-to-practise tribunals — confirm whether a named medic has faced misconduct proceedings and read the outcome, in their own name.

## When to use
Your subject is (or claims to be) a UK doctor, physician associate or anaesthesia associate, and you want to know whether they have faced disciplinary adjudication. The MPTS publishes scheduled hearings and past **decisions** naming the practitioner, their GMC reference (`document-id`), the allegations, and the outcome (conditions, suspension, erasure). That confirms identity/employment (`employer-org` where a workplace is named), establishes character/history, and — for interim orders tribunals — flags a doctor currently under restriction. Useful for vetting an identity claim or building background on a person in the medical field.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mpts-uk.org/hearings-and-decisions.
2. Choose the relevant section — **upcoming tribunal hearings**, **tribunal hearings and decisions** (medical practitioners tribunals), or **interim orders tribunals**.
3. Search/filter by the doctor's `name` (and cross-check against a known GMC number if you have one).
4. Open the decision/determination document: read the named practitioner, GMC number, allegations, findings, and sanction.
5. Pivot: the GMC number feeds the GMC register for registration status/qualifications; a named employer/hospital feeds employer OSINT; the decision text often names dates/locations useful for timeline building.

## Inputs → Outputs
- **In:** doctor `name` (optionally GMC number / `employer-org`)
- **Out:** `name`, GMC `document-id`, `employer-org` where stated, hearing dates and published misconduct outcomes
- **Empty/negative result looks like:** no hearing/decision listed for the name — the doctor has not (publicly) been before a tribunal; this is common and normal, not evidence of anything adverse. Confirm the person is actually registered via the GMC register.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a straightforward public search.
- OpSec: **passive** — reading a public register, no notification to the subject.
- Scope: only covers doctors/associates who reached a *tribunal*; GMC warnings, undertakings, and voluntary erasures may not appear here — cross-check the GMC register. Names can collide; verify with the GMC number before attributing a decision.

## Overlaps ("do both")
- Pairs with `[[gmc-register]]` — the GMC register confirms whether the person is a registered doctor and their current status/qualifications, while MPTS supplies the detail of any tribunal proceedings; use the GMC number to tie the two together.

## Trust & verifiability
`trust: trusted` — an official statutory register published by the MPTS. Decisions are authoritative primary documents; the only caveat is same-name ambiguity, resolved by the GMC reference number.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mpts-uk-org-2 |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
