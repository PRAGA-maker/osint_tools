---
id: reed-uk
name: Reed (UK)
description: Use when you have a `name` or `username` and want a UK jobseeker/CV or employer footprint — returns `social-profile`, `employer-org` and skills/work history leads.
url: https://www.reed.co.uk
category: people-search
path:
- people-search
bestFor: Checking one of the UK's largest job boards for a subject's public jobseeker profile, CV traces, or an employer's hiring footprint.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Free to browse jobs and register as a jobseeker/recruiter. Full CV database access is a paid recruiter product; public profiles/CV fragments may surface via search engines.
opsec: passive
opsecNote: Browsing jobs and public pages is passive. Viewing candidate CVs requires a recruiter account and may be logged; use a sock-puppet recruiter account and do not contact the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major, legitimate UK recruitment platform. Jobseeker-supplied data (CV, skills, history) is self-reported and unverified.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Reed.co.uk
- reed.co.uk
tags:
- job-search-resources
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Reed (UK)

> One of the UK's largest job boards — a place to find a subject's public jobseeker/CV footprint or an employer's hiring activity.

## When to use
Your subject is UK-based and may be job-hunting or working in a sector Reed covers. Use it to look for a public jobseeker profile, CV fragments (often surfaced via search engines), or the companies advertising roles tied to them — yielding `employer-org`, skills, and work-history leads that corroborate a professional identity or current location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search the open site (https://www.reed.co.uk) for the employer, role, or location relevant to your subject.
2. For candidate/CV data, use Google dorking (`site:reed.co.uk "<name>"`) since much of the CV database sits behind a recruiter login.
3. If you have a legitimate recruiter account (sock puppet), search the CV database by name/skills/location.
4. Read the `social-profile`/CV: current/past `employer-org`, job titles, skills, location, availability.
5. Pivot: take employer + role into LinkedIn/Companies House and cross-check the work history against other sources.

## Inputs → Outputs
- **In:** `name` or `username` (+ location/sector helps)
- **Out:** `social-profile`/CV fragments, `employer-org`, skills and work-history leads
- **Empty/negative result looks like:** no public match — the person isn't on Reed, has a private profile, or their CV is only in the recruiter-side database. Absence isn't proof they're not job-seeking; try other UK job boards and LinkedIn.

## Gotchas & OpSec
- **CV database is largely paywalled** to recruiters — the freely-visible surface is jobs and whatever search engines have indexed.
- Self-reported data: treat CV claims (titles, dates) as unverified.
- OpSec: browsing passive; recruiter-side CV views are account-linked — never reach out to the subject.

## Overlaps ("do both")
- Pairs with LinkedIn and other UK job boards (Indeed, TotalJobs) plus Companies House — Reed gives one slice of the employment footprint, cross-referencing confirms it.

## Trust & verifiability
`trust: community` — a legitimate major platform, but candidate content is self-authored. Verify employment claims against an employer directory or Companies House before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reed-uk |
| category | people-search |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
