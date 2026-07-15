---
id: here-20
name: X/Twitter User-ID Resolver
description: Use when you have a numeric X/Twitter user ID and want the account's current @handle/profile — the /i/user/ redirect resolves ID to the live social-profile.
url: https://x.com/i/user/
category: social-networks
path:
- social-networks
bestFor: Turning a numeric Twitter/X user ID into the account's current handle and profile via X's built-in redirect.
selectorsIn:
- device-id
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free; it is a native X URL pattern. Viewing the resolved profile in full may prompt an X login for logged-out users.
opsec: passive
opsecNote: You load a public X URL; the account owner gets no notification. If you are logged into your own X account while browsing, that activity is attributable to you — use a logged-out or sock-puppet session. No contact is made with any infrastructure other than X itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: This is X's own first-party redirect endpoint (x.com/i/user/<id>), not a third-party service, so the ID→handle mapping is authoritative.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Twitter user ID to username
- x.com/i/user
tags:
- xtwitter
- X / Twitter Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# X/Twitter User-ID Resolver

> X's native `/i/user/<id>` redirect, used to turn a numeric Twitter/X user ID into the account's current @handle and profile.

## When to use
You have a numeric X/Twitter **user ID** (from an archived tweet, an API dump, a scraper, or another tool) and need the account's **current handle**. Because the numeric ID never changes but handles do, this resolves a stale or renamed account back to whoever holds it now — the key move for re-finding a target who changed their @name to evade searches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take the numeric user ID and append it to the path: `https://x.com/i/user/<ID>` (e.g. `https://x.com/i/user/44196397`).
2. Load that URL in a logged-out or sock-puppet browser.
3. X redirects you to the account's current profile — note the live `@handle`.
4. Pivot: the resolved handle feeds username-search and archive tools; confirm identity continuity by checking join date and older content.

## Inputs → Outputs
- **In:** numeric X/Twitter user ID (`device-id`-style stable identifier)
- **Out:** current `social-profile` / `username` (the account's live @handle)
- **Empty/negative result looks like:** X shows "This account doesn't exist" or an error — the account was suspended, deactivated, or the ID is wrong; the mapping itself doesn't produce false handles.

## Gotchas & OpSec
- Logged-out users may hit a login wall when viewing the full profile — the redirect to the handle still resolves first, which is the part you need.
- Works only on X/Twitter numeric IDs; other platforms use their own ID schemes.
- OpSec: **passive**; just avoid browsing while logged into an attributable X account.

## Overlaps ("do both")
- Pair with any username-search tool once you have the resolved handle — this step un-hides the current name, the username tools then spread it across other platforms.

## Trust & verifiability
`trust: trusted` — it is X's own endpoint, so the ID→handle resolution is authoritative. There is no third-party data-quality risk; only availability depends on X.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | here-20 |
| category | social-networks |
| selectorsIn → selectorsOut | device-id, username → social-profile, username |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
