---
id: twitch-username-and-user-id-addons-mozilla-org
name: Twitch Username & User ID (Firefox add-on)
description: Use when you have a Twitch `username` (or numeric user ID) and want to convert between them to get a stable identifier that survives renames — returns the persistent Twitch user ID / social-profile handle.
url: https://addons.mozilla.org/en-US/firefox/addon/twitch-username-and-user-id/
category: social-networks
path:
- social-networks
bestFor: Converting a Twitch username to its permanent numeric user ID (and back) to track an account across name changes.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free Firefox add-on; no account or payment required.
opsec: passive
opsecNote: The lookup queries Twitch's public API for the ID↔name mapping; the account owner is not notified. Passive, though the request originates from your browser/IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A small third-party Firefox add-on (v1.8, last updated 2021); it simply wraps Twitch's public ID lookup, so risk is low, but it is unmaintained and could break if Twitch changes its API.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Twitch username to user id
- Twitch ID lookup
tags:
- twitch
- Twitch Related Sites
- account-id
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Twitch Username & User ID (Firefox add-on)

> A one-purpose Firefox add-on: convert a Twitch username to its permanent numeric user ID (and back), giving you an identifier that survives display-name changes.

## When to use
You have a Twitch `username` and want its stable numeric user ID — the ID never changes even when the streamer renames, so it lets you re-find and track an account after a handle change, and correlate the same person across third-party Twitch analytics that key on ID. Conversely, given a leaked/logged user ID you can recover the current username.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the add-on from https://addons.mozilla.org/en-US/firefox/addon/twitch-username-and-user-id/ in Firefox.
2. Enter a Twitch `username` to get its numeric user ID, or enter a user ID to get the current username.
3. Read the result; the add-on flags invalid usernames/IDs.
4. Pivot: use the stable user ID in Twitch analytics/tracking sites and to re-locate the account after future renames; use a recovered username for cross-platform username search.

## Inputs → Outputs
- **In:** Twitch `username` (or numeric user ID)
- **Out:** the persistent numeric user ID / current `username` (`social-profile` anchor)
- **Empty/negative result looks like:** an "invalid" notice — the username/ID doesn't exist (or the account was deleted); a rename shows as the same ID mapping to a new name.

## Gotchas & OpSec
- Unmaintained since 2021 — if Twitch changes its API the add-on may stop working; the same ID↔name lookup can also be done via Twitch's API directly or other converters.
- The user ID is the durable identifier; the display name is not — always record the ID for long-term tracking.
- OpSec: passive; the owner isn't notified, though the query comes from your browser.

## Overlaps ("do both")
- Do both with cross-platform username-search tools (to find the same handle elsewhere) — this pins the *stable Twitch identity* while those spread the search across other networks.

## Trust & verifiability
`trust: community` — a lightweight third-party wrapper over Twitch's public ID lookup; low-risk and easy to cross-check against Twitch's own API.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-username-and-user-id-addons-mozilla-org |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
