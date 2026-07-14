---
id: fb-identify-requires-logout
name: FB Identify (Requires Logout)
description: Use when you have an `email`, `phone`, or `name` and want to confirm whether it maps to a Facebook account — returns the matched profile's name and photo (must be logged out).
url: https://www.facebook.com/login/identify
category: social-networks
path:
- social-networks
- facebook
- search
bestFor: Confirming a Facebook account exists for an email/phone and revealing the matched profile's name and photo via the account-recovery flow.
selectorsIn:
- email
- phone
- name
selectorsOut:
- name
- image
- social-profile
status: live
pricing: free
costNote: Free; uses Facebook's own "Find Your Account" recovery page, no account needed (in fact you must be logged out).
opsec: active
opsecNote: You query Facebook's recovery system about the target's identifier. Facebook logs the attempt and applies anti-abuse rate limits. Stop at the identification card — do NOT send or enter a login/reset code, which would alert the account owner. Use a sock-puppet browser/IP; repeated attempts trigger CAPTCHAs and blocks.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Facebook's first-party account-recovery endpoint; the match it returns is authoritative for account existence.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- facebook-search
- account-live-com
aliases:
- Facebook Find Your Account
- facebook.com/login/identify
tags:
- facebook
- account-existence
- account-recovery
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# FB Identify (Requires Logout)

> Facebook's "Find Your Account" recovery page used as an identity oracle: enter an email or phone and Facebook shows you the name and profile photo of the account it belongs to — but only while you're logged out.

## When to use
You have an `email`, `phone`, or `name` and want to confirm it belongs to a Facebook account and put a face and name to it. This is one of the most reliable email/phone → identity pivots available, because Facebook's recovery flow displays the matched account's real profile name and photo before asking for any verification — no login, no friend connection required.

## How to use it (`bestInteractionPattern`: web-manual)
1. **Log out of Facebook** (or use a fresh incognito/sock-puppet session) — the page behaves differently or hides the identification card when you are authenticated. This is the reason for the tool's name.
2. Go to https://www.facebook.com/login/identify.
3. Enter the target `email` or `phone` (or a `name` to browse candidate matches) and submit.
4. Read the identification card: Facebook shows the matched account's **name and profile photo** and asks how you want to reset. That card is your result.
5. STOP — do not choose a reset method or request a code (it alerts the owner). Note the name/photo and pivot: search that exact name to locate the public profile, run the photo through [[facebook-search]] or reverse-image tools.

## Inputs → Outputs
- **In:** `email`, `phone`, or `name`
- **Out:** `name` and profile `image` of the matched account, a `social-profile` lead (the account itself)
- **Empty/negative result looks like:** "No search results" / "We couldn't find your account" — the identifier isn't tied to a Facebook account (or the account has disabled recovery-by-that-identifier).

## Gotchas & OpSec
- **Must be logged out** — the single most common mistake; an authenticated session suppresses the useful card.
- Human-in-the-loop: CAPTCHAs appear quickly, and repeated queries get rate-limited/blocked — space them out from a clean session.
- OpSec: **active** — Facebook logs the attempt against your session/IP. Never advance the reset; use a sock puppet.
- Users can hide themselves from lookup-by-email/phone in privacy settings, so a negative isn't conclusive.

## Overlaps ("do both")
- Pairs with [[facebook-search]] (once you have the name/photo, find and enumerate the actual profile) and with [[account-live-com]] (same existence-oracle technique on Microsoft) to test an identifier across platforms.

## Trust & verifiability
`trust: trusted` — it is Facebook's own recovery endpoint, so a returned name/photo is an authoritative match for the identifier; only privacy-hidden accounts and anti-abuse gating limit it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fb-identify-requires-logout |
| category | social-networks |
| selectorsIn → selectorsOut | email, phone, name → name, image, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
