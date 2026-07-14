---
id: ebay-co-uk
name: ebay.co.uk
description: Use when you have an `email` or `username` and want to confirm whether it is tied to a live eBay account — returns account existence plus masked recovery hints.
url: https://www.ebay.co.uk/pages/help/account/forgot-password.html
category: username
path:
- username
bestFor: Confirming whether an email or username belongs to a registered eBay account via the password-recovery flow.
selectorsIn:
- email
- username
selectorsOut:
- username
- phone
status: live
pricing: free
costNote: Free; eBay's own account-recovery flow, no account or payment needed to run the existence check.
opsec: active
opsecNote: This queries eBay's auth system about the target's identifier. eBay may log the attempt and can send a security notification if you advance the reset. Stop at the existence check — never request or enter a recovery code. Use a sock-puppet browser/IP.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by eBay; this is the genuine first-party account-recovery endpoint, not a third-party scraper.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- account-live-com
- paypal-com
aliases:
- eBay UK password reset
- eBay account recovery
tags:
- passwordreset
- Password Reset Details
- account-existence
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# ebay.co.uk

> eBay's password-recovery flow used as an account-existence oracle: does this email or username belong to a live eBay account?

## When to use
You have an `email` or a candidate `username` and want to know whether the subject has an eBay presence. A positive result confirms the identifier is a real, registered eBay account (implying buying/selling activity, a linked payment method, and often a shipping address history), and the recovery step can leak masked hints toward a linked phone or email.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a clean/sock-puppet browser session, open eBay's sign-in and choose "Forgot password" (from https://www.ebay.co.uk/pages/help/account/forgot-password.html follow through to the recovery flow).
2. Enter the target `email` or `username` and submit.
3. Read the response:
   - If eBay proceeds to "how do you want to receive your code" and shows a masked email/phone (e.g. `j****@gmail.com`, `••• ••• ••89`), the account EXISTS and those masks are pivot hints.
   - If it says it can't find an account matching that detail, the identifier is not a registered eBay account.
4. STOP. Do not request, receive, or enter a verification code — that alerts the owner and is intrusive.
5. Pivot: a confirmed username feeds username-enumeration tools and eBay's own feedback/profile pages; masked recovery contacts feed phone/email OSINT.

## Inputs → Outputs
- **In:** `email` or `username`
- **Out:** account-exists boolean, masked secondary recovery `phone`/email hints, a confirmed `username`
- **Empty/negative result looks like:** "we couldn't find your account" — treat as not-an-eBay-account, not as proof the person has no online presence.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA and/or interstitial commonly appears; solve it manually.
- eBay's flow and error wording change periodically; interpret the current UI, not a fixed string.
- OpSec: this is **active** — you are querying eBay about the target. Never advance the actual reset or you may notify the owner.
- Masks are deliberately partial — revealed characters are leads, not confirmed values.

## Overlaps ("do both")
- Pairs with [[account-live-com]] and [[paypal-com]] — the same existence-oracle technique across different platforms; run several to map which ecosystems an identifier is registered in.

## Trust & verifiability
`trust: trusted` — it is eBay's first-party recovery endpoint, so the existence signal is authoritative (no third-party data-quality risk); only the masked hints are partial by design.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ebay-co-uk |
| category | username |
| selectorsIn → selectorsOut | email, username → username, phone |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
