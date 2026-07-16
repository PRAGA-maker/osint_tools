---
id: email-verifier
name: Hunter Email Verifier
description: Use when you have an `email` and want to know whether it is a real, deliverable mailbox before acting on it — returns a validity/deliverability verdict and confidence score.
url: https://hunter.io/email-verifier
category: email
path:
- email
bestFor: Confirming an email address is deliverable (format, domain/MX, SMTP, disposable/spam-trap checks) before treating it as a live selector.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: freemium
costNote: Single verifications are free with no signup. A free account allows ~50-100 verifications/month; bulk verification and API access require registration and paid tiers for volume.
opsec: passive
opsecNote: Verification is server-side against mail infrastructure and does NOT send a visible email to the target, so it is passive from the subject's view. Note Hunter itself sees every address you check — use it for triage, not for addresses you must keep confidential from a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hunter.io is a well-established, widely used email-intelligence company; the verifier is a mainstream, reputable service.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Hunter.io Email Verifier
- Hunter email checker
tags:
- email
- email-verification
- deliverability
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- hunter
- hunter-io
---

# Hunter Email Verifier

> Hunter.io's free single-address checker — tells you whether an email is real and deliverable before you build an investigation on it.

## When to use
You have an `email` (from a breach, a form, a guess, a pattern like `first.last@company.com`) and need to know whether it is a live, deliverable mailbox. A "valid/deliverable" verdict says the address is worth pivoting on; "invalid" or "does not exist" saves you from chasing a dead selector. Use it as the triage step right after you obtain any email and before you feed it into account-existence tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://hunter.io/email-verifier.
2. Paste the single `email` address and submit (no signup for one-off checks).
3. Read the verdict: `valid`, `invalid`, `accept-all` (catch-all domain — can't be sure), `disposable`, `unknown`, plus a confidence score and the checks that ran (format, MX/domain, SMTP).
4. For many addresses at once, register and use bulk upload or the API (paid at volume).
5. Pivot: a valid address feeds `[[account-live-com]]`, `[[holehe]]`/`[[palenath]]` and breach-search tools; an `accept-all` result means verify existence another way.

## Inputs → Outputs
- **In:** `email`
- **Out:** deliverability verdict + confidence score for the same `email` (valid / invalid / accept-all / disposable / unknown)
- **Empty/negative result looks like:** `invalid` or "we couldn't verify" — treat invalid as a dead mailbox; treat `accept-all`/`unknown` as inconclusive (the domain accepts anything), not as confirmation.

## Gotchas & OpSec
- `accept-all` (catch-all) domains return a soft result — the address may still not exist; corroborate with an account-existence oracle.
- Free tier is capped; heavy verification needs a paid plan or the API.
- OpSec: passive — no email is sent to the subject. But Hunter logs every address you submit, so don't paste addresses that must stay private from a service provider.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` — the verifier says the mailbox is deliverable, account.live.com says whether it is a Microsoft identity worth pivoting on.
- Pairs with `[[palenath]]`/Holehe — verify the address is live, then enumerate which sites it is registered on.

## Trust & verifiability
`trust: trusted` — Hunter.io is a mainstream, reputable email-intelligence provider; the SMTP/MX verdict is technically sound, with `accept-all` being the honest "can't tell" case rather than a false positive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-verifier |
