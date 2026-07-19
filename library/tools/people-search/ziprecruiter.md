---
id: ziprecruiter
name: ZipRecruiter
description: Use when you have a `name` and want employment/job-history leads — returns candidate resumes, job-seeker profiles and employer context from a major US job marketplace.
url: https://www.ziprecruiter.com
category: people-search
path:
- people-search
bestFor: Finding a subject's job-seeker profile/resume or employer/job-posting context on a large US employment marketplace.
selectorsIn:
- name
selectorsOut:
- employer-org
- geolocation
- social-profile
status: live
pricing: freemium
costNote: Free to browse job listings and register as a job-seeker; recruiter-side candidate search (full resume database) requires a paid employer account. Public job postings and some profile data are free.
opsec: passive
opsecNote: Browsing public listings is passive. Accessing candidate resumes at scale means posing as an employer (paid account) — that leaves a footprint and may notify candidates their profile was viewed. Use a sock-puppet employer identity only if genuinely necessary and lawful.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A large, legitimate US job marketplace; profile/resume data is self-reported by job-seekers, so treat stated employers/locations as claims to corroborate.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- ZipRecruiter.com
tags:
- job-search-resources
- employment
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# ZipRecruiter

> A major US job marketplace — useful for tying a `name` to employment history, a current job search, or an employer, via job-seeker profiles/resumes and job postings.

## When to use
You have a `name` and want employment leads: is the subject job-hunting, where have they worked, what's their claimed location and role, and which employers are connected. Job-seeker profiles and resumes can reveal `employer-org` history, `geolocation`, skills, and sometimes contact/`social-profile` links — valuable for locating someone through their work life or confirming an occupation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ziprecruiter.com. For public data, use a search engine `site:ziprecruiter.com "<name>"` to surface indexed profiles/postings.
2. For the candidate/resume database, an employer account (paid) is required — only pursue this lawfully and with justification.
3. Read the profile/resume for work history (`employer-org`), location, skills, and any linked contacts.
4. Corroborate self-reported details against LinkedIn and other records — job profiles are unverified.
5. Pivot: employer names feed company/colleague OSINT; location feeds people-search; linked handles feed username enumeration.

## Inputs → Outputs
- **In:** `name`
- **Out:** job-seeker profile/resume data — `employer-org` history, `geolocation`, skills, possible `social-profile`/contact
- **Empty/negative result looks like:** no public profile — the subject may not use ZipRecruiter, has a private profile, or isn't job-seeking. Absence says nothing about their employment; check LinkedIn and other job sites.

## Gotchas & OpSec
- Deep candidate search is paywalled behind an employer account and may alert candidates to profile views.
- Self-reported data — corroborate employers/locations elsewhere.
- OpSec: passive for public browsing; employer-account use leaves a footprint.

## Overlaps ("do both")
- Pairs with LinkedIn X-ray tools like `[[recruitem]]` and Indeed/other job boards — cross-reference employment claims across platforms, since each holds different self-reported detail.

## Trust & verifiability
`trust: community` — a legitimate large marketplace, but profile content is self-reported and unverified; use it for leads and confirm identity/employment against authoritative or cross-referenced sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ziprecruiter |
| category | people-search |
| selectorsIn → selectorsOut | name → employer-org, geolocation, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
