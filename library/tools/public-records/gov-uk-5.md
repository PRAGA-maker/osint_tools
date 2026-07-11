---
id: gov-uk-5
name: gov.uk
description: Use when you have a `name` of someone who worked in UK schools and want teacher-misconduct/prohibition records — returns the person's `name`, the `employer-org` (school), and a case `document-id`/outcome.
url: https://www.gov.uk/guidance/teacher-misconduct-attend-a-professional-conduct-panel-hearing-or-meeting
category: public-records
path:
- public-records
bestFor: Checking whether a named individual has a UK teacher-misconduct panel outcome or prohibition order.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free UK government guidance and published panel-outcome decisions; no account needed.
opsec: passive
opsecNote: Reading published government misconduct decisions is passive and does not notify the subject. These records concern professional conduct findings — handle the sensitive personal information they contain responsibly and lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UK Government (gov.uk) / Teaching Regulation Agency material; published misconduct outcomes and prohibition data are authoritative.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Teacher misconduct panel outcomes
- Teaching Regulation Agency
- TRA prohibition
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# gov.uk

> The UK government's teacher-misconduct pages (Teaching Regulation Agency) — an entry point to published professional-conduct panel outcomes and prohibition orders naming individuals.

## When to use
Your subject has worked (or claims to have worked) in English schools and you want to check for a professional-conduct history: a misconduct panel hearing, a finding, or a prohibition order barring them from teaching. Useful for vetting, corroborating a subject's account of their career, or explaining a gap/departure from the profession.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start from this guidance page (https://www.gov.uk/guidance/teacher-misconduct-attend-a-professional-conduct-panel-hearing-or-meeting) and follow through to the published "Teacher misconduct: panel outcomes / decisions" collections on gov.uk.
2. Search or browse the published decision documents for the subject's `name`.
3. Open a matching decision: read the individual's `name`, the `employer-org` (school/employer at the time), the case reference (`document-id`), the findings, and the outcome (e.g. prohibition order, with or without a review period).
4. Cross-check the Teaching Regulation Agency's teacher-status/prohibition information where applicable.
5. Pivot: the school (`employer-org`) and dates feed employment-history checks; the outcome contextualises a career gap.

## Inputs → Outputs
- **In:** `name` (of a current/former teacher)
- **Out:** `name`, `employer-org` (school), case `document-id`, and the misconduct finding/outcome
- **Empty/negative result looks like:** no published decision — the vast majority of teachers have none, so absence is expected and simply means no published misconduct finding, not a positive clearance beyond that.

## Gotchas & OpSec
- Scope is professional-conduct outcomes for the teaching profession in England — not a general criminal or safeguarding check.
- Decisions are sensitive personal data; use lawfully and avoid over-reading a single document.
- Common names require care; confirm via school, dates, and case details.

## Overlaps ("do both")
- Pairs with other UK professional registers and `[[companies-house]]` — the misconduct record covers teaching specifically, while other registers/records cover different professions and business roles.

## Trust & verifiability
`trust: trusted` — official gov.uk / Teaching Regulation Agency records; published outcomes are authoritative and cite their case references.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-5 |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
