---
id: competeshark
name: CompeteShark
description: Use when you have an `employer-org` or `domain` and want to monitor how a target company changes its website, pricing, and marketing over time — returns tracked change history for that `domain`.
url: http://competeshark.com
category: public-records
path:
- public-records
bestFor: Real-time competitive-intelligence monitoring of a company's website and marketing changes.
selectorsIn:
- domain
- employer-org
selectorsOut:
- domain
- employer-org
status: live
pricing: freemium
costNote: Free trial with no credit card required; ongoing monitoring and history are primarily a paid plan.
opsec: passive
opsecNote: Tracking is server-side and does not touch the target from your IP, but you must create an account to set up monitors — use a sock-puppet email. Do not enter a subject's private site if it is behind auth.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial competitive-intelligence SaaS; useful but marketing-oriented, and its OSINT value is indirect (business/marketing footprint, not personal identifiers).
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- competeshark.com
tags:
- company-research
- competitive-intelligence
- change-monitoring
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# CompeteShark

> A competitive-intelligence service that watches a company's website for changes — best for tracking a business's evolving marketing and pricing footprint, not people.

## When to use
You have a target company (`employer-org`) or its `domain` and want a running log of how its website, promotions, pricing, and landing pages change over time. This is a business-footprint tool: relevant when a missing-persons lead runs through a company (a subject's employer, a shell business, a scam site) and you want to observe activity or catch when the operation goes quiet or rebrands.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://competeshark.com and start the free trial (sock-puppet email; no card needed to begin).
2. Add the target `domain` as a monitored competitor.
3. Let it capture snapshots; review the visual change timeline and diff reports it produces.
4. Watch for meaningful events: new/removed pages, pricing or contact changes, rebrands, or a site going dormant.
5. Pivot: a changed contact block, new domain, or removed page feeds WHOIS/archive tools (`[[wayback-machine]]`-style) and company-registry lookups.

## Inputs → Outputs
- **In:** `domain` / `employer-org`
- **Out:** change history and visual diffs for that `domain` (structure, marketing, pricing over time)
- **Empty/negative result looks like:** a static site produces no change events; that means "no changes captured," not that the business is inactive. History only begins from when you start monitoring — it is not retroactive.

## Gotchas & OpSec
- Human-in-the-loop: requires account signup to configure monitors; deeper history and more monitors are gated behind paid plans.
- Not retroactive: for past states of a site use a web archive instead — CompeteShark only tracks forward from setup.
- OpSec: monitoring is server-side (passive from your perspective), but keep account identity separate from the investigator.

## Overlaps ("do both")
- Pairs with web-archive tools for historical snapshots (which CompeteShark lacks) and with WHOIS/domain tools to tie a monitored site back to a registrant.

## Trust & verifiability
`trust: community` — a legitimate commercial SaaS, but its output is marketing-change data, not verified records. Its relevance to a person is indirect; treat it as business-context intelligence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | competeshark |
| category | public-records |
