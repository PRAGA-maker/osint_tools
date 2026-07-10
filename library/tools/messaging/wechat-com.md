---
id: wechat-com
name: WeChat
description: Use when you have a `phone` or WeChat ID (`username`) and want to confirm it maps to a WeChat account and view its public profile — returns social-profile existence and display data.
url: http://www.wechat.com/en/
category: messaging
path:
- messaging
bestFor: Confirming a phone/WeChat-ID maps to a live WeChat account and reading its public profile card.
selectorsIn:
- phone
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free app. There is no public web search; account/ID lookup happens inside the WeChat mobile/desktop app after login.
opsec: active
opsecNote: You must be logged into a WeChat account to search a phone/ID, and searching or adding a contact can generate a friend request or be visible to the target. WeChat (Tencent) is subject to Chinese data law and heavy logging. Use a dedicated sock-puppet account and number; never your own.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: WeChat is Tencent's first-party platform; account existence and profile data are authoritative, though user-set names/photos are self-asserted.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- telegram
- whatsapp
aliases:
- wechat.com
- Weixin
tags:
- messengerapps
- Messenger Apps
- china
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# WeChat

> Tencent's dominant Chinese messaging super-app — usable as a phone/ID existence oracle: does this number or WeChat ID belong to a live account, and what does its public card show?

## When to use
You have a `phone` number or a WeChat ID (`username`) for a subject with China/CIS/diaspora ties and want to confirm they are on WeChat and pull their public profile card (display name, avatar, region, signature). The website wechat.com is only a download/marketing page — the actual lookup is done inside the app.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install WeChat and sign in with a **sock-puppet** account (dedicated number, not your own).
2. Use "Add Contacts" → search by the target's phone number or WeChat ID.
3. If an account exists, WeChat shows a profile card: display name, avatar, and often region and a personal signature. STOP at viewing — do NOT send the friend request, which notifies the target.
4. Pivot: the avatar feeds reverse-image/face search; the region narrows geolocation; the display name feeds name searches.

## Inputs → Outputs
- **In:** `phone` or `username` (WeChat ID)
- **Out:** `social-profile` (account exists + public card: name, avatar, region, signature)
- **Empty/negative result looks like:** "user does not exist" / no result means the number/ID isn't a WeChat account (or privacy settings block phone lookup) — not proof the person has no messaging presence.

## Gotchas & OpSec
- Human-in-the-loop: requires a logged-in app; there is no anonymous web search.
- OpSec: **active** — searching happens under your account; sending the add request alerts the target. Sock-puppet only.
- Privacy settings: many users disable "find me by phone number," so a negative is not conclusive.

## Overlaps ("do both")
- Pairs with `[[telegram]]` and `[[whatsapp]]` — run the same phone number across all three; coverage of a person's messaging footprint differs by region and app.

## Trust & verifiability
`trust: trusted` — first-party Tencent platform, so a positive existence signal is authoritative; the caveat is operational risk (login + potential alerting) and self-asserted profile fields.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wechat-com |
| category | messaging |
| selectorsIn → selectorsOut | phone, username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
