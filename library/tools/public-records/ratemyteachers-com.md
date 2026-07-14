---
id: ratemyteachers-com
name: ratemyteachers.com
description: Use when you have a teacher's `name` (and ideally their school as `employer-org`) and want to confirm where they teach/taught — returns `employer-org` (school), subject, and public rating history.
url: https://ratemyteachers.com/
category: public-records
path:
- public-records
bestFor: Tying a named teacher to a specific school and time period via a public review profile.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
status: degraded
pricing: free
costNote: Free to search and read. Posting a review requires a free account; reading does not.
opsec: passive
opsecNote: Searching and reading profiles is passive and unauthenticated. Do NOT post a review — that is active, logged to an account, and pollutes the record.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced student reviews; useful for the structural fact (teacher X at school Y) but the ratings/comments themselves are unverified opinion.
missingPersonsRelevance: high
coverage:
- us
- ca
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Rate My Teachers
- RMT
tags:
- professionlicensing
- Profession & Licensing Sites
- education
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# ratemyteachers.com

> Crowd-sourced teacher-review directory whose OSINT value is the structured link between a teacher's `name` and a `school` — not the star ratings.

## When to use
You have a subject who is (or was) a schoolteacher and want to pin down which school they work at, what they teach, and roughly when they were active. A profile page can corroborate an employer and locale that other records only hint at. Note the site was rebuilt after a 2018 acquisition: pre-2019 written reviews were purged, EU listings were switched from teachers to courses to comply with GDPR, and coverage/quality is now uneven — hence `status: degraded`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ratemyteachers.com/ and search the teacher's `name`, optionally narrowing by school/city.
2. Open the matching profile; read the associated school (`employer-org`), subject, and any surviving rating history.
3. Cross-check the school + subject against other records (LinkedIn, district staff pages, licensing boards).
4. Pivot: a confirmed school feeds an employer/geolocation lens and staff-directory searches; the teacher's full name feeds people-search tools.

## Inputs → Outputs
- **In:** `name` (teacher), optionally `employer-org` (school) to disambiguate
- **Out:** `employer-org` (school), confirmed `name` spelling, subject, activity window
- **Empty/negative result looks like:** no profile, or only a course/school stub with no named teacher (common in EU/GDPR regions) — absence here does NOT mean the person isn't a teacher.

## Gotchas & OpSec
- Common names collide; always disambiguate with the school before attributing.
- Historical reviews were deleted in the 2018–2019 rebuild, so an empty/old profile is expected, not disproof.
- Ratings are unverified student opinion — use the *employment link*, not the sentiment, as intelligence.

## Overlaps ("do both")
- Pairs with `[[ratemyprofessors-com]]` (higher-ed equivalent) and general people-search tools — RMT covers K-12/secondary teachers those miss.

## Trust & verifiability
`trust: community` — user-submitted content on a commercial review platform; treat the teacher↔school association as a lead to verify, and the star ratings as opinion only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ratemyteachers-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
