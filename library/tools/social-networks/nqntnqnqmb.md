---
id: nqntnqnqmb
name: nqntnqnqmb
description: Use when you have a `name` or `employer-org` and want to enumerate LinkedIn profiles, company employees, and their contact details programmatically — returns `social-profile`, `associate`, `email`, and `phone`.
url: https://pypi.org/project/nqntnqnqmb/
category: social-networks
path:
- social-networks
bestFor: Scripted LinkedIn extraction — all employees of a company, full profile info, and contact details (email/phone) — using your own session cookies.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- associate
- email
- phone
- name
status: live
pricing: free
costNote: Free open-source Python tool (megadose/nqntnqnqmb). No paid tier; the "cost" is that it needs a working LinkedIn account's session cookies to function.
opsec: active
opsecNote: This drives LinkedIn's private endpoints using YOUR li_at / JSESSIONID cookies, so all activity is attributable to that account and violates LinkedIn's ToS — expect scraping detection, rate-limiting, and possible account ban. Use a dedicated sock-puppet LinkedIn account (never a real/attributable one), route through a clean IP, and pace requests. Extracting employees also touches the target company's profiles, which can leave viewer/PYMK traces.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: python-lib
trust: community
trustNote: Open-source tool by a known OSINT author (megadose, also maintains holehe/toutatis). Community-trusted for what it does, but it relies on unofficial LinkedIn internals that break when LinkedIn changes.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
aliases:
- megadose nqntnqnqmb
- linkedin-osint
tags:
- linkedin
- employee-enumeration
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# nqntnqnqmb

> A Python LinkedIn OSINT tool that scripts profile lookups, company-employee enumeration, and contact extraction — using your own logged-in session cookies to reach data the web UI rations out.

## When to use
You have a `name` or `employer-org` and need to go beyond a single profile: enumerate every employee of a company, pull full profile details, or extract contact info (email/phone) at scale. Ideal when mapping a subject's professional network (`associate` links) or building a candidate list of people around a target organization.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install nqntnqnqmb` (PyPI), or `git clone https://github.com/megadose/nqntnqnqmb && cd nqntnqnqmb && python3 setup.py install` (Python 3.6+).
2. Provide auth: log into a **sock-puppet** LinkedIn account in a browser, copy the `li_at` and `JSESSIONID` cookies into `config.json` (arrays of cookie sets enable account rotation).
3. Run a mode:
   - `getProfileInformations` — full info on a profile.
   - `getEmployees` / `getAllEmployees` — all employees from a company LinkedIn URL.
   - `searchCompany` / `getCompanyFromName` — resolve a company from its name.
   - `searchProfile` / `getProfileFromName` — find a profile from a name.
   - `getContactInformations` — extract email/phone exposed on profiles.
4. Read output: structured profile/company data with `social-profile` URLs, co-workers (`associate`), and any `email`/`phone`.
5. Pivot: employee lists feed email-pattern guessing and username checks; a phone/email feeds phone- and email-OSINT tools.

## Inputs → Outputs
- **In:** `name` (person or company) or `employer-org` / company LinkedIn URL
- **Out:** `social-profile` URLs, `associate` (colleagues, employees), `email`, `phone`, confirmed `name`
- **Empty/negative result looks like:** empty JSON / auth errors — usually expired or blocked cookies, a rate-limit trip, or a LinkedIn internal change breaking the tool. Not proof the person/company is absent.

## Gotchas & OpSec
- Requires valid session cookies; they expire and can be invalidated when LinkedIn flags automation. Refresh from a fresh sock-puppet login.
- **Never** use a real account — enumeration is detectable and gets accounts restricted or banned. Pace requests; use rotation.
- Relies on unofficial LinkedIn endpoints — it periodically breaks until updated. Cross-check counts against `[[linkedin-x-ray-search]]`.
- OpSec: **active** and ToS-violating; queries and profile views are attributable to your session.

## Overlaps ("do both")
- Pairs with `[[linkedin-x-ray-search]]` — X-ray finds the right profile passively and safely; nqntnqnqmb then extracts depth and contacts once you've confirmed the target. Use X-ray to verify, this to enrich.

## Trust & verifiability
`trust: community` — well-regarded open-source tooling from a known OSINT author, but it depends on brittle LinkedIn internals and unofficial access. Verify extracted contact details independently (e.g. email-existence checks) before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nqntnqnqmb |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile, associate, email, phone, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |
