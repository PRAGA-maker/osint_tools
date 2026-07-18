---
id: qilt-university-australia
name: QILT (Australia)
description: Use when you have an Australian `employer-org` (university/college) and want to verify it and its outcomes — returns institution profiles, student-experience and graduate-employment data.
url: http://www.qilt.edu.au
category: search-engines
path:
- search-engines
bestFor: Confirming an Australian higher-education institution exists and comparing its official student/graduate outcome data.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free, government-funded public data portal (results published via the ComparED site); no account needed.
opsec: passive
opsecNote: Browsing published survey data is fully passive and anonymous; you are reading aggregate statistics, not querying any individual, so nothing is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Australian Government-endorsed survey program run by the Social Research Centre for the Department of Education; authoritative institution-level data.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- QILT
- Quality Indicators for Learning and Teaching
- ComparED
tags:
- toddington
- curated-directory
- specialty-search
- education
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# QILT (Australia)

> The Australian Government's higher-education survey portal: a directory of every Australian university and ~90 non-university providers with official student-experience and graduate-outcome statistics.

## When to use
A subject claims to have studied at, or works for, an Australian tertiary institution and you want to confirm the `employer-org` is real and government-recognised, or to characterise it (size, fields, outcomes). QILT lists all 43 Australian universities plus ~90 approved non-university providers, so it doubles as an authoritative registry of legitimate Australian higher-education bodies — useful for spotting a fabricated or unaccredited "university." It does not identify individuals; it is institutional context only.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to qilt.edu.au and open the ComparED explorer.
2. Search or browse for the named institution (`employer-org`); if it isn't listed among participating providers, that's itself a signal.
3. Read the institution's profile: study areas offered, and the four survey datasets — Student Experience (SES), Graduate Outcomes (GOS/GOS-L, incl. employment and salary), and Employer Satisfaction (ESS).
4. Pivot: a confirmed institution corroborates a subject's stated education/employer; its study areas and location feed further org and people searches.

## Inputs → Outputs
- **In:** `employer-org` (an Australian university/college name)
- **Out:** `employer-org` verification plus institution profile and outcome statistics
- **Empty/negative result looks like:** the named institution isn't among listed providers — either it's not an accredited Australian higher-ed body, is named differently, or is a private RTO outside QILT's scope; investigate the name before concluding it's fake.

## Gotchas & OpSec
- Human-in-the-loop: none; fully public.
- Scope is Australian higher education only (universities and approved providers) — vocational RTOs and overseas institutions won't appear.
- Data is aggregate and institution-level; it will never confirm that a specific person attended — use it only to validate the organisation.

## Overlaps ("do both")
- Pairs with national business/charity registries and the institution's own alumni-verification channels — QILT confirms the body is a recognised provider, while a registry or the university itself confirms an individual's enrolment/degree.

## Trust & verifiability
`trust: trusted` — QILT is a government-endorsed survey program (Department of Education / Social Research Centre), so its list of providers and outcome data are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | qilt-university-australia |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
