---
id: facebook-messenger-app-mobile-android
name: Facebook Messenger App (Mobile – Android)
description: Use when you have a `social-profile` on Facebook and want activity/presence signals — Meta's Messenger app shows active status, last-active, and read receipts.
url: https://play.google.com/store/apps/details?id=com.facebook.orca&hl=en
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Reading Facebook presence signals (active-now, last-active, read receipts) for a known Facebook account.
selectorsIn:
- social-profile
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Meta app; requires a Facebook/Messenger account to use.
opsec: active
opsecNote: Messenger is inherently active — viewing a profile, appearing online, and especially sending a message are all visible to the target, and read receipts run both ways. Use a fully built sock-puppet Facebook account, disable your own active status, and never message from an attributable identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: First-party Meta application; the presence data it shows is authoritative for that account, though users can disable active status, so absence of a signal proves nothing.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Facebook Messenger
- Messenger Android
tags:
- add-ons-apps-extensions
- social-media
- facebook
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Facebook Messenger App (Mobile – Android)

> Meta's Messenger app, used as a presence sensor: for a known Facebook `social-profile`, it can reveal active-now/last-active status and read receipts.

## When to use
You already have a subject's Facebook account and want low-level activity signals — is the account still in use, roughly when was it last active, does a message get read. Useful for confirming an account is live and a person reachable, in support of (not as the core of) a persons investigation. It does not *find* accounts; you must already have one.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Messenger on an Android device/emulator and log in with a **sock-puppet** Facebook account (well-aged, with friends/history).
2. In your own privacy settings, turn OFF active status so you don't broadcast your presence.
3. Locate the subject's account in Messenger.
4. Observe presence: an "active now" dot or "active Xm ago" timestamp, if they haven't hidden it.
5. Only send a message if the investigation genuinely warrants contact — that's overt and leaves a record with the target.

## Inputs → Outputs
- **In:** a known Facebook `social-profile` (or `name` to locate it)
- **Out:** presence signals (active-now/last-active), read receipts, confirmation the account is live
- **Empty/negative result looks like:** no presence shown — the user disabled active status or hasn't been on; this is not proof of inactivity, only that the signal is hidden.

## Gotchas & OpSec
- **Active and overt:** presence visibility is mutual, and messaging is a direct, attributable contact with the subject. Sock-puppet only; message only when justified.
- Users routinely turn off active status, so absent signals mean little.
- Requires a maintained fake account; thin new accounts get flagged and reveal little.

## Overlaps ("do both")
- Pairs with Facebook profile/graph search tools that *find* and enumerate the account — Messenger only adds the live presence layer on top of an account you already have.

## Trust & verifiability
`trust: trusted` — first-party Meta app, so the presence data is genuine; just remember it's easily suppressed by the user and that using it is a visible action, not a passive read.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-messenger-app-mobile-android |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | social-profile, name → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
