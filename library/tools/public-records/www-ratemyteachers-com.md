---
id: www-ratemyteachers-com
name: RateMyTeachers
description: Use when you have a teacher/educator `name` and want to confirm and place them at a specific school — returns employer-org (school), address (school location) and corroborating name.
url: http://ie.ratemyteachers.com/
category: public-records
path:
- public-records
bestFor: Placing a named teacher at a named school and confirming the employer/location link.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
status: degraded
pricing: free
costNote: Free to browse and search; no account needed to view ratings.
opsec: passive
opsecNote: Third-party review site; querying does not alert the subject. Only browse — do not post a rating or comment, as that leaves an attributable trace and taints the record.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: User-generated review site; entries are crowd-submitted and unverified, and can be fabricated or misattributed. Use only to corroborate a teacher↔school link, never as sole proof.
missingPersonsRelevance: high
coverage:
- ie
- us
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Rate My Teachers
- ratemyteachers.com
- ie.ratemyteachers.com
tags:
- professionlicensing
- Profession & Licensing Sites
- education
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# RateMyTeachers

> A crowd-sourced teacher-review directory, useful as a soft confirmation that a named educator worked at a particular school.

## When to use
You have a `name` you believe belongs to a teacher and you want to tie them to a specific `employer-org` (school) and its `address`. Because entries are organised school-by-school, finding a teacher listed under a school corroborates an employment/location link that can anchor a wider search. Best treated as a corroboration source, not a discovery engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ratemyteachers.com/ie (or the country/region index) in a normal browser.
2. Search or drill down by region → school, then scan the school's teacher list for the `name`. You can also search a teacher name directly.
3. Read the result: a match places the person at a named school with a location; the profile may show subject taught and rating history that corroborates tenure/era.
4. Pivot: the confirmed school (`employer-org` + `address`) feeds staff directories, local news, and social-profile searches for colleagues/associates.

## Inputs → Outputs
- **In:** `name` (teacher), optionally `employer-org`/`address` to narrow
- **Out:** `employer-org` (school), `address` (school location), corroborating `name`
- **Empty/negative result looks like:** no teacher entry under the school, or a same-name teacher at a different school — not proof the person isn't/wasn't a teacher.

## Gotchas & OpSec
- **Degraded for the EU:** to comply with GDPR the site shifted EU listings (including Ireland) from rating individual teachers to rating courses/schools, so person-level detail is thinner there than in the US. Adjust expectations by region.
- Entries are unverified user content — names can be misspelled, fabricated, or attributed to the wrong person. Corroborate the teacher↔school link elsewhere before relying on it.
- Passive: browse only. Do not submit a rating/comment — that is attributable and pollutes the record.

## Overlaps ("do both")
- Pairs with an official teaching-registration/licensing register for the jurisdiction — the register authoritatively confirms qualification/registration, while RateMyTeachers suggests the specific school placement the register may not name.

## Trust & verifiability
`trust: unverified` — crowd-sourced, moderator-light review content with no identity verification. Good for generating a lead ("teacher X at school Y"); never sufficient as sole confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | www-ratemyteachers-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
