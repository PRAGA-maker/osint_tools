---
id: verify-email-address
name: Verify Email address
description: Use when you have an email address and need to confirm it is real/deliverable before pivoting — returns a validity verdict (syntax, MX, SMTP mailbox).
url: https://email-checker.net
category: email
path:
- email
bestFor: Free single-address deliverability/existence check (syntax, MX, SMTP) on an email.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: freemium
costNote: Free web checks for single addresses; bulk/API verification is paid.
opsec: active
opsecNote: The check performs a live SMTP/MX probe against the target's mail provider; it does not email the person, but the lookup touches their mail server, so treat as active, not passive.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running public email-validation site (email-checker.net); a utility service, not a curated OSINT source. Verdicts are heuristic, not authoritative.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- email-checker.net
tags:
- email
- verification
source: metaosint
lastVerified: ''
enrichment: full
---

# Verify Email address

> Free web checker (email-checker.net) that tells you whether a single email address is syntactically valid and likely deliverable, via MX and SMTP mailbox probing.

## When to use
You have an `email` (from a breach dump, a social profile, a guessed pattern, or a tip) and you need to know whether it is a live mailbox before you build on it. Use it to triage candidate addresses: a "valid/deliverable" verdict tells you the address is worth pivoting on (search the local-part as a `username`, reverse-search the address); an "invalid" verdict lets you discard a dead lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://email-checker.net.
2. Paste the candidate `email` into the single-address field and submit (you may have to clear a captcha).
3. Read the verdict: it reports syntax validity, MX records for the domain, and an SMTP mailbox check result (valid / invalid / unknown / accept-all).
4. Pivot: if valid, take the local-part as a `username` seed for [[voilanorbert]]-style discovery and username search; cross-check deliverability against another verifier such as [[verifyemail-r]] before trusting a single verdict.

## Inputs → Outputs
- **In:** `email`
- **Out:** `email` (a deliverability/validity verdict on that same address)
- **Empty/negative result looks like:** "invalid" or "mailbox not found", or an "unknown/accept-all" result where the server accepts everything — in the accept-all case you cannot conclude the specific mailbox exists.

## Gotchas & OpSec
- Human-in-the-loop: expect a captcha on the free single-address form; bulk checking is gated behind a paid plan/API key.
- "Accept-all" (catch-all) domains return false-positives — many corporate/custom domains accept any address, so a "valid" result there is not proof the mailbox is real.
- OpSec: this is **active** — the verifier opens an SMTP conversation with the target's mail provider. It does not send mail, but the provider's logs see a verification probe. Do not run it from an address/IP you want to keep clean; it does not, however, alert the person.

## Overlaps ("do both")
- Pairs with `[[verifyemail-r]]` (Emailable) — run a candidate through both; agreement on "deliverable" is much stronger than either alone, and they disagree on catch-all domains.

## Trust & verifiability
`trust: community` — a well-established general-purpose email validation utility, not a curated OSINT/investigative source. Treat its verdict as a probabilistic signal (especially on catch-all domains), not ground truth.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | verify-email-address |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
