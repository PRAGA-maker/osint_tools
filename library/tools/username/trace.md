---
id: trace
name: Trace (Trace OSINT)
description: Use when you have a `username`, `email`, or `phone` and want a one-page sweep across 600+ sites plus breach and phone checks — returns social-profile links, breach hits, and phone metadata.
url: https://trace.manus.space
category: username
path:
- username
bestFor: Fast, free browser sweep of a username across 600+ platforms with added email-breach and phone lookups.
selectorsIn:
- username
- email
- phone
selectorsOut:
- social-profile
- email
- geolocation
status: live
pricing: free
costNote: Free web tool; no login required. Breach checks are powered by XposedOrNot and BreachDirectory (no API key needed).
opsec: passive
opsecNote: Username enumeration runs server-side from Trace's infrastructure, so your IP does not hit each target site directly. But you disclose the target selectors to a third-party (Manus-hosted) app that may log queries. Avoid for the most sensitive subjects.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Hosted on manus.space (an AI-app platform), so it may be ephemeral and its result quality is unaudited; treat hits as leads. Aggregates public checkers rather than proprietary data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-web
- sherlock
- holehe
aliases:
- Trace OSINT
- trace.manus.space
tags:
- username-check
- breach-search
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Trace (Trace OSINT)

> A free, browser-based OSINT dashboard that streams a username across 600+ sites and bolts on email-breach and phone-number lookups plus an AI risk score.

## When to use
You have a `username` (or `email`/`phone`) and want a fast, no-install first pass: which of 600+ platforms the handle exists on, whether an email appears in breaches, and basic phone metadata (carrier, line type, region). Good as an opening sweep before committing to slower CLI tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://trace.manus.space in a clean browser.
2. Enter the `username` to run the 600+ platform scan (results stream in as each site responds), or paste an `email`/`phone`/profile URL for the other modules.
3. Read results: confirmed profile URLs, breach hits (via XposedOrNot/BreachDirectory), phone carrier/line-type/region, and the AI risk score.
4. Verify each profile hit manually — automated checkers false-positive on parked/lookalike accounts.
5. Pivot: confirmed handles feed per-site lookups; breach hits feed `[[holehe]]`; phone data feeds phone OSINT.

## Inputs → Outputs
- **In:** `username`, `email`, or `phone`
- **Out:** `social-profile` (platform hits), `email` (breach associations), `geolocation` (phone region)
- **Empty/negative result looks like:** few or no hits — often means a rare handle, or that sites rate-limited the scan. Re-run and cross-check with a second enumerator before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: none; fully web-based.
- OpSec: **passive** toward targets (checks run server-side), but you trust a third-party AI-hosted app with your selectors.
- Reliability: manus.space apps can disappear or change; don't build a workflow that depends solely on it.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-web]]` and `[[sherlock]]` — established enumerators; run one to validate Trace's platform hits.
- Pairs with `[[holehe]]` — silent email-registration checks to complement Trace's breach-oriented email module.

## Trust & verifiability
`trust: unverified` — a convenient aggregator of public checkers on an ephemeral host; treat every hit as a lead to confirm on the source platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trace |
| category | username |
| selectorsIn → selectorsOut | username, email, phone → social-profile, email, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
