---
id: rapusia
name: Rapusia
description: Use when you want an alternative, non-tracking general web search that may surface results your primary engine ranks differently — returns web `social-profile` / `domain` links.
url: https://rapusia.org
category: search-engines
path:
- search-engines
bestFor: A privacy-oriented alternate general search engine to diversify result sets away from Google's ranking.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free ad-supported search; the operator donates a share of ad revenue to charity. No account, no payment.
opsec: passive
opsecNote: Rapusia states it does not track users or share data with advertisers and encrypts browser-to-server traffic — reasonable for querying selectors, but as with any third-party engine, run it from a sock-puppet browser and assume your query could be logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legitimate small charity-search project, but a thin front over upstream index(es); result completeness and its no-tracking claims are not independently audited.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- rapusia.org
tags:
- toddington
- curated-directory
- search-engines
- privacy
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Rapusia

> A privacy-marketed general web search engine — worth a pass as a *diversifying* alternate engine, not as a specialist OSINT tool.

## When to use
You have already run a `name`, `username`, or `email` through your primary engines and want a different ranking/index to catch links they buried or omitted. Rapusia is a general-purpose, non-tracking web search; its OSINT value is simply "another engine that ranks results differently," so use it to broaden coverage, not for any unique dataset.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://rapusia.org.
2. Enter your selector — a `name`, `"quoted exact phrase"`, `username`, or `email` — and search as you would on any engine.
3. Skim results for links your primary engine did not surface (forum posts, profiles, cached pages).
4. Pivot: feed any new `social-profile` or `domain` hit into the appropriate specialist tool.

## Inputs → Outputs
- **In:** `name` / `username` / `email` (free-text query)
- **Out:** ranked web links → `social-profile`, `domain`
- **Empty/negative result looks like:** thin or generic results, or the same links your primary engine already returned — treat that as "no added value this run," not as confirmation nothing exists.

## Gotchas & OpSec
- It is a **general** engine, not a people-search — expect no structured PII, just web links.
- Result completeness depends on its upstream index and may lag mainstream engines; never treat an empty Rapusia result as authoritative.
- The privacy/no-tracking claims are the operator's own; use a sock-puppet browser regardless.

## Overlaps ("do both")
- Use alongside your primary search engine and other privacy engines — the point is index diversity, so run the same query across several and compare.

## Trust & verifiability
`trust: unverified` — a legitimate charity-funded project, but a thin, unaudited front over an upstream index; corroborate anything it surfaces against a first-party source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rapusia |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
