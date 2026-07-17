---
id: alumni-net
name: Alumni.NET
description: Use when you have a `name` plus a school/location and want to find their alumni-directory profile — returns a `social-profile` and school/graduation-year context.
url: https://www.alumni.net
category: communities-forums
path:
- communities-forums
bestFor: Searching a global school/university alumni directory for a person's profile, school, and graduation year.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
status: degraded
pricing: free
costNote: Free to search and register; ad-supported. Largely superseded by Facebook/LinkedIn, so coverage is patchy and profiles are often old.
opsec: passive
opsecNote: Browsing/searching is passive. Viewing full member details or messaging typically requires you to register — do so only with a sock-puppet account, as registering and interacting is attributable and may notify members.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Old-style alumni social directory; profiles are self-submitted and frequently stale, so data is lead-quality and must be corroborated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- alumni-member-search
- classmates
aliases:
- Alumni.net
- alumni.net
tags:
- classmates
- alumni
- people-search
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
---

# Alumni.NET

> An old-school global alumni directory — a place to look for a person tied to a specific school or university, and the era they were there.

## When to use
You have a `name` and a school/university (or a rough location and age) and want to find them via an alumni listing. Alumni.NET lets you browse/search by institution and country for member profiles that state school, graduation year, and sometimes location or contact. It's most useful for older subjects or historical connections that predate mainstream social media. Temper expectations: it has largely been superseded by Facebook/LinkedIn, so coverage is thin and profiles are often years out of date.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.alumni.net.
2. Browse by country → school, or search by the subject's `name` / institution.
3. Open candidate profiles: check school, graduation year, stated location, and any linked contact.
4. Match against what you already know (age, region) to disambiguate common names.
5. Pivot: a graduation year + school narrows other searches; a confirmed profile (`social-profile`) and any listed employer/location feed people-search and social tools.

## Inputs → Outputs
- **In:** `name` (plus a school/institution or location to disambiguate)
- **Out:** `social-profile` (alumni listing), school/graduation-year context, sometimes `employer-org` or location
- **Empty/negative result looks like:** no profile — very common, since most people never registered here. Absence says nothing; move to mainstream social networks.

## Gotchas & OpSec
- Sparse and dated: many schools have few or no members; treat a miss as expected, not meaningful.
- Full details/messaging often need a (free) account — use a sock puppet, since registering and contacting members is attributable.
- OpSec: passive to search; active if you register or message.

## Overlaps ("do both")
- Pairs with `[[classmates]]` and `[[alumni-member-search]]` — cross-check the same person across alumni directories, and confirm any lead on LinkedIn/Facebook, which now hold most of this data.

## Trust & verifiability
`trust: unverified` — self-submitted, often-stale alumni profiles on a legacy platform. Useful as a lead source for school/era, but every detail should be corroborated against a current source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alumni-net |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
