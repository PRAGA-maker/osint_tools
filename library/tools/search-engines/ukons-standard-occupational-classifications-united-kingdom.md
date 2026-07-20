---
id: ukons-standard-occupational-classifications-united-kingdom
name: UK ONS Standard Occupational Classification (SOC 2010)
description: Use when you have a UK job-title lead and want to normalize it to the ONS SOC occupation code — returns the standard classification, not a person.
url: https://webarchive.nationalarchives.gov.uk/20160106024159/http://www.ons.gov.uk/ons/guide-method/classifications/current-standard-classifications/soc2010/index.html
category: search-engines
path:
- search-engines
bestFor: Normalizing a UK job title into the ONS Standard Occupational Classification (SOC) code and understanding what a role covers.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free UK government reference (archived ONS guidance); no account needed.
opsec: passive
opsecNote: A static classification reference — reading it submits nothing about the subject and touches no target infrastructure. Purely a passive interpretation aid.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the UK Office for National Statistics; SOC is the official UK occupation taxonomy. The linked copy is a National Archives web-archive snapshot of the SOC 2010 pages.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- ONS SOC 2010
- UK Standard Occupational Classification
tags:
- toddington
- curated-directory
- specialty-search
- occupation-reference
source: toddington-resources
lastVerified: '2026-07-20'
---

# UK ONS Standard Occupational Classification (SOC 2010)

> The UK's official occupation taxonomy (ONS SOC) — a reference for interpreting and normalizing a UK job title, not a way to find the person holding it.

## When to use
You have a UK occupational lead — a stated job title, a role from a profile or CV, an `employer-org` position — and you want to normalize it to the official ONS Standard Occupational Classification (SOC 2010) code, or to understand precisely what a vague UK title covers. Useful for interpreting UK labour/administrative data that uses SOC codes, disambiguating a job title, or comparing roles consistently. It's a **classification reference**: it returns codes and definitions, never a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the SOC 2010 index (linked via the National Archives web-archive; the live ONS site has since reorganized — search "ONS SOC 2020/2010" for the current version).
2. Drill through the SOC hierarchy (major group → sub-major → minor → unit group) or search the job title.
3. Read the group definition to confirm the tasks/skills the title encompasses; note the numeric SOC code.
4. Use the code to cross-reference occupation fields in UK datasets or to standardize a role description.
5. Pivot: an interpreted occupation sharpens searches on UK professional registers, licensing bodies, and employer records.

## Inputs → Outputs
- **In:** a UK job title / role (an `employer-org` lead)
- **Out:** the ONS SOC code and definition (a normalized `employer-org`/role descriptor)
- **Empty/negative result looks like:** a title with no clean SOC match usually means a vanity/marketing title — map it to the nearest unit group by task description.

## Gotchas & OpSec
- Reference only — it classifies *occupations*, so no person will be found here.
- The URL is an archived snapshot; ONS has newer SOC editions (SOC 2020) — check whether you need the current version.
- OpSec: fully passive; no subject data entered.

## Overlaps ("do both")
- Pairs with `[[international-standard-classification-of-occupations]]` (ISCO) — SOC is the UK national scheme; ISCO is the international equivalent for cross-country comparison.

## Trust & verifiability
`trust: trusted` — SOC is maintained by the UK ONS and is the authoritative national occupation classification; definitions are reliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukons-standard-occupational-classifications-united-kingdom |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
