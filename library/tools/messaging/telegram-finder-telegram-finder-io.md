---
id: telegram-finder-telegram-finder-io
name: Telegram Finder (telegram-finder.io)
description: Use when you have a `phone`, `email` or LinkedIn `social-profile` and want to find the matching Telegram account — returns the linked Telegram social-profile and basic account info.
url: https://telegram-finder.io
category: messaging
path:
- messaging
bestFor: Contact enrichment — resolving a phone/email/LinkedIn to a Telegram account and username.
selectorsIn:
- phone
- email
- social-profile
selectorsOut:
- social-profile
- username
- associate
status: live
pricing: freemium
costNote: Free tier gives 2 phone-based lookups per day with basic info. Premium is ~$29.90/month (100 hourly lookups plus email/LinkedIn enrichment, 30 monthly credits); failed enrichments don't consume credits, successful reverse lookups do.
opsec: active
opsecNote: You are submitting the target's phone/email to a third-party enrichment service that logs and monetises queries. The subject is not notified, but the query is tied to your session/account and the operator sees what you look up. Use a research account and never enrich identifiers you are not authorised to investigate.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial contact-enrichment service of unknown provenance; results are probabilistic matches from aggregated data, so a returned account is a lead to confirm, not proof of ownership.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
aliases:
- telegram-finder.io
tags:
- telegram
- contact-enrichment
source: kimi-telegram
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- telegram-finder
---

# Telegram Finder (telegram-finder.io)

> A contact-enrichment service that reverses a phone, email or LinkedIn into the person's Telegram account — the pivot from "I have their number" to "here's their Telegram."

## When to use
You already hold a `phone`, `email`, or LinkedIn `social-profile` for the subject and want to know whether they are on Telegram and under what handle. Useful when Telegram is the subject's primary channel and you need the account to monitor activity or cross-reference group membership.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://telegram-finder.io.
2. Enter the identifier — phone number (free tier), or email/LinkedIn (premium enrichment).
3. Run the lookup; the free tier allows 2 phone lookups/day. It returns any matched Telegram account and basic profile info.
4. For email→phone / LinkedIn→phone reverse enrichment or higher volume, a paid plan is required.
5. Pivot: a resolved Telegram username feeds `[[username-to-id-bot]]` for the permanent numeric ID, then group/membership tools; the account's display name and photo feed identity confirmation and reverse-image search.

## Inputs → Outputs
- **In:** `phone`, `email`, or LinkedIn `social-profile`
- **Out:** matched Telegram `social-profile`/`username`, basic account info, possible linked `associate` contacts
- **Empty/negative result looks like:** no match returned (credit not consumed on failure) — means the enrichment set has no Telegram account tied to that identifier; the person may still be on Telegram under an unlinked number.

## Gotchas & OpSec
- **Paywall:** meaningful volume and email/LinkedIn enrichment need the ~$29.90/mo plan; the free tier is a taster.
- Matches are probabilistic from aggregated/leaked contact data — a returned account can be wrong or stale. Confirm before asserting ownership.
- OpSec: **active** — you hand the target's identifier to a third party that logs it. Use a research account; only enrich identifiers you're authorised to investigate.

## Overlaps ("do both")
- Pairs with `[[username-to-id-bot]]` — Telegram Finder gets you the account/handle, that bot pins it to a permanent numeric ID.
- Pairs with breach/enrichment tools that go the other direction (phone→email) to triangulate the same identity.

## Trust & verifiability
`trust: community` — an unvetted commercial aggregator. The Telegram account it returns is checkable (open it and compare details), but the underlying phone/email linkage is not authoritative — verify independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-finder-telegram-finder-io |
| category | messaging |
| selectorsIn → selectorsOut | phone, email, social-profile → social-profile, username, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (payment-wall-partial) |
