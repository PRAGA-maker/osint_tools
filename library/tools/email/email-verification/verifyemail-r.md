---
id: verifyemail-r
name: VerifyEmail (R$)
description: Use when you need to verify whether an email address is deliverable (single or in bulk) — returns a deliverability state plus signals like disposable/role/free/accept-all.
url: https://emailable.com/
category: email
path:
- email
- email-verification
bestFor: Commercial-grade single and bulk email deliverability verification with rich per-address flags.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: freemium
costNote: A small free credit allotment on signup; sustained single/bulk verification and API access are paid (credit-based). The "(R$)" in the name flags it as a paid/credits service.
opsec: active
opsecNote: Verification performs live MX/SMTP probing against the target's mail provider. It does not email the person but does touch their mail server.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Emailable is an established commercial email-verification vendor; reliable as a deliverability utility, not a curated investigative source.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Emailable
- emailable.com
tags:
- email
- verification
source: arf-seed
lastVerified: ''
enrichment: full
---

# VerifyEmail (R$)

> Emailable — a paid email-verification service that confirms whether an `email` is deliverable and returns useful flags (disposable, role-based, free provider, accept-all), single or in bulk.

## When to use
You hold one or many candidate `email` addresses (breach data, scraped profiles, pattern guesses) and need a higher-confidence deliverability verdict than a quick free checker gives. Use it especially when you have a list to triage in bulk, or when you want the extra flags — "disposable" tells you a throwaway address (weak identity link), "role" (info@, admin@) tells you it's not a personal mailbox, "free" tells you it's a consumer provider worth username-pivoting.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at https://emailable.com/ (account required; uses credits).
2. For one address, paste the `email` into the single-verify box. For many, upload a list (CSV) for bulk verification.
3. Read each result's state — `deliverable`, `undeliverable`, `risky`, or `unknown` — plus the boolean flags (disposable, role, free, accept_all).
4. Pivot: keep `deliverable` addresses; treat `risky`/accept-all as unconfirmed. For API automation, use the API key with a script. Feed surviving local-parts into username/people search.

## Inputs → Outputs
- **In:** `email` (single or bulk list)
- **Out:** `email` (a deliverability state + quality flags per address)
- **Empty/negative result looks like:** `undeliverable` (mailbox does not exist) or `unknown`/`accept_all` where the provider accepts everything and existence cannot be confirmed.

## Gotchas & OpSec
- Human-in-the-loop: account signup and credit purchase are required beyond the small free allotment; the name's "(R$)" marks it as a paid service.
- Accept-all/catch-all domains and greylisting produce `risky`/`unknown` rather than a clean yes — do not over-read these.
- OpSec: **active** — it probes the target's mail server via SMTP. No message is sent to the person, but the provider sees verification traffic. Use sock infrastructure if you care about your verification footprint.

## Overlaps ("do both")
- Pairs with `[[verify-email-address]]` (email-checker.net) — use the free checker for one-off triage and Emailable for bulk/high-confidence work; cross-checking reduces false "valid" on catch-all domains.

## Trust & verifiability
`trust: community` — a reputable commercial verification vendor. Accurate as a deliverability tool; it is not an OSINT data source and returns no identity info beyond the address state and flags.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | verifyemail-r |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | freemium (paid credits) |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
