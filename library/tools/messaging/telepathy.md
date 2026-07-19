---
id: telepathy
name: Telepathy
description: Use when you have a Telegram channel/group or `username` and want to archive and analyze it at scale — returns member lists, message archives, forward maps and user activity.
url: https://github.com/proseltd/Telepathy-Community
category: messaging
path:
- messaging
bestFor: Command-line archiving and analysis of Telegram chats — member lists, message history, top posters, and forward/edge mapping.
selectorsIn:
- username
- social-profile
selectorsOut:
- username
- name
- associate
- geolocation
status: live
pricing: free
costNote: Free and open-source (MIT) Community edition installable via pip; a commercial "Telepathy Pro" exists but the free CLI covers core OSINT needs.
opsec: active
opsecNote: Telepathy operates through YOUR authenticated Telegram account and its API credentials — scanning a group means your account joins/queries it, which admins and anti-bot tooling can detect. Use a dedicated sock-puppet Telegram account and number, never your real identity.
humanInLoop: true
humanInLoopReason:
- api-key
- account-login
bestInteractionPattern: cli
trust: community
trustNote: A well-known Bellingcat-listed toolkit maintained by Prose (proseltd) on GitHub; open-source and actively maintained, though results depend on Telegram's API behavior.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- telepahty
- telegram
- find-telegram-channels-bots-groups
aliases:
- Telepathy-Community
tags:
- bellingcat-toolkit
- telegram
- cli
source: bellingcat-toolkit
lastVerified: '2026-07-19'
enrichment: full
---

# Telepathy

> The "swiss army knife" of Telegram OSINT — a Python CLI that archives chats and dumps member lists, top posters, and forward networks for a target channel or group.

## When to use
You have a Telegram channel/group tied to your case (from `[[find-telegram-channels-bots-groups]]` or a lead) and need more than manual scrolling: a full member list, an archived copy of the message history before it's deleted, an analysis of who posts most, and a map of which channels forward to which. Also useful to enrich a single `username`. Best when a subject or associate is active in Telegram communities.

## How to use it (`bestInteractionPattern`: cli)
1. Register a sock-puppet Telegram account and obtain API credentials (api_id/api_hash) from my.telegram.org.
2. Install Telepathy: `pip install telepathy` (or clone the Community repo and install from source).
3. Authenticate the tool with your sock-puppet account when first run.
4. Run a basic scan on a target: `telepathy -t <channel>` for metadata, participant count, and member list (up to ~5,000).
5. Add `-c` for a comprehensive scan (message archive, reactions, forwards, replies) and `-m` to archive media.
6. Use user lookup and location features to enrich a `username`, and edgelist export to map forward relationships.
7. Pivot: member/`username` lists → cross-platform username checks; forward edges → associated channels/`associate`s; location data → `geolocation`.

## Inputs → Outputs
- **In:** a Telegram channel/group handle or `username` (`social-profile`)
- **Out:** member lists, archived messages, top-poster stats, forward/edge maps, and per-user info (`name`, `associate` links, `geolocation` hints)
- **Empty/negative result looks like:** the group is private/invite-only and your account can't join, or member listing is restricted — Telegram limits visible members on large groups, so a partial list is common, not a failure.

## Gotchas & OpSec
- Requires a real (sock-puppet) Telegram account and API credentials; your account interacts with the target group and can be flagged or banned.
- Large groups cap the visible member list (~5,000) and hide some data; treat exports as partial.
- Legal/ethical: mass-archiving a group collects many uninvolved people's data — keep collection proportionate and lawful.
- OpSec: **active** — never run this from an identity linked to you or the investigation.

## Overlaps ("do both")
- Pairs with `[[find-telegram-channels-bots-groups]]` (discover the channel first) and native `[[telegram]]` review — use Telepathy to bulk-archive and analyze once you've found the right group.

## Trust & verifiability
`trust: community` — an open-source, Bellingcat-referenced toolkit; the data it returns comes straight from Telegram's API, so it's as accurate as Telegram exposes, but archive and cite the raw messages since accounts and groups can vanish.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telepathy |
| category | messaging |
| selectorsIn → selectorsOut | username, social-profile → username, name, associate, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key, account-login) |
