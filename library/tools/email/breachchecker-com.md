---
id: breachchecker-com
name: Breachchecker.com
description: Use when you have an `email` and want the history of data breaches it appears in, including which fields leaked — returns breach names and exposed selectors like address and password hints.
url: https://breachchecker.com/
category: email
path:
- email
bestFor: Checking which known data breaches exposed a given email and what data leaked.
selectorsIn:
- email
selectorsOut:
- address
- email
status: live
pricing: freemium
costNote: Free breach lookup by email; detailed per-breach exposure and monitoring features are gated behind paid/registered tiers.
opsec: passive
opsecNote: Passive toward the subject (they are not notified), but you are submitting the target's email to a third-party breach aggregator that logs queries. Use a sock-puppet session; automated/bot access may hit a Cloudflare challenge.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial breach-lookup aggregator of unverified sourcing; corroborate significant hits against an independent breach source (e.g. HIBP) before acting.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- BreachChecker
- breachchecker.com
tags:
- Emails
- breach-check
source: cyb-detective
lastVerified: '2026-07-14'
enrichment: full
---

# Breachchecker.com

> An email-to-breach lookup: enter an address and see which known data leaks it turned up in, and which fields were exposed.

## When to use
You have an `email` and want to establish that the address is real, in circulation, and historically exposed — plus which data classes leaked (passwords, addresses, phone, etc.). Useful to confirm an address belongs to an active person, to date their online presence, and to surface secondary selectors (a leaked `address`) that leaked alongside the email.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://breachchecker.com/ in a sock-puppet browser (expect a possible Cloudflare/captcha challenge for automated access).
2. Enter the target `email` and run the check.
3. Read the results: a list of breaches the address appears in and the categories of data exposed in each.
4. Corroborate: cross-check notable hits against an independent breach source before drawing conclusions.
5. Pivot: an exposed `address`/username/phone from a breach feeds the matching selector tool; confirmed exposure dates anchor a presence timeline.

## Inputs → Outputs
- **In:** `email`
- **Out:** breach names the address appears in, categories of exposed data (`address`, password/username hints, etc.)
- **Empty/negative result looks like:** "no breaches found" — which means not in *this* aggregator's dataset, not proof the address was never leaked; datasets differ between checkers.

## Gotchas & OpSec
- Human-in-the-loop: Cloudflare/captcha may block bot access; run it manually.
- Unverified aggregator: breach attributions can be wrong or stale; confirm against a second source (HIBP or similar).
- Never enter your own email here during an investigation; use a sock-puppet.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` and other breach checkers — different tools cover different dumps, so run more than one to close coverage gaps; account-existence checks confirm the address is live where breach data only shows past exposure.

## Trust & verifiability
`trust: unverified` — a commercial aggregator with opaque sourcing; treat hits as leads to corroborate against an independent breach index.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | breachchecker-com |
| category | email |
| selectorsIn → selectorsOut | email → address, email |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
