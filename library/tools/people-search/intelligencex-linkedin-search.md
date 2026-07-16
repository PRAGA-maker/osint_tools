---
id: intelligencex-linkedin-search
name: IntelligenceX LinkedIn Search
description: Use when you have a `name` (plus optional employer/location) and want to build a precise LinkedIn people search — returns social-profile, employer-org.
url: https://intelx.io/tools?tab=linkedin
category: people-search
path:
- people-search
bestFor: Turning partial identity fields (name + employer/title/location) into a targeted LinkedIn profile search without guessing search syntax.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: The IntelX web tool itself is free (no IntelX account needed). It hands the query off to LinkedIn, where you must be logged in to see results.
opsec: active
opsecNote: The final search runs on LinkedIn while you are logged in, so viewing a target's profile can trigger LinkedIn's "who viewed your profile" and connection suggestions. Use a sock-puppet LinkedIn account in private/anonymous browsing mode; do not run this from your real professional account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Intelligence X is an established OSINT provider; this tool is a query-builder that redirects to LinkedIn/Google — it stores nothing and simply constructs the search.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- intelligence-x
- intelligence-x-person-tools
- facebook-graph-searcher-intelligencex
aliases:
- IntelligenceX LinkedIn
- IntelX LinkedIn search
tags:
- linkedin
- intelx
- people-search
source: osintambition-social
lastVerified: '2026-07-16'
enrichment: full
---

# IntelligenceX LinkedIn Search

> A free query-builder on intelx.io that assembles a precise LinkedIn people search from the identity fields you have, then launches it against LinkedIn.

## When to use
You have a `name` plus one or more weak signals — an `employer-org`, job title, or location — and you want to find the subject's LinkedIn profile without hand-crafting boolean/`site:linkedin.com` queries. The tool takes your fields, builds the search string, and sends it to LinkedIn (or Google Custom Search), returning `social-profile` links and the `employer-org`/title context that confirms identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock-puppet** LinkedIn account in a private browser session first (results require being logged in).
2. Go to https://intelx.io/tools?tab=linkedin and fill the available fields: name, company, title, location, etc.
3. Submit — the tool constructs and launches the search on LinkedIn/Google CSE.
4. Review candidate profiles; use the employer/title/location to disambiguate people with the same name.
5. Pivot: a confirmed profile URL feeds username/email enrichment and cross-network correlation; the employer feeds company-directory lookups.

## Inputs → Outputs
- **In:** `name`, plus optional `employer-org`, title, or location
- **Out:** LinkedIn `social-profile` candidate links and the `employer-org`/title shown on them
- **Empty/negative result looks like:** LinkedIn returns no/low-confidence matches — the person may not be on LinkedIn, uses a different name, or their profile is out of your network's visibility. Not being logged in also yields empty/blocked results.

## Gotchas & OpSec
- Human-in-the-loop: you must be **logged into LinkedIn** (`account-login`) for the handoff to work.
- OpSec: **active** — the search executes as your LinkedIn session; profile views can notify the target and seed "people you may know." Always use a maintained sock-puppet, never your real account.
- IntelX periodically changes which filters are available (it has shifted some searches to Google Custom Search); expect the field set to vary.

## Overlaps ("do both")
- Do both with `[[intelligence-x]]` and `[[intelligence-x-person-tools]]` — the same suite's other builders (Facebook, username, email) let you correlate the LinkedIn hit across networks.

## Trust & verifiability
`trust: trusted` — a thin, reputable query-builder that stores nothing; the trust in any *result* is really trust in LinkedIn's own data, so confirm identity from the profile's details rather than the match alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelligencex-linkedin-search |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
