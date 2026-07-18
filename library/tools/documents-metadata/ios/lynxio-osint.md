---
id: lynxio-osint
name: Lynxio OSINT
description: Use when you have an `email`, `username`, `phone`, `ip-address`, or `domain` and want an aggregated multi-source lookup — returns linked accounts, breach hits, and a risk report.
url: https://lynxio.io/
category: documents-metadata
path:
- documents-metadata
- ios
bestFor: One-tap aggregated reconnaissance across many OSINT modules for a single identifier, with an AI-summarised report.
selectorsIn:
- email
- username
- phone
selectorsOut:
- social-profile
- password
status: live
pricing: freemium
costNote: Lite tier free (5 searches/day, no card); Standard €2.99/mo (12/day) and Premium €5.99/mo (30/day, unlimited history).
opsec: passive
opsecNote: Lynxio queries third-party sources and breach datasets on its servers — the target is not contacted, so it's passive to them. But you submit the selector to a commercial platform behind a login; assume they log queries. Use a dedicated account and don't feed it selectors you must keep siloed.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: mobile-app
trust: community
trustNote: A commercial aggregator orchestrating 10+ modules; results are only as good as the upstream sources it queries, and aggregated breach data can be stale or false-positive.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
aliases:
- LynxIO
- lynxio.app
tags:
- osint-aggregator
- breach-check
- multi-identifier
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Lynxio OSINT

> A mobile-first OSINT aggregator: feed it one identifier and it runs 10+ modules (email/username/phone/IP/domain + breach data) and returns an AI-summarised report.

## When to use
You have a single strong selector — an `email`, `username`, or `phone` (also `ip-address`/`domain`) — and want a fast, broad first sweep before you go deep with specialised tools. Good as an early-stage triage: it checks the identifier against thousands of platforms and tens of millions of breach entries and hands back linked accounts, exposure, and a risk score in seconds. Treat its output as leads to verify, not conclusions.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install the Lynxio iOS app (web at lynxio.app; Android reportedly coming) and create an account — the free Lite tier needs no card.
2. Enter the selector (`email`, `username`, `phone`, `ip-address`, or `domain`).
3. Let the modules run; read the structured report: matched platforms/`social-profile`s, breach/`password`-exposure hits, exposure timeline, and risk score.
4. Mind the free-tier cap (5 searches/day) — batch your priorities.
5. Pivot: each linked account and breach hit is a new lead — verify it directly at the source before relying on it.

## Inputs → Outputs
- **In:** `email`, `username`, or `phone` (also IP/domain)
- **Out:** linked `social-profile`s, breach/`password` exposure, risk report
- **Empty/negative result looks like:** few or no modules return hits — meaning the identifier is thin across Lynxio's sources, not proof of a clean footprint (aggregators miss plenty).

## Gotchas & OpSec
- Human-in-the-loop: requires an account (login) and enforces a daily search cap on the free tier.
- Aggregated results can be **stale or false-positive** — especially breach matches and "linked account" guesses; always confirm at the primary source.
- OpSec: passive to the target, but you disclose the selector to a commercial third party — use a dedicated account for sensitive work.

## Overlaps ("do both")
- Pairs with dedicated single-purpose tools: use Lynxio to *find* candidate accounts/breaches fast, then confirm each with a first-party check (e.g. an account-existence oracle) rather than trusting the aggregate.

## Trust & verifiability
`trust: community` — a commercial aggregator, not a primary source. Its breadth is the value; its reliability depends on upstream data quality, so every hit needs independent verification before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lynxio-osint |
