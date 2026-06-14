---
id: briteverify-email-verification
name: BriteVerify Email Verification
description: Use when you have an email address and want to confirm it is real/deliverable (mailbox exists, domain valid) — returns a deliverability verdict, not personal data about the owner.
url: http://www.briteverify.co.uk
category: email
path:
- email
bestFor: Validating whether an email address is live and deliverable before pivoting on it.
selectorsIn:
- email
selectorsOut:
- email
status: degraded
pricing: freemium
costNote: BriteVerify (a Validity product) is a paid bulk email-verification service; small free checks may exist. The listed .co.uk host may be a stale/parked mirror.
opsec: passive
opsecNote: Verification probes the mail provider, not the subject. SMTP-level checks can register on the receiving mail server but do not notify the address owner.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Real product is briteverify.com (Validity). The harvested .co.uk URL is not the canonical domain and may be defunct; verify before use.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- BriteVerify
- Validity BriteVerify
tags:
- email
- email-verification
source: metaosint
lastVerified: ''
enrichment: full
---

# BriteVerify Email Verification

> A commercial email-deliverability checker (now part of Validity) that tells you whether an address is valid and reachable — it validates, it does not enrich identity.

## When to use
You have a candidate `email` for a missing person or associate and need to know whether it is still a live mailbox before spending effort on it (e.g. deciding whether a recovery-email guess is worth pivoting on). It confirms existence/deliverability; it does **not** return the owner's name, accounts, or location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use the canonical product at briteverify.com / Validity (the harvested .co.uk URL appears stale — verify it resolves first).
2. Create/sign in to an account; single or bulk-upload the `email`(s) to verify.
3. Read the verdict: valid / invalid / accept-all (catch-all) / unknown.
4. Pivot: a "valid" address is worth running through breach and account-discovery tools; "invalid" lets you discard a dead lead.

## Inputs → Outputs
- **In:** `email`
- **Out:** deliverability status for that `email` (valid/invalid/catch-all/unknown) — no personal identity data
- **Empty/negative result looks like:** "invalid"/"undeliverable," or "catch-all" meaning the domain accepts anything and existence can't be confirmed.

## Gotchas & OpSec
- Scope mismatch: harvested as a "person search / email" tool, but it is a *deliverability validator*. Do not expect name/social output.
- Canonical domain is briteverify.com (Validity); the listed .co.uk host is unverified and likely defunct — status set to degraded.
- Human-in-the-loop: account login and a paywall for any volume.
- OpSec: passive toward the subject; SMTP checks touch the mail provider, not the person.

## Overlaps ("do both")
- Use a free disposable/validity check like `[[disposable-email-address-dea-detector]]` first to filter junk, then BriteVerify only on addresses worth confirming.

## Trust & verifiability
`trust: unverified` — the real service is reputable, but the harvested URL is non-canonical and possibly dead. Confirm the live endpoint before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | briteverify-email-verification |
| category | email |
| selectorsIn → selectorsOut | email → email (deliverability) |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
