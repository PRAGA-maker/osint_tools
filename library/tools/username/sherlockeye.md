---
id: sherlockeye
name: SherlockEye
description: Use when you have a `username`, `email`, `phone`, `name`, `domain` or `ip-address` and want an aggregated reverse-lookup across 800+ sources — returns `social-profile`, `associate`, breach and identity links.
url: https://sherlockeye.io/
category: username
path:
- username
bestFor: One-dashboard reverse lookup of a selector across 800+ open sources, linking aliases to a single identity.
selectorsIn:
- username
- email
- phone
- name
selectorsOut:
- social-profile
- associate
- email
status: live
pricing: freemium
costNote: Freemium — free tier on sign-up; paid credit plans (Essential $16/mo up to Enterprise) unlock volume and advanced features. Results are credit-metered.
opsec: passive
opsecNote: Queries are run server-side across aggregated sources, so your IP isn't hitting each target site — but you register an account and the platform logs your searches. Use a dedicated investigative account; don't enter case-sensitive selectors you wouldn't want a third party to hold.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial AI-OSINT aggregator; breadth is real but results are machine-correlated across sources of varying quality, so confirm before relying.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- SherlockEye.io
tags:
- username-check
- reverse-lookup
- aggregator
- digital-footprint
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# SherlockEye

> An AI-driven OSINT aggregator: feed it one selector (username, email, phone, name, domain, IP) and it reverse-looks-up across 800+ open sources, correlating aliases into a single identity dashboard.

## When to use
You have a single strong selector and want a fast, broad enrichment pass that links it to social profiles, other accounts, associated identifiers and breach mentions — the kind of cross-source correlation that's tedious to do by hand. Good for turning one handle/email into a map of a subject's footprint early in a case, then verifying the strongest links manually.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at https://sherlockeye.io/ (free tier) with an investigative account.
2. Enter the selector — `username`, `email`, `phone`, `name`, `domain`, or `ip-address`.
3. Run the search (credit-metered); read the dashboard: linked accounts, aliases, associated identifiers, source references.
4. Export (PDF/CSV/JSON/etc.) for the case file, and note which findings cite a source you can independently confirm.
5. Pivot: verify high-value links directly on the source platform; feed newly found handles/emails back in or into [[user-scanner]]/[[namint]].

## Inputs → Outputs
- **In:** `username`, `email`, `phone`, `name` (also domain, IP)
- **Out:** `social-profile` links, `associate`/alias correlations, related `email`/identifiers, breach mentions
- **Empty/negative result looks like:** thin dashboard or only low-confidence guesses — the selector has little public footprint, or the correlations are weak; treat unsourced links as hypotheses, not facts.

## Gotchas & OpSec
- Results are **machine-correlated** across sources of mixed quality — false links happen; verify before asserting.
- Credit-metered: the free tier is limited; deep work needs a paid plan.
- Your searches are logged by the platform — use a dedicated account and avoid the most sensitive selectors.

## Overlaps ("do both")
- Pairs with [[user-scanner]] (open-source enumeration) and [[namint]] — the aggregator casts wide across paid/aggregated sources; the free tools give inspectable, corroborating hits.

## Trust & verifiability
`trust: community` — a commercial aggregator with genuine breadth but automated correlation; use it to generate leads and always confirm the important ones on the underlying source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sherlockeye |
| category | username |
| selectorsIn → selectorsOut | username, email, phone, name → social-profile, associate, email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
