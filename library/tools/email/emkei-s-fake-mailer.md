---
id: emkei-s-fake-mailer
name: Emkei's Fake Mailer
description: Use when you must send an email with a chosen/spoofed From header (e.g. controlled pretext or a tracked message) to a target address — it sends mail; it does not look anyone up.
url: https://emkei.cz
category: email
path:
- email
bestFor: Sending an email with custom/spoofed headers (anonymous mailer).
selectorsIn:
- email
selectorsOut: []
status: live
pricing: free
costNote: Free public web mailer.
opsec: active
opsecNote: ACTIVE and intrusive — it actually delivers a message to the recipient, alerting them. Spoofing sender headers may be illegal/unethical and is logged by your IP. Not a passive OSINT lookup.
humanInLoop: true
humanInLoopReason:
- captcha
- legal-gate
bestInteractionPattern: web-manual
trust: community
trustNote: Long-known free "fake mailer"; functions as advertised but is an anonymous third-party relay with obvious abuse potential.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- emkei
- fake mailer
tags:
- email
- mailer
- active
source: metaosint
lastVerified: ''
enrichment: full
---

# Emkei's Fake Mailer

> A free web service that sends email with arbitrary/spoofed From, Reply-To, and other headers — a sending tool, not a lookup tool. Use with extreme caution.

## When to use
Rarely, and only where active engagement is authorized: sending a controlled pretext message or a tracked email to a known `email` to elicit a response or confirm an account is live. It produces **no** investigative output about a person. For passive discovery, do not use this.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open emkei.cz; fill From, To (the target `email`), subject, body, and optional attachments/headers.
2. Solve the CAPTCHA and send.
3. There is no "result" to read here — any intelligence comes from the recipient's reaction or a separately embedded tracker, not from this tool.

## Inputs → Outputs
- **In:** `email` (the recipient)
- **Out:** none (this is an action, not a query)
- **Empty/negative result looks like:** N/A — the only feedback is delivery success and whatever the recipient does.

## Gotchas & OpSec
- OpSec: ACTIVE — you are contacting the target; they will see the message. This is the opposite of passive OSINT.
- Legal/ethical gate: sender spoofing can constitute fraud, harassment, or impersonation depending on jurisdiction and intent; in a missing-persons context this can be illegal and harmful. Get authorization first.
- Your traffic to emkei.cz is logged; do not assume anonymity.

## Overlaps ("do both")
- For passive account confirmation use `[[holehe]]` or `[[epieos-email-tool]]` instead of sending mail.

## Trust & verifiability
`trust: community` — a well-known free mailer that does what it claims; listed here for completeness and warning, not as a recommended missing-persons technique.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | emkei-s-fake-mailer |
| category | email |
| selectorsIn → selectorsOut | email → (none; sends mail) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha, legal-gate) |
