---
id: legistorm
name: LegiStorm
description: Use when you have a `name` tied to US Congress and want their staff role, salary and financial disclosures — returns employer-org, salary and disclosure records.
url: https://www.legistorm.com/
category: search-engines
path:
- search-engines
bestFor: Profiling US congressional staff and the "revolving door" — salaries, financial/gift disclosures, and moves between the Hill and lobbying.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free tier: browse staff by member/state, financial disclosures, foreign-gift and (older) earmark data. Deeper contact-list building, Congressional Record and lobbying searches require a paid LegiStorm Pro subscription.
opsec: passive
opsecNote: Read-only queries against a public transparency database; the subject is not notified. Use a research browser; some deep features require an account/subscription.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A respected transparency/journalism data service; core figures derive from official disclosures, so the free data is reliable, though the richest tools are paywalled.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- legistorm.com
tags:
- toddington
- curated-directory
- congress
- specialty-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# LegiStorm

> The go-to database on US congressional staff — who works for whom, their salary, their disclosures, and where they went next.

## When to use
Your subject is (or was) a US congressional staffer, member, or Hill-adjacent lobbyist. LegiStorm ties a `name` to their office/employer, salary history, financial and foreign-gift disclosures, and revolving-door moves. Useful to confirm a government employment claim, establish a work timeline, or map a subject's professional network in and around Congress.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.legistorm.com/.
2. Browse the free surface: staff by member/state, financial disclosures, foreign gifts, older earmark data.
3. Search the subject `name`; open their profile for office (`employer-org`), salary history and disclosures.
4. Note that contact-list building, Congressional Record and lobbying-client searches sit behind LegiStorm Pro — stop at the free tier and pivot rather than paying.
5. Pivot: an office/employer and dates feed LinkedIn and lobbying-registration OSINT; disclosed associates/relationships are `associate` leads.

## Inputs → Outputs
- **In:** `name` (US congressional staffer/member/lobbyist)
- **Out:** `employer-org` (office/firm), salary history, financial/gift disclosures, revolving-door moves, `associate` relationships
- **Empty/negative result looks like:** no profile — the person never held a covered Hill/lobbying role, or predates coverage; not proof of no government work generally.

## Gotchas & OpSec
- The most powerful searches are **paywalled** (`payment-wall-partial`); the free tier is browsing/disclosures.
- Scope is US federal Congress — not the executive branch, not state legislatures beyond the paid tier.
- Disclosures are point-in-time filings; a role may have changed since.

## Overlaps ("do both")
- Pairs with lobbying-disclosure (Senate LDA) and USASpending/FEC tools — LegiStorm gives the staff/salary/disclosure view, those give lobbying clients, contracts and donations.

## Trust & verifiability
`trust: community` — a well-regarded transparency service built on official disclosures; the free data is trustworthy, and any figure can be checked against the underlying government filing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | legistorm |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
