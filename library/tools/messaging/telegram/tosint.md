---
id: tosint
name: TOSINT
description: Use when you have a Telegram bot token or a public group/channel and want to extract its metadata, admins and settings — returns social-profile, associate (admins) and metadata.
url: https://github.com/drego85/tosint
category: messaging
path:
- messaging
- telegram
bestFor: Telegram OSINT from the CLI — extracting bot identity, chat/channel metadata, admin lists and permissions from a bot token or public chat.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Python); no cost. You supply a bot token or a public chat identifier.
opsec: active
opsecNote: TOSINT queries Telegram's API directly (via a bot token) to resolve and enumerate the target chat, so the activity runs through a Telegram bot you control and touches the target chat's server side. Use a throwaway bot/account, and note that adding a bot to a group is visible to admins — prefer public metadata extraction over intrusive joins.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Open-source Telegram-OSINT tool by Andrea Draghetti (drego85); source is inspectable and the project is maintained, but it's a community tool, not an official Telegram product.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Tosint
- Telegram OSINT
- drego85/tosint
tags:
- telegram
- bot-recon
- cli
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# TOSINT

> A command-line Telegram-OSINT tool — feed it a bot token or a public chat and it extracts the bot's identity, the chat/channel's metadata, and the full admin roster with their permissions.

## When to use
You're investigating a Telegram bot, group or channel and want structured intelligence about it: who administers it (`associate`), its settings (history visibility, member-hiding, content protection, join-by-request), member counts, description and invite links, plus the identity/permissions of any bot involved. It's the tool for turning a raw bot token or public chat link into a metadata report you can act on.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install (`pip install -r requirements.txt`).
2. Run interactively (`python3 tosint.py`) or via CLI (`python3 tosint.py -t <BOT_TOKEN> -c <CHAT_ID>`).
3. Read the report: bot info, chat metadata (title/type/ID/username/description/flags), and per-admin details (name, user ID, username, role, permissions).
4. Optionally export JSON and download chat history/media for forensic review.
5. Pivot: admin usernames/IDs feed `[[sangmatainfo-bot]]` and cross-platform enumeration; invite links and channel IDs feed `[[telemetr-io]]`.

## Inputs → Outputs
- **In:** a Telegram bot token, and/or a public chat identifier (`username`/ID)
- **Out:** `social-profile` (bot/chat identities), `associate` (admins with roles), `metadata-exif` (chat settings, counts, invite links, downloadable history)
- **Empty/negative result looks like:** an invalid/revoked token, or a private chat the bot can't see — TOSINT can only report what the token/permissions expose; a locked-down chat yields little.

## Gotchas & OpSec
- Requires a valid bot token or a bot with access; you can't enumerate a private chat you have no bot presence in.
- **Active:** it hits Telegram's API from your bot — use a throwaway bot, and remember joining/adding a bot to a group is visible to admins.
- Extracted admin data is a point-in-time snapshot; roles/usernames change.

## Overlaps ("do both")
- Pairs with `[[telemetr-io]]` (channel analytics/search) and `[[sangmatainfo-bot]]` (name history) — TOSINT gives structural metadata and admins, the others give reach analytics and identity history.

## Trust & verifiability
`trust: community` — a maintained, inspectable open-source tool; output comes straight from Telegram's API, so it's reliable for what the token can see, though coverage depends on permissions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tosint |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile, associate, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
