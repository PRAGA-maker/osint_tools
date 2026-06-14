---
id: email-finder
name: Email Finder
description: Use when you have an email address and want associated accounts and exposure in one lookup — returns linked social/registration hints and breach signals from the OSINT.SH suite.
url: https://osint.sh/email/
category: email
path:
- email
bestFor: A free reverse-email lookup that surfaces associated accounts and exposure for an address.
selectorsIn:
- email
selectorsOut:
- social-profile
- username
- metadata
status: live
pricing: freemium
costNote: Free reverse-email lookups on OSINT.SH; the suite also offers paid/API tiers and rate limits free use.
opsec: passive
opsecNote: The query hits OSINT.SH's aggregated sources, not the target's mailbox, so the owner is not alerted; you disclose the address to OSINT.SH, so use a clean context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: OSINT.SH is a popular free OSINT toolkit; aggregated results are convenient but coverage/freshness vary and should be corroborated.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- OSINT.SH Email
tags:
- email
- reverse-email
source: osint4all
lastVerified: ''
enrichment: full
---

# Email Finder

> OSINT.SH's reverse-email tool: paste an address and get back associated accounts, registration hints, and exposure in one lookup.

## When to use
You have an `email` for a missing person or associate and want a quick aggregated picture: which platforms/services it links to and whether it has been exposed. A good single-shot pivot from a bare address toward `social-profile`s and reused `username`s.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://osint.sh/email/.
2. Enter the email address and submit.
3. Read the aggregated results — linked accounts, services the address registered with, any breach/Gravatar signals.
4. Pivot: take recovered `username`s to username-search tooling and each `social-profile` to platform tooling; confirm exposure with `[[email-breach-analysis]]`.

## Inputs → Outputs
- **In:** `email`
- **Out:** linked `social-profile`s, reused `username`s, registration/exposure `metadata`
- **Empty/negative result looks like:** no associations returned — typical for fresh/disposable addresses, or where the aggregated sources simply lack coverage (a negative is weak evidence).

## Gotchas & OpSec
- Human-in-the-loop: free use is rate-limited; heavy use needs the paid/API tier.
- OpSec: passive toward the target (no mailbox contact); you disclose the address to OSINT.SH.
- Aggregated coverage and freshness vary; corroborate any hit before acting on it.

## Overlaps ("do both")
- Pairs with `[[email-assumptions]]` (IntelTechniques) and `[[e-mail-search-tool]]` — overlapping aggregators; run more than one to widen source coverage.

## Trust & verifiability
`trust: community` — widely used free toolkit; convenient but opaque about sources, so treat results as leads to verify, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-finder |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, username, metadata |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
