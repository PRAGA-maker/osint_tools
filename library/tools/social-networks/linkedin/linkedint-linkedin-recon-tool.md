---
id: linkedint-linkedin-recon-tool
name: LinkedInt - LinkedIn Recon Tool
description: Use when you have an `employer-org` and want to enumerate its LinkedIn employees and guess their corporate emails — returns names, social-profile, and email (DEPRECATED, largely non-functional).
url: https://github.com/vysecurity/LinkedInt
category: social-networks
path:
- social-networks
- linkedin
bestFor: Historical reference — company-to-employee LinkedIn enumeration with email-format guessing (no longer reliably works).
selectorsIn:
- employer-org
selectorsOut:
- name
- social-profile
- email
status: down
pricing: free
costNote: The script itself is free/open-source, but it required a paid email-discovery API key (e.g. Hunter.io) to generate/verify email addresses. Both the LinkedIn scraping and that integration are broken by platform changes.
opsec: active
opsecNote: It automated authenticated LinkedIn scraping, which violates LinkedIn's ToS and reliably triggers detection/bans. Never point it at a real personal or corporate LinkedIn account. Historically it needed valid LinkedIn credentials — a fast way to get an account flagged.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: A well-known but now-deprecated red-team/OSINT script (vysecurity/LinkedInt). Not maintained; LinkedIn's anti-scraping changes broke it years ago. Documented here so it's recognised as obsolete, not as a working recommendation.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
invitationOnly: false
deprecated: true
relatedTools: []
aliases:
- LinkedInt
- vysecurity LinkedInt
tags:
- linkedin
- employee-enumeration
- deprecated
- red-team
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# LinkedInt - LinkedIn Recon Tool

> A historical Python script for enumerating a company's LinkedIn employees and guessing their emails — now deprecated and largely non-functional due to LinkedIn changes.

## When to use
Recognise the name, don't rely on the tool. LinkedInt was built to take an `employer-org`, scrape its LinkedIn employees, and generate likely corporate email addresses (verified via an email API). LinkedIn's authentication and anti-scraping changes broke this approach; today it typically fails or gets the driving account banned. Use a current alternative for employee/email enumeration.

## How to use it (`bestInteractionPattern`: cli)
1. (Historical) Clone vysecurity/LinkedInt, install Python deps, and supply LinkedIn credentials plus a Hunter.io-style API key.
2. Run it against a target company name to scrape employee profiles and build an email list from a chosen format.
3. In practice now: expect authentication failures, empty results, or account flagging. Do not run it against accounts or orgs you care about.
4. Pivot instead: use a maintained employee/email-enumeration tool and manual LinkedIn search from a sock-puppet account.

## Inputs → Outputs
- **In:** `employer-org` (company name / LinkedIn company URL), LinkedIn creds, email-API key
- **Out (historically):** employee `name`s, `social-profile` links, guessed/verified corporate `email` addresses
- **Empty/negative result looks like:** the normal outcome today — login/scrape errors or nothing returned, because the tool no longer matches LinkedIn's site/flow.

## Gotchas & OpSec
- Deprecated: `status: down` — kept for recognition, not recommendation.
- OpSec: **active and risky** — authenticated auto-scraping violates LinkedIn ToS and gets accounts banned; only ever a burner, if at all.
- Needs a paid email API key on top of LinkedIn creds.

## Overlaps ("do both")
- Superseded by maintained approaches: manual LinkedIn search + a current email-format/verification service, or actively-developed people/employee enumerators. Prefer those; treat LinkedInt as historical context.

## Trust & verifiability
`trust: unverified` — an unmaintained third-party red-team script. Documented so an agent recognises it as obsolete; do not depend on it, and expect it not to work against today's LinkedIn.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkedint-linkedin-recon-tool |
| category | social-networks |
| selectorsIn → selectorsOut | employer-org → name, social-profile, email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, api-key) |
