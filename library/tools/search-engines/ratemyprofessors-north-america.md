---
id: ratemyprofessors-north-america
name: RateMyProfessors (North America)
description: Use when you have a `name` you think teaches at a college and want to confirm their institution and department — returns employer-org, geolocation.
url: http://www.ratemyprofessors.com
category: search-engines
path:
- search-engines
bestFor: Confirming that a named person is a professor/instructor and tying them to a specific school and department in North America.
selectorsIn:
- name
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free to search and read ratings; an account is only needed to post reviews.
opsec: passive
opsecNote: Passive read of a public reviews site — the professor is not notified you looked. Browse without logging in; a review account would tie your identity to the query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Student-submitted ratings (Cheddar/owned brand); the school/department linkage is reliable, but the review text is subjective and occasionally spoofed.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- RateMyProfessors
- RMP
tags:
- toddington
- specialty-search
- academia
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# RateMyProfessors (North America)

> Student-review directory of college instructors: a name confirms whether someone teaches, and pins them to a specific school and department.

## When to use
You have a `name` and a hint that the person is (or was) a college/university instructor in the US or Canada, and you want to confirm the affiliation cheaply. A hit ties the individual to a specific `employer-org` (institution), a department, and — via the campus — an approximate `geolocation`, plus a review history that can indicate the years they were active. Useful for occupation/affiliation confirmation in a broader profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ratemyprofessors.com and use the professor search; optionally scope by school first to disambiguate common names.
2. Open the professor page: institution, department, overall rating, tag cloud, and dated individual reviews.
3. Read the review timeline to bound the years the person taught there and to spot mentions of specific courses.
4. Pivot: the institution + department feeds a university staff-directory lookup for an official email/bio; the name + school feeds people-search and LinkedIn.

## Inputs → Outputs
- **In:** `name` (instructor)
- **Out:** `employer-org` (school + department), `geolocation` (campus location), plus an activity timeline from dated reviews
- **Empty/negative result looks like:** no profile — the person may not teach, may teach outside North America, may go by a different name, or simply was never reviewed. Absence is weak evidence.

## Gotchas & OpSec
- Human-in-the-loop: none to read; account only to post.
- OpSec: **passive** — no notification.
- Ratings are unverified student opinion and can be gamed; treat the institutional linkage as the reliable signal and the review content as soft. Common names collide — always disambiguate by school.

## Overlaps ("do both")
- Do both with the institution's official faculty/staff directory — RMP confirms the affiliation and rough tenure; the staff directory gives the authoritative email, title, and bio.

## Trust & verifiability
`trust: community` — crowd-sourced reviews; the school/department association is dependable, the prose is subjective. Corroborate the affiliation on the university's own site before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ratemyprofessors-north-america |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
