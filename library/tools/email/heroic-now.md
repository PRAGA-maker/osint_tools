---
id: heroic-now
name: HEROIC.NOW
description: Use when you want to check an email against a large aggregated breach dataset via HEROIC's consumer breach-search product.
url: https://heroic.com/
category: email
path:
- email
bestFor: Searching an email/username against an aggregated breach-compilation dataset.
selectorsIn:
- email
- username
selectorsOut:
- email
- metadata-exif
status: degraded
pricing: freemium
costNote: HEROIC has pivoted toward identity-protection/security products; the free breach-search front end ("HEROIC.NOW") has been deprecated/folded into paid offerings. Expect account/paywall gating.
opsec: passive
opsecNote: Queries an aggregated breach database; the target is not notified. You disclose the searched email to HEROIC.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: HEROIC.com is a real cybersecurity company, but the "HEROIC.NOW" breach-search product appears deprecated/rebranded. Dataset provenance and current availability are unconfirmed without checking the live site.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- HEROIC.com
tags:
- data-breach-search-engines
relatedTools:
- have-i-been-pwned
- iknowyour-dad
- h8mail
source: awesome-osint
lastVerified: ''
enrichment: full
---

# HEROIC.NOW

> HEROIC's consumer-facing breach-search product — check an email/username against a large aggregated leak compilation. The "HEROIC.NOW" brand appears to have been folded into HEROIC's broader identity-protection products.

## When to use
You have an `email` or `username` for a missing person or associate and want a second breach-aggregator beyond HIBP, in case it indexes leaks the others miss. Use as a corroborating source, not a primary one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://heroic.com/ and locate the breach/identity-monitoring search (may now require an account).
2. Enter the `email` (or `username`).
3. Read returned breach hits / exposed data classes.
4. Pivot breach names to the services the person used (account-enumeration tools).

## Inputs → Outputs
- **In:** `email`, `username`
- **Out:** breach source hits, exposed data attributes (`metadata-exif`-style)
- **Empty/negative result looks like:** no breaches returned, or a signup/paywall prompt before any result is shown.

## Gotchas & OpSec
- The free "HEROIC.NOW" search has been deprecated/rebranded — verify it still functions before relying on it.
- Human-in-the-loop: likely requires an account to see results.
- OpSec: passive toward the target; you reveal the searched email to HEROIC.

## Overlaps ("do both")
- Corroborate with `[[have-i-been-pwned]]` (authoritative) and `[[iknowyour-dad]]` / `[[h8mail]]` (alternate breach aggregators and credential contents).

## Trust & verifiability
`trust: unverified` — legitimate company but the specific breach-search product's current availability and dataset coverage are unconfirmed; verify on the live site before quoting results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | heroic-now |
| category | email |
| selectorsIn → selectorsOut | email, username → email, metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
