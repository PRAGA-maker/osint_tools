---
id: account-live-com
name: account.live.com
description: Use when you have an `email` and want to confirm whether it is a registered Microsoft/Outlook/Hotmail account — returns account existence plus partial recovery hints.
url: https://account.live.com/resetpassword.aspx
category: email
path:
- email
bestFor: Confirming whether an email/phone is tied to a live Microsoft (Outlook/Hotmail/Live) account.
selectorsIn:
- email
- phone
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free Microsoft service; no account or payment needed to start the recovery flow.
opsec: active
opsecNote: This touches Microsoft's auth infrastructure for the target's address. Microsoft may log the attempt and, if you proceed, may send a security alert to the account owner. Stop at the existence check; do NOT request or enter recovery codes. Use a sock-puppet browser/IP.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Microsoft; this is the genuine account-recovery endpoint, not a third-party scraper.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- app-profiler-me
- behindtheemail-com
aliases:
- Microsoft account recovery
- account.live.com password reset
tags:
- hackedaccounts
- Hacked / Breached Account Sites
- account-existence
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# account.live.com

> Microsoft's own password-recovery flow, used as an account-existence oracle: does this email/phone belong to a Microsoft account?

## When to use
You have an `email` (or `phone`) and need to know whether the subject has a Microsoft/Outlook/Hotmail/Live identity worth pivoting on. A positive result tells you a Microsoft ecosystem account exists (Outlook mail, Skype, Xbox, OneDrive), which can corroborate that an address is real and in active use.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://account.live.com/resetpassword.aspx in a clean/sock-puppet browser session.
2. Enter the target `email` (or `phone`) at the "recover your account" prompt and submit.
3. Read the response:
   - If Microsoft asks "where should we send a code" and shows a masked recovery email/phone (e.g. `j****@gmail.com`, `+** *** ** 89`), the account EXISTS — and those masks are pivotable hints toward a secondary address/number.
   - If it says the account doesn't exist / "we couldn't find an account," the address is not a Microsoft account.
4. STOP here. Do not request, receive, or enter a verification code — that would alert the owner and is intrusive.
5. Pivot: a masked recovery contact feeds phone-OSINT or another email lookup; a confirmed account feeds `[[app-profiler-me]]` / `[[behindtheemail-com]]`.

## Inputs → Outputs
- **In:** `email` or `phone`
- **Out:** account-exists boolean, masked secondary recovery `email`/`phone` hints
- **Empty/negative result looks like:** "We couldn't find an account with that username" — treat as not-a-Microsoft-account, not as proof the person has no email.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA frequently appears; solve it manually.
- OpSec: this is **active** — you are querying Microsoft about the target's address. Proceeding past the existence check sends a real security notification to the owner. Never advance the actual reset.
- Masks are deliberately partial; treat the revealed characters as leads, not confirmed values.

## Overlaps ("do both")
- Pairs with `[[app-profiler-me]]` and `[[behindtheemail-com]]` — those enrich an email into profiles, while this only confirms Microsoft-account existence and leaks masked recovery contacts.

## Trust & verifiability
`trust: trusted` — it is Microsoft's first-party recovery page, so the existence signal is authoritative (no third-party data quality risk).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | account-live-com |
| category | email |
| selectorsIn → selectorsOut | email, phone → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
