---
id: jobsite-uk
name: Jobsite (UK)
description: Use when you have a `name` or `employer-org` and want UK job-market context — returns job listings and, for logged-in recruiters, candidate profiles.
url: https://www.jobsite.co.uk
category: people-search
path:
- people-search
bestFor: UK job-board context — listings by employer/role and (recruiter-gated) candidate CV search.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- social-profile
status: live
pricing: freemium
costNote: Free for jobseekers to browse and set up a profile; recruiter CV-database search is a paid employer product.
opsec: passive
opsecNote: Browsing public job listings is passive and unauthenticated. The candidate/CV database is not openly searchable — it sits behind a paid recruiter login — so any people-search use requires an employer account and is limited by what candidates chose to publish.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by The Stepstone Group (a major job-board operator); a legitimate site, but weak as a direct people-search source because candidate data is employer-gated and self-reported.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Jobsite
- jobsite.co.uk
- StepStone Jobsite
tags:
- employment
- job-board
- uk
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Jobsite (UK)

> A mainstream UK job board (StepStone Group) — mostly useful for employment context and, only via a recruiter account, candidate CV search.

## When to use
A low-yield people-search resource, best when a subject's UK employment is the question. Two uses: (1) unauthenticated, browse job listings to understand an `employer-org`'s hiring, roles, and locations; (2) with a recruiter/employer account, search the candidate/CV database for a `name`. Manage expectations — the candidate side is paywalled and only contains what jobseekers voluntarily posted, so this rarely locates a person on its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.jobsite.co.uk.
2. **Public use:** search listings by role, sector, employer, or location to profile an organisation's hiring footprint.
3. **Recruiter use:** log into an employer account and use CV/candidate search to look up a `name` (paid; requires registration).
4. Read the output: for listings, employer + role + location; for candidate hits, a self-reported profile/CV.
5. Pivot: a candidate profile can yield employment history, skills, and a partial location — corroborate against LinkedIn and other employment sources.

## Inputs → Outputs
- **In:** `name` (recruiter search) or `employer-org`/role (public listings)
- **Out:** job listings, employer context; recruiter-gated candidate `social-profile`/CV
- **Empty/negative result looks like:** no listings for an employer/role, or (as a recruiter) no candidate by that name — the latter is weak evidence since most people aren't in any single job board's CV pool.

## Gotchas & OpSec
- Candidate/CV search is **not free or open** — it needs a paid employer login; without one this is only a job-listings site.
- Candidate data is self-reported and sparse; treat any match as a lead, not confirmation.
- OpSec: passive for listings; a recruiter login ties queries to your account.

## Overlaps ("do both")
- Pairs with LinkedIn and dedicated employment/people-search tools, which cover professional history far more completely — use Jobsite only for UK job-board-specific context or when you already have recruiter access.

## Trust & verifiability
`trust: community` — a legitimate commercial job board, but for people-search the data is self-reported and employer-gated, so it's a weak, corroborating source rather than an authoritative one.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jobsite-uk |
