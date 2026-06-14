---
id: verify-email-2
name: Verify Email
description: Use when you have an email and want a free web check of whether the mailbox exists and can receive mail (syntax, MX, SMTP) — returns deliverability metadata, not identity.
url: https://verify-email.org/
category: email
path:
- email
bestFor: Free single-address SMTP/MX email verification (HTTPS endpoint of verify-email.org).
selectorsIn:
- email
selectorsOut:
- metadata
- domain
status: live
pricing: freemium
costNote: Free single lookups via the web form; an API and higher-volume verification are paid.
opsec: passive
opsecNote: Probes the address's mail server (MX + SMTP RCPT) from verify-email.org's infrastructure to test whether the mailbox accepts mail; no message is delivered and the subject is not notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: HTTPS variant of verify-email.org, a long-standing free SMTP email checker; verdicts are weak against catch-all/greylisting and should be treated as probabilistic. Duplicate entry of the http version.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- verify-email
- verify-an-email-address-mailtester
aliases:
- verify-email.org
tags:
- email
- email-validation
source: osint4all
lastVerified: ''
enrichment: full
---

# Verify Email

> The HTTPS entry for verify-email.org — a free SMTP-level email verifier that probes the mail server to estimate whether a mailbox exists.

## When to use
You have an `email` and want to gauge whether it is real/deliverable before pivoting on it. Returns deliverability `metadata` and `domain` (MX) info — not a `name`, `phone`, or `social-profile`. This is the same service as the HTTP entry [[verify-email]]; prefer this HTTPS URL.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `https://verify-email.org/`.
2. Enter the email and submit the check.
3. Read the verdict: format ok?, MX found?, mailbox accepted by SMTP?
4. Pivot: a deliverable address is worth running through reverse-lookup/breach tools ([[venacus]], [[thatsthem]]); a dead one is a dead end.

## Inputs → Outputs
- **In:** `email`
- **Out:** `metadata` (validity/deliverability), `domain` (MX)
- **Empty/negative result looks like:** "invalid"/"no MX", or an "accept-all/unknown" verdict that does not confirm the specific mailbox.

## Gotchas & OpSec
- SMTP verdicts are unreliable against catch-all and greylisting servers — "exists" can be a false positive.
- Free web form rate-limits; the API requires signup (hence freemium).
- OpSec: passive; the probe originates from the service, not you, and no mail is sent.

## Overlaps ("do both")
- Duplicate of [[verify-email]] (HTTP URL); also overlaps [[verify-an-email-address-mailtester]] — cross-check when the verdict matters.

## Trust & verifiability
`trust: community` — a known free verifier; reliable as a quick gate but confirm the specific mailbox another way before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | verify-email-2 |
| category | email |
| selectorsIn → selectorsOut | email → metadata, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
