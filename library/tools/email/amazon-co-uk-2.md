---
id: amazon-co-uk-2
name: amazon.co.uk
description: Use when you have an `email` and want to test whether it is a registered Amazon UK account via the sign-in / account-assistance flow — returns account existence.
url: https://www.amazon.co.uk/gp/help/contact-us/account-assistance.html/280-8919602-0117510?ie=UTF8&nodeId=&type=email&skip=true#csTop
category: email
path:
- email
bestFor: Confirming whether an email is tied to a live Amazon.co.uk account.
selectorsIn:
- email
selectorsOut:
- name
status: live
pricing: free
costNote: Free Amazon help/account-assistance flow; no payment.
opsec: active
opsecNote: Probing Amazon's sign-in/recovery touches Amazon's auth infra for the target's address and can trigger a security email to the owner. Limit yourself to the existence check; never advance a password reset. Use a sock-puppet session.
humanInLoop: true
humanInLoopReason:
- captcha
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Amazon UK help/account-assistance page; not a third-party scraper.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- account-live-com
aliases:
- Amazon UK account assistance
tags:
- hackedaccounts
- Hacked / Breached Account Sites
- account-existence
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# amazon.co.uk

> Amazon UK's account-assistance/sign-in flow used as a soft existence check for an email address.

## When to use
You have an `email` and want a weak signal of whether the subject shops/has an account on Amazon.co.uk. Best used as corroboration alongside other account-existence checks (e.g. `[[account-live-com]]`), not as a standalone identifier.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Amazon UK sign-in / account-assistance page in a clean sock-puppet browser session.
2. Begin the sign-in or "I need help with my account" flow and enter the target `email`.
3. Read whether Amazon recognises the address (it advances to a password/OTP step) versus offers to create a new account / says it doesn't recognise it.
4. STOP at the recognition step — do not request or enter any code, and do not attempt a reset.
5. Pivot: a recognised account is a weak corroborating data point; combine with `[[account-live-com]]` and people-search.

## Inputs → Outputs
- **In:** `email`
- **Out:** account-exists signal (and sometimes a partially masked name on a recognised account)
- **Empty/negative result looks like:** Amazon prompts to create a new account or doesn't recognise the address — treat as "no AMZ UK account," not as identity proof.

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHA and login walls are common; Amazon actively rate-limits/throttles repeated probes.
- OpSec: this is **active** — Amazon may email the owner about a sign-in attempt. Keep to the existence check only.
- Signal is weak and noisy; Amazon's anti-enumeration measures can mask whether an account exists.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` — both are first-party account-existence oracles for different ecosystems; agreement across providers strengthens an address-attribution.

## Trust & verifiability
`trust: trusted` — genuine Amazon UK page, so the platform itself is reliable; the limitation is Amazon's deliberate anti-enumeration, not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-co-uk-2 |
| category | email |
| selectorsIn → selectorsOut | email → name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha, account-login) |
