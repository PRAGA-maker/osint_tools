---
id: osint-sync
name: Osint-Sync
description: Use when you have a `username`, `email`, or `phone` and want to fan the search across 20+ platforms and premium tools from the browser — returns `social-profile`, email, and phone intel via a right-click extension.
url: https://github.com/mixaoc/Osint-Sync
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Right-click, multi-platform lookups of usernames, emails, and phones (with GHunt/IntelX/Epieos integrations) from one browser extension.
selectorsIn:
- username
- email
- phone
selectorsOut:
- social-profile
- email
- phone
status: live
pricing: freemium
costNote: Open-source (MIT) extension, but searches run on a credit system — new accounts get free credits; more credits are paid. The premium integrations (GHunt, IntelX, Epieos) sit behind those credits.
opsec: active
opsecNote: Queries route through the extension's backend/premium APIs, so your selectors leave your browser to third parties and are tied to your Osint-Sync account. Use a dedicated investigation account and avoid entering anything that identifies you or a client.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source (MIT) with modest adoption (~58 stars); it brokers queries to third-party OSINT services, so trust hinges on those upstreams and on the credit-backed backend it routes through.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
relatedTools: []
aliases:
- Osint Sync
- OsintSync
tags:
- browser-extension
- username
- multi-platform
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Osint-Sync

> A browser extension that fans a `username`, `email`, or `phone` across 20+ platforms and premium tools (GHunt, IntelX, Epieos) from a right-click menu — a credit-metered aggregator.

## When to use
You have a `username`, `email`, or `phone` and want a fast, broad first pass without opening each service by hand. Osint-Sync sends the selector to many platforms and integrated premium tools at once and collects the hits, with context-menu integration so you can search selected text directly. It is a speed/aggregation layer over tools you might otherwise run individually.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the Firefox add-ons store or load the repo build manually (Chrome store listed as "coming soon"); use a dedicated investigation browser profile.
2. Register an Osint-Sync account to receive free starting credits (each search costs a credit).
3. Enter or right-click a `username`, `email`, or `phone` and run the search across the selected platforms/integrations.
4. Read the aggregated results: `social-profile` hits, email intelligence, phone carrier/location data; use the history/export to keep a record.
5. Pivot: confirmed profiles/emails/phones feed the dedicated tools behind them (GHunt for Google accounts, Epieos for email, etc.) for deeper, verifiable results.

## Inputs → Outputs
- **In:** a `username`, `email`, or `phone`
- **Out:** `social-profile` matches, email intel, and phone carrier/location data across many platforms
- **Empty/negative result looks like:** no hits (or you are out of credits) — a selector too common/absent, or the metered backend blocking further queries; top up or query the underlying tool directly.

## Gotchas & OpSec
- Human-in-the-loop: requires account registration and manages a credit balance; premium integrations consume credits.
- OpSec: **active** — selectors leave your browser to the extension's backend and third-party APIs, tied to your account. Use a burner account; never enter self- or client-identifying data.
- Credit-metered: heavy use hits a paywall, and results depend entirely on the third-party services it brokers.
- Modest, community-scale project — corroborate anything important with the authoritative underlying tool.

## Overlaps ("do both")
- Overlaps with `[[trufflepiggy-context-search]]` (right-click multi-engine launcher) and dedicated tools (Sherlock, holehe, GHunt, Epieos): Osint-Sync aggregates and integrates them behind credits, so use it to triage, then confirm with the standalone tool for a citable result.

## Trust & verifiability
`trust: community` — open-source but reliant on a credit-backed backend and third-party APIs; treat its aggregated output as leads and verify each in the primary tool it came from.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-sync |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | username, email, phone → social-profile, email, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
