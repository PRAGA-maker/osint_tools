---
id: raven
name: raven
description: Use when you have an employer/organisation (`employer-org`) and want to enumerate its LinkedIn employees and guess their work emails — returns names and generated emails. Unmaintained.
url: https://github.com/0x09AL/raven
category: social-networks
path:
- social-networks
- linkedin
bestFor: Enumerating an organisation's employees from LinkedIn (via Google) and generating likely work-email formats, with optional breach checks.
selectorsIn:
- employer-org
selectorsOut:
- name
- email
status: degraded
pricing: free
costNote: Free and open-source (Python), but the README states it is no longer maintained; expect breakage against current LinkedIn/Google.
opsec: active
opsecNote: Raven drives Google searches for LinkedIn profiles and can query breach data using credentials you configure; automated LinkedIn-adjacent scraping is easily rate-limited or flagged. Use a sock-puppet LinkedIn account and a VPN, and expect Google to CAPTCHA automated queries.
humanInLoop: true
humanInLoopReason:
- account-login
- captcha
bestInteractionPattern: cli
trust: unverified
trustNote: Community pentest tool by 0x09AL, explicitly marked "currently not being maintained"; usefulness today is limited by LinkedIn/Google anti-automation changes.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- raven linkedin
- 0x09AL/raven
tags:
- linkedin
- employee-enumeration
- email-generation
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# raven

> A LinkedIn organisation-mapping tool: give it a company and it enumerates employees via Google-indexed LinkedIn profiles and generates their likely work emails — though it is no longer maintained.

## When to use
You have an `employer-org` and want a roster of its people plus probable work-email addresses — useful for placing a subject at an organisation, finding colleagues (`associate` leads via `name`s), or deriving an email to run through email OSINT. Because it's unmaintained and LinkedIn/Google have tightened anti-automation, treat it as a legacy option to try when nothing better is at hand, and verify everything it produces.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install dependencies; add a sock-puppet LinkedIn login to `config.conf`.
2. Run against a company: `python raven.py -c "Company Name"` (see `-h`).
3. It searches Google for the company's LinkedIn employees, extracts names, and generates emails in multiple formats (first.last, flast, etc.), optionally checking Have I Been Pwned.
4. Review the employee `name`s and candidate `email`s; validate emails with a separate verifier before trusting them.
5. Pivot: names feed people-search and LinkedIn profile lookups; verified emails feed `[[buster]]`/breach checks.

## Inputs → Outputs
- **In:** `employer-org` (company name)
- **Out:** `name` (employees), `email` (algorithmically generated candidates)
- **Empty/negative result looks like:** few/no results or Google CAPTCHAs — increasingly the default, because the tool is unmaintained and LinkedIn/Google block automated enumeration. Absence here says more about the tooling than the company.

## Gotchas & OpSec
- **Unmaintained + fragile:** expect it to break; have manual Google dorking (`site:linkedin.com/in "Company"`) as a fallback.
- Generated emails are guesses — verify before use; don't treat them as confirmed.
- **Active:** automated LinkedIn/Google queries get flagged; use a puppet and a VPN, and solve CAPTCHAs manually.

## Overlaps ("do both")
- Pairs with manual LinkedIn X-ray dorking and `[[blog-compass-security-com]]` techniques — those are the durable methods; raven just tries to automate them.

## Trust & verifiability
`trust: unverified` — an unmaintained community tool; treat both the employee list and the generated emails as leads to confirm via LinkedIn and an email verifier.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | raven |
| category | social-networks |
| selectorsIn → selectorsOut | employer-org → name, email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
