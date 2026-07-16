---
id: here-19
name: X (Twitter) intent — user_id → profile
description: Use when you have a numeric X/Twitter user ID (`document-id`) and want the account's current handle/profile — append the ID to the intent URL and it resolves to the live `social-profile` and `username`.
url: https://x.com/intent/user?user_id=
category: social-networks
path:
- social-networks
bestFor: Resolving a stable numeric Twitter/X user ID to the account's current @handle and profile, even after the user renamed.
selectorsIn:
- document-id
selectorsOut:
- social-profile
- username
- name
status: live
pricing: free
costNote: Native X endpoint; free. Viewing the resolved profile may prompt an X login depending on X's current gating.
opsec: passive
opsecNote: You hit X's own intent endpoint, not the target directly; it does not notify the account owner. If X requires login to view the profile, use a sock-puppet X account, never your own.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A first-party X.com endpoint (the "intent" system), so the ID→account mapping is authoritative straight from the platform.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- help-x-com
- here-20
- twitter-search
- twitter-x-advanced-search
- verif-cation-quiz-bot
- x-com
- x-com-3
- x-com-4
- x-com-6
aliases:
- x.com intent user
- Twitter user_id lookup
- twitter intent user
tags:
- xtwitter
- X / Twitter Related Sites
- id-resolution
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# X (Twitter) intent — user_id → profile

> A native X.com trick: a numeric user ID never changes, so appending it to the intent URL always resolves to the account's *current* handle — the fix for "they renamed and I lost them".

## When to use
You have a Twitter/X numeric user ID (a `document-id` you captured earlier, pulled from an API/archive, or found in a scrape) and the @handle it belonged to no longer works — because the user renamed, or you only ever had the ID. Because X user IDs are permanent while handles are not, this endpoint re-links the ID to whoever holds it now.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take the numeric user ID (e.g. `1234567890`).
2. Load `https://x.com/intent/user?user_id=<id>` in the browser.
3. X redirects/renders the current profile for that ID — read the live `username` (@handle), display `name`, bio, and links.
4. Pivot: the recovered current handle feeds normal profile analysis and cross-platform username enumeration; a rename from a known old handle is itself a lead (why did they switch?).

## Inputs → Outputs
- **In:** numeric X user ID (`document-id`)
- **Out:** current `social-profile`, `username` (@handle), display `name`
- **Empty/negative result looks like:** an error or "account doesn't exist" page — the account was deleted/suspended, or the ID is wrong; a suspended ID won't resolve to a handle.

## Gotchas & OpSec
- Needs the numeric ID, not the handle — pair it with an ID-lookup tool if you only have a handle.
- X's login-gating changes frequently; if the profile won't render logged-out, view it from a sock-puppet account.
- OpSec: passive — you query X's endpoint, not the person.

## Overlaps ("do both")
- Pairs with handle→ID lookup tools (and account-history services) — those give you the ID from an old handle; this turns an ID back into the current handle, closing the loop across renames.

## Trust & verifiability
`trust: trusted` — a first-party X endpoint; the ID→account resolution comes straight from the platform and is authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | here-19 |
