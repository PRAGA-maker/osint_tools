---
id: recover-fb-account
name: Recover FB Account (existence oracle)
description: Use when you have an `email` or `phone` and want to confirm whether it is tied to a Facebook account — returns account existence plus the masked name/photo Facebook shows on the recovery screen.
url: https://www.facebook.com/login/identify?ctx=recover
category: social-networks
path:
- social-networks
- facebook
- search
bestFor: Confirming whether an email/phone belongs to a Facebook account and reading the profile name/photo Facebook reveals during recovery.
selectorsIn:
- email
- phone
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free Facebook account-recovery flow; no account or payment needed to reach the identification step.
opsec: active
opsecNote: This queries Facebook's auth infrastructure about the target's identifier and may be logged. Facebook can show a security prompt to the account owner and CAPTCHAs to you. Stop at the identification screen; NEVER request or enter a login/reset code, which would alert the owner. Use a logged-out sock-puppet browser and clean IP.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: This is Facebook's genuine first-party account-recovery endpoint, not a third-party scraper — the existence signal is authoritative.
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
- facebook
- facebook-ad-s-link
- facebook-com
- facebook-com-2
- facebook-directory-users-by-name
- facebook-live-map
- facebook-photos-by-id
- facebook-profile-directory
- facebook-watch
- fb-email-search
- fb-identify-requires-logout
aliases:
- Facebook account recovery
- facebook.com/login/identify
- FB email/phone lookup
tags:
- facebook
- account-existence
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Recover FB Account (existence oracle)

> Facebook's own "find your account" recovery flow, used as an existence oracle: does this email/phone belong to a Facebook account — and whose?

## When to use
You have an `email` or `phone` and need to know whether the subject has a Facebook identity to pivot on. Facebook's recovery/identification page confirms whether an account is tied to that identifier and, crucially, often previews the matching profile — a `name` and profile `image` — on the confirmation screen. That preview both proves the identifier is real/in-use and links it to a specific person and photo (a strong pivot for reverse-image/face work).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.facebook.com/login/identify?ctx=recover in a **logged-out**, clean/sock-puppet browser (being logged in ties the query to you and changes the flow).
2. Enter the target `email` or `phone` and submit.
3. Read the response:
   - If Facebook shows a matching profile (name + photo) and asks how to reset, the account **EXISTS** — capture the name/photo.
   - If it says "No search results" / "We couldn't find your account," no Facebook account is tied to that identifier.
4. **STOP** at the identification screen. Do not choose a reset method, request a code, or enter one — that sends a real alert to the account owner.
5. Pivot: the revealed profile `name`/`image` feeds face/reverse-image search and profile lookup; a confirmed identifier corroborates other findings.

## Inputs → Outputs
- **In:** `email` or `phone`
- **Out:** account-exists signal plus, frequently, the matching profile `name` and photo (`image`, `social-profile`)
- **Empty/negative result looks like:** "We couldn't find your account" — treat as no-FB-account-for-this-identifier, not proof the person has no Facebook (they may use a different email/phone).

## Gotchas & OpSec
- **Human-in-the-loop:** CAPTCHAs appear frequently; solve manually. Repeated queries from one IP/session get throttled or blocked.
- **OpSec (active):** you are querying Facebook about the target. The identification step is relatively quiet, but advancing to an actual reset alerts the owner — never proceed past existence/preview.
- The preview may be partially masked or, for privacy-locked accounts, absent even when the account exists.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` (Microsoft existence oracle) and email/phone enrichment tools — run the same identifier across providers, since each confirms a different ecosystem and Facebook uniquely tends to leak a name/photo.

## Trust & verifiability
`trust: trusted` — Facebook's first-party recovery endpoint, so the existence signal and any revealed profile are authoritative (no third-party data-quality risk).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | recover-fb-account |
| category | social-networks |
| selectorsIn → selectorsOut | email, phone → social-profile, name, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
