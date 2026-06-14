---
id: email-dossier
name: Email Dossier
description: Use when you have an email address and want a technical validity report — returns syntax, domain/MX records, and a live SMTP mailbox-existence probe.
url: https://centralops.net/co/emaildossier.aspx
category: email
path:
- email
bestFor: A technical email validation report with MX lookup and live SMTP mailbox verification.
selectorsIn:
- email
selectorsOut:
- metadata
- domain
- ip-address
status: live
pricing: freemium
costNote: Free interactive checks on CentralOps with daily usage limits; heavier use is gated.
opsec: active
opsecNote: The dossier opens a live SMTP conversation with the target's mail server to test the mailbox; that server can log the probe, so do not run it against an address you must not alert.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: CentralOps is a long-established free network-tools site; the mailbox probe is reliable except where servers block VRFY/RCPT or use catch-all.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CentralOps Email Dossier
tags:
- email
- validation
source: osint4all
lastVerified: ''
enrichment: full
---

# Email Dossier

> CentralOps' Email Dossier: a technical validity report that resolves the domain's MX and runs a live SMTP probe to test whether the mailbox exists.

## When to use
You have a candidate `email` and need a deeper technical verdict than syntax-only validators give — including whether the mailbox actually accepts mail. Use it to confirm the live address among guessed permutations and to capture the receiving server's `domain`/`ip-address` for further mapping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://centralops.net/co/emaildossier.aspx.
2. Enter the email address and submit.
3. Read the staged report: syntax check, MX records for the domain, the connecting mail server, and the SMTP dialogue showing whether the mailbox is accepted or rejected.
4. Pivot: a confirmed live address goes to `[[email-breach-analysis]]`; the MX `domain`/server `ip-address` can be mapped with WHOIS/IP tooling.

## Inputs → Outputs
- **In:** `email`
- **Out:** validity report and SMTP transcript (`metadata`), MX `domain`, mail server `ip-address`
- **Empty/negative result looks like:** server rejects the mailbox (likely invalid), or returns "accept-all"/blocks VRFY so existence is inconclusive — common on hardened or catch-all domains.

## Gotchas & OpSec
- Human-in-the-loop: daily free-use limits may throttle you.
- OpSec: ACTIVE — it opens a real SMTP session with the target's mailserver, which is logged on their side. Treat as touching the target's infrastructure.
- Many modern servers disable VRFY/RCPT verification, so a "could not verify" is not the same as "invalid."

## Overlaps ("do both")
- Pairs with `[[email-address-validator]]` and `[[email-address-verifier]]` — cross-check, since servers that block this probe may still be graded by another engine.

## Trust & verifiability
`trust: community` — well-established free network-tools provider; technical output is dependable within SMTP probing's inherent limits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-dossier |
| category | email |
| selectorsIn → selectorsOut | email → metadata, domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
