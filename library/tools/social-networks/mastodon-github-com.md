---
id: mastodon-github-com
name: Mastodon accounts/lookup API
description: Use when you have a known Mastodon `username`/handle on a specific instance and want to resolve it to a stable account ID and profile metadata — returns the account's social-profile and id.
url: https://github.com/mastodon/mastodon/discussions/21156
category: social-networks
path:
- social-networks
bestFor: Resolving a known Mastodon handle on a given instance to its numeric account ID and public profile via the REST API.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Mastodon is open-source; the API endpoint is free on any public instance, no key needed for public account lookups.
opsec: passive
opsecNote: A read of the public `/api/v1/accounts/lookup` endpoint does not notify the account owner and looks like ordinary traffic. Query the instance the account actually lives on; hitting an unrelated instance leaks your interest to that instance's admins for no benefit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: This is the official Mastodon project's own REST API, documented in the project's GitHub discussions; the data returned is the instance's authoritative record for that account.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- mastodon-social
aliases:
- Mastodon API account lookup
- accounts/lookup
tags:
- mastodon
- Mastodon Related Sites
- api-technique
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Mastodon accounts/lookup API

> The federated-network equivalent of a username-to-ID resolver: turn a known Mastodon handle into a stable account ID and its public profile via one API call.

## When to use
You have a subject's Mastodon handle (e.g. `@alice@mastodon.social`) and need the account's stable numeric ID — because Mastodon usernames can be reused or changed, but the ID is permanent — plus the public profile fields (display name, bio, join date, post/follower counts). This is the anchoring step before you scrape their public timeline or track the account across handle changes.

## How to use it (`bestInteractionPattern`: api)
1. Identify the instance the account lives on (the part after the second `@` — `mastodon.social` in `@alice@mastodon.social`).
2. Call the instance's public endpoint:
   `https://<instance>/api/v1/accounts/lookup?acct=<username>`
   e.g. `https://mastodon.social/api/v1/accounts/lookup?acct=alice`
3. Read the JSON: `id` (the stable account ID), `display_name`, `note` (bio), `created_at`, `followers_count`, `url`.
4. Use the returned `id` with other public endpoints (e.g. `/api/v1/accounts/<id>/statuses`) to pull the public timeline.
5. Pivot: the bio/`note` and `url` often link out to other `social-profile`s; the `created_at` dates the account.

## Inputs → Outputs
- **In:** `username` (a handle) **and** the instance it belongs to.
- **Out:** the account's stable `id`, display `name`, bio, join date, and public `social-profile` URL.
- **Empty/negative result looks like:** a 404 / empty response. Critically, `accounts/lookup` **does not resolve remote accounts** — it only returns accounts the queried instance already knows about. If you query the wrong instance, you get nothing even for a real account; always query the account's home instance.

## Gotchas & OpSec
- The single biggest trap: this endpoint only works for accounts local to (or already federated into) the instance you query. For discovery of an unknown handle across the fediverse, use `/api/v2/search` on an instance that already knows the account, or query the home instance directly.
- No auth is needed for public accounts, so it is a clean passive read; heavily rate-limited endpoints or locked accounts will return restricted data.
- Instances can be private or defederated; a missing result may reflect instance policy, not a missing person.

## Overlaps ("do both")
- Pairs with `[[mastodon-social]]` — use the flagship instance's web search to discover a handle, then use this API call against the handle's home instance to lock in the permanent account ID and full public profile.

## Trust & verifiability
`trust: trusted` — it is the official Mastodon REST API. Each instance returns its own authoritative record, so the data is as reliable as that instance; there is no third-party scraper in the loop.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mastodon-github-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
