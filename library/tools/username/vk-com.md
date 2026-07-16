---
id: vk-com
name: VK Account Recovery (existence check)
description: Use when you have an `email`, `phone` or VK `username` and want to confirm whether it's tied to a VK account — returns account existence plus a masked recovery `phone` hint.
url: https://vk.com/restore
category: username
path:
- username
bestFor: Confirming an email/phone/handle belongs to a VK account and leaking a masked recovery phone.
selectorsIn:
- email
- phone
- username
selectorsOut:
- username
- phone
status: live
pricing: free
costNote: Free; VK's own recovery flow, no account or payment to start.
opsec: active
opsecNote: This queries VK's auth system about the target's identifier and shows a CAPTCHA; do NOT proceed past the existence/masked-hint step or VK may send the owner a security alert. Use a sock-puppet browser/IP; VK is a Russian platform, so weigh jurisdiction before touching it.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: VK's genuine first-party account-recovery endpoint — the existence signal is authoritative, not third-party scraped.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- vk.com/restore
- VKontakte password reset
tags:
- passwordreset
- Password Reset Details
- account-existence
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- community-search
- get-user-info
- item
- people-search-results-vk
- vk
- vk-com-2
- vk-community-search
- vk-people-search
---

# VK Account Recovery (existence check)

> VK's own password-recovery flow used as an account-existence oracle: does this email/phone/handle belong to a VKontakte account, and what masked recovery phone is attached?

## When to use
You have an `email`, `phone`, or VK `username` and need to know whether the subject has a VKontakte identity worth pivoting on — VK is the dominant social network across Russia and the former USSR, so a hit is high-value there. A positive result confirms the identifier is registered and often leaks a masked recovery phone as a further lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vk.com/restore in a clean/sock-puppet browser session.
2. Enter the target's `phone`, `email`, or profile URL/`username` at the "recover access" prompt and submit; solve the CAPTCHA.
3. Read the response:
   - If VK shows the account (often with a masked phone like `+7 *** *** ** 89`), the account EXISTS — the mask is a pivotable hint.
   - If it says no account/page is found, the identifier isn't registered on VK.
4. STOP here — do not request or enter a confirmation code; that alerts the owner.
5. Pivot: a confirmed profile feeds VK-specific OSINT (friends, photos, groups); a masked phone feeds phone-OSINT.

## Inputs → Outputs
- **In:** `email`, `phone`, or `username`/profile URL
- **Out:** account-exists confirmation, masked recovery `phone` hint, and the resolved profile/`username`
- **Empty/negative result looks like:** "account not found" / no page — the identifier isn't a VK account; it doesn't rule out other networks.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA is required — solve it manually.
- **Active** — you're querying VK about the target; never advance the actual reset, which notifies the owner.
- VK is Russian-operated; consider jurisdiction/attribution before interacting, and use a sock puppet.
- Masks are deliberately partial — treat revealed digits as leads, not confirmed values.

## Overlaps ("do both")
- Pairs with other account-existence oracles ([[account-live-com]], provider recovery flows) and VK profile tooling — this confirms VK existence and leaks a masked phone; profile tools then enrich the account.

## Trust & verifiability
`trust: trusted` — VK's first-party recovery page, so the existence signal is authoritative; the masked phone is a hint to corroborate, not a confirmed number.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vk-com |
| category | username |
| selectorsIn → selectorsOut | email, phone, username → username, phone |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
