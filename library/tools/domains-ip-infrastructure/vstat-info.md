---
id: vstat-info
name: vstat.info
description: Use when you have a `domain` and want estimated traffic, audience and referral data — returns visitor estimates, traffic sources and related `domain`s.
url: https://vstat.info
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Estimating a website's traffic volume, audience profile and referral/linked sites.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free traffic estimates per domain; deeper analytics/exports and the browser extension sit behind paid tiers.
opsec: passive
opsecNote: You query vstat's own aggregated panel data, not the target site, so nothing touches the subject's server. vstat sees which domains you look up.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party estimate based on panel/modelled data (roughly tracks Similarweb for large sites). Numbers are estimates, not the site's real analytics.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatruns
aliases:
- VStat
tags:
- Domain/IP/Links
- Website traffic look up
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# vstat.info

> A free website-traffic estimator — get a domain's approximate visitor volume, audience and referral sources, including numbers for smaller sites that bigger tools skip.

## When to use
You have a `domain` and want a sense of its scale and audience: how much traffic it gets, where visitors come from, and what other sites relate to it. Helps you judge whether a site is a busy operation or a personal page, and surfaces referral/linked `domain`s to chase. Peripheral to missing-persons work; mainly for profiling a domain's reach.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://vstat.info and enter the `domain`.
2. Read the estimates: monthly/daily visitor counts, traffic trend charts (typically ~6 months), audience sources, and interest/profile breakdowns.
3. Note any referral or related sites listed — these are candidate `domain` pivots.
4. Treat every figure as a modelled estimate; corroborate scale with a second traffic tool before drawing conclusions.

## Inputs → Outputs
- **In:** `domain`
- **Out:** estimated visitor volume, traffic sources, audience profile, related `domain`s
- **Empty/negative result looks like:** very low or "no data" for a small/new/private site — vstat covers more small sites than most, but genuinely obscure domains still return little. The web fetch may 403 to bots; use a normal browser.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — you query vstat's aggregated data, not the target. Use a burner session if the lookup itself is sensitive.
- Figures are estimates from panel/modelled data; they are directional, not the site's true analytics.

## Overlaps ("do both")
- Pairs with `[[whatruns]]` — vstat.info estimates who visits a site while WhatRuns fingerprints how it's built; together they profile a domain's reach and stack.

## Trust & verifiability
`trust: unverified` — a third-party estimator; useful for relative scale, but never cite its numbers as exact and confirm with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vstat-info |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
