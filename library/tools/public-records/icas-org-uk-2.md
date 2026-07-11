---
id: icas-org-uk-2
name: ICAS Disciplinary Notices
description: Use when you have a `name` of a Scottish chartered accountant and want to check for published disciplinary findings against them — returns name, employer-org context and a case document-id.
url: https://www.icas.com/regulation/regulatory-monitoring/disciplinary-notices
category: public-records
path:
- public-records
bestFor: Checking whether a chartered accountant has published ICAS disciplinary findings.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free public regulatory notices published by ICAS; no account required.
opsec: passive
opsecNote: Public regulator notices; reading them is anonymous and does not notify anyone. Only your IP touches the ICAS site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Institute of Chartered Accountants of Scotland (ICAS) is the statutory professional body; published disciplinary notices are authoritative records of findings against its members/firms.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- ICAS disciplinary notices
- Institute of Chartered Accountants of Scotland
- icas.com
tags:
- professionlicensing
- Profession & Licensing Sites
- accountancy
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# ICAS Disciplinary Notices

> The Scottish chartered-accountancy body's published disciplinary findings — check whether a named accountant or firm has been sanctioned.

## When to use
You have a `name` (or firm) that claims to be, or is, a chartered accountant regulated by ICAS, and you want to know whether they have been the subject of published disciplinary action — findings, sanctions, exclusions. A hit confirms the person's professional identity/employer context and surfaces an authoritative account of misconduct; the absence of a notice is itself reassurance (within ICAS's remit). Useful for background/integrity checks and for corroborating a person's professional standing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.icas.com/regulation/regulatory-monitoring/disciplinary-notices.
2. Browse or search the published notices for the person's or firm's `name`.
3. Open a matching notice: it names the member/firm, describes the findings and sanction, and carries a case reference (`document-id`) and date.
4. Pivot: a notice confirms the accountant's identity and often names their firm (`employer-org`); combine with Companies House and news for the fuller picture; a sanction/exclusion is a significant integrity finding.

## Inputs → Outputs
- **In:** `name` (chartered accountant or firm)
- **Out:** `name`, `employer-org` (firm) context, case `document-id`, findings/sanction, date
- **Empty/negative result looks like:** no notice for the name — the person has no *published ICAS* disciplinary finding; they may be clean, regulated by a different body (ICAEW/ACCA), or not an accountant at all.

## Gotchas & OpSec
- Scope is **ICAS members/firms only** — English/Welsh (ICAEW) and ACCA accountants are disciplined by their own bodies; check the right regulator.
- Notices cover disciplinary findings, not routine membership — this is not a full "is X a member" register.
- Older notices may be removed after a retention period; absence isn't proof none ever existed.

## Overlaps ("do both")
- Pairs with `[[niscc-org]]`-style professional registers and the ICAEW/ACCA disciplinary pages — verify the person against the regulator that actually governs them, and cross-check the firm via Companies House.

## Trust & verifiability
`trust: trusted` — authoritative notices from the statutory professional body. What is published is reliable; just confirm you are looking at the correct regulator for the individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | icas-org-uk-2 |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
