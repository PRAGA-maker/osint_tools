---
id: tginfo-me
name: tginfo.me
description: Use when you're trying to resolve a `phone` or `username` on Telegram and need to understand the add-by-number technique and its privacy/rate limits — returns process knowledge, not a lookup.
url: https://tginfo.me/user-not-found-by-phone-number-en/
category: messaging
path:
- messaging
bestFor: Understanding how Telegram phone-number-to-profile discovery works and why it fails, before you attempt it.
selectorsIn:
- phone
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free reference article.
opsec: passive
opsecNote: Reading the guide is passive. The technique it describes — importing a number as a contact to reveal a Telegram profile — is ACTIVE and can alert nobody directly but is logged by Telegram and rate-limited/banned if abused; use a burner Telegram account on a dedicated number.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: tginfo.me is a community Telegram-tips site; the article accurately documents Telegram's own contact-discovery behavior, which is verifiable in the app.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Telegram user not found by phone number
tags:
- telegram
- Telegram
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# tginfo.me

> A reference that explains Telegram's phone-number-to-profile discovery — how the add-a-contact technique reveals a target's Telegram account, why it returns "user not found", and the privacy settings and rate limits that gate it.

## When to use
You have a `phone` number and want to know whether it belongs to a Telegram user — a common early step in resolving a subject who uses Telegram. Telegram has no global phone search; instead you import the number as a contact and see if a profile appears. This page tells you exactly how that works, what a null result means (privacy setting vs no account), and how to avoid the temporary bans Telegram issues for excessive lookups — so you run the technique correctly instead of getting your account throttled.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read https://tginfo.me/user-not-found-by-phone-number-en/ to understand the mechanics and failure modes.
2. On a **burner** Telegram account (dedicated SIM/number), save the target `phone` to contacts and open Telegram contacts to see if a profile surfaces.
3. If a profile appears, record the `username`, display name, photo, and "last seen" — those are your pivots. If "user not found", note it could be a privacy restriction, not an absence.
4. Pivot: a revealed username feeds Telegram channel/username searches and cross-platform handle checks.

## Inputs → Outputs
- **In:** `phone` (or `username` to reverse-check)
- **Out:** knowledge of the technique → a Telegram `social-profile`, username, photo, activity signal when applied
- **Empty/negative result looks like:** "user not found by phone number" — ambiguous by design: could mean no account, or the target restricted phone-number discovery. Do not treat it as definitive.

## Gotchas & OpSec
- The page is passive; **the lookup itself is active** — Telegram processes your contact import. Use a burner account so it isn't tied to you, and don't message the target.
- Human-in-the-loop / **rate-limit**: bulk or rapid lookups trigger temporary bans ("too many requests"); pace them.
- Privacy settings and Telegram's behavior change over time; re-verify against the current app.

## Overlaps ("do both")
- Pairs with `[[tg-me-com]]` and Telegram username/channel search tools — this explains phone→profile discovery; those help enumerate and view the channels/handles you uncover.

## Trust & verifiability
`trust: community` — a community tips site, but the described behavior is Telegram's own and directly verifiable in-app; treat the guide as accurate for mechanics while confirming specifics yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tginfo-me |
| category | messaging |
| selectorsIn → selectorsOut | phone, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
