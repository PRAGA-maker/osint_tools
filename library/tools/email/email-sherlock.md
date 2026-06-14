---
id: email-sherlock
name: Email Sherlock
description: Use when you have an email address and want a reverse lookup of which social networks/sites it is registered on plus any public profile snippets — returns social-profile, name hints.
url: https://www.emailsherlock.com
category: email
path:
- email
bestFor: Reverse-email lookup across social networks to see where an address is registered.
selectorsIn:
- email
selectorsOut:
- social-profile
- name
status: degraded
pricing: freemium
costNote: Free basic reverse lookup; deeper "background"/profile data is upsold to paid partner reports.
opsec: passive
opsecNote: Passive third-party lookup; the address is sent to Email Sherlock's servers, not to the target. Some results are gated behind upsell pages.
humanInLoop: true
humanInLoopReason:
- captcha
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running consumer reverse-email site; results quality is inconsistent and heavily monetized via partner data brokers.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- emailsherlock
tags:
- email
- reverse-email
source: metaosint
lastVerified: ''
enrichment: full
---

# Email Sherlock

> Consumer-grade reverse-email lookup that reports which social networks an address is tied to and teases broader "background report" data.

## When to use
You have an `email` and want a quick check of which social platforms it is registered on. Useful as a secondary confirmation when an account-existence tool returns ambiguous results; weaker than dedicated enumeration tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the site and enter the `email` in the search box.
2. Solve any CAPTCHA / continue past interstitials.
3. Read the social-network match grid; note which platforms show "registered".
4. Pivot: confirm matched `social-profile` hits with `[[holehe]]` or `[[epieos-email-tool]]` rather than trusting the upsell summary. Ignore the paid "full report" CTA unless you have independent reason to buy.

## Inputs → Outputs
- **In:** `email`
- **Out:** `social-profile` (platform registration grid), occasional `name` fragments
- **Empty/negative result looks like:** no platform matches and a prompt to buy a "people search" report — treat as no public footprint, not as a paywalled find.

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHAs and aggressive upsell/partner-broker redirects; the most useful-looking data is often behind a payment wall and of questionable freshness.
- Results can be stale or false-positive — verify before acting.
- OpSec: passive; the address goes to a third-party broker's servers. Use a clean browser.

## Overlaps ("do both")
- Pairs with `[[holehe]]`: Holehe enumerates account existence deterministically and offline-ish; Email Sherlock adds a human-readable grid but is less reliable.

## Trust & verifiability
`trust: community` — established but commercially-driven consumer service; treat its claims as leads to verify, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-sherlock |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha, payment-wall-partial) |
