---
id: mpts-uk-org
name: MPTS – Medical Practitioners Tribunals
description: Use when you have a UK doctor's `name` and want fitness-to-practise tribunal records — returns hearing listings and decision documents naming the doctor and outcome.
url: https://www.mpts-uk.org/hearings-and-decisions/medical-practitioners-tribunals
category: public-records
path:
- public-records
bestFor: Finding whether a UK doctor has faced a fitness-to-practise tribunal and reading the hearing outcomes and decision documents.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- employer-org
status: live
pricing: free
costNote: Free public hearings-and-decisions listings from the tribunal service; no account or payment.
opsec: passive
opsecNote: Public tribunal records; the subject is not notified. These name real doctors and disciplinary findings — handle the sensitive personal data responsibly and stick to legitimate investigative use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The MPTS is the statutory tribunal service (part of the UK GMC framework) that adjudicates doctors' fitness to practise; its published decisions are authoritative primary records.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- medicalcouncil-ie
- mpts-uk-org-2
aliases:
- Medical Practitioners Tribunal Service
- MPTS hearings
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- medical
- disciplinary
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# MPTS – Medical Practitioners Tribunals

> The UK medical tribunal service's public record: has this doctor faced a fitness-to-practise hearing, and what did the tribunal decide?

## When to use
You have a UK doctor's `name` and want the disciplinary/fitness-to-practise angle that a plain registration check won't show. MPTS publishes hearing listings and full decision documents — naming the doctor, the allegations, and the outcome (warning, conditions, suspension, erasure). Use it to background a doctor, corroborate or challenge a subject's professional standing, or find the detailed narrative behind a restricted GMC registration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.mpts-uk.org/hearings-and-decisions/medical-practitioners-tribunals.
2. Browse or search the hearings/decisions listings by doctor `name` (upcoming hearings and past decisions are both listed).
3. Open a decision document: it names the doctor, GMC reference (`document-id`), the allegations, findings, and the sanction imposed.
4. Cross-reference the doctor's GMC registration status to see how the tribunal outcome affected their right to practise.
5. Pivot: the named employer/hospital (`employer-org`) and dates feed further background; the GMC reference anchors identity across medical records.

## Inputs → Outputs
- **In:** `name` (UK doctor)
- **Out:** `name`, hearing/decision `document-id` (GMC reference, outcome), and `employer-org`/context from the decision text
- **Empty/negative result looks like:** no listing. That is the common, *good* case — most doctors never face a tribunal, so absence means no published fitness-to-practise proceedings, not that the doctor doesn't exist (verify existence via the GMC register).

## Gotchas & OpSec
- MPTS covers **tribunal proceedings**, not basic registration — use the GMC register to confirm a doctor exists/is registered; use MPTS for the disciplinary layer.
- Decisions contain sensitive findings about named individuals — treat responsibly and use only for legitimate purposes.
- Older cases and outcomes may be archived differently; check both current listings and decision archives.
- OpSec: passive; a public-record read.

## Overlaps ("do both")
- Pairs with the GMC register (registration status) and `[[medicalcouncil-ie]]` (Irish equivalent) — registration confirms the licence, MPTS reveals whether it has been challenged; do both when vetting a doctor.

## Trust & verifiability
`trust: trusted` — MPTS is the statutory UK medical tribunal service, so its published decisions are authoritative primary documents. Read the outcome carefully (findings vs. allegations differ) and confirm current registration effect via the GMC.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mpts-uk-org |
</content>
