---
id: reversegenie
name: ReverseGenie
description: Use when attempting a reverse-email-to-owner lookup via the legacy ReverseGenie site — an old, likely-defunct people-search aggregator.
url: http://www.reversegenie.com/email.php
category: email
path:
- email
bestFor: A legacy reverse-email lookup attempt; historically a free-teaser people-search that upsold paid reports.
selectorsIn:
- email
selectorsOut:
- name
- address
- phone
status: down
pricing: freemium
costNote: Historically free teaser results with paid full reports; HTTP-only legacy site that appears defunct.
opsec: passive
opsecNote: Reverse lookup is passive toward the subject, but the operator is unknown and the site is HTTP-only — use a VPN and never enter your own identity.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Old reverse-lookup aggregator (reversegenie.com), HTTP-only and apparently no longer operational. Provenance and data sourcing unverified; treat as likely-dead and any output as unconfirmed.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- reverse-lookup
- legacy
source: metaosint
lastVerified: ''
enrichment: full
---

# ReverseGenie

> A legacy reverse-email-lookup site that historically returned a teaser owner identity and upsold paid reports — now appears defunct.

## When to use
You have only an `email` and are exhausting low-confidence reverse-lookup options. Reach for this only as a last resort; it is an old aggregator that may no longer load, and any result needs corroboration elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL over a VPN / clean browser (HTTP-only, no TLS); expect it may be dead or redirect.
2. If it loads, enter the target email in the lookup form.
3. Read any teaser (claimed `name`/`address`/`phone`), then expect a paywall for the full report.
4. Treat any preview as a lead to verify with a current tool, not as fact.

## Inputs → Outputs
- **In:** `email`
- **Out:** claimed `name` / `address` / `phone` (unverified, likely paywalled).
- **Empty/negative result looks like:** site fails to load, "no records found," or a generic upsell with no specific data.

## Gotchas & OpSec
- Human-in-the-loop: payment-wall-partial; the site may simply be offline.
- OpSec: HTTP-only and operator-unknown — use a VPN, do not submit your own details. Passive toward the subject.

## Overlaps ("do both")
- Prefer maintained reverse tools; cross-check any claim against `[[reverse-whois]]` and current reverse-email services.

## Trust & verifiability
`trust: unverified` — old, HTTP-only aggregator of unknown provenance that appears defunct; do not rely on it as a source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reversegenie |
| category | email |
| selectorsIn → selectorsOut | email → name, address, phone |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
