---
id: dice
name: Dice
description: Use when you have a `name` or `username` of a US tech worker and want their professional profile — returns employer, skills, location, and career history.
url: https://www.dice.com
category: people-search
path:
- people-search
bestFor: Finding a US technology professional's resume/profile — employer, skills, and metro location — via a tech-specialty job board.
selectorsIn:
- name
- username
- employer-org
selectorsOut:
- employer-org
- name
- geolocation
status: live
pricing: freemium
costNote: Free to create a profile and browse jobs; recruiter-side candidate search is a paid employer product, so free reconnaissance is mostly via profiles surfaced in search engines.
opsec: passive
opsecNote: Browsing public Dice job posts and any indexed candidate pages is passive. Do NOT sign up as an employer and run candidate searches against a target — that leaves a business-account trail and may notify the candidate. Stick to what's publicly indexable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Dice is a long-established, reputable US tech-recruitment marketplace (owned by DHI Group); profile data is self-reported by the professionals themselves.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- linkedin
- indeed
aliases:
- dice.com
- Dice Careers
tags:
- job-search-resources
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Dice

> A US tech-specialty job board — a niche people-search angle for confirming a technology professional's current employer, skills, and metro area.

## When to use
Your subject works in IT/software/engineering in the United States. Where LinkedIn is your first stop, Dice is a useful corroborating source: tech professionals post resumes and profiles here, and job-history/skills details sometimes appear that aren't on their LinkedIn. Use it to confirm an `employer-org`, a skill set, or a work `geolocation` for a tech-sector subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try a scoped search-engine query first — `site:dice.com "Full Name"` on `[[google]]`/`[[bing]]` — since indexed profile/resume pages are the most reliable free entry point.
2. On dice.com, browse job postings that might name the person's team/company, and use the profile search where public.
3. Read the profile: title, skills, listed employers, metro location, and any linked portfolio.
4. Cross-reference every claim — profiles are self-reported and often stale.
5. Pivot: confirmed employer/skills → `[[linkedin]]` and `[[indeed]]` for a fuller work history; company name → corporate-records and staff-directory lookups.

## Inputs → Outputs
- **In:** `name`, `username`, or `employer-org` of a US tech worker
- **Out:** `employer-org`, current `name`/title, skills, and work `geolocation` (metro)
- **Empty/negative result looks like:** no matching profile — the person may not be in tech, may not use Dice, or their profile isn't public (recruiter-side search is paywalled); fall back to LinkedIn/Indeed.

## Gotchas & OpSec
- Real candidate search is an employer-paid product; free OSINT here is mostly limited to what search engines have indexed. Don't pay for/register an employer account to hunt an individual — it's a heavy, traceable footprint.
- US-tech-centric: near-useless outside the US or for non-technical subjects.
- Profiles are self-reported and frequently outdated; treat as leads, not facts.

## Overlaps ("do both")
- Pairs with `[[linkedin]]` — LinkedIn is broader and current; Dice sometimes exposes resume detail (past contracts, niche skills) LinkedIn hides.
- Pairs with `[[indeed]]` — another resume/job source to triangulate employment history.

## Trust & verifiability
`trust: trusted` — Dice is an established, legitimate recruitment platform. The *platform* is reliable; the *profile content* is self-authored by users, so corroborate specifics independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dice |
| category | people-search |
| selectorsIn → selectorsOut | name, username, employer-org → employer-org, name, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
