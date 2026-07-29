---
id: angellist
name: AngelList
description: Use when you have a `name` or startup/`employer-org` and want founder, employee, and investor profiles from the startup ecosystem — returns employer-org, associate and social-profile leads.
url: https://angel.co
category: documents-metadata
path:
- documents-metadata
bestFor: Profiling startups and the people around them — founders, employees, and investors — via the AngelList/Wellfound ecosystem.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- social-profile
status: live
pricing: freemium
costNote: Free to browse many company and people profiles; angel.co now redirects to Wellfound (the talent/jobs side). Some profiles/features and full recruiter tools need a free account or paid plan.
opsec: passive
opsecNote: Passive — browsing public startup/people profiles. Signing in (recommended for fuller profiles) ties viewing to your account and some profiles can see recruiter/viewer activity — use a sock-puppet account and avoid "connect"/message actions that notify the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known startup platform (AngelList → Wellfound); profiles are largely self-reported by users and companies, so treat roles/titles as claimed, not verified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- AngelList
- Wellfound
- angel.co
tags:
- toddington
- companies-finance
- startups
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# AngelList

> The startup ecosystem's directory (now Wellfound for talent) — founder, employee, and investor profiles you can use to map who's behind a company and who they're connected to.

## When to use
You have a `name` or a startup/`employer-org` and want the human graph around it: who founded or works at a company, who invested, and the roles people claim. Profiles link individuals to companies (current and past), surfacing `associate` relationships (co-founders, colleagues, investors) and self-listed social/portfolio links. Useful for corporate/people investigations in the tech/startup world, or to enrich a subject who works in startups. Note angel.co now redirects to Wellfound (the jobs/talent product).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://angel.co (redirects to Wellfound) — browse public content, or sign in with a sock-puppet account for fuller profiles.
2. Search a person's `name` or a company; open the profile.
3. On a company: read the team (founders/employees), investors, and description. On a person: their current/past companies, role, and linked profiles.
4. Follow the links between people and companies to build the network.
5. Pivot: a founder/employee `name` → LinkedIn/other social; linked personal site → domain tooling; investor list → the funding network around the company.

## Inputs → Outputs
- **In:** a person `name` or a startup `employer-org`
- **Out:** company team/investor lists, individuals' current/past roles (`employer-org`), co-workers/co-founders/investors (`associate`), self-listed links (`social-profile`)
- **Empty/negative result looks like:** no profile, a bare stub, or a login wall — the person/company isn't on the platform or keeps a minimal profile; absence here ≠ no startup involvement.

## Gotchas & OpSec
- Profiles are self-reported — titles, dates, and affiliations are claims to verify, not facts.
- Full profiles increasingly need a login; use a sock-puppet and avoid connect/message actions that alert the subject.
- Post-rebrand the talent side is Wellfound; some legacy AngelList venture features live elsewhere.

## Overlaps ("do both")
- Pairs with LinkedIn, Crunchbase, and corporate registries (`[[federalcorporation]]`) — AngelList/Wellfound is strong on early-stage startup people; the others cover formal filings and broader employment.

## Trust & verifiability
`trust: community` — reputable platform, but content is user/company-submitted; corroborate roles and affiliations against filings or a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | angellist |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
