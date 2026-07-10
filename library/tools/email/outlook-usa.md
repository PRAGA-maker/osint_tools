---
id: outlook-usa
name: Outlook (USA)
description: Use when you have an `email` and want to confirm whether it is a live Microsoft/Outlook account — the login.live.com sign-in flow acts as an account-existence oracle.
url: https://login.live.com
category: email
path:
- email
bestFor: Confirming whether an email address is a registered Microsoft/Outlook/Live account via the sign-in flow.
selectorsIn:
- email
selectorsOut:
- email
- social-profile
status: live
pricing: free
costNote: Free Microsoft sign-in page; no account or payment needed to run the existence check by entering an address.
opsec: active
opsecNote: You are entering the target's address into Microsoft's live auth system. Stop at the existence signal — do NOT proceed to password entry, account recovery, or code requests, which can alert the owner. Run logged out from a sock-puppet browser/IP; expect a CAPTCHA on repeat attempts.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Microsoft sign-in endpoint; the exists / doesn't-exist response is authoritative, not third-party scraped data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- account-live-com
- app-profiler-me
aliases:
- Outlook login
- login.live.com
- Microsoft account existence check
tags:
- toddington
- curated-directory
- email-addresses
- account-existence
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Outlook (USA)

> Microsoft's sign-in page (login.live.com) used as an account-existence oracle: does this email belong to a live Microsoft/Outlook/Live account?

## When to use
You have an `email` and need to know whether it maps to a Microsoft identity (Outlook/Hotmail/Live mail, Skype, Xbox, OneDrive) worth pivoting on. Microsoft's login flow reveals whether an address is registered before it ever asks for a password, so it works as a quick existence check that corroborates an address is real and in use.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://login.live.com **logged out**, in a clean/sock-puppet browser.
2. Enter the target `email` and continue.
3. Read the response:
   - It advances to a password prompt → the account EXISTS.
   - It says "That Microsoft account doesn't exist. Enter a different account…" → not a Microsoft account.
4. STOP. Do not enter a password, request a code, or start recovery — that risks alerting the owner.
5. Pivot: a confirmed account feeds `[[account-live-com]]` (recovery flow, which also leaks masked secondary email/phone hints) and `[[app-profiler-me]]`.

## Inputs → Outputs
- **In:** `email`
- **Out:** account-exists boolean; confirms a Microsoft-ecosystem `social-profile`/identity behind the `email`
- **Empty/negative result looks like:** "That Microsoft account doesn't exist" — treat as not-a-Microsoft-account, not as proof the address is dead.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA commonly appears, especially on repeated checks — solve it manually and pace queries.
- OpSec: **active** — you query Microsoft about the target's address. Never advance past the existence step into password/recovery, which can notify the owner.
- This is the same signal as the dedicated recovery flow; for masked recovery-contact hints use `[[account-live-com]]` instead, which exposes more.

## Overlaps ("do both")
- Near-duplicate of `[[account-live-com]]` — this confirms existence via login; that confirms existence via the recovery page AND leaks masked secondary `email`/`phone` hints. Prefer `[[account-live-com]]` when you want the extra pivots.

## Trust & verifiability
`trust: trusted` — it is Microsoft's first-party sign-in endpoint, so the existence response is authoritative with no third-party data-quality risk.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | outlook-usa |
| category | email |
| selectorsIn → selectorsOut | email → email, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
