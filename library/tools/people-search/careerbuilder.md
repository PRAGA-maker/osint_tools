---
id: careerbuilder
name: CareerBuilder
description: Use when you have a `name` or role and want employment/career signal — a US job board where public job postings and (employer-gated) resumes can corroborate a subject's work history.
url: https://www.careerbuilder.com
category: people-search
path:
- people-search
bestFor: Surfacing employment context — job postings tied to an employer, and (for recruiters) resume-database leads on a person's work history.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: freemium
costNote: Free to browse and search job postings; the resume database that contains individuals' CVs is a paid, employer/recruiter-gated product, not open to the public.
opsec: passive
opsecNote: Passive — browsing job listings leaks nothing about a subject. Creating a jobseeker or employer account to reach resumes is active and identity-linked; use a sock puppet and remember resume access is a paid recruiter feature, not free OSINT.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A major, legitimate US job board; its public job postings are reliable, but individual resume data sits behind an employer paywall and is self-reported by candidates.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- careerbuilder.com
tags:
- job-search-resources
- employment
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# CareerBuilder

> A large US job board — useful for employment context (who's hiring, role/employer links), but the part that actually profiles individuals (the resume database) is a paid recruiter product, not open OSINT.

## When to use
You want employment signal around a `name` or an `employer-org`: what roles a company is advertising, industry/location context, and — if you have legitimate recruiter access — a subject's self-posted resume with work history and contact details. For most open-source work its value is the public job side (corroborating an employer, understanding a role) rather than free people lookup, because resumes are paywalled.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.careerbuilder.com and use job search to explore postings by company, title, or location — this is free and public.
2. Note employer names, locations, and role details that corroborate a subject's stated job or employer.
3. For resume data (a candidate's CV, history, contact info): this requires a paid employer/recruiter account — only accessible with legitimate access, from a sock-puppet identity, and within terms of use.
4. Pivot: a confirmed `employer-org` feeds corporate-registry and LinkedIn research; a resume (if lawfully accessed) yields work history, skills, and contact selectors.

## Inputs → Outputs
- **In:** a `name` (for resume search, paid) or an `employer-org`/role (for free job search)
- **Out:** job postings and employer context; (paid) resume records with `name`, work history, and contacts
- **Empty/negative result looks like:** no job postings for a company just means nothing is currently advertised; no public result for a person is expected — individuals aren't searchable without the paid resume product.

## Gotchas & OpSec
- **Resumes are paywalled:** the individual-profiling capability is a recruiter feature, not free OSINT — don't assume you can look a person up here for free.
- US-focused; limited value outside the US market.
- Job-board data (postings) is reliable; resume content is self-reported by candidates — corroborate before trusting.

## Overlaps ("do both")
- Complements LinkedIn and corporate-registry tools — CareerBuilder adds job-posting/employer context, while those provide the person-level professional profile more directly (and often without a paywall).

## Trust & verifiability
`trust: community` — an established, legitimate job board; public postings are trustworthy, while resume records are gated and candidate-self-reported, so verify any personal detail against an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | careerbuilder |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
