---
id: telepathy-2
name: Telepathy
url: https://github.com/jordanwildon/Telepathy
category: messaging
path:
- messaging
description: Use when you have a Telegram channel/group or a user's `social-profile` and want to archive it and enumerate members — returns member lists, message history and `associate` links.
bestFor: Archiving a Telegram chat and extracting member lists, top posters, forward networks and user metadata for investigation.
selectorsIn:
- social-profile
- username
selectorsOut:
- associate
- username
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (MIT). Requires your own Telegram API credentials from my.telegram.org; a Pro/hosted tier exists but the CLI is fully free.
opsec: active
opsecNote: You must authenticate with a real Telegram account (phone + code) whose identity Telegram — and potentially group admins — can see. Joining/scraping a group can expose that account. Use a dedicated burner Telegram number/account, never your real one, and note some groups detect scraping.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Widely-used open-source Telegram OSINT toolkit by researcher Jordan Wildon; code is public and auditable, but it drives your own account so responsibility (and risk) is yours.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
aliases:
- Telepathy Telegram OSINT
- jordanwildon/Telepathy
tags:
- kimi-2026
- telegram
- chat-archiving
source: kimi-telegram
lastVerified: '2026-07-10'
enrichment: full
---

# Telepathy

> The "swiss-army knife" of Telegram OSINT — a Python CLI that archives a chat wholesale and extracts member lists, top posters, forward networks and per-user metadata.

## When to use
You have a Telegram channel/group (or a `username`/`social-profile` seen in one) and need to map who is in it, who posts, and how messages propagate. Telepathy archives messages/media/reactions, dumps member lists (up to ~5,000 for groups), finds top posters, and traces forwarded-message chains — turning a single chat into an `associate` network and a searchable message archive. High value when a subject is active on Telegram, which is often the primary channel in cross-border and extremist/trafficking cases.

## How to use it (`bestInteractionPattern`: cli)
1. Get Telegram API credentials (api_id/api_hash) at my.telegram.org — use a **burner** account, not your real one.
2. Install: `pip install telepathy` (or clone the GitHub repo and run from source).
3. Authenticate the CLI with your burner phone number and the login code.
4. Run against a target: e.g. `telepathy -t <channel>` to scan a chat, add flags for comprehensive archive (`-c`), member export, or forward analysis.
5. Read the CSV/JSON output: member lists, message history, top posters, forward map.
6. Pivot: exported `username`s/user IDs feed cross-platform enumeration; forward networks reveal linked channels and `associate` clusters.

## Inputs → Outputs
- **In:** a Telegram channel/group handle, or a `username`/`social-profile`
- **Out:** member lists (`associate`, `username`), message archive, top-poster stats, forward network, chat metadata (`metadata-exif`)
- **Empty/negative result looks like:** a private/invite-only chat your account can't join, or a group with member-list hiding enabled — you get chat metadata but no member export. An empty member dump usually means restricted access, not an empty group.

## Gotchas & OpSec
- **Active and account-bound:** it drives *your* Telegram account; scraping is visible to Telegram and can get the account limited/banned. Always use a dedicated burner number.
- Member export caps around 5,000 for large groups and can't see admins who hide membership.
- Requires API credentials and comfort with a CLI; not a point-and-click tool.
- Respect legal boundaries — mass-collecting members can be regulated depending on jurisdiction and purpose.

## Overlaps ("do both")
- Pairs with `[[telesearch]]`/`[[tginfo-me]]`-style Telegram directory lookups — those find channels by keyword; Telepathy deep-scrapes the channel you've found.

## Trust & verifiability
`trust: community` — a public, auditable, widely-cited OSINT toolkit; the data it returns comes straight from Telegram's own API, so it is authoritative, but you bear the operational and legal risk of running it under your account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telepathy-2 |
| category | messaging |
| selectorsIn → selectorsOut | social-profile, username → associate, username, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, api-key) |
