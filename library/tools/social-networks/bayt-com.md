---
id: bayt-com
name: bayt.com
description: Use when you have a `name`/`username` of a Middle East / Gulf professional and want their CV-style profile and work history — returns a `social-profile`, `name`, and `employer-org`.
url: https://www.bayt.com/
category: social-networks
path:
- social-networks
bestFor: Profiling a Middle East / Gulf region jobseeker or professional via their Bayt CV/profile and employment history.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- employer-org
status: live
pricing: freemium
costNote: Free to browse the site and some public profiles; recruiter/full-CV access and messaging require an account (jobseeker or employer), and employer/CV-search features are paid.
opsec: active
opsecNote: Viewing profiles typically requires a logged-in account, and recruiter-side actions can leave visitor/contact traces. Register and browse from a sock-puppet account with a plausible regional persona; never use an attributable identity, especially given the professional context.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Bayt is the leading legitimate Middle East job/professional platform; profiles are self-submitted CVs, so employment claims are user-stated and should be corroborated.
missingPersonsRelevance: high
coverage:
- ae
- sa
auth: account
api: false
localInstall: false
registration: true
aliases:
- Bayt
- bayt.com
tags:
- linkedin
- LinkedIn & Similar Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# bayt.com

> The Middle East's leading job site and professional network — a LinkedIn-style source for a Gulf/MENA subject's CV, work history, and skills.

## When to use
Your subject is (or was) a jobseeker or professional in the Gulf/MENA region and you want their career footprint: employment history, employers (`employer-org`), education, skills, and location. When LinkedIn is thin for a Middle East subject, Bayt often holds a fuller CV-style profile, making it a key regional pivot for identity and employment verification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a sock-puppet account at https://www.bayt.com/ (a regional persona/email helps).
2. Search by `name` or `username`, optionally filtering by country/industry.
3. Open candidate profiles: read the `name`, current/previous `employer-org`, job titles, dates, education, and skills.
4. Corroborate identity via employer + location + timeline before trusting; CV data is self-reported.
5. Pivot: employers feed company registries and LinkedIn cross-checks; a confirmed name/photo feeds reverse-image and other regional platforms.

## Inputs → Outputs
- **In:** `name` or `username` (ideally + country/industry)
- **Out:** `social-profile` (CV-style), `name`, `employer-org` and job history, education, skills
- **Empty/negative result looks like:** no profile, or a sparse one — many users maintain minimal CVs, and privacy/recruiter-only settings hide detail without a suitable account. Absence is common and not conclusive; self-reported employment can be exaggerated.

## Gotchas & OpSec
- Account gate: meaningful access needs a login; recruiter/CV-search features are paid.
- Self-reported CVs — verify employers and dates against company registries and other sources.
- Regional focus (Gulf/MENA); little value outside that region.

## Overlaps ("do both")
- Pairs with `[[linkedin]]` and regional company registries (`[[traderegistry-ae]]`, `[[gov-hk]]`) — Bayt fills LinkedIn's MENA gaps, while registries confirm the employers a self-reported CV claims.

## Trust & verifiability
`trust: community` — a legitimate major platform, but profiles are user-submitted CVs; treat employment/education claims as leads to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bayt-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
