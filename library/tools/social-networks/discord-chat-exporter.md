---
id: discord-chat-exporter
name: DiscordChatExporter
description: Use when you have access to a Discord server/channel and want an offline, searchable archive of its messages — returns exported chat logs (HTML/JSON/CSV) with authors, timestamps, attachments.
url: https://github.com/Tyrrrz/DiscordChatExporter
category: social-networks
path:
- social-networks
bestFor: Exporting Discord channel/DM history to a searchable, preservable file (HTML/JSON/CSV) for evidence capture and analysis.
selectorsIn:
- social-profile
- username
selectorsOut:
- username
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (GUI, CLI, and Docker builds). No cost beyond your own Discord account/token.
opsec: active
opsecNote: Exporting requires your (or a sock-puppet) Discord account's token and reads channels that account can see — using a personal user token to automate reads is against Discord's ToS and can get the account banned. Use a dedicated sock-puppet account, only in servers you have legitimate access to, and never share the token.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: A very popular, actively maintained open-source tool by Tyrrrz, featured in Bellingcat's toolkit; the export faithfully reflects what your account can see, so accuracy is high but scope is limited by your access.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- DiscordChatExporter
- Tyrrrz DiscordChatExporter
tags:
- bellingcat-toolkit
- discord
- evidence-preservation
source: bellingcat-toolkit
lastVerified: '2026-07-19'
enrichment: full
---

# DiscordChatExporter

> A free, open-source tool that pulls a Discord channel or DM's full history into a searchable, archivable file — the standard way to preserve Discord evidence before it can be deleted.

## When to use
You have legitimate access (via your own or a sock-puppet account) to a Discord server, channel, or DM relevant to an investigation and need a durable, searchable copy — because Discord messages can be edited or deleted at any time. It captures message text, `username`s and display names, timestamps, edits, attachments, and embeds, letting you analyse a community offline and preserve chat as evidence.

## How to use it (`bestInteractionPattern`: cli)
1. Download a build from https://github.com/Tyrrrz/DiscordChatExporter (GUI for Windows, CLI, or Docker for cross-platform/automation).
2. Obtain your Discord account token (the tool's wiki explains how) — use a **dedicated sock-puppet** account, never a personal one.
3. Run an export, e.g. CLI: `DiscordChatExporter.Cli export -t <TOKEN> -c <CHANNEL_ID> -f HtmlDark -o out/`. GUI: pick the server/channel and format.
4. Choose a format: HTML (readable, with images), JSON (for parsing/analysis), or CSV.
5. Analyse or preserve the output; hash the file for chain-of-custody.
6. Pivot: `username`s/IDs in the log feed cross-platform username search; linked accounts and shared media feed further OSINT.

## Inputs → Outputs
- **In:** a Discord channel/DM you can access (identified via the `social-profile`/server you're in)
- **Out:** exported logs containing `username`s, user IDs, timestamps, edits, and attachment `metadata-exif`; links to authors' `social-profile`s
- **Empty/negative result looks like:** an empty/partial export because your account lacks access to the channel, the token is invalid, or the channel was purged — you can only export what your account can already read.

## Gotchas & OpSec
- **ToS risk:** automating reads with a user token violates Discord's terms and risks a ban — use a disposable sock-puppet account and expect it may be lost.
- You cannot export channels your account can't see; there's no privilege escalation here.
- Handle exported personal data lawfully and preserve integrity (hashes, read-only storage) if it's evidence.

## Overlaps ("do both")
- Pairs with broad username-search and social-media archiving tools — this preserves the *conversation*, while those map the *identities* of the people in it.

## Trust & verifiability
`trust: community` — a well-regarded, actively maintained open-source project in Bellingcat's toolkit; the export is a faithful capture of what your account sees, so trust rests on your access legitimacy and on preserving the file's integrity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discord-chat-exporter |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → username, social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
