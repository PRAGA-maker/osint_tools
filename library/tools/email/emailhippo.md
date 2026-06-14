---
id: emailhippo
name: EmailHippo
description: Use when you need to verify whether an email address is real and deliverable (syntax, DNS/MX, SMTP, disposable/role detection) — returns validity/metadata only, not profiles.
url: https://tools.verifyemailaddress.io
category: email
path:
- email
bestFor: Reputable single-address deliverability verification.
selectorsIn:
- email
selectorsOut:
- metadata
status: live
pricing: freemium
costNote: Free interactive single-address checker; bulk and API use are paid (Email Hippo commercial plans).
opsec: passive
opsecNote: Server-side verification including an SMTP handshake against the recipient mail server; the target person is not alerted, though their mail server may log the probe. Free tool has a CAPTCHA.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Email Hippo is an established commercial email-verification vendor; the free verifyemailaddress.io tool is its public front end.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Email Hippo
- verifyemailaddress.io
tags:
- email
- verification
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# EmailHippo

> Email Hippo's free public verifier — confirms an address is well-formed, has valid DNS/MX, and accepts mail via SMTP, flagging disposable/role/catch-all addresses.

## When to use
You hold an `email` and need a trustworthy yes/no on whether it is real and deliverable before pivoting or attempting contact. It returns no identity data — it is a quality gate, not a discovery tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to tools.verifyemailaddress.io.
2. Enter the `email` and solve the CAPTCHA.
3. Read the verdict: syntax, DNS/MX, SMTP/mailbox check, plus flags for disposable, role-based, and catch-all/free-provider addresses.
4. Pivot: a verified deliverable address is worth running through `[[email-reputation]]` and `[[epieos-email-tool]]`; a disposable/invalid one is low value.

## Inputs → Outputs
- **In:** `email`
- **Out:** `metadata` (deliverability status + disposable/role/catch-all flags)
- **Empty/negative result looks like:** "Bad"/"undeliverable" status, or "catch-all" meaning the server accepts everything (verification inconclusive — do not over-read).

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHA on the free tool; bulk/automation requires the paid API.
- Catch-all domains return ambiguous results — neither confirm nor deny.
- OpSec: passive toward the person, but an SMTP probe touches their mail server; avoid for sensitive targets where even server logs matter.

## Overlaps ("do both")
- More reputable than the generic `[[email-validator]]` / `[[email-validator-tool]]`; use EmailHippo as the verification step, then a discovery tool like `[[epieos-email-tool]]`.

## Trust & verifiability
`trust: trusted` — public tool of Email Hippo, a long-standing commercial email-verification vendor with documented methodology.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | emailhippo |
| category | email |
| selectorsIn → selectorsOut | email → metadata |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
