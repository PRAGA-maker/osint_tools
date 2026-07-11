---
id: dev-to
name: dev.to (Find a Mastodon account ID)
description: Use when you have a Mastodon `username`/handle and want the numeric account ID via the public API — returns social-profile metadata to pivot into Mastodon tooling.
url: https://dev.to/khenhey/how-to-find-your-mastodon-account-id-489d
category: social-networks
path:
- social-networks
bestFor: A technique reference for resolving a Mastodon handle to its numeric account ID (and profile JSON) via the instance's public lookup API.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free public-API technique documented in a free dev.to article; no account or key needed for the lookup endpoint.
opsec: passive
opsecNote: The Mastodon `accounts/lookup` endpoint reads public profile data and does not notify the account owner. The request goes to the target's home instance, whose admins can see your IP in server logs — use a VPN/sock-puppet if the instance is small and the case sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: A community how-to article; the underlying method is the standard, documented Mastodon public API, so the technique is reliable even though the article is informal.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- fedidb
- clearsky-app
aliases:
- Mastodon account ID lookup
- Mastodon accounts/lookup
tags:
- mastodon
- Mastodon Related Sites
- fediverse
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# dev.to (Find a Mastodon account ID)

> A short dev.to how-to documenting the standard Mastodon public-API trick to turn a `@user@instance` handle into a stable numeric account ID and full profile JSON.

## When to use
You have a Mastodon `username`/handle and need its numeric account ID — the stable key you feed into other Mastodon/fediverse tooling, API scripts, or to fetch a profile's raw JSON (avatar, bio, follower/following counts, created-at). Reach for this when a handle-based tool isn't enough and you want the account's canonical identifier or machine-readable profile data.

## How to use it (`bestInteractionPattern`: api)
1. Identify the target's home instance and handle (e.g. `@alice@mastodon.online`).
2. Query the public lookup endpoint in a browser or with curl:
   `https://<INSTANCE>/api/v1/accounts/lookup?acct=<USERNAME>`
   e.g. `https://mastodon.online/api/v1/accounts/lookup?acct=alice`
3. Read the returned JSON: `id` (the numeric account ID), plus display `name`, bio, URLs, avatar, and created-at timestamp.
4. Pivot: use the numeric ID with statuses/followers endpoints or fediverse indexers; use avatar/bio to corroborate identity and to seed reverse-image and username searches.

## Inputs → Outputs
- **In:** `username` (Mastodon handle) + home instance
- **Out:** numeric account `id`, display `name`, profile JSON (`social-profile` metadata: bio, avatar, counts, created-at)
- **Empty/negative result looks like:** a 404 / "Record not found" — the handle doesn't exist on that instance, or you queried the wrong instance (a migrated account changes ID between instances); re-check the correct home server.

## Gotchas & OpSec
- Mastodon account IDs are **per-instance** — unlike Twitter, an account that migrates instances gets a new ID, so an old ID may be stale. Always resolve against the current home instance.
- Some instances rate-limit or restrict the public API; if `lookup` is blocked, try fetching the profile page's WebFinger (`/.well-known/webfinger?resource=acct:user@instance`).
- OpSec: passive — the owner isn't notified; only the instance's server logs see your request.

## Overlaps ("do both")
- Pairs with fediverse indexers like [[fedidb]] (instance/network context) and, for the block-analytics analog on Bluesky, [[clearsky-app]] — this article is the low-level ID-resolution step those higher-level tools build on.

## Trust & verifiability
`trust: community` — an informal community write-up, but it documents the official, well-established Mastodon public API. The method is reliable and the JSON it returns comes straight from the target's instance, so results are self-verifying.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dev-to |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
