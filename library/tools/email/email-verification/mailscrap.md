---
id: mailscrap
name: MailScrap
description: Use when you have an email address and want to verify it exists / is deliverable and flag disposable or role addresses — returns validation status without sending mail.
url: https://mailscrap.com/
category: email
path:
- email
- email-verification
bestFor: Email validation, list cleaning, and disposable-email detection.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: freemium
costNote: Free tier with limited checks; paid plans for bulk verification and API access.
opsec: passive
opsecNote: Verification uses DNS/MX checks and SMTP RCPT probes without delivering a message, so the target mailbox owner is not notified. The probe does touch the receiving mail server, which logs it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Hosted email-verification service (mailscrap.com); functionally similar to many validators. Vendor accuracy claims not independently tested.
missingPersonsRelevance: high
coverage: []
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- mailtester
- mxtoolbox
aliases: []
tags:
- email-verification
source: arf-seed
lastVerified: ''
enrichment: full
---

# MailScrap

> Hosted email-verification service — checks whether an address is deliverable and flags disposable/role accounts, without sending a message.

## When to use
You have an `email` (e.g. a guessed permutation or an address found in a breach/profile) and need to know whether it is real and reachable before acting on it. Good for triaging which of several candidate addresses for a subject actually exist.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to mailscrap.com and enter the candidate `email` (single check) or upload a list.
2. Read the result: valid / invalid / risky, plus flags like disposable, role-based, or catch-all domain.
3. For bulk or automated triage, use the API tier instead of the web form.
4. Pivot: a "valid" address feeds breach-check (`[[monitor-firefox-com]]`) and permutation confirmation; "catch-all" means the result is inconclusive.

## Inputs → Outputs
- **In:** `email`
- **Out:** deliverability/validation status for that `email` (valid/invalid/risky, disposable/role flags)
- **Empty/negative result looks like:** "invalid" (mailbox rejected) or "catch-all/unknown" (domain accepts everything, so existence can't be confirmed). Catch-all domains defeat verification — note this clearly.

## Gotchas & OpSec
- Catch-all and greylisting domains return "unknown" or false "valid"; never treat a single validator's pass as proof the person owns/uses the address.
- SMTP probes hit the receiving server, which logs the connection; some providers rate-limit or block validators.
- Cross-check with a second validator (`[[mailtester]]`) before drawing conclusions.

## Trust & verifiability
`trust: unverified` — standard hosted validator with no independent accuracy benchmark; treat results as a signal, not proof. Behavior described from category and common validator mechanics.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mailscrap |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
