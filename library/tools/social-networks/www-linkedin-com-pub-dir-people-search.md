---
id: www-linkedin-com-pub-dir-people-search
name: LinkedIn Public Directory People Search
description: Use when you have a `name` (optionally + employer) and want to find a subject's LinkedIn profile — returns their profile, current/past employer and professional history; now requires a logged-in account.
url: http://www.linkedin.com/pub/dir/people/search
category: social-networks
path:
- social-networks
bestFor: Finding a person's LinkedIn profile by name (and disambiguating by employer) to pull employment and professional history.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
- name
status: degraded
pricing: freemium
costNote: Free with a LinkedIn account; the old unauthenticated /pub/dir public directory has been largely locked down, so you now need to be logged in (a free account works; Sales Navigator is not required).
opsec: active
opsecNote: LinkedIn logs profile views and, by default, tells a member when you view their profile. Use a dedicated sock-puppet account set to Private/anonymous browsing mode, never your real account, and be aware LinkedIn actively rate-limits and blocks scraping.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: First-party LinkedIn data (authoritative for self-reported employment), but profiles are self-asserted and LinkedIn increasingly gates and obfuscates search for non-logged-in and non-premium users.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- LinkedIn people directory
- linkedin.com/pub/dir
tags:
- linkedin
- LinkedIn & Similar Sites
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
relatedTools:
- griffin-glynn-hatless1der
- hatless-investigations-group
- linkedin
- linkedin-advanced-search
- linkedin-com
- linkedin-groups
- robert-devere-bunn
---

# LinkedIn Public Directory People Search

> LinkedIn's name-based people search: find a subject's profile and pull their employment and professional history — the legacy public `/pub/dir` path now funnels into logged-in search.

## When to use
You have a `name` (and ideally an `employer-org`, school, or location to disambiguate) and want the subject's LinkedIn profile: current and past employers, job titles, education, location, and connections' context. LinkedIn is the authoritative source for self-reported professional history, so it confirms a workplace, timeline, and often a photo — high value for identity confirmation and for pivoting to colleagues.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log in with a dedicated sock-puppet LinkedIn account (never your real one). In Settings, set profile-viewing to Private/anonymous mode first.
2. Use LinkedIn's people search (the legacy `linkedin.com/pub/dir/people/search` URL now redirects into the standard logged-in search). Enter the `name`.
3. Narrow with filters — current/past company (`employer-org`), location, school — to cut down common-name noise.
4. Open the matching profile: employment history, titles with dates, education, location, and the profile photo. Note the "People also viewed" panel for colleagues/`associate` leads.
5. Pivot: an employer feeds company-registry and staff-directory searches; a photo feeds reverse-image/face search; the vanity URL/handle feeds cross-platform username search.

## Inputs → Outputs
- **In:** `name` (+ optional `employer-org`, school, location)
- **Out:** `social-profile`, current/past `employer-org`, titles/dates, education, photo
- **Empty/negative result looks like:** no matching profile, or search results hidden behind a "commercial use limit" / auth wall — the latter is a rate-limit signal, not proof the person has no LinkedIn.

## Gotchas & OpSec
- Human-in-the-loop: you must be logged in; unauthenticated `/pub/dir` browsing is effectively closed.
- OpSec: **active** — LinkedIn notifies members of profile views by default and aggressively rate-limits/blocks. Use anonymous-viewing mode and a disposable account; expect "commercial use limit reached" if you search heavily.
- Self-reported data: titles and dates can be inflated — corroborate against company registries where it matters.

## Overlaps ("do both")
- Pairs with X-ray Google searches (`site:linkedin.com/in "Name" "Company"`) — those surface profiles without logging in and sidestep LinkedIn's in-app gating, while the logged-in directory gives the full profile.

## Trust & verifiability
`trust: community` — first-party and authoritative for self-reported employment, but profiles are user-written and LinkedIn's gating/obfuscation means coverage depends on your account and rate limits; corroborate key claims externally.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | www-linkedin-com-pub-dir-people-search |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
