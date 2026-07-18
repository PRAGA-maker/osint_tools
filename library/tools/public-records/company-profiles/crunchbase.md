---
id: crunchbase
name: Crunchbase
description: Use when you have a company or person name and want funding history, investors, acquisitions, and named executives — returns employer-org, associates, and social profiles.
url: https://www.crunchbase.com/
category: public-records
path:
- public-records
- company-profiles
bestFor: Mapping a startup's funding, investors, and leadership team, and tying a person to the companies and boards they are involved with.
input: Company name, person name, or investor name
output: Funding history, investors, acquisitions, team profiles, and news
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- social-profile
status: live
pricing: freemium
costNote: Free registered account gives limited profile views and search; full financial/contact data and advanced search require a paid Pro/Enterprise plan or the free trial.
opsec: passive
opsecNote: Queries run on Crunchbase servers behind a login, so your account (email/IP) is tied to what you view; profiles you visit may surface in your activity. Targets are not notified. Use a dedicated research account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-known, widely cited private-market database; data is community- and company-submitted plus editorial, so individual fields can be stale or self-reported.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- crunchbase.com
tags:
- public-records
- company-profiles
- funding
- business-intelligence
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Crunchbase

> The best-known database of private companies, funding rounds, investors, and founders — a fast way to connect a person to the startups and boards they sit on.

## When to use
You have a person `name` or an `employer-org` and want to establish their business footprint: which companies they founded, funded, advise, or lead. Crunchbase links people to organizations and to each other (co-founders, investors, board members), so it turns a lone name into an `employer-org` and a web of `associate` connections, often with links to a LinkedIn or Twitter/X `social-profile`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in at https://www.crunchbase.com/ with a dedicated research account (registration is required to see meaningful results).
2. Search the person or company name. On a person profile, read current and past roles, board seats, and investments; on a company, read the founders/team, funding rounds, and investors.
3. Note the named humans around the entity — co-founders, executives, and lead investors are pivotable `associate` leads.
4. Pivot: follow a profile's linked LinkedIn/Twitter for a `social-profile`; use a company's HQ/registration for jurisdiction, then corroborate leadership names against a companies-registry tool. Hit a paywall on a field? Record what's visible and move on.

## Inputs → Outputs
- **In:** `name` (person) or `employer-org` (company/investor)
- **Out:** `employer-org` (roles, boards), `associate` (co-founders, execs, investors), `social-profile` (linked LinkedIn/Twitter)
- **Empty/negative result looks like:** no profile, or a bare stub with no funding/team data — common for very small, non-VC-backed, or non-US/EU businesses that Crunchbase under-covers.

## Gotchas & OpSec
- Human-in-the-loop: an account login is required, and much of the deep data (contacts, full financials, advanced filters) sits behind a paid tier — expect partial results on the free plan.
- OpSec: passive but authenticated — your account and IP are logged against your searches; use a sock-puppet research account, never a personal login. Targets are not alerted.
- Data is largely self-/community-submitted: titles, dates, and amounts can be stale or aspirational. Corroborate before relying on a figure.

## Overlaps ("do both")
- Pairs with official company registries (e.g. Companies House / OpenCorporates-style tools) — Crunchbase is richer on funding, people, and narrative, while a registry gives you legally-filed directors and addresses that Crunchbase omits.

## Trust & verifiability
`trust: trusted` — Crunchbase is an established, widely relied-upon source, but because much of its data is submitted rather than filed, treat individual fields as leads to verify, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crunchbase |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, social-profile |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
