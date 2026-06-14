---
id: trumail
name: Trumail
description: Use when you want a programmatic email-validation/verification API to check deliverability and risk of an address — returns validity, deliverability, and risk flags (project is largely defunct).
url: https://trumail.io/
category: email
path:
- email
bestFor: Open-source email verification/validation API (syntax, MX, SMTP, disposable/role flags).
selectorsIn:
- email
selectorsOut:
- metadata
- domain
status: down
pricing: freemium
costNote: Originally a free open-source self-hosted service with a paid hosted tier; the hosted service (trumail.io) has been discontinued — self-host from source instead.
opsec: passive
opsecNote: Performs MX/SMTP checks against the email's mail server, not the person; the subject is not notified. SMTP probes originate from wherever the service runs (the hosted host, or your own box if self-hosted).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: Trumail was a popular open-source (Go) email verification project; the hosted trumail.io endpoint is no longer reliably operational. Use the open-source code or a maintained fork rather than assuming the live API works.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- verify-email
- verify-an-email-address-mailtester
aliases:
- trumail.io
tags:
- email
- email-validation
- api
source: osint4all
lastVerified: ''
enrichment: full
---

# Trumail

> An open-source email-verification API (syntax/MX/SMTP/disposable checks) — useful self-hosted, but the public trumail.io service is effectively dead.

## When to use
You have an `email` and want to programmatically check whether it is well-formed, has valid MX, is accepted by SMTP, and whether it is disposable/role-based — to score how real an address is before pivoting. Best when you need this at scale in a script rather than one address in a browser.

## How to use it (`bestInteractionPattern`: api)
1. Do not rely on the hosted `https://trumail.io/` endpoint — it has been discontinued.
2. Clone the open-source project (or a maintained fork) and run it yourself, e.g. via Docker/Go binary.
3. Query the validation endpoint with an email; parse the JSON (validFormat, deliverable, fullInbox, disposable, catchAll, etc.).
4. Pivot: addresses scored deliverable are worth pushing into reverse-lookup/breach tools ([[venacus]], [[thatsthem]]); disposable ones are low-value.

## Inputs → Outputs
- **In:** `email`
- **Out:** `metadata` (validity/deliverability/risk flags), `domain` (MX info)
- **Empty/negative result looks like:** the hosted API not responding (expected), or a "deliverable: false / catchAll: true" verdict that gives only weak signal.

## Gotchas & OpSec
- The public service is down — treat this as a self-host-only tool.
- SMTP verification is unreliable against catch-all and greylisting servers.
- OpSec: passive toward the subject; if self-hosting, the SMTP probes come from your IP — use a dedicated host if that matters.

## Overlaps ("do both")
- Same job as [[verify-email]] and [[verify-an-email-address-mailtester]] (web verifiers); use those for one-off checks and Trumail (self-hosted) for batch/API checks.

## Trust & verifiability
`trust: community` — a well-known open-source verifier whose hosted endpoint is no longer dependable; trust the code, not the live site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trumail |
| category | email |
| selectorsIn → selectorsOut | email → metadata, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
