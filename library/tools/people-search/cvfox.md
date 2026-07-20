---
id: cvfox
name: CVFox
description: Use when you have a `name` (± employer/skill) and want to find a subject's CV/résumé published online — returns résumé documents yielding `email`, `phone`, `employer-org`, and `address`.
url: http://www.cvfox.com
category: people-search
path:
- people-search
bestFor: Surfacing a person's résumé/CV posted anywhere on the web, which often carries direct contact details and full work/education history.
selectorsIn:
- name
- employer-org
selectorsOut:
- email
- phone
- employer-org
status: live
pricing: free
costNote: Free web tool / portal of résumé-search utilities and boolean-string generators; no payment to run the searches.
opsec: passive
opsecNote: CVFox builds Google/boolean queries that run against public search engines — it doesn't touch the subject. Passive. Still run the resulting searches from a sock-puppet/logged-out session and avoid opening subject-controlled links directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: CVFox is an established recruiter-focused résumé-search portal with in-house boolean tooling; it's a query builder over public indexes, so results are only as good as what's publicly posted.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- cvfox.com
- CV Fox
tags:
- job-search-resources
- resume-search
- people-search
source: awesome-osint
lastVerified: '2026-07-20'
---

# CVFox

> A résumé-search portal — it builds boolean/Google queries that surface a subject's CV wherever it's posted online, and CVs are a goldmine of direct contact and history.

## When to use
You have a `name` (optionally plus an `employer-org`, skill, or location) and want to find a résumé/CV the subject has published — on a personal site, a job board, a university page, or a stray PDF. Résumés are exceptionally rich: `email`, `phone`, full `employer-org` history, education, `address`, and sometimes references (`associate`s). CVFox aggregates résumé-hunting search engines and generates boolean/`filetype:` strings tuned to find CVs across the public web, saving you from hand-crafting each dork.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.cvfox.com.
2. Use its résumé-search tools / boolean generators, entering the subject's `name` plus a discriminator (skill, employer, city).
3. Run the generated queries (they target CV-like pages: `filetype:pdf resume "Name"`, site-restricted job-board searches, etc.).
4. Open candidate résumés and extract `email`, `phone`, employment/education history, `address`.
5. Pivot: contact details feed email/phone OSINT; employment history feeds registry and professional-network searches.

## Inputs → Outputs
- **In:** `name` (+ optional `employer-org`/skill/location)
- **Out:** résumé documents → `email`, `phone`, `employer-org` history, `address`, education
- **Empty/negative result looks like:** no résumé indexed for the subject — common if they never posted one publicly; absence is not evidence they're unemployed or hidden.

## Gotchas & OpSec
- It's a query *builder* over public search engines, not a private database — coverage equals what's publicly indexed.
- Common names need a strong discriminator or you'll drown in false résumés.
- OpSec: passive, but run the searches from a clean session; verify a résumé actually belongs to your subject before trusting its contacts.

## Overlaps ("do both")
- Pairs with the Google operators reference (`[[google-search-operators-guide]]`) and professional-network searches — CVFox seeds the dorks; those refine and corroborate the person behind the CV.

## Trust & verifiability
`trust: community` — a legitimate recruiter tool, but it only finds public content; always confirm a found résumé matches your subject (name collisions are common) before acting on its details.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cvfox |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → email, phone, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
