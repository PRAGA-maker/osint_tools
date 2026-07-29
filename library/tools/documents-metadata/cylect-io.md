---
id: cylect-io
name: Cylect.io
description: Use when you have a `name`, `email`, `username`, or `phone` and want a one-stop AI-assisted search across many OSINT sources — returns aggregated matches to triage.
url: https://cylect.io
category: documents-metadata
path:
- documents-metadata
bestFor: A single AI-driven interface that fans a selector out across multiple OSINT databases and consolidates the hits.
selectorsIn:
- name
- email
- username
- phone
selectorsOut:
- social-profile
- email
- phone
- address
status: live
pricing: freemium
costNote: Freemium — a limited number of free searches, with paid plans for higher volume and full result access. Account required.
opsec: active
opsecNote: You submit the subject's selector to a third-party aggregator, which queries many sources on your behalf; the query and your account activity are logged by Cylect and the downstream providers. Use a dedicated investigative account, not a personal one, and avoid submitting selectors you must keep confidential.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial AI OSINT aggregator; convenient but a black box — it does not always show which source produced a hit, and result quality/coverage cannot be independently audited. Treat outputs as leads to verify at the primary source.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- osint-industries
- epieos
- maltego
aliases:
- cylect
- cylect.io
tags:
- aggregator
- ai-osint
- people-search
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Cylect.io

> An AI-assisted OSINT aggregator — feed it one selector and it searches many databases at once, then surfaces consolidated matches through a single interface.

## When to use
Early, broad-net stage of a person-focused investigation: you have a `name`, `email`, `username`, or `phone` and want a fast, wide sweep across many sources without querying each individually. Good for quickly seeing where a selector shows up and generating leads; not a substitute for confirming each hit at its authoritative source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create an account at https://cylect.io (free tier has limited searches).
2. Enter the selector — `name`, `email`, `username`, or `phone`.
3. Review the aggregated results: linked `social-profile`s, related `email`/`phone`, possible `address`, and cross-source matches.
4. For each promising hit, go to the underlying/primary source to confirm — aggregators mix strong and weak matches.
5. Pivot: confirmed selectors feed dedicated tools (email → `[[epieos]]`, entity mapping → `[[maltego]]`).

## Inputs → Outputs
- **In:** `name` / `email` / `username` / `phone`
- **Out:** aggregated `social-profile`s, `email`s, `phone`s, possible `address`es across sources
- **Empty/negative result looks like:** few or no matches — the selector is sparse online, or the free tier limited the sources queried; try an alternative selector or a specialised tool.

## Gotchas & OpSec
- **Black-box aggregation:** it may not attribute each result to a source, so you can't gauge reliability from the UI. Always verify at the primary source before acting.
- Freemium limits both the number of searches and the depth of results on the free tier.
- Submitting a selector discloses your interest to a third party — use an investigative account and avoid confidential selectors.

## Overlaps ("do both")
- Overlaps with other aggregators like `[[osint-industries]]` and `[[epieos]]` — different aggregators cover different sources, so running the same selector through two or three catches what any one misses. Use `[[maltego]]` to structure and cross-link the combined results.

## Trust & verifiability
`trust: unverified` — a convenient commercial aggregator whose sourcing and coverage can't be independently audited. Every hit is a lead to confirm at the authoritative source, not a fact on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cylect-io |
