---
id: ok-ru
name: ok.ru (Odnoklassniki account-existence check)
description: Use when you have an `email`/`phone` or `username` and want to confirm whether it maps to an Odnoklassniki (OK.ru) account — the recovery flow returns account existence plus masked recovery hints.
url: https://ok.ru/dk?st.cmd=anonymRecoveryStart
category: username
path:
- username
bestFor: Confirming whether an email/phone/login belongs to a live Odnoklassniki (OK.ru) account and leaking masked recovery contacts.
selectorsIn:
- email
- phone
- username
selectorsOut:
- social-profile
- phone
- email
status: live
pricing: free
costNote: Free Russian social-network recovery flow; no account or payment needed to run the existence check.
opsec: active
opsecNote: This touches OK.ru's auth infrastructure for the target's identifier. OK.ru (a Russian, VK-group platform) may log the attempt and could notify the account owner if you proceed. Stop at the existence check; never request or enter a recovery code. Use a sock-puppet browser/IP and assume Russian-jurisdiction logging.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: This is Odnoklassniki's own first-party account-recovery endpoint, so the existence signal is authoritative; it is not a third-party scraper.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Odnoklassniki
- OK.ru account recovery
- ok.ru password reset
tags:
- passwordreset
- Password Reset Details
- account-existence
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# ok.ru (Odnoklassniki account-existence check)

> Odnoklassniki's own password-recovery flow used as an account-existence oracle: does this email/phone/login belong to an OK.ru account, and what masked recovery contact does it leak?

## When to use
You have an `email`, `phone`, or OK.ru `username`/login and need to know whether the subject has an Odnoklassniki identity worth pivoting on. OK.ru is a major Russian/CIS social network, so a positive result is a strong lead when a subject has a Russian-speaking or post-Soviet connection. The recovery flow confirms the account exists and often reveals a masked secondary recovery `email`/`phone`, which is itself pivotable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ok.ru/dk?st.cmd=anonymRecoveryStart in a clean/sock-puppet browser session (ideally with an appropriate exit IP).
2. Enter the target `email`, `phone`, or profile login at the "recover access" prompt and submit.
3. Read the response:
   - If OK.ru proceeds to a "where to send the code" step showing a masked recovery `email`/`phone` (e.g. `j***@mail.ru`, `+7 *** *** ** 89`), the account EXISTS and those masks are leads toward a secondary address/number.
   - If it says no account matches, the identifier is not tied to an OK.ru account.
4. STOP here. Do not request, receive, or enter a verification code — that alerts the owner and is intrusive.
5. Pivot: a confirmed account feeds OK.ru profile search and cross-platform username tooling; a masked recovery contact feeds phone/email OSINT.

## Inputs → Outputs
- **In:** `email`, `phone`, or `username`/login
- **Out:** account-exists boolean, masked secondary recovery `email`/`phone` hints, `social-profile` confirmation
- **Empty/negative result looks like:** "we couldn't find your profile" (or Russian equivalent) — treat as not-an-OK.ru-account, not proof the person has no online presence.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA commonly appears; solve it manually. The interface may be in Russian.
- OpSec: this is **active** — you are querying a Russian platform about the target's identifier, and proceeding past the existence check sends a real recovery notification to the owner. Never advance the actual reset; assume the query is logged under Russian jurisdiction.
- Masks are deliberately partial; treat revealed characters as leads, not confirmed values.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` — same account-existence-oracle technique on a different provider; run both (and other providers') recovery checks against an email to map which ecosystems a subject uses.

## Trust & verifiability
`trust: trusted` — it is Odnoklassniki's first-party recovery page, so the existence signal is authoritative with no third-party data-quality risk; only the masked hints are intentionally partial.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ok-ru |
| category | username |
| selectorsIn → selectorsOut | email, phone, username → social-profile, phone, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
