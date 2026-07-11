---
id: mailboxlayer-api
name: mailboxlayer API
description: Use when you have an `email` and want to validate its deliverability and quality (syntax, MX, live SMTP, disposable/free flags) — returns an `email` validity verdict and quality score.
url: https://mailboxlayer.com/
category: email
path:
- email
bestFor: Programmatically checking whether an email is syntactically valid, has MX records, and passes a live SMTP existence probe.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: freemium
costNote: Freemium (apilayer). 1,000 free requests/month with an API key; higher volume and some fields require paid plans.
opsec: active
opsecNote: The SMTP check makes a real (non-sending) connection to the target's mail server to test whether the mailbox exists — that touches the target's infrastructure and may be logged there. It requires your API key, tying lookups to your account. Prefer it over doing the SMTP probe from your own IP.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: Run by apilayer, an established API vendor; SMTP/catch-all results are best-effort and providers increasingly defeat them, so treat "valid" as probabilistic.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- mailboxlayer
- apilayer email verification
tags:
- Emails
- email-verification
- deliverability
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# mailboxlayer API

> A REST email-verification API: give it an address and it returns syntax validity, MX records, a live SMTP existence check, catch-all/role/disposable/free flags and a quality score.

## When to use
You have an `email` and want to know if it's real and deliverable before building on it — confirming a candidate address you derived from a name pattern, or triaging a list. A positive SMTP result strengthens the case that an address exists and is in use; the flags tell you whether it's disposable/role/free (context that changes how much weight to give it).

## How to use it (`bestInteractionPattern`: api)
1. Sign up at https://mailboxlayer.com/ for an API key (1,000 free requests/month).
2. Call `https://apilayer.net/api/check?access_key=KEY&email=target@example.com&smtp=1&format=1`.
3. Read the JSON: `format_valid`, `mx_found`, `smtp_check`, `catch_all`, `role`, `disposable`, `free`, and a `score` (0–1).
4. Interpret: `smtp_check: true` on a non-catch-all domain is a strong "mailbox exists" signal; catch-all domains make it inconclusive.
5. Pivot: a verified `email` feeds account-existence checks (account.live.com, VK/Gmail recovery) and breach lookups.

## Inputs → Outputs
- **In:** `email`
- **Out:** `email` validity (format/MX/SMTP), catch-all/role/disposable/free flags, quality `score`
- **Empty/negative result looks like:** `format_valid: false` or `smtp_check: false` — the address is malformed or the server rejects it; on catch-all domains `smtp_check` may be true for *any* address, so it proves nothing.

## Gotchas & OpSec
- The live SMTP probe touches the target domain's mail server — active, and loggable there; using the API keeps it off your own IP.
- Catch-all domains return "valid" for everything — the result is then meaningless for existence.
- Big providers (Gmail/Outlook) increasingly block/greylist SMTP verification, degrading accuracy.
- API key + registration required.

## Overlaps ("do both")
- Pairs with account-existence oracles ([[account-live-com]], provider recovery flows) and other verifiers (Hunter, ZeroBounce) — SMTP validity plus a provider account hit is far stronger than either alone.

## Trust & verifiability
`trust: community` — a legitimate commercial verifier; results are best-effort and defeated by catch-all/greylisting, so treat "valid" as probabilistic, not proof the person owns the address.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mailboxlayer-api |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | api |
| opsec | active |
| human-in-loop | yes (api-key) |
