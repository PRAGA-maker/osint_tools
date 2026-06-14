---
id: facebook-com-2
name: facebook.com
description: Use when you want to test whether an email or phone is tied to a Facebook account via the account-recovery/"hacked" flow — returns account-existence and a masked name/profile hint.
url: http://www.facebook.com/hacked
category: email
path:
- email
bestFor: Confirming Facebook account existence for an email/phone via the recovery flow.
selectorsIn:
- email
- phone
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free (Facebook's own recovery flow).
opsec: active
opsecNote: Semi-active — querying the recovery flow interacts with Facebook's auth system tied to the target's account and can, depending on settings, send the account owner a notification/recovery email. Not fully passive.
humanInLoop: true
humanInLoopReason:
- captcha
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: This is Facebook/Meta's official account-recovery endpoint; the OSINT use (existence/identity confirmation) is a technique, not a dedicated tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- facebook account recovery
- facebook hacked flow
tags:
- email
- facebook
- account-existence
- Hacked / Breached Account Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# facebook.com (recovery / "hacked" flow)

> Facebook's account-recovery endpoint, used as an OSINT technique: enter an email or phone and the flow reveals whether a Facebook account exists for it, often with a masked name and profile photo.

## When to use
You have an `email` or `phone` and want to know if it belongs to a Facebook account — and ideally glimpse the masked name/photo to confirm identity. High value in missing-persons work, since Facebook is a dominant platform and the recovery flow can tie an identifier to a real profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to facebook.com/login/identify (the "find your account" / recovery entry; facebook.com/hacked routes into the same recovery system).
2. Enter the `email` or `phone`.
3. If an account exists, Facebook shows the matching profile(s) with a masked name and (often) a profile photo before prompting for a recovery method.
4. Pivot: a confirmed `social-profile`/`name` feeds image search and people-search; STOP at confirmation — do not attempt to actually reset/recover the account.

## Inputs → Outputs
- **In:** `email`, `phone`
- **Out:** `social-profile` (account existence), `name` (masked), profile photo hint
- **Empty/negative result looks like:** "No search results" / "We couldn't find your account" — no Facebook account tied to that identifier (or privacy settings hide it).

## Gotchas & OpSec
- OpSec: semi-active — Facebook may notify the account owner of a recovery attempt and logs the request against your IP/session. Use a sock-puppet account/clean browser; never proceed past identity confirmation.
- Human-in-the-loop: CAPTCHAs and flow changes are frequent; Meta deliberately limits enumeration.
- Legal/ethical line: confirming existence is reconnaissance; attempting actual account recovery is account takeover — do not.

## Overlaps ("do both")
- Pairs with `[[holehe]]`/`[[epieos-email-tool]]` for cross-platform existence, but Facebook's own flow is the authoritative check for Facebook specifically.

## Trust & verifiability
`trust: trusted` — it is Meta's official endpoint; the data is authoritative for Facebook, though the OSINT use is a technique and Meta actively restricts enumeration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-com-2 |
| category | email |
| selectorsIn → selectorsOut | email, phone → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha, account-login) |
