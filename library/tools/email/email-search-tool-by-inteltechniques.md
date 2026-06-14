---
id: email-search-tool-by-inteltechniques
name: Email Search Tool by IntelTechniques
description: Use when you have an email address and want to fan it out across dozens of third-party lookup services from one dashboard — returns links to social-profile, breach, and registration hits.
url: https://inteltechniques.com/osint/email.search.html
category: email
path:
- email
bestFor: One-click fan-out of an email across many external OSINT services.
selectorsIn:
- email
selectorsOut:
- social-profile
- name
- username
- metadata
status: live
pricing: free
costNote: Free web tool; the linked third-party services have their own pricing/limits.
opsec: passive
opsecNote: Runs locally in your browser and hands off to third-party sites; queries are passive but each external service sees your IP. Use a clean browser/VPN.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Michael Bazzell (IntelTechniques), a long-standing and widely cited OSINT authority.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- IntelTechniques Email Tool
tags:
- email
- meta-search
source: metaosint
lastVerified: ''
enrichment: full
---

# Email Search Tool by IntelTechniques

> Michael Bazzell's browser-based email dashboard — type one address and open it across many breach, reverse-lookup, and social services in sequence.

## When to use
You have an `email` and want a fast, comprehensive sweep without manually visiting each service. Strong early step in a missing-persons email pivot: it surfaces which platforms, breaches, and reverse-lookup sites have something on the address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the page in your browser (it runs client-side; nothing is stored server-side).
2. Enter the `email` once in the top field; the tool populates per-service fields.
3. Click an individual service to open it, or use "Submit All" to fan out into multiple tabs/popups (allow popups).
4. Manually review each opened service for hits, then pivot: a matched `social-profile` or `username` feeds account-enumeration tools like `[[holehe]]` / `[[epieos-email-tool]]`.

## Inputs → Outputs
- **In:** `email`
- **Out:** links that may yield `social-profile`, `name`, `username`, `metadata` (breach membership)
- **Empty/negative result looks like:** every opened service returns "no results" — the address has a thin or compartmentalized footprint.

## Gotchas & OpSec
- Human-in-the-loop: you must read each external result yourself; the tool only dispatches queries.
- "Submit All" opens many popups — your browser may block them; whitelist the page.
- Bazzell periodically restructures the tools after services break; links can rot. OpSec: passive, but every third-party site logs your visit — use a sock-puppet browser/VPN.

## Overlaps ("do both")
- Pairs with `[[epieos-email-tool]]` and `[[holehe]]`: the dashboard finds *where* to look; those confirm specific account existence programmatically.

## Trust & verifiability
`trust: trusted` — built and maintained by Michael Bazzell of IntelTechniques, a primary reference in the OSINT field; the tool is open and inspectable in-page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-search-tool-by-inteltechniques |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, name, username, metadata |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
