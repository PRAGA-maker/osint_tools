---
id: glassdoor
name: Glassdoor
description: Use when you have an `employer-org` (or a person's employer) and want inside detail — returns salaries, reviews, interview accounts, and occasionally employee `associate`/role signals.
url: https://www.glassdoor.com
category: public-records
path:
- public-records
bestFor: Researching a company's pay, culture, locations, and workforce from employee-submitted reviews and salary reports.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free to use, but Glassdoor gates most content behind a free account and a "give to get" wall (you must post a review/salary or register to read others'). No payment for the core content.
opsec: passive
opsecNote: Browsing company pages is passive and does not touch your target. However Glassdoor requires an account to see most content — register with a sock-puppet email, never a work/attributable identity, and avoid posting real content to unlock pages.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Reviews and salaries are self-reported, unverified, and can be manipulated (astroturfed or review-bombed); treat aggregate patterns as signal and individual reviews as anecdotes.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- glassdoor.com
tags:
- company-research
- employer
- reviews
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Glassdoor

> Employee-submitted salaries, reviews, and interview reports — a window into a target's employer, its offices, roles, and pay bands.

## When to use
You have an `employer-org` (perhaps a company where your subject works, or one you are vetting) and want context that public filings don't give: real salary ranges by role, office locations, org culture, hiring process, and sometimes named managers or team structure surfaced in reviews. Good for corroborating a claimed job/salary, understanding a workplace, or generating leads about roles and colleagues.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.glassdoor.com and search the `employer-org`.
2. Register a sock-puppet account if prompted (most content is gated behind login / the give-to-get wall).
3. Read the company profile: overall rating, reviews (pros/cons, often role and location tagged), salary reports by title, interview experiences, and photos.
4. Mine reviews and interview reports for role names, office locations, management structure, and occasional named individuals (`associate` leads).
5. Pivot: a confirmed role/employer feeds LinkedIn and people-search; office locations feed geolocation; named managers feed further person lookups.

## Inputs → Outputs
- **In:** `employer-org` (or a `name` to confirm against an employer)
- **Out:** `employer-org` detail (salaries, locations, culture), `associate`/role leads from reviews and interview accounts
- **Empty/negative result looks like:** small or private employers may have zero or a handful of reviews — thin data, not proof the company is fake; large firms may drown a specific office in generic reviews.

## Gotchas & OpSec
- Human-in-the-loop: an account is required for most pages; use a sock puppet and don't post attributable content to unlock.
- Self-reported and gameable — companies astroturf positive reviews and disgruntled staff review-bomb; weight the aggregate, distrust outliers.
- It profiles companies, not individuals — person-level leads are incidental, not a directory.

## Overlaps ("do both")
- Pairs with LinkedIn and people-search tools — Glassdoor gives the inside view of the `employer-org` (pay, culture, locations) while those confirm the specific person's role and identity.

## Trust & verifiability
`trust: community` — crowd-sourced, unverified employee content. Reliable as a directional read on a company; verify any specific claim (a salary, a name, a location) through a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | glassdoor |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
