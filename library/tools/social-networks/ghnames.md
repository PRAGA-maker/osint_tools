---
id: ghnames
name: GHNames
description: Use when you have a GitHub `username` and want its history — which accounts have held that handle and their user IDs — returns username/account reuse leads.
url: https://ghnames.com/
category: social-networks
path:
- social-networks
bestFor: Resolving GitHub username history — spotting when a handle was renamed, reused, or held by multiple accounts, via stable numeric user IDs.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free to search; in open-alpha. No account required to query.
opsec: passive
opsecNote: You query a third-party dataset of historical GitHub handles, not GitHub or the subject live; nothing is disclosed to the target. Use a research browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community project (open alpha) built on scraped GitHub username/ID history; useful as a lead source but coverage and freshness are unproven — confirm against GitHub itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ghnames.com
tags:
- github
- username
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# GHNames

> A GitHub username-history lookup: who has held a handle over time, tied to stable numeric user IDs.

## When to use
You have a GitHub `username` and need to untangle its history: has it been renamed, abandoned and re-registered, or held by several accounts? GitHub recycles freed usernames, so a handle you find today may not be the same account that used it before. GHNames maps a handle to the numeric user ID(s) that held it, which is the reliable way to tell "same person" from "same name, different account."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ghnames.com/.
2. Search the GitHub `username` (exact match, case-insensitive).
3. Read the results: the numeric user ID(s) and history for that handle; multiple IDs mean the name has been held by more than one account.
4. Take a numeric user ID to GitHub directly — `https://github.com/` profile lookups and the API resolve an ID to the current account, confirming continuity.
5. Pivot: a confirmed account feeds commit-email/repo OSINT; a renamed handle may reveal an older identity to search.

## Inputs → Outputs
- **In:** GitHub `username`
- **Out:** numeric GitHub user ID(s) and handle history → `username` reuse leads and the resolvable current `social-profile`
- **Empty/negative result looks like:** no history for the handle — it may be unused, too new, or the owner opted out of the dataset (GHNames supports a privacy opt-out), so absence isn't conclusive.

## Gotchas & OpSec
- Open-alpha, scraped data — coverage is partial and users can opt out, so it can miss real history.
- The numeric ID is the trustworthy anchor; verify it against GitHub before concluding "same person."
- Username identity ≠ personal identity; corroborate before attributing.

## Overlaps ("do both")
- Pairs with GitHub commit-email harvesting and username-enumeration tools — GHNames tells you which account really owns a handle over time; those pull the identity behind it.

## Trust & verifiability
`trust: community` — a small community project on scraped data; treat its history as a lead and confirm every claim via GitHub's own ID→account resolution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghnames |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
