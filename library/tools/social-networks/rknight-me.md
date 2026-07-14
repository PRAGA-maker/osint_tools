---
id: rknight-me
name: Get Mastodon Account ID from Username (technique)
description: Use when you have a Mastodon `username`/handle and want its numeric account ID to unlock API/RSS access to the account's posts — returns the account ID and canonical `social-profile`.
url: https://rknight.me/blog/get-mastodon-account-id-from-username/
category: social-networks
path:
- social-networks
bestFor: Resolving a Mastodon @user@instance handle to its numeric account ID so you can pull its public feed via API/RSS.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free technique using Mastodon's own public API endpoints; no account or key needed for public data.
opsec: passive
opsecNote: The lookup queries the target's home instance API for public account data — read-only and not tied to following or notifying the user. Requests hit that instance's server from your IP; use a sock-puppet/VPN context for sensitive work. You are not authenticating, so nothing is attributable to a Mastodon account of yours.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A clear how-to by developer Robb Knight describing Mastodon's documented public API behavior; the technique is verifiable against Mastodon's own docs, independent of the blog.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Mastodon account id lookup
- mastodon username to id
tags:
- mastodon
- Mastodon Related Sites
- api-technique
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Get Mastodon Account ID from Username (technique)

> A small but pivotal Mastodon trick: turn a human `@user@instance` handle into the numeric account ID that unlocks programmatic access to everything the account has posted publicly.

## When to use
You have a Mastodon handle for a subject and want to go beyond scrolling the web profile — enumerate their public posts programmatically, subscribe to an RSS feed of their activity, or monitor changes. Mastodon's API keys most account operations off a **numeric account ID**, not the username, so this resolution step is the gateway to feed/post extraction on the Fediverse.

## How to use it (`bestInteractionPattern`: web-manual / API)
1. Identify the subject's home instance from the handle `@username@instance.tld`.
2. Resolve the ID via the instance's public lookup endpoint:
   `https://<instance>/api/v1/accounts/lookup?acct=<username>` — returns JSON including the numeric `id`, display `name`, bio, and profile URL.
3. Use that ID for further public calls, e.g. statuses:
   `https://<instance>/api/v1/accounts/<id>/statuses` — the account's public posts (with timestamps, media, boosts).
4. For passive monitoring, many instances expose an RSS feed at `https://<instance>/@<username>.rss`.
5. Pivot: post timestamps feed pattern-of-life; linked accounts, media, and mentioned handles feed cross-platform and reverse-image work.

## Inputs → Outputs
- **In:** Mastodon `username` / `@user@instance` handle
- **Out:** numeric account `id`, canonical `social-profile` URL, display `name`, and (via follow-on calls) the public post feed
- **Empty/negative result looks like:** a 404 or empty JSON — the username doesn't exist on that instance, the instance is down/defederated, or the account is locked/suspended. A locked account exposes little via API even when the ID resolves.

## Gotchas & OpSec
- You must target the **correct home instance** — the same username can exist on many instances as different people. Confirm the instance from the full handle.
- Locked/private accounts and some hardened instances limit or block unauthenticated API reads.
- Instance admins can see requests hitting their API; use a neutral IP for sensitive monitoring.
- OpSec: passive and unauthenticated — no Mastodon account of yours is involved.

## Overlaps ("do both")
- Pairs with general Fediverse search and username-enumeration tools — those find *where* a handle exists; this technique unlocks *deep* read access (full public feed, RSS) once you've located the account. Also pairs with timestamp/pattern-of-life analysis on the recovered posts.

## Trust & verifiability
`trust: community` — a developer how-to, but it describes Mastodon's documented public API, so you can verify the endpoints against official Mastodon docs and the returned data against the live web profile. The data comes straight from the instance, not the blog.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rknight-me |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
