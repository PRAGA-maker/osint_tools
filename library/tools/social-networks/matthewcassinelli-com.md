---
id: matthewcassinelli-com
name: matthewcassinelli.com
description: Use when you have a Mastodon/fediverse handle or profile link and want its stable numeric account ID — this free Apple Shortcut returns the account ID via the Mastodon lookup API so you can track the account across handle changes.
url: https://matthewcassinelli.com/shortcuts-mastodon-lookup-account-id/
category: social-networks
path:
- social-networks
bestFor: Resolving a Mastodon handle/profile URL to its permanent numeric account ID (which survives display-name and handle changes).
selectorsIn:
- social-profile
- username
selectorsOut:
- device-id
- social-profile
status: live
pricing: free
costNote: This specific shortcut is a free download; the author's broader Shortcuts Library is membership-based, but the Mastodon lookup shortcut itself is free. Requires Apple Shortcuts (iOS/macOS).
opsec: passive
opsecNote: The shortcut calls the target instance's public /api/v1/accounts/lookup endpoint — an unauthenticated read that any client makes when loading a profile. No follow, no interaction, no notification to the account. Passive, though the request originates from your IP unless you route it.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: Published by Matthew Cassinelli, a well-known Shortcuts author; the shortcut is a thin wrapper over Mastodon's documented public API, so its output is as reliable as the instance's own API.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- trevorfox-com-2
aliases:
- Mastodon Lookup Account ID shortcut
- Matthew Cassinelli Shortcuts
tags:
- mastodon
- Mastodon Related Sites
- fediverse
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# matthewcassinelli.com — Mastodon Lookup Account ID

> An Apple Shortcut that turns a fediverse handle into its permanent numeric account ID, so you can keep tracking an account even after it renames itself.

## When to use
You are following a Mastodon/fediverse account and need its stable internal ID rather than its handle. Handles and display names on Mastodon change freely, but the numeric account ID on a given instance does not — pinning it lets you re-find the account, build reliable API queries, and detect when a "new" account is actually the same person.

## How to use it (`bestInteractionPattern`: mobile-app)
1. On the page https://matthewcassinelli.com/shortcuts-mastodon-lookup-account-id/, tap **Get Shortcut** to add it to Apple Shortcuts (iOS/iPadOS/macOS).
2. Run the shortcut and give it a fediverse link (or copy the profile URL to your clipboard first).
3. It parses the instance host and `@handle`, then calls `https://{instance}/api/v1/accounts/lookup?acct={handle}`.
4. It returns the account's numeric ID (and you can extend it to grab other public profile fields the API exposes).
5. Pivot: use the ID to query that instance's public API for the account's posts/followers, or to confirm two handles resolve to the same ID.

## Inputs → Outputs
- **In:** a Mastodon `username`/handle or profile `social-profile` URL
- **Out:** the account's numeric ID (a stable `device-id`-style identifier) plus a confirmed canonical `social-profile`
- **Empty/negative result looks like:** an API error / empty ID if the handle doesn't exist on that instance, the instance is down, or the account was moved/deleted — try the account's current home instance explicitly.

## Gotchas & OpSec
- Requires the Apple Shortcuts app; there is no web version. On non-Apple platforms, hit the same `/api/v1/accounts/lookup` endpoint manually with curl.
- The ID is only stable **within one instance** — the same person on a different instance has a different ID; the fediverse has no global user ID.
- OpSec: **passive** — a normal public API read, but sent from your IP. Route through a research VPN if attribution matters.

## Overlaps ("do both")
- Pairs with `[[trevorfox-com-2]]` — both recover a durable identifier/timestamp from a social URL (LinkedIn post time vs Mastodon account ID); use whichever matches the platform in hand.

## Trust & verifiability
`trust: community` — a reputable independent Shortcuts author wrapping Mastodon's own documented public API. The result is verifiable by calling the same endpoint yourself, so reliability tracks the instance, not the shortcut.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | matthewcassinelli-com |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → device-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | yes (account-login) |
