---
id: awesome-opt-out-guide-2026
name: Opt-Out Manual 2026
description: Use when you (the investigator) want to remove your own footprint from data brokers — returns categorized opt-out links, templates and step-by-step removal instructions.
url: https://github.com/thumpersecure/opt-out-manual-2026
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- privacy-clean-up
bestFor: Systematically removing your (or a client's) personal data from people-search sites and data brokers, upstream-first.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open (public domain / The Unlicense). GitHub repo plus a hosted web app and downloadable PDF; no account.
opsec: passive
opsecNote: This is a defensive reference — reading it exposes nothing. The opt-out actions it describes DO require contacting each broker (often with real ID/email), so use a dedicated removal identity/email and understand each site's process before submitting personal data to it.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A comprehensive community-maintained opt-out guide (442+ sites, upstream-first strategy) in the public domain. Broker processes change, so verify each site's current opt-out steps as you go.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Awesome Opt-Out Guide 2026
- opt-out-manual-2026
- data broker opt-out guide
tags:
- privacy
- opt-out
- data-broker-removal
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# Opt-Out Manual 2026

> A comprehensive, public-domain guide to removing yourself from data brokers and people-search sites — organised upstream-first so one removal cascades to many downstream sites.

## When to use
This is an OpSec / self-defence resource, not an investigative lookup. Use it to shrink your own (or a client's or a protected person's) exposure on the very people-search and data-broker sites investigators otherwise mine — before running sensitive operations, or when hardening a subject who is at risk (e.g. a stalking or domestic-violence victim). Investigators should know it both to protect themselves and to understand what their targets may have already scrubbed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo (https://github.com/thumpersecure/opt-out-manual-2026) or its hosted web app with progress tracking; optionally grab the PDF for offline use.
2. Start **upstream**: opt out of the major aggregators first (Acxiom, Data Axle, LexisNexis, etc.) — removing data there causes it to disappear from many downstream sites automatically.
3. Work the prioritised list of 442+ sites; each entry gives step-by-step instructions, difficulty/time estimates, and whether email or ID verification is required.
4. Use a dedicated removal email/identity for submissions; track completions and set reminders to re-check (brokers frequently re-list).
5. Pivot: after opting out, re-run people-search tools against yourself to confirm removals actually took effect.

## Inputs → Outputs
- **In:** none (a reference guide) — you supply your own details to each broker's opt-out flow
- **Out:** categorised opt-out links, request templates, and step-by-step removal instructions
- **Empty/negative result looks like:** not applicable — it's a static guide; the failure mode is an outdated step for a specific broker (verify the site's current process if instructions don't match).

## Gotchas & OpSec
- Opt-outs are not permanent — brokers re-acquire and re-list data; treat removal as an ongoing chore, not one-and-done.
- Some brokers require ID/email to opt out — you disclose data to remove data; use a dedicated identity and read each site's handling first.
- US-focused; EU/other jurisdictions have separate GDPR-based routes.

## Overlaps ("do both")
- Pairs with people-search tools used *reflexively against yourself* — the guide tells you where to remove data, and re-running the lookups verifies the removal worked and catches re-listings.

## Trust & verifiability
`trust: community` — a public-domain, community-maintained guide that is comprehensive and widely referenced; individual broker steps drift over time, so confirm each site's current opt-out process as you execute it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-opt-out-guide-2026 |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
