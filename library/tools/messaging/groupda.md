---
id: groupda
name: GroupDa
description: Use when you have a topic, country, or language and want to find public Telegram (and WhatsApp) groups a subject may be active in — returns group listings you can pivot to a `social-profile`.
url: https://groupda.com/telegram/group/search
category: messaging
path:
- messaging
bestFor: Discovering public Telegram/WhatsApp groups by category, country, or language to locate a subject's community presence.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public directory; no account or payment required to search or open group links.
opsec: passive
opsecNote: Searching the directory is passive. Joining a linked Telegram group, however, exposes your account to that group's admins and members and may reveal your username to everyone — join only from a sock-puppet Telegram account, and prefer previewing public groups without joining.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running community group-directory populated by user submissions; widely used but unvetted, so links can be stale, mislabeled, or spam.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- groupda.com
tags:
- telegram
- whatsapp
- group-discovery
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# GroupDa

> A searchable directory of public Telegram and WhatsApp groups — use it to find the communities a subject frequents by topic, country, and language, then pivot into the messenger itself.

## When to use
You believe a subject participates in public Telegram/WhatsApp groups tied to an interest, location, or cause, and you want to find those groups without already knowing their invite links. Especially valuable when a subject is thin on mainstream social media but active in messaging communities — a common pattern in many regions and subcultures.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://groupda.com/telegram/group/search (and the WhatsApp equivalent on the same site).
2. Filter by **Category** (gaming, business, dating, entertainment, sports…), **Country**, and **Language**, or search a keyword tied to your subject's interest/location.
3. Browse the feed (use "Load More Group" to page); each entry shows a group name, description, and a Join link.
4. Pivot: open a promising Telegram group in a sock-puppet client, read the member list / admin handles / pinned messages for the subject's `username`, and feed handles into username tools.

## Inputs → Outputs
- **In:** a topic/country/language tied to a `name` or `username`
- **Out:** Telegram/WhatsApp group listings (`social-profile` leads) with links
- **Empty/negative result looks like:** only generic promoted groups match your filter — the directory hasn't indexed your subject's group (owners self-submit), not proof it doesn't exist. Cross-check with native Telegram search and other directories.

## Gotchas & OpSec
- Human-in-the-loop: none to search; joining a group requires a Telegram/WhatsApp account.
- Listings are **self-submitted and unmoderated** — expect dead invites, spam/scam groups, and mislabeled categories. Verify identity inside the group before attributing.
- OpSec: searching is passive; **joining is active and exposes your account**. Use a sock puppet and prefer read-only preview of public channels.

## Overlaps ("do both")
- Pairs with `[[wachannelsfinder-com]]` (WhatsApp channels) and other Telegram directories — each indexes a self-submitted slice, so run several to widen coverage of where a subject might be active.

## Trust & verifiability
`trust: community` — an established, widely-used directory maintained by user submissions; treat every hit as a lead to verify inside Telegram/WhatsApp, not confirmed attribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | groupda |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
