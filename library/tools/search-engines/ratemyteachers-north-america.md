---
id: ratemyteachers-north-america
name: RateMyTeachers (North America)
description: Use when you have a teacher's `name` or a school and want to confirm an `employer-org` affiliation and location — returns school/district links and ratings.
url: http://ratemyteachers.com
category: search-engines
path:
- search-engines
bestFor: Tying a K-12 teacher's name to the specific school/district (and thus town) where they work, via a crowd-sourced ratings directory.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- geolocation
status: degraded
pricing: free
costNote: Free to search and read. A 2019 relaunch wiped all legacy open-text reviews, so historical commentary is gone; current data is thinner survey-style ratings.
opsec: passive
opsecNote: Read-only public search; the teacher is not notified. Posting a rating would be active and is unnecessary for OSINT — stay on the search/read side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced ratings site; the school/location linkage is generally reliable, but ratings themselves are anonymous, sparse post-2019, and easily gamed.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ratemyteachers-com
- www-ratemyteachers-com
aliases:
- ratemyteachers.com
- Rate My Teachers
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# RateMyTeachers (North America)

> A crowd-sourced US/Canada directory of school teachers, most useful now as a name→school→town affiliation lookup rather than for its (largely wiped) reviews.

## When to use
You have the `name` of a K-12 teacher and want to confirm **where** they teach — the specific school and district, which places them in a town/region — or you're working a school and want the roster of named staff. The ratings themselves are secondary and thin since the 2019 review purge; the durable value is the person↔school↔location link.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://ratemyteachers.com and pick the country/state (it is organised US/Canada by state → district → school).
2. Search the teacher `name`, or drill down through the school if you already suspect one.
3. Read the profile: associated school(s), subject/role, and any surviving ratings.
4. Extract the `employer-org` (school/district) and its `geolocation` (city/state).
5. Pivot: confirm current employment on the school's own staff directory or district site; use the town to seed local records searches.

## Inputs → Outputs
- **In:** `name` (teacher) or `employer-org` (school)
- **Out:** `employer-org` (school/district) and `geolocation` (city/state)
- **Empty/negative result looks like:** no listing — common now, because the 2019 relaunch dropped much legacy content and many teachers were never re-added. Absence is not evidence the person isn't a teacher; fall back to the school's own directory.

## Gotchas & OpSec
- **Post-2019 the archive is gutted:** all old open-text reviews were deleted for GDPR/ToS reasons, so expect sparse coverage and survey-style ratings only.
- Ratings are anonymous and gameable — never treat a rating as fact; use the site for the affiliation, not the opinions.
- OpSec: passive read-only search.

## Overlaps ("do both")
- Pairs with [[ratemyteachers-com]] / [[www-ratemyteachers-com]] (the same service under sibling entries) and with official school staff directories, which confirm the current employment this site only suggests.

## Trust & verifiability
`trust: community` — crowd-sourced. The school/location association is usually right and easy to verify against the school's own site; the ratings are anonymous and low-coverage, so corroborate before relying on any of it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ratemyteachers-north-america |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
