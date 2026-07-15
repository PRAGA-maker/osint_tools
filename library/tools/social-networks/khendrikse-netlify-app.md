---
id: khendrikse-netlify-app
name: Find Your Mastodon Account ID (guide)
description: Use when you have a Mastodon handle (`username`@instance) and want its stable numeric account ID for API queries — a short guide returning the social-profile ID and account JSON.
url: https://khendrikse.netlify.app/blog/find-your-mastodon-account-id/
category: social-networks
path:
- social-networks
bestFor: Resolving a Mastodon @user@instance handle to its permanent numeric account ID via the public lookup API.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free how-to blog post; the technique it teaches uses Mastodon's own public, unauthenticated lookup API — no account, key, or payment.
opsec: passive
opsecNote: The lookup endpoint is public and read-only; the target's instance may log the request under your IP but the account owner is not notified. Query from a VPN/sock-puppet if you don't want the instance operator tying the request to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: A personal developer blog documenting a genuine, official Mastodon API endpoint. The method is authoritative (it's Mastodon's own API); the page is just the reference for it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- mastodon
aliases:
- Mastodon account ID lookup
- khendrikse.netlify.app
tags:
- mastodon
- Mastodon Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Find Your Mastodon Account ID (guide)

> A concise reference for turning a Mastodon `@user@instance` handle into its permanent numeric account ID using Mastodon's own public lookup API — the anchor for any further Mastodon API work.

## When to use
You have a Mastodon handle and need its **stable numeric account ID** — because display names and even handles can change, but the ID is fixed, and most Mastodon API endpoints (statuses, followers, following) key off the ID, not the handle. Resolve it once, then you can pull a subject's public post history and social graph programmatically.

## How to use it (`bestInteractionPattern`: api)
1. Identify the subject's home instance and username (e.g. `@alice@mastodon.social`).
2. Call the public lookup endpoint in a browser or with `curl`:
   `https://<INSTANCE>/api/v1/accounts/lookup?acct=<USERNAME>`
   e.g. `https://mastodon.social/api/v1/accounts/lookup?acct=alice`
3. Read the returned JSON: the `id` field is the numeric account ID; you also get `username`, `display_name`, `note` (bio), avatar, and counts.
4. Use that `id` with follow-on endpoints, e.g. `/api/v1/accounts/<ID>/statuses` for public posts.
5. Pivot: post content reveals location/timezone tells; following/followers map `associate`s.

## Inputs → Outputs
- **In:** `username` (the `acct` handle, local or `user@instance`)
- **Out:** `social-profile` (numeric account ID + profile JSON), `name` (display name)
- **Empty/negative result looks like:** an HTTP 404 / error JSON — wrong instance or the account moved/was suspended; try the account's current home instance.

## Gotchas & OpSec
- Query the account's **home instance** — looking it up via a different instance may return a stale federated copy or nothing.
- The endpoint is unauthenticated but instances can rate-limit; space out bulk lookups.
- OpSec: passive and unnotified, but the instance sees your request — use a VPN for sensitive work.

## Overlaps ("do both")
- Pairs with a general Mastodon/fediverse search (e.g. instance search or fediverse-wide indexers) that finds the handle in the first place; this converts it to the durable ID.
- Feed the resolved ID into scripts that pull the subject's public timeline and follower graph.

## Trust & verifiability
`trust: community` — the guide is a hobbyist blog, but it documents Mastodon's official, first-party API, so the resulting ID and JSON are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | khendrikse-netlify-app |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
