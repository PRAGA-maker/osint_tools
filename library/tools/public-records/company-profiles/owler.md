---
id: owler
name: Owler
description: Use when you have an `employer-org` and want company profile, leadership and competitor context — returns employer-org, associate and domain.
url: https://www.owler.com/corp
category: public-records
path:
- public-records
- company-profiles
bestFor: Quick company profiles — HQ, size, leadership, competitors and news — to contextualise a subject's employer.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
- domain
status: live
pricing: freemium
costNote: Free profiles are viewable with a free account (registration/login); deeper competitive-intel features are paid.
opsec: passive
opsecNote: Viewing public company profiles is passive. Registration ties access to an account — use a sock-puppet email; crowd-sourced fields can be inaccurate, so don't act on a single unverified detail.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A crowd-sourced competitive-intelligence platform; profiles blend public data and community estimates, so figures (revenue, headcount) are approximate.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- Owler
- owler.com
tags:
- company-research
- competitive-intelligence
- business
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Owler

> A crowd-sourced company-profile service — a fast way to size up a subject's employer: what it does, who runs it, its rivals, and recent news.

## When to use
You have an `employer-org` (from a resume, a donation record, a bio) and want quick context: headquarters, approximate size/revenue, industry, named leadership, competitors, and recent company news. This helps you understand a subject's workplace, spot named executives to pursue as `associate`s, and find the company `domain` for infrastructure work. It profiles **companies**, not individuals — a person search only helps insofar as they are named in leadership.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account (sock-puppet email) at https://www.owler.com/corp.
2. Search the `employer-org` and open its profile.
3. Read HQ/location, industry, leadership names, competitor list, and news feed.
4. Cross-check figures — headcount/revenue are community estimates, not filings.
5. Pivot: leadership names → `associate`/people-search; company `domain` → WHOIS/infrastructure (`[[ipaddress-tools]]`); competitors/news → sector context and adjacent entities.

## Inputs → Outputs
- **In:** `employer-org` (or a `name` only if they are named company leadership)
- **Out:** `employer-org` (profile/HQ/industry), `associate` (named executives), `domain` (company site)
- **Empty/negative result looks like:** no profile, or a thin auto-generated stub with no leadership — meaning the company is too small/private for Owler; use a corporate registry instead.

## Gotchas & OpSec
- Crowd-sourced/estimated data — revenue, headcount, and even leadership can be stale or wrong; corroborate before relying.
- Requires a login even for free profiles — use a sock-puppet account.
- OpSec: passive; the registration is the only footprint.

## Overlaps ("do both")
- Pairs with authoritative corporate registries (`[[rusprofile]]` for Russia, Companies House, etc.) and LinkedIn — Owler gives fast competitor/leadership context, while registries confirm the legal facts and LinkedIn maps the actual people.

## Trust & verifiability
`trust: unverified` — a crowd-sourced platform; useful for orientation and leads, but treat its figures as estimates and confirm company facts against primary filings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | owler |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate, domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
