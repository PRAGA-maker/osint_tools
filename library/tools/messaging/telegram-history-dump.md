---
id: telegram-history-dump
name: telegram-history-dump
description: Use when you have access to a Telegram account and want to export its chat/group history for offline analysis — returns social-profile message logs (JSON/HTML) from dialogs the account can see.
url: https://github.com/tvdstaaij/telegram-history-dump
category: messaging
path:
- messaging
bestFor: Bulk-exporting a Telegram account's own chat and group history to JSON for offline searching.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free and open-source, but depends on telegram-cli, which is largely unmaintained and often broken against the current Telegram API.
opsec: passive
opsecNote: Runs locally against an account you control; it reads history the logged-in account already has access to and does not scrape strangers. Exporting private group content still carries legal/ethical duties — only export what you are authorized to.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Community project (last release 2017); functional only if you can get its telegram-cli dependency working, so verify before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- telegram history dump
tags:
- telegram
- export
- history
source: osintambition-social
lastVerified: '2026-07-23'
enrichment: full
---

# telegram-history-dump

> A Ruby CLI that backs up a logged-in Telegram account's chat and group history to JSON/HTML — useful, but shackled to the aging telegram-cli.

## When to use
You have (lawful) access to a Telegram account — your own, a subject's device you are authorized to examine, or a sanctioned monitoring account inside a group — and you want the full dialog history exported for offline searching and analysis rather than scrolling in-app. It exports what the account can already see; it is **not** a way to read a stranger's private messages.

## How to use it (`bestInteractionPattern`: cli)
1. Build and configure **telegram-cli** with the account, then launch it in JSON mode: `telegram-cli --json -P 9009`. (This dependency is the hard part — it is unmaintained and may not work with the current API.)
2. Install Ruby 2+, clone the repo, and copy `config.example.yaml` to `config.yaml`.
3. Run `./telegram-history-dump.rb`; it pulls dialogs and writes per-chat logs (JSON, HTML, plaintext, or PISG). Re-runs do incremental backups (only new messages).
4. Grep/parse the JSON for usernames, links, media references, and timestamps.
5. Pivot: exported `social-profile` handles/links → Telegram-username OSINT and cross-platform search.

## Inputs → Outputs
- **In:** a logged-in Telegram account (via telegram-cli); optionally a `username`/chat to focus on.
- **Out:** exported chat/group history as JSON/HTML — messages, `social-profile` handles, links, timestamps, media manifests.
- **Empty/negative result looks like:** telegram-cli fails to authenticate or connect (the common failure today), or an empty export because the account has no accessible history — not a data finding, a tooling failure.

## Gotchas & OpSec
- **Fragile dependency:** telegram-cli is effectively unmaintained; if you can't get it running, prefer Telegram Desktop's built-in **Export chat history** or a Telethon-based exporter. That's why this is marked `status: degraded`.
- Only exports what the logged-in account can see — no magic access to closed chats.
- Exporting others' private messages has legal/consent implications; stay within authorization.

## Overlaps ("do both")
- Overlaps with Telegram Desktop's native export and modern Telethon/MTProto dumpers — same goal, but those are actively maintained; use this only if it already works in your environment.

## Trust & verifiability
`trust: community` — an open but dormant project; treat any successful export as authentic to the account, but confirm the tool still functions before depending on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-history-dump |
