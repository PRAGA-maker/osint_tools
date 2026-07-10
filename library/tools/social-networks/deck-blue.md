---
id: deck-blue
name: deck.blue
description: Use when you have a Bluesky `username` and want to monitor their posts, searches and lists in real time across columns — returns live `social-profile` activity.
url: https://deck.blue/
category: social-networks
path:
- social-networks
bestFor: TweetDeck-style multi-column monitoring of Bluesky accounts, searches, feeds and lists.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free third-party Bluesky client; you connect with your own Bluesky handle and an app password. No paid tier required for core columns.
opsec: passive
opsecNote: Viewing public Bluesky posts is passive and does not notify the subject. However, you must log in with a Bluesky account — always use a sock-puppet handle and a Bluesky app password (never your main password), since deck.blue is a third party receiving that credential. Following/liking/replying from the tool is active and attributable.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A popular third-party Bluesky deck client, not an official Bluesky product; you trust it with an app-password credential, so scope it narrowly with a puppet account.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- deck.blue
- Bluesky deck
tags:
- bluesky
- BlueSky / BSky Related Sites
- monitoring
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# deck.blue

> A TweetDeck-for-Bluesky: pin a subject's profile, a keyword search, and a feed side by side and watch them update live.

## When to use
You have a Bluesky `username` (or a `name` to search) and want to monitor their activity as it happens — new posts, replies, follows, and keyword mentions — laid out in parallel columns. Ideal when a missing-persons or investigative subject is active on Bluesky and you need situational awareness rather than a one-off profile read.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://deck.blue/ and sign in with a **sock-puppet** Bluesky handle using a Bluesky **app password** (Settings → App Passwords), never your main password.
2. Add columns: the subject's profile, a keyword/handle search, their followers/following, a custom feed, or a list.
3. Watch the columns update live; use search columns for mentions of their name/handle/associated terms.
4. Stay read-only — do not follow/like/reply from the deck (that's attributable to your puppet).
5. Pivot: capture post URLs for archiving, run profile images through reverse-image/face tools, and cross-check the handle with `[[sherlock]]`/`[[namechk]]`.

## Inputs → Outputs
- **In:** Bluesky `username` (or `name` to search)
- **Out:** live `social-profile` activity — posts, replies, follows, search hits, confirmed display `name`
- **Empty/negative result looks like:** empty columns / no search hits — the subject isn't on Bluesky under that handle, or is inactive. Not proof of absence elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** — a Bluesky account (app password) is required. Use a puppet.
- OpSec: **passive** for reading; the credential goes to a third party, so scope it (app password, puppet). Any interaction is active and attributable.
- It's an unofficial client; features and availability depend on Bluesky's API remaining open.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`/`[[namechk]]` (is the handle reused elsewhere?) and archival tools (save post URLs) — deck.blue watches Bluesky live; the others broaden and preserve.

## Trust & verifiability
`trust: unverified` — a useful third-party client you must trust with a login. Use a puppet account/app password, and verify anything material on the live Bluesky profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deck-blue |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
