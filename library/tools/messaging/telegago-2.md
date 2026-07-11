---
id: telegago-2
name: Telegago
description: Use when you have a `name`, `username`, keyword, or phone and want to find public Telegram content mentioning it — a Google Custom Search Engine over t.me returning channels, groups, and messages.
url: https://cse.google.com/cse?q=+&cx=006368593537057042503:efxu7xprihg#gsc.tab=0&gsc.q=%20&gsc.page=1
category: messaging
path:
- messaging
bestFor: Keyword/username searching public Telegram channels, groups, and messages via Google — no Telegram account needed.
selectorsIn:
- username
- name
- phone
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account, no Telegram login.
opsec: passive
opsecNote: You query Google, not Telegram — the target's channels are not touched and you leave no footprint on Telegram. Standard Google-query privacy applies; use a clean session for sensitive terms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely-used, Bellingcat-referenced Google CSE scoped to Telegram's public web domains; results are only as complete as Google's index of t.me.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Telegago Telegram search
tags:
- telegram
- search-engine
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Telegago

> A Google Custom Search Engine aimed at Telegram's public web (t.me): search channels, groups, and messages by keyword without a Telegram account.

## When to use
You have a `username`, `name`, keyword, `phone`, or handle and want to know where it surfaces in public Telegram content — which is notoriously hard to search inside Telegram itself. Telegago leans on Google's index of Telegram's public web preview pages (t.me / telegram.me) so you can find channels a subject runs or is discussed in, leaked-data groups, and message mentions, all without logging in.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Telegago CSE (https://cse.google.com/cse?cx=006368593537057042503:efxu7xprihg).
2. Enter your term — a username, real name, keyword, phone number, or channel name. Use Google operators (quotes, `-`, `site:t.me/...`) to refine.
3. Read results: links to public channels/groups and indexed messages.
4. Open promising `t.me` links (in a sock-puppet browser) to confirm and read; note channel handles and admins.
5. Pivot: a discovered channel/username feeds broader username mapping; message content feeds timeline and `associate` work; a phone hit corroborates a Telegram account.

## Inputs → Outputs
- **In:** `username` / `name` / keyword / `phone`
- **Out:** public Telegram `social-profile`s (channels/groups) and indexed message mentions
- **Empty/negative result looks like:** no results. This means Google hasn't indexed matching public t.me content — private channels, un-previewed groups, and deleted content never appear. Absence is NOT proof the subject has no Telegram presence; it's proof nothing public was indexed.

## Gotchas & OpSec
- Coverage is bounded by Google's crawl of Telegram's public preview pages — a lot of Telegram is invisible here.
- OpSec: **passive** — you query Google, not Telegram, so no footprint on the target's channels.
- For a real Telegram account/handle you already have, complement with in-app or API-based tools that Telegago can't reach.

## Overlaps ("do both")
- Pairs with dedicated Telegram tools (Telemetryapp/Telepathy-style) and general dorking — Telegago is fast for discovery, those go deeper on a known channel/handle for membership and history.

## Trust & verifiability
`trust: community` — a well-known community CSE; results are real Google-indexed Telegram pages, so verify each by opening the live t.me link before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegago-2 |
| category | messaging |
| selectorsIn → selectorsOut | username, name, phone → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
