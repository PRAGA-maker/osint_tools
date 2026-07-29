---
id: scrummage
name: Scrummage
description: Use when you have a selector (name, username, email, domain, IP, wallet) and want to run it across many OSINT sources at once from one self-hosted dashboard — returns aggregated `social-profile`, `email`, `domain`, `ip-address` hits.
url: https://github.com/matamorphosis/Scrummage
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: Fanning a single selector out across 50+ OSINT plugins from one self-hosted web console and archiving the results.
selectorsIn:
- username
- email
- domain
- ip-address
selectorsOut:
- social-profile
- email
- domain
- ip-address
status: live
pricing: free
costNote: Fully open-source (GPL-3.0); free of charge. You supply your own API keys for plugins that need them (Shodan, HIBP, etc.) and your own hosting.
opsec: active
opsecNote: Scrummage is only as passive as its plugins — some (e.g. Shodan lookups, HIBP) are passive, others actively query targets or third parties from your server's IP. Self-host it behind a VPN/VPS you control, and review which plugins fire before running a query so you don't touch a target directly.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: docker
trust: community
trustNote: Open-source project (matamorphosis) with active commit history; you run the code yourself, so you can audit it, but plugin output quality depends on the underlying third-party sources.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
relatedTools: []
aliases:
- Scrummage OSINT platform
tags:
- osint-automation
- aggregator
- self-hosted
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Scrummage

> A self-hosted "holistic OSINT" web platform — one dashboard that fans a selector out across 50+ plugins (HIBP, Shodan, blockchain, Ahmia dark web, Yandex, social media) and archives every hit.

## When to use
You have a selector — `username`, `email`, `domain`, `ip-address`, or a wallet — and want to sweep many sources in one pass instead of visiting each site by hand, with results, screenshots, and HTML archived to a case dashboard. Good for standing up a repeatable, multi-user OSINT workflow with logging and task scheduling, e.g. an investigation team working shared identifiers.

## How to use it (`bestInteractionPattern`: docker)
1. Clone `https://github.com/matamorphosis/Scrummage` and deploy via the included Dockerfile (or install the Python/Flask app directly) on a VPS you control.
2. Complete first-run setup to create the admin account, then add API keys for the plugins you'll use (Shodan, HIBP, etc.).
3. Log in to the web dashboard and run a task against your selector; enable only the plugins relevant to the pivot.
4. Review aggregated results, archived screenshots/HTML, and the event log; export findings.
5. Pivot: profiles/emails/domains it surfaces feed dedicated deep-dive tools; schedule recurring tasks to monitor a selector over time.

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, `ip-address` (and wallet/other plugin-specific inputs)
- **Out:** aggregated `social-profile`, `email`, `domain`, `ip-address` results with archived evidence
- **Empty/negative result looks like:** plugins return no hits (or error on missing API keys) — check that keys are configured before reading a blank result as "nothing exists."

## Gotchas & OpSec
- **Plugin-dependent OpSec**: it is not uniformly passive — know which plugins actively query targets before you run.
- Self-hosting and API-key management are on you; a misconfigured plugin silently returns nothing.
- Result quality mirrors the upstream sources; Scrummage aggregates but does not itself verify.

## Overlaps ("do both")
- Complements single-purpose deep-dive tools — Scrummage is the wide first pass that tells you which selectors light up; follow each hit into the dedicated tool for that source (e.g. a username hit into a username-enumeration tool).

## Trust & verifiability
`trust: community` — an open-source, auditable project you host yourself; the code is inspectable, but every result inherits the reliability of the third-party plugin that produced it, so verify individual findings at their source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scrummage |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email, domain, ip-address → social-profile, email, domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | docker |
| opsec | active |
| human-in-loop | yes (account-login) |
