---
id: verify-an-email-address-mailtester
name: Verify an email address - Mailtester
description: Use when you have an email and want a fast free SMTP/MX deliverability check to see if the mailbox likely exists — returns validity/deliverability metadata, not identity.
url: http://www.mailtester.com
category: email
path:
- email
bestFor: Free single-address SMTP verification (syntax, MX, mailbox-exists probe).
selectorsIn:
- email
selectorsOut:
- metadata
- domain
status: live
pricing: free
costNote: Classic free single-lookup web checker; bulk/commercial verification is a separate paid product (mailtester.ninja / vendors).
opsec: passive
opsecNote: Connects to the address's mail server to probe whether the mailbox accepts mail, from Mailtester's infrastructure; the subject is not notified. No mail is actually delivered.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Mailtester is a long-standing free email-verification site; its SMTP verdicts are weak against catch-all/greylisting servers, so treat results as probabilistic.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- verify-email
- validateemailaddress-org
aliases:
- Mailtester
- mailtester.com
tags:
- email
- email-validation
source: metaosint
lastVerified: ''
enrichment: full
---

# Verify an email address - Mailtester

> A classic free SMTP-level email verifier: enter an address and it probes the mail server to estimate whether the mailbox exists.

## When to use
You have an `email` from another source and want to gauge whether it is real/deliverable before pivoting on it. It returns deliverability `metadata` and `domain` (MX) info — never a `name`, `phone`, or `social-profile` (the seed's outputs for those are incorrect).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `http://www.mailtester.com`.
2. Enter the email address and run the check.
3. Read the verdict: format ok?, MX found?, server accepts the mailbox?
4. Pivot: a deliverable address is worth running through reverse-lookup/breach tools ([[venacus]], [[thatsthem]]); a dead one is a dead end.

## Inputs → Outputs
- **In:** `email`
- **Out:** `metadata` (validity/deliverability), `domain` (MX)
- **Empty/negative result looks like:** "invalid"/"no MX", or an "accept-all/unknown" verdict that does not confirm the specific mailbox.

## Gotchas & OpSec
- SMTP verdicts are unreliable against catch-all and greylisting servers — "exists" can be a false positive.
- Free site; can rate-limit on repeated checks.
- OpSec: passive; the probe originates from Mailtester, not you, and no mail is sent.

## Overlaps ("do both")
- Same job as [[verify-email]] and [[validateemailaddress-org]]; cross-check with one when the verdict is load-bearing.

## Trust & verifiability
`trust: community` — a well-known free verifier; reliable as a quick gate but verify the specific mailbox another way before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | verify-an-email-address-mailtester |
| category | email |
| selectorsIn → selectorsOut | email → metadata, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
