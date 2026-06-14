---
id: email-address-verifier
name: Email Address Verifier
description: Use when you have an email address and need to confirm it is deliverable and check for breach/social signals — returns a deliverability grade plus disposable/MX flags and (on paid tiers) social/Gravatar links.
url: https://tools.emailhippo.com
category: email
path:
- email
bestFor: Grading whether a single email address is real and deliverable, with extra intelligence on paid tiers.
selectorsIn:
- email
selectorsOut:
- metadata
- social-profile
status: live
pricing: freemium
costNote: Free single-address deliverability check on the tools page; bulk verification and the "More/Hippo" intelligence (social, Gravatar, breach) require an account/paid API.
opsec: active
opsecNote: Deliverability grading performs live SMTP checks against the target's mail server, which can be logged; passive enrichment (Gravatar/social) is less exposing but still routes through Email Hippo.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Email Hippo is a reputable commercial verification vendor; free-tier output is mostly deliverability, and the richer person-intelligence fields are gated behind paid plans.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Email Hippo
tags:
- email
source: metaosint
lastVerified: ''
enrichment: full
---

# Email Address Verifier

> Email Hippo's free verifier (tools.emailhippo.com) grades whether an email is deliverable; paid tiers add social/Gravatar and breach enrichment.

## When to use
You have a candidate `email` and need a deliverability verdict before pivoting, or you want the lightweight enrichment Hippo exposes (e.g. a linked Gravatar / social hint) to connect the address to a person. Useful to pick the live address out of a set of guessed permutations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tools.emailhippo.com.
2. Enter the email in the single-check field and submit (captcha may appear).
3. Read the grade (e.g. Ok / Bad / Unknown) plus syntax, MX, and disposable flags; note any Gravatar/social hint shown.
4. Pivot: a deliverable address goes to `[[email-breach-analysis]]` and username pivoting; a surfaced `social-profile` goes to social-media tooling.

## Inputs → Outputs
- **In:** `email`
- **Out:** deliverability grade + syntax/MX/disposable flags (`metadata`); possible Gravatar/`social-profile` link (paid tiers richer)
- **Empty/negative result looks like:** "Bad" (undeliverable) or "Unknown" on catch-all/greylisting servers; no social enrichment on the free tier.

## Gotchas & OpSec
- Human-in-the-loop: captcha on the free check; deeper intelligence needs an account/API key.
- OpSec: ACTIVE — deliverability grading does live SMTP probing of the target's mailserver. The Gravatar/social enrichment is more passive but still goes through Hippo.
- The free tool is mostly deliverability; do not assume rich person-data without a paid plan.

## Overlaps ("do both")
- Pairs with `[[email-address-validator]]` — cross-check ambiguous verdicts; the two engines disagree on catch-all and greylisted domains.

## Trust & verifiability
`trust: community` — established vendor with transparent grading; person-intelligence fields are gated and should be treated as paid-tier, not free-tier, output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-address-verifier |
| category | email |
| selectorsIn → selectorsOut | email → metadata, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
