---
id: follower-wonk-compare
name: Followerwonk Compare
description: Use when you have two or three Twitter/X `username`s and want their shared audience — returns followers-in-common and overlap analysis to prove a connection between accounts.
url: https://followerwonk.com/compare/
category: social-networks
path:
- social-networks
bestFor: Comparing 2–3 Twitter/X accounts to reveal followers in common and audience overlap, plus Twitter bio search.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: degraded
pricing: freemium
costNote: Free tier (sign-up) covers basic compare/bio search; deeper analytics and full follower exports are paid. Now delivered via Fedica after Followerwonk's Moz-era rebrand.
opsec: passive
opsecNote: Passive to the targets — comparing public accounts does not notify them. You must create an account (and connect an X login for some features), so use a sock-puppet account, never your real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: An established Twitter-analytics service (formerly Moz's Followerwonk, now under Fedica); reliability of follower data now depends on X API access, which has tightened, so treat results as indicative.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- followerwonk
- search-twitter-bios-and-profiles
- followerwonk-tools-for-twitter-analytics-bio-search-and-more
aliases:
- Followerwonk
- Followerwonk Compare
tags:
- Social Media
- Twitter
- audience-overlap
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Followerwonk Compare

> A Twitter/X audience-overlap tool — feed it two or three handles and it shows the followers they share, a concrete way to establish that separate accounts belong to the same circle (or person).

## When to use
You have two or three Twitter/X `username`s and want to know how connected they are — do a suspected sock-puppet and a real account share an unusually large follower overlap? Which followers do a subject and their associate have in common? Overlap analysis is a strong link-analysis signal for tying accounts to a shared community or operator. Also useful for its bio search (finding accounts by keywords in their profile).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://followerwonk.com/compare/ (now served through the Fedica dashboard) and sign in with a sock-puppet account.
2. Enter 2–3 Twitter/X handles to compare.
3. Read the overlap: total followers in common, the shared-follower list, and audience/demographic breakdowns.
4. For discovery instead, use the bio-search feature to find accounts whose profiles mention a keyword, location, or employer.
5. Pivot: a large shared-follower set corroborates a connection between accounts; individual shared followers feed further `[[followerwonk]]` or username OSINT.

## Inputs → Outputs
- **In:** 2–3 `username`s (Twitter/X handles)
- **Out:** followers-in-common count and list, overlap/audience analysis — evidence linking `social-profile`s
- **Empty/negative result looks like:** near-zero overlap suggests the accounts don't share an audience (weak or no connection); an error/empty pull may mean X API limits blocked the data rather than a true zero.

## Gotchas & OpSec
- **Account required:** you must register (and connect an X login for some features) — always use a sock puppet; never attach your real identity to investigative queries.
- **API-dependent and degraded:** since X restricted its API, follower data can be incomplete or delayed; treat overlap figures as indicative, not exhaustive.
- Only covers Twitter/X — no other network.

## Overlaps ("do both")
- Pairs with `[[followerwonk]]` (single-account analytics and bio search) and `[[search-twitter-bios-and-profiles]]` — Compare proves overlap between known handles, while those discover new handles to compare.

## Trust & verifiability
`trust: community` — a well-known analytics service, but its accuracy now hinges on constrained X API access; verify a decisive overlap claim against the raw follower lists where you can.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | follower-wonk-compare |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
