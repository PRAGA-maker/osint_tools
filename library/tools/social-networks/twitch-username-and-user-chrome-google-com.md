---
id: twitch-username-and-user-chrome-google-com
name: Twitch Username ↔ User ID Translator
description: Use when you have a Twitch `username` (or its numeric user ID) and want to resolve one to the other — returns the stable social-profile identifier that survives display-name changes.
url: https://chromewebstore.google.com/detail/twitch-username-and-user/laonpoebfalkjijglbjbnkfndibbcoon
category: social-networks
path:
- social-networks
bestFor: Converting between a Twitch username and its permanent numeric user ID so you can track an account across name changes.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free Chrome extension (10k+ users, 4.3★). Uses the official Twitch Helix API; by default it obtains a token via TwitchTokenGenerator.com, or you can supply your own client ID/secret from developer.twitch.tv.
opsec: passive
opsecNote: The lookup queries the Twitch API, not the target's session, so nothing is sent to or seen by the account owner. Caveat: the default flow routes through a third party (TwitchTokenGenerator) — provide your own Twitch client ID/secret if you don't want that middleman seeing your queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Published by developer "swiftyspiffy" on the Chrome Web Store; 10k+ users, declares no data collection. Uses Twitch's official API so results are authoritative, but it's a community extension, not a Twitch product.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- twitch
aliases:
- Twitch username and user id
- twitch id translator
tags:
- twitch
- Twitch Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Twitch Username ↔ User ID Translator

> A tiny Chrome extension that resolves a Twitch username to its permanent numeric user ID (and back) via the official Twitch API — your anchor when a streamer renames.

## When to use
You are tracking a Twitch account and need its **stable identifier**. Twitch display names/usernames can change, but the numeric user ID never does. Convert a known `username` to its user ID early so you can keep following the same person even after a rename — or reverse a numeric ID you found in a URL/API dump back to the current username.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Twitch Username and User ID Translator" from the Chrome Web Store (link above).
2. Open the extension popup.
3. Enter a Twitch username to get its numeric user ID, or enter a numeric ID to get the current username.
4. (Optional but recommended for OpSec) In options, supply your own Twitch client ID/secret from developer.twitch.tv instead of the default TwitchTokenGenerator token.
5. Pivot: record the numeric ID as the durable key; feed the username into cross-platform username enumeration.

## Inputs → Outputs
- **In:** `username` (or a numeric Twitch user ID)
- **Out:** `social-profile` — the corresponding numeric user ID or current username
- **Empty/negative result looks like:** an "invalid username/ID" notice — the account doesn't exist or was deleted/banned; a former ID that now resolves to nothing signals the account is gone.

## Gotchas & OpSec
- Human-in-the-loop: none; but decide upfront whether to use the default third-party token or your own Twitch app credentials.
- Only resolves the ID↔name mapping — it does not pull followers, chat logs, or VODs.
- OpSec: passive API lookup; nothing reaches the target.

## Overlaps ("do both")
- Pairs with direct Twitch profile/VOD review — this gives the durable ID, Twitch gives the content.
- Combine with username-enumeration tools: the resolved username seeds a cross-site sweep for the same handle.

## Trust & verifiability
`trust: community` — a well-used community extension wrapping Twitch's official Helix API, so the ID mapping itself is authoritative; the only trust question is the default token middleman, which you can bypass.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-username-and-user-chrome-google-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
