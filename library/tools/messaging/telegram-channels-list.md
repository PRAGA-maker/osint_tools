---
id: telegram-channels-list
name: Telegram Channels List (tlgrm.eu)
description: Use when you have a topic/keyword and want to discover public Telegram channels around it — returns social-profile and username.
url: https://tlgrm.eu/channels
category: messaging
path:
- messaging
bestFor: Browsing a categorised directory of public Telegram channels to find communities relevant to a subject or event.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free public directory; no account required to browse.
opsec: passive
opsecNote: Browsing the directory is passive. Opening a listed channel inside a real Telegram account exposes your identity to that channel's admins/analytics — use a sock-puppet Telegram account and viewer.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party channel catalog (tlgrm.eu); listings are submitted/curated and not exhaustive of Telegram.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- tlgrm-eu-channels
aliases:
- tlgrm.eu channels
- Telegram channel directory
tags:
- telegram
- directory
- messaging
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Telegram Channels List (tlgrm.eu)

> A browsable catalogue of public Telegram channels — a starting point for finding the communities, local groups, or topic channels a subject might inhabit.

## When to use
You want to map the Telegram landscape around a subject, place, or event — local news channels, regional groups, hobby/interest communities, or a channel a person is known to run. Browsing by category surfaces public channels (`social-profile`) and their handles (`username`) you can then monitor or search from a sock-puppet account. Best treated as a discovery index; it will not find private groups or every channel.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tlgrm.eu/channels and browse the category tree (News, Politics, Technology, Education, etc.), or use its channel search.
2. Note candidate channels — name, @handle, subscriber count, description.
3. Open promising channels **inside a sock-puppet Telegram** (or a web viewer) to read content and member/admin signals.
4. Pivot: a channel `@handle` → search its posts for the subject; admin/owner handles → `username`/`social-profile` OSINT; linked chat groups → membership analysis.

## Inputs → Outputs
- **In:** topic keyword, `name`, or a known `username`
- **Out:** `social-profile` (channels), `username` (@handles)
- **Empty/negative result looks like:** no listed channel matches the topic/handle — the directory simply hasn't indexed it (many channels are unlisted); search directly in Telegram and via other channel-search tools.

## Gotchas & OpSec
- Coverage is partial — a channel's absence here means nothing; the directory only holds submitted/curated public channels.
- OpSec: browsing the web directory is passive, but **joining or opening channels ties activity to your Telegram identity** — always use a dedicated sock-puppet account.
- No adult/private content is listed.

## Overlaps ("do both")
- Pairs with keyword-based Telegram search tools and channel analytics (e.g. Telemetr-style) — this is the browse-by-category discovery layer; those add full-text post search and subscriber/growth analytics.

## Trust & verifiability
`trust: community` — a third-party curated catalogue; a listing confirms a channel exists publicly but nothing about its authenticity or the accuracy of its content — verify in Telegram directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-channels-list |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
