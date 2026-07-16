---
id: mnp-bot
name: mnp_bot
description: Use when you have a `phone` number and want its geographic region and mobile carrier via a Telegram bot — returns region/operator context on the number.
url: https://t.me/mnp_bot
category: messaging
path:
- messaging
bestFor: Identifying the region and (ported) mobile operator behind a phone number via a Telegram bot.
selectorsIn:
- phone
selectorsOut:
- phone
- geolocation
status: live
pricing: free
costNote: Free region/operator lookups; no payment required for the basic result.
opsec: passive
opsecNote: Resolves number metadata (region + carrier) against numbering databases, not the subscriber, so it does not ping or alert the phone's owner. The bot operator still logs your queries — use a sock-puppet Telegram account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: An anonymous Telegram bot returning MNP (mobile number portability) region/operator data; accurate for numbering-plan lookups but the operator and data source are undocumented.
missingPersonsRelevance: high
coverage:
- ru
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- mnp_bot
- MNP bot
tags:
- telegram
- phone
- carrier-lookup
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# mnp_bot

> A Telegram bot that resolves a phone number to its region and current mobile operator — the first triage step on any unknown number.

## When to use
You have a `phone` number tied to a subject or associate and want to place it: which region/country and which mobile carrier it belongs to, accounting for number portability (MNP). Useful early in a missing-persons case to confirm a number is plausible, narrow a region, and pick the right downstream phone-OSINT tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet Telegram account, open https://t.me/mnp_bot and press Start.
2. Send the phone number in international format.
3. Read the reply: the bot returns the number's region and current operator (post-porting), which differs from the original block owner if the number was ported.
4. Pivot: use the region to focus people/address search and the operator for provider-specific follow-up; feed the number into fuller phone-OSINT (messaging-app checks, breach lookups).

## Inputs → Outputs
- **In:** `phone`
- **Out:** region/`geolocation` context and current mobile operator for the number
- **Empty/negative result looks like:** "not found" / an error for malformed or out-of-coverage numbers — the bot is strongest on Russian/CIS numbering plans; a non-covered number returns nothing useful.

## Gotchas & OpSec
- Human-in-the-loop: requires a Telegram account-login; use a sock puppet.
- Region = the numbering-plan area, not the subscriber's live location; a ported or roaming number can mislead. Treat as context, not a pin.
- Coverage is oriented to Russian/CIS numbers; results for other countries may be thin or absent.

## Overlaps ("do both")
- Pairs with messaging-app existence checks and breach-lookup tools — this classifies the number; those attach it to accounts and identities.

## Trust & verifiability
`trust: unverified` — an anonymous Telegram bot; the region/operator mapping is generally reliable numbering-plan data, but there is no accountable maintainer, so confirm anything decision-critical against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mnp-bot |
| category | messaging |
| selectorsIn → selectorsOut | phone → phone, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
