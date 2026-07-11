---
id: groupio
name: Groupio
description: Use when you have a topic, tag, or language and want to find public WhatsApp groups a subject may belong to — returns group listings with member counts and join links.
url: https://en.groupio.app/
category: messaging
path:
- messaging
bestFor: Discovering public WhatsApp groups by category, tag, or language to locate a subject's community presence.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public directory; no account needed to browse or search.
opsec: passive
opsecNote: Searching the directory is passive and does not touch the target. Opening/joining a listed WhatsApp group loads it in WhatsApp under your account and exposes your number/username to that group — join only from a sock-puppet WhatsApp account, and prefer reading over participating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Multi-language, user-submitted WhatsApp group directory; listings are self-promoted and unvetted, so coverage is partial and each hit must be verified inside WhatsApp.
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
- Groupio
- groupio.app
tags:
- whatsapp
- group-discovery
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Groupio

> A multilingual directory of public WhatsApp groups — search by category, tag, age range, or language to find the communities a subject frequents, then pivot into WhatsApp.

## When to use
You think a subject participates in public WhatsApp groups tied to an interest, fandom, marketplace, or language community, and you want to find those groups without an invite link. Especially useful where WhatsApp is the dominant platform and a subject is thin on mainstream social media. It's a discovery step: it points at rooms, and the members/admins inside are the leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.groupio.app/ (multi-language).
2. Browse or filter by **category** (general, gaming, fan, flea market, music, self-help, friendship, adult…), **tag** (e.g. #anime, #gaming), **age range**, and **language**.
3. Read each listing: group name, description, member count, update date, tags, and a join link.
4. Pivot: open a promising group in a sock-puppet WhatsApp account; read the admin number/handle, participants, and pinned info for the subject; feed numbers/handles into phone/username tools.

## Inputs → Outputs
- **In:** a topic/tag/language tied to a `name` or `username`
- **Out:** WhatsApp group listings (`social-profile` leads) with member counts and join links
- **Empty/negative result looks like:** only generic self-promoted groups match — the directory hasn't indexed the subject's group (owners self-submit), not proof it doesn't exist. Cross-check WhatsApp's in-app search and other directories.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; joining needs a WhatsApp account.
- Listings are **self-submitted and unmoderated** — expect dead invites, spam, and mislabeled/adult content. Verify identity inside the group before attributing.
- OpSec: browsing is passive; **joining exposes your account** — use a sock puppet and prefer read-only.

## Overlaps ("do both")
- Pairs with `[[wachannelsfinder-com]]` (WhatsApp channels) and `[[groupda]]` (Telegram/WhatsApp groups) — each indexes a different self-submitted slice, so run several to widen coverage.

## Trust & verifiability
`trust: community` — a user-submitted directory; treat every hit as a lead to confirm inside WhatsApp, not as verified attribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | groupio |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
