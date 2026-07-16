---
id: openoversight
name: OpenOversight
description: Use when you have a `name`, badge, or `image` of a US police officer and want to identify them — returns name, image, dob.
url: https://openoversight.com/
category: public-records
path:
- public-records
bestFor: Identifying US law-enforcement officers from a name, badge/department, or a photo, using a crowd-sourced accountability database.
selectorsIn:
- name
- employer-org
- image
selectorsOut:
- name
- image
- dob
status: live
pricing: free
costNote: Free and volunteer-funded (Lucy Parsons Labs). No account needed to search; submitting photos is optional and free.
opsec: passive
opsecNote: A passive read of a public transparency database — no subject is notified. It concerns public officials acting in an official capacity; keep use within lawful accountability/research purposes and avoid uploading investigation material you don't want public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced from public and volunteer-processed records (Lucy Parsons Labs); accurate where curated, but coverage is limited to participating departments.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OpenOversight
- Lucy Parsons Labs OpenOversight
tags:
- public-records
- police-accountability
- face-search
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# OpenOversight

> A crowd-sourced accountability database of US police officers: turn a name, badge, department, or photo into an identified officer with photos and biographical details.

## When to use
You have a US law-enforcement officer to identify — a `name`, a badge/star number, a department (`employer-org`), or a uniformed `image` — and you want to match them to a person. OpenOversight consolidates officer `name`s, badge numbers, `dob`s, salaries, news mentions, and `image`s for participating departments, and supports a "browse by department to identify a face" workflow. Useful for confirming an officer's identity or building a profile from a single photo.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://openoversight.com and pick the target department (coverage spans a couple dozen departments across several states plus some federal agencies).
2. Search by officer name or badge number, or use the "Find an Officer" / gallery flow to compare a photo you hold against uniformed images in that department.
3. Open a matched profile: name, badge/star, department, recorded DOB, salary history, news mentions, and photos.
4. Pivot: a confirmed `name` feeds people-search and court-records; the `dob` narrows identity matches; the photo feeds reverse-image/face tooling.

## Inputs → Outputs
- **In:** `name`, `employer-org` (department), and/or an `image` of a uniformed officer
- **Out:** officer `name`, `image`(s), `dob`, plus badge number, salary, and news mentions
- **Empty/negative result looks like:** no match — the officer's department isn't covered, or their record hasn't been added. Coverage is partial and department-scoped, so absence is common and not conclusive.

## Gotchas & OpSec
- Human-in-the-loop: none required; the face-matching step is your own visual comparison, not automated recognition.
- OpSec: **passive**, concerning public officials. Do not upload sensitive case imagery you don't want in a public database.
- Coverage is narrow (participating departments only) and crowd-maintained — verify a match against an official source before acting on it.

## Overlaps ("do both")
- Do both with public salary/payroll databases and court-records search — OpenOversight gives the identification and photo; payroll and court records corroborate employment and surface incidents.

## Trust & verifiability
`trust: community` — volunteer-curated from public records; individual profiles are as good as their sourcing. Confirm any identification against department rosters or official disclosures.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openoversight |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, image → name, image, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
