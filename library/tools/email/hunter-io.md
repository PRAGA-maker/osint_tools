---
id: hunter-io
name: hunter.io
description: Use when you have a company domain and want all known work emails for that org plus its email-address pattern (Hunter.io Domain Search).
url: https://hunter.io/domain-search
category: email
path:
- email
bestFor: Listing known business emails and the address pattern for a given domain.
selectorsIn:
- domain
- employer-org
selectorsOut:
- email
- name
- employer-org
status: live
pricing: freemium
costNote: Free tier (after signup) returns limited Domain Search results per month; full results and API are paid.
opsec: passive
opsecNote: Queries Hunter's index of publicly-found emails; does not contact anyone at the domain.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: This is the Domain-Search page of Hunter.io — the same well-established service as the `hunter` entry; deduplicate against `[[hunter]]`.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Hunter Domain Search
tags:
- email
- Email Related Sites
relatedTools:
- hunter
- holehe
source: uk-osint
lastVerified: ''
enrichment: full
---

# hunter.io

> The Domain Search view of Hunter.io: enter a company `domain` and get the org's known emails plus its address pattern (e.g. first.last@). Same service as `[[hunter]]`.

## When to use
You have a company `domain` or `employer-org` linked to a missing person or associate and want the full set of known work emails and the pattern, so you can derive a specific person's address even if it isn't listed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://hunter.io/domain-search (sign in to the free tier).
2. Enter the `domain`.
3. Read the result: list of discovered emails (with role/name where known) and the dominant pattern.
4. Combine the pattern with a known `name` to construct the target's likely email, then verify it.
5. Pivot a confirmed email into `[[holehe]]` and breach tools.

## Inputs → Outputs
- **In:** `domain`, `employer-org`
- **Out:** list of `email`s + associated `name`s, the org email pattern
- **Empty/negative result looks like:** few/no emails and no clear pattern — common for small orgs with little public footprint.

## Gotchas & OpSec
- Duplicate of the `[[hunter]]` skill (this is just its Domain-Search URL); consolidate when navigating.
- Business emails only; weak for purely personal/webmail targets.
- Human-in-the-loop: account required; monthly rate limits on the free tier.

## Overlaps ("do both")
- Same product as `[[hunter]]` (Email Finder/Verifier). Pair with `[[holehe]]` to map an email to live accounts.

## Trust & verifiability
`trust: trusted` — Hunter.io is a mature service with cited sources per result; treat this entry as the Domain Search facet of the same tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hunter-io |
| category | email |
| selectorsIn → selectorsOut | domain, employer-org → email, name, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, rate-limit) |
