---
id: telegram-finder
name: Telegram Finder
description: Use when you have a `phone` number (or email) and want to find the linked Telegram account — returns the Telegram profile/username where the number is publicly visible.
url: https://www.telegram-finder.io/
category: messaging
path:
- messaging
bestFor: Resolving a phone number to a Telegram user when that user has left their number publicly visible.
selectorsIn:
- phone
- email
selectorsOut:
- social-profile
- username
- name
status: live
pricing: freemium
costNote: Free tier allows ~2 Telegram lookups per day by phone; email/LinkedIn enrichment and higher volume require a paid plan (from ~€29.90/month).
opsec: passive
opsecNote: The service performs the Telegram lookup on its own infrastructure, so you are not adding the target as a contact yourself. Still, you disclose the target's number to a third-party enrichment vendor — use a sock-puppet account and treat the vendor as able to log your queries.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: A contact-enrichment vendor; it can only surface users who left their phone number visible to everyone in Telegram, so a null result is common and not conclusive.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- numberingplans-com
- telegram-finder-telegram-finder-io
aliases:
- telegram-finder.io
tags:
- telegram
- phone-to-social
- messaging
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Telegram Finder

> A contact-enrichment service that resolves a phone number (or, on paid tiers, an email/LinkedIn) to the linked Telegram account — when the user has left their number publicly visible.

## When to use
You have a `phone` number and want to know if it maps to a Telegram user, and if so which profile/username/name. This is a strong pivot in missing-persons and messaging OSINT because Telegram is widely used and a resolved profile can reveal a username, display name, photo and activity. The key constraint: it only finds users whose Telegram privacy leaves the phone number visible to *everyone*, so it catches the less privacy-conscious subset.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.telegram-finder.io/ and enter the target `phone` in full international format.
2. Run the free lookup (limited to ~2/day) and read the result: linked Telegram username, display name, and profile if the number is publicly visible.
3. For email/LinkedIn-based enrichment or more than a couple of checks, a paid plan is required.
4. Pivot: a returned Telegram `username` feeds username enumeration and Telegram-specific investigation; cross-check the `phone` type first with `[[numberingplans-com]]`.

## Inputs → Outputs
- **In:** `phone` (free) or `email` (paid)
- **Out:** linked `social-profile` (Telegram), `username`, `name`
- **Empty/negative result looks like:** "no user found" — which usually means the person hid their number in Telegram privacy settings, not that they lack Telegram; treat a null as inconclusive.

## Gotchas & OpSec
- Only finds users with **publicly visible** numbers — a huge blind spot for privacy-aware targets, so absence proves nothing.
- Free tier is rate-limited (~2/day); plan your queries.
- OpSec: passive toward the target, but you hand their number to a third-party vendor — use a sock-puppet account and assume queries are logged.

## Overlaps ("do both")
- Pairs with `[[numberingplans-com]]` — classify the number's country/type before spending a limited daily lookup, and use the result to decide whether a Telegram hit is plausible.

## Trust & verifiability
`trust: community` — a functional enrichment vendor, but coverage is limited to publicly-visible numbers and results are only as fresh as their data; confirm any resolved profile directly in Telegram before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-finder |
| category | messaging |
| selectorsIn → selectorsOut | phone, email → social-profile, username, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
</content>
