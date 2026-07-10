---
id: x-com-4
name: x.com (X / Twitter native search)
description: Use when you have a `username` or `name` and want the subject's X (Twitter) profile and posts via the platform's own search — returns `social-profile`, `name`, bio, posts, and connections.
url: https://www.x.com/
category: social-networks
path:
- social-networks
bestFor: The primary platform check — finding and reading a subject's X (Twitter) account, bio, posts, and network directly on X.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to view, but X now gates most search and profile browsing behind a logged-in account and rate-limits heavily; some data needs a paid Premium/API tier.
opsec: active
opsecNote: Browsing X while logged in exposes your account/session to X, and viewing profiles/following can leave traces (e.g. appearing in "who viewed"-style signals, follow notifications). Use a dedicated sock-puppet X account on a clean browser/IP; never a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: The genuine first-party X platform; profiles and posts are authoritative, though user content is self-authored and can be false.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: false
aliases:
- X
- Twitter
- x.com
tags:
- xtwitter
- X / Twitter Related Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# x.com (X / Twitter native search)

> The platform itself — find and read a subject's X (Twitter) account, posts, and network using X's own people/keyword search.

## When to use
You have a `username` or `name` and want to check the subject's presence on X (Twitter) and read their profile, posts, and connections directly at the source. This is the baseline platform check that the many third-party X tools supplement — start here to confirm the account exists, then use specialist tools for history, deleted content, and analytics.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet X account (clean browser/IP).
2. Use X search: `from:username`, a `name`, or keywords; the People tab finds accounts, Latest gives chronological posts.
3. Open the profile for bio, location, joined date, links, following/followers, and pinned/recent posts.
4. Note the account's handle and numeric ID for cross-tool tracking.
5. Pivot: handle history via `[[memory-lol-github-com]]`; date-bounded posts via `[[twitter-date-search]]`; deleted/walled content via `[[wayback-machine-2]]`; audience/location via `[[fedica]]`.

## Inputs → Outputs
- **In:** `username` or `name` (+ keywords)
- **Out:** `social-profile` (X account), `name`, bio, location field, posts, following/followers
- **Empty/negative result looks like:** no account or an empty/limited view — the person may not be on X, uses a different handle, is suspended/protected, or X's login-gating is hiding results. Sparse results often reflect X's restrictions, not absence.

## Gotchas & OpSec
- **Login-gated and rate-limited** — meaningful searching now generally needs an account; sock-puppet only.
- The `location` field and bio are self-reported — verify, don't trust.
- Active toward the platform; follows/likes from your account are visible — browse read-only.

## Overlaps ("do both")
- Pairs with `[[twitter-search-tool]]`, `[[twitter-search-engine]]`, `[[memory-lol-github-com]]`, and `[[twitter-date-search]]` — native X is the source of truth for live content; the others recover history, defeat handle changes, and query Google's cache when X is walled.

## Trust & verifiability
`trust: trusted` — the authentic first-party platform; the account/posts are real, but treat self-authored bio/location and any claim as needing corroboration.
