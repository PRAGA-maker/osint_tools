---
id: international-standard-classification-of-occupations
name: International Standard Classification of Occupations
description: Use when you have an `employer-org`/job-title lead and want to normalize or interpret an occupation into a standard ISCO code — returns the canonical occupation classification, not a person.
url: http://www.ilo.org/public/english/bureau/stat/isco/index.htm
category: search-engines
path:
- search-engines
bestFor: Normalizing a subject's stated job title into the ILO's standard ISCO occupation code and understanding what that role covers.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free reference maintained by the International Labour Organization; no account needed.
opsec: passive
opsecNote: A static ILO reference — reading it submits nothing about the subject and touches no target infrastructure. Purely a passive interpretation aid.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the International Labour Organization (a UN agency); ISCO is the authoritative international occupation taxonomy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ISCO
- ISCO-08
- ILO occupation classification
tags:
- toddington
- curated-directory
- specialty-search
- occupation-reference
source: toddington-resources
lastVerified: '2026-07-20'
relatedTools:
- ilo-world-employment-and-social-outlook-trends
- ilostat
---

# International Standard Classification of Occupations

> The ILO's authoritative occupation taxonomy — a reference for interpreting and normalizing a subject's job title, not a way to find the subject.

## When to use
You have an occupational lead — a stated job title, an `employer-org` role, or a description from a résumé or profile — and you want to normalize it to a standard code (ISCO-08) or understand precisely what a vaguely worded title covers. This helps when comparing occupation data across countries or datasets, disambiguating a foreign-language job title, or interpreting labour/professional records that use ISCO codes. It is a **classification reference**, not a people-search: it returns codes and definitions, never a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the ISCO index at ilo.org (it now redirects to `webapps.ilo.org`; the site may block automated fetches but is reachable in a browser).
2. Browse the ISCO-08 structure (major → sub-major → minor → unit groups) or search for the occupation title.
3. Read the group definition to confirm what tasks/skills the title encompasses and note its numeric code.
4. Use the code to cross-reference occupation fields in other datasets, or to translate a foreign job title into a comparable role.
5. Pivot: an interpreted occupation sharpens searches on professional registries, licensing boards, and employer directories.

## Inputs → Outputs
- **In:** a job title / occupation description (an `employer-org` role lead)
- **Out:** the standard ISCO occupation code and definition (a normalized `employer-org`/role descriptor)
- **Empty/negative result looks like:** a title with no clean ISCO match usually means it's a marketing/vanity title — map it to the nearest unit group by task description rather than name.

## Gotchas & OpSec
- Reference only — it identifies *occupations*, so agents hoping to find a named person here will find nothing.
- The ILO domain moved (`webapps.ilo.org`) and may 403 automated tools; use a real browser.
- OpSec: fully passive; no subject data is entered.

## Overlaps ("do both")
- Pairs with `[[ilostat]]` and `[[ilo-world-employment-and-social-outlook-trends]]` — those provide labour statistics; this provides the occupation taxonomy that structures them.

## Trust & verifiability
`trust: trusted` — ISCO is maintained by the ILO (UN agency) and is the international standard for occupation classification, so its definitions are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-standard-classification-of-occupations |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
