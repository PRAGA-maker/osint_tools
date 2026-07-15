---
id: discord-sensor
name: Discord Sensor
description: Use when you have a Discord `username`/`device-id` (user ID) or server and want analytics on that user/community's activity — returns `social-profile` activity data via a Telegram bot, behind a channel-subscription gate.
url: https://telegram.me/discordsensorbot
category: messaging
path:
- messaging
bestFor: Querying Discord user/server activity and analytics from within Telegram via the @DiscordSensorbot bot.
selectorsIn:
- username
- device-id
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Menu-driven Telegram bot; core use is free but full functionality requires subscribing to the bot's linked Telegram channel (used as access control), and some "probiv" query bots in this ecosystem gate deeper data behind payment.
opsec: active
opsecNote: Interacting requires a Telegram account, which ties the query to that account's identity/number — always use a dedicated sock-puppet Telegram account on a burner number, never your real one. These pribiv/analytics bots log queries; assume the operator sees who looked up whom.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: unverified
trustNote: Anonymous Telegram bot from the Russian-language "probiv" (data-lookup) bot ecosystem; operator identity and data provenance are unknown, so treat every result as an unverified lead.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- discord-lookup
aliases:
- Discord Sensor
- DiscordSensorbot
tags:
- telegram
- discord
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Discord Sensor

> A Telegram bot that returns Discord user/server analytics on demand — part of the Russian-language "probiv" bot ecosystem, powerful for a quick pull but unattributed and unverifiable.

## When to use
Your subject has a Discord footprint — you have a `username`, a Discord user ID (`device-id`), or a server they frequent — and you want activity insight without building your own scraper: when a user is active, which channels/communities they engage with, and community-level patterns that can expose `associate` links. Because it runs entirely inside Telegram, it's a fast, low-setup pull when you're already working the messaging-platform angle. Treat everything it returns as a lead to corroborate, not fact.

## How to use it (`bestInteractionPattern`: mobile-app)
1. From a **sock-puppet** Telegram account (burner number), open the bot at https://telegram.me/discordsensorbot (@DiscordSensorbot).
2. Send `/start` to load the menu-driven interface.
3. Subscribe to the bot's linked Telegram channel if prompted — this is its access gate.
4. Navigate the menu to the relevant report and submit your Discord `username`/user ID or server.
5. Read the returned analytics (activity timing, engagement, member/community data).
6. Pivot: identified co-members become `associate` leads; a resolved Discord ID feeds a dedicated Discord user-lookup; activity timing corroborates timezone/pattern-of-life.

## Inputs → Outputs
- **In:** Discord `username` / user ID (`device-id`) / server
- **Out:** `social-profile` activity analytics, community/`associate` signals
- **Empty/negative result looks like:** the bot returns "no data", an error, or demands payment/subscription before showing anything — treat as no-result and corroborate elsewhere rather than assuming the subject is inactive.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** — you must operate a Telegram account and join a channel to use it; do this only from a disposable identity.
- OpSec: **active** — your query is tied to your Telegram account and logged by an unknown operator. Never use your real Telegram; assume the operator can see and retain your lookups.
- Trust: this is an anonymous probiv-ecosystem bot — data provenance is opaque, results may be scraped, stale, or fabricated, and some of these bots are outright scams or data-harvesting fronts. Verify independently before acting.

## Overlaps ("do both")
- Pairs with `[[discord-lookup]]` — use a transparent Discord ID/username resolver to independently confirm the account, then treat Discord Sensor's analytics as supplementary and unverified.

## Trust & verifiability
`trust: unverified` — an anonymous Telegram bot with no disclosed operator or data source. Useful only as a lead generator; corroborate any claim with a first-party or reputable tool, and never rely on it for anything you can't confirm elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discord-sensor |
| category | messaging |
| selectorsIn → selectorsOut | username, device-id → social-profile, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
