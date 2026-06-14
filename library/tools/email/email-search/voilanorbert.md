---
id: voilanorbert
name: VoilaNorbert
description: Use when you have a person's name plus their company/domain and need to find or verify their work email — returns a likely business email address with a confidence score.
url: https://www.voilanorbert.com/
category: email
path:
- email
- email-search
bestFor: Finding a person's professional email from their name + employer domain (name → email).
selectorsIn:
- name
- domain
- employer-org
selectorsOut:
- email
status: live
pricing: freemium
costNote: Free trial (a handful of lookups); sustained single/bulk lookups and the API are paid (credit/subscription).
opsec: passive
opsecNote: Searches/derives addresses from public sources and verification heuristics; does not contact the target. Verification step may SMTP-probe the domain mail server.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial email-finder (sales/recruiting tool); reliable utility but a third-party guess engine, not an authoritative directory.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Norbert
- voilanorbert.com
tags:
- email
- email-finder
source: arf-seed
lastVerified: ''
enrichment: full
---

# VoilaNorbert

> A commercial email-finder: give it a person's `name` and their company `domain`, and it returns the most likely work `email` with a confidence score (plus bulk and verify modes).

## When to use
You know a subject's `name` and where they work (an `employer-org` / company `domain`) and you need a contact `email` — for example to confirm an identity, locate the person's online accounts (the address becomes a `username`/account seed), or contact an employer for a missing-persons lead. Best when the target has a professional/corporate footprint; weak for purely personal consumer addresses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at https://www.voilanorbert.com/ (free trial credits, then paid).
2. In "Find email", enter the person's full `name` and the company `domain` (or company name). For many, use the bulk upload.
3. Read the returned `email` and its confidence indicator; optionally run the result through Norbert's verify step.
4. Pivot: take a confident address to a deliverability check ([[verify-email-address]] / [[verifyemail-r]]), reverse-search the address, and use the local-part as a `username` seed across social and breach data.

## Inputs → Outputs
- **In:** `name` + `domain` / `employer-org`
- **Out:** `email` (best-guess professional address + confidence)
- **Empty/negative result looks like:** no address returned or a low-confidence guess — common when the person has no corporate email or the domain doesn't follow a guessable pattern. Low confidence ≠ correct; always verify.

## Gotchas & OpSec
- Human-in-the-loop: account required; only a few free lookups before the paywall, and bulk/API are paid.
- Results are *derived/predicted* (pattern + verification), not pulled from an authoritative directory — confidence scores can be wrong, especially for catch-all domains.
- OpSec: largely **passive** toward the person (no message sent), but the verification step may SMTP-probe the employer's mail server. Use a sock account; don't tie lookups to attributable billing if footprint matters.

## Overlaps ("do both")
- Pairs with deliverability verifiers [[verify-email-address]] and [[verifyemail-r]] — Norbert *finds* the candidate address; the verifiers *confirm* it's live, which Norbert's confidence score alone doesn't guarantee.

## Trust & verifiability
`trust: community` — a mainstream sales/recruiting email-finder. Dependable as a tool, but every result is a prediction; treat the returned email as a lead to verify, not a confirmed contact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | voilanorbert |
| category | email |
| selectorsIn → selectorsOut | name, domain, employer-org → email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
