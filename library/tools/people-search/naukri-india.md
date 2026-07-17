---
id: naukri-india
name: Naukri (India)
description: Use when you have a `name` for an India-based subject and want employment/CV context — returns `employer-org`, skills and career history from public résumé/profile pages.
url: https://www.naukri.com
category: people-search
path:
- people-search
bestFor: Employment and résumé context for jobseekers in India (roles, skills, employers, location).
selectorsIn:
- name
selectorsOut:
- employer-org
- address
- name
status: live
pricing: freemium
costNote: Jobseeker accounts and job search are free. The résumé database (Resdex) that lets you search 90M+ CVs is a paid recruiter subscription; the free investigative angle is search-engine dorking of public profile pages.
opsec: passive
opsecNote: Google-dorking public naukri.com pages is passive and leaves no trace with the subject. A recruiter/Resdex login ties every résumé search to your account and, on some flows, notifies the jobseeker that a recruiter viewed their profile — avoid the logged-in path for sensitive work.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: India's largest, long-established job portal (Info Edge); the underlying data is self-submitted résumés, so it's genuine but as current/accurate as the jobseeker keeps it.
missingPersonsRelevance: medium
coverage:
- in
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Naukri.com
- naukri
tags:
- job-search-resources
- employment
- india
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Naukri (India)

> India's dominant job portal — a large pool of self-submitted résumés you can mine (via public pages, or paid Resdex) for a subject's employer, skills and career history.

## When to use
Your subject is based in India (or worked there) and you want employment context: current/past `employer-org`, job titles, skills, and often a city/`address`. Naukri holds tens of millions of jobseeker résumés. Because the full résumé search sits behind a paid recruiter product, the practical free technique is to surface public profile/résumé-display pages through a search engine and read what's indexed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Free angle — dork the public pages: search engines with `site:naukri.com "Full Name"`, or `site:naukri.com <name> <city|company>` to find indexed profile/résumé-display URLs.
2. Read the page for employer, designation, experience, key skills and location.
3. Cross-check the same person on LinkedIn and other people-search tools — Naukri data is self-reported and may be older than their current role.
4. Paid angle (human-in-the-loop): a recruiter Resdex subscription lets you keyword-search the résumé database directly by name/skill/company/location. Treat this as a budgeted, account-logged step, not a casual query, and note it may alert the jobseeker.
5. Pivot: employer + title feeds corporate/LinkedIn OSINT; a city feeds address/location work.

## Inputs → Outputs
- **In:** `name` (optionally + company/city to disambiguate)
- **Out:** `employer-org`, job title, skills, experience, city/`address`
- **Empty/negative result looks like:** no indexed public page and no Resdex hit — common, since most résumés aren't publicly indexed. Absence here does **not** mean the person has no Naukri profile; it may simply be private/behind the paywall.

## Gotchas & OpSec
- Coverage is India-centric; near-useless for subjects with no Indian employment footprint.
- Data is self-submitted and often stale — verify current employer independently.
- Common Indian names produce heavy collisions; always disambiguate with a second selector (company, city, skill).
- Stay on the public/dork path for OpSec; the logged-in recruiter path is attributable and can notify the target.

## Overlaps ("do both")
- Pairs with LinkedIn and general people-search tools — Naukri fills in the Indian employment/skills layer they may miss, while they provide the identity anchor to disambiguate common names.

## Trust & verifiability
`trust: trusted` — Naukri is India's largest and longest-running job platform (operated by Info Edge). The résumé data is authentic first-party self-submission; its only weakness is currency, so date-check any employer/title before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | naukri-india |
| category | people-search |
| selectorsIn → selectorsOut | name → employer-org, address, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
