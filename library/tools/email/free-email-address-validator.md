---
id: free-email-address-validator
name: Free email address validator
description: Use when you have a candidate email and need to confirm it is real/deliverable before relying on it as a contact point.
url: https://verifalia.com/validate-email
category: email
path:
- email
bestFor: Verifying whether an email address exists and is deliverable (syntax, MX, mailbox, disposable check).
selectorsIn:
- email
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free web widget validates a small daily quota; bulk/API validation is paid (Verifalia subscription).
opsec: passive
opsecNote: Verifalia probes the mail server (SMTP-level) rather than contacting the person; the address is disclosed to the vendor but no message is sent to the target.
humanInLoop: true
humanInLoopReason:
- captcha
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Verifalia is a long-running commercial email-verification service; the free web validator is widely used and its deliverability verdicts are reproducible.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Verifalia
tags:
- email
relatedTools:
- findemail-io
source: metaosint
lastVerified: ''
enrichment: full
---

# Free email address validator (Verifalia)

> Web validator that tells you whether an email address is syntactically valid, has a live MX, and accepts mail — without emailing the person.

## When to use
You have a candidate `email` (from a guess via `[[findemail-io]]`, a breach dump, or a social profile) and need to know if it is real and deliverable before using it as a pivot or contact point. Also flags disposable/role/catch-all addresses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://verifalia.com/validate-email.
2. Enter the candidate `email` and solve any CAPTCHA.
3. Read the verdict: Deliverable / Undeliverable / Risky (catch-all, disposable, role account), plus MX and SMTP checks.
4. Pivot: a "Deliverable" address supports proceeding to account-existence/breach checks; "Undeliverable" tells you to drop or re-guess it.

## Inputs → Outputs
- **In:** `email`
- **Out:** deliverability verdict + technical flags (`metadata-exif`: MX present, disposable, catch-all, role)
- **Empty/negative result looks like:** "Undeliverable" or hard SMTP rejection — the mailbox does not accept mail. "Catch-all" means the server accepts everything, so a positive is inconclusive.

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHA and a small free daily quota; bulk needs the paid API.
- Catch-all domains return "accept" for any address, so deliverability there is not proof the specific mailbox exists.
- OpSec: passive — it queries the mail server, it does not send a visible email to the subject. The address is still disclosed to Verifalia.

## Overlaps ("do both")
- Pairs with `[[findemail-io]]` (guess the address) → Verifalia (confirm it).

## Trust & verifiability
`trust: community` — established commercial verifier; verdicts are based on MX/SMTP checks you could reproduce with mail tooling.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-email-address-validator |
| category | email |
| selectorsIn → selectorsOut | email → metadata-exif (deliverability flags) |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
