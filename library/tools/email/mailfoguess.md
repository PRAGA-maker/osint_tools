---
id: mailfoguess
name: Mailfoguess
description: Use when you have a person's `name`/`username` and want to derive and test their likely email addresses — generates permuted local-parts, applies per-provider rules, and verifies which exist.
url: https://github.com/WildSiphon/Mailfoguess
category: email
path:
- email
bestFor: Turning first/middle/last name + username + a number into a ranked set of candidate emails, then checking which are real.
selectorsIn:
- name
- username
selectorsOut:
- email
status: live
pricing: free
costNote: Free, open-source Python CLI; no account or key. Optional verification uses the holehe library, also free.
opsec: active
opsecNote: Generation itself is offline/passive, but the optional verification step probes real provider/site endpoints for each candidate address — that traffic touches those services with the guessed addresses. Run verification behind a VPN and pace it; rate limits cause false negatives.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: A community open-source tool (WildSiphon); the generation logic is transparent and auditable, but verification accuracy is bounded by provider anti-abuse behaviour.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- WildSiphon Mailfoguess
tags:
- Emails
- email-permutation
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# Mailfoguess

> A CLI that manufactures every plausible email a person might use — from name and username fragments — then filters to the ones that actually exist.

## When to use
You know a subject's `name` (first/middle/last), maybe a `username`, and a distinguishing `number` (birth year, house number), but you don't have their email. Mailfoguess builds the combinatorial space of likely local-parts (`john.doe`, `jdoe`, `doe.j92`, `johnnyd`…), attaches provider domains while respecting each provider's account-creation rules, and optionally verifies which addresses are live. Reach for it to convert identity fragments into a testable shortlist of emails.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/WildSiphon/Mailfoguess and install its Python requirements.
2. Run it with the known fragments: firstname, middlename, lastname, username, a number, plus a generation level (`min`→`max`) and separators.
3. It outputs candidate local-parts grouped by domain, saved as JSON in `./output/`.
4. Enable holehe-based verification to flag which addresses appear registered (expect some false negatives from rate limits).
5. Pivot: a verified address feeds `[[account-live-com]]`, `[[palenath]]`/Holehe (site enumeration) and breach-search tools; a strong candidate that won't verify can still be tested via a provider's account-existence flow.

## Inputs → Outputs
- **In:** `name` (first/middle/last), `username`, a distinguishing number
- **Out:** ranked candidate `email` addresses (grouped by domain), each optionally flagged exists/not-exists
- **Empty/negative result looks like:** all candidates flagged non-existent — either the person uses none of the guessed patterns/providers, or (common) verification was throttled and returned false negatives; treat "not found" as inconclusive, not disproven.

## Gotchas & OpSec
- Combinatorial blow-up: higher generation levels produce huge lists — start low and widen only if needed.
- Verification is noisy: provider rate limits and catch-all domains cause both false negatives and false positives; corroborate any "hit" with a second tool.
- OpSec: **active** during verification — those probes reach real services; run behind a VPN.

## Overlaps ("do both")
- Pairs with `[[email-verifier]]` (Hunter) — Mailfoguess generates candidates; Hunter independently confirms deliverability.
- Pairs with `[[palenath]]`/Holehe — once an address verifies, enumerate where it's registered.

## Trust & verifiability
`trust: community` — open-source and transparent in how it builds candidates, but any "exists" verdict depends on flaky provider endpoints, so confirm a hit before treating an email as the subject's.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mailfoguess |
