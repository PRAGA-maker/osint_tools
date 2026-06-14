---
id: email-address-validator
name: Email Address Validator
description: Use when you have an email address and need to confirm it is real and deliverable — returns syntax/MX/mailbox validity plus disposable and role-account flags.
url: http://www.email-validator.net
category: email
path:
- email
bestFor: Verifying whether a single email address is syntactically valid, has live MX, and accepts mail.
selectorsIn:
- email
selectorsOut:
- metadata
- domain
status: live
pricing: freemium
costNote: Free single-address checks on the site; bulk uploads and the API require a paid plan/credits.
opsec: active
opsecNote: Deliverability checks perform live SMTP probing against the target's mail server, which can be logged by that server; do not validate an address you must not alert.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: email-validator.net is a long-running commercial validation service; results are reliable for syntax/MX but mailbox-existence checks can be inconclusive on catch-all domains.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases: []
tags:
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Email Address Validator

> A free single-address email validator (email-validator.net) that checks syntax, MX records, and live mailbox acceptance.

## When to use
You have a candidate `email` — a guessed permutation, a breach hit, or an address from a record — and need to know if it is real before investing in it. Confirming deliverability tells you which of several guessed addresses is the live one to pivot on; a disposable/role flag tells you the owner is anonymizing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.email-validator.net.
2. Enter the email address in the single-check box and submit (solve a captcha if shown).
3. Read the verdict: syntax OK, domain/MX present, mailbox exists, and disposable/role/catch-all flags.
4. Pivot: a confirmed live address goes to `[[email-breach-analysis]]` and `[[email-dossier]]`; a disposable flag deprioritizes it.

## Inputs → Outputs
- **In:** `email`
- **Out:** validity verdict and flags (`metadata`), MX/domain info (`domain`)
- **Empty/negative result looks like:** "invalid" (bad syntax or no MX) or "unknown/accept-all" on catch-all domains where mailbox existence can't be confirmed.

## Gotchas & OpSec
- Human-in-the-loop: occasional captcha on the free single check; bulk/API needs an account.
- OpSec: ACTIVE — mailbox verification does live SMTP probing of the target's server, which that server can log. Treat as touching the target's infrastructure.
- Catch-all domains return "accept-all," which is not proof the specific mailbox exists.

## Overlaps ("do both")
- Pairs with `[[email-address-verifier]]` (Email Hippo) — run both when a single verdict is ambiguous; engines differ on catch-all and greylisted servers.

## Trust & verifiability
`trust: community` — established commercial validator; syntax/MX results are dependable, mailbox results are probabilistic on catch-all setups.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-address-validator |
| category | email |
| selectorsIn → selectorsOut | email → metadata, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
