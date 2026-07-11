---
id: maltego-telegram
name: Maltego Telegram
description: Use when you have a `phone`, Telegram `username`, or channel and want to map users, groups, admins, and forwards in Maltego — returns social-profile, associate, and username links.
url: https://github.com/vognik/maltego-telegram
category: messaging
path:
- messaging
bestFor: Telegram OSINT inside Maltego — resolve a phone to a Telegram user, enumerate group members/admins, and map channel authors and forwarded/related channels.
selectorsIn:
- phone
- username
selectorsOut:
- social-profile
- associate
- username
status: live
pricing: free
costNote: Free and open source (GPL-3.0). Needs the free Maltego client plus your own Telegram API credentials; a paid Maltego tier isn't required for the community client.
opsec: active
opsecNote: Transforms authenticate with YOUR Telegram account/API credentials and actively query Telegram — resolving a phone can add the target to your contacts and, in some configs, make you visible to them. Use a dedicated sock-puppet Telegram account and burner API credentials, and understand each transform before running it against a live target.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: desktop-app
trust: community
trustNote: Community open-source Maltego transform set on GitHub; it uses Telegram's own API (data is authoritative), but the tooling is third-party and unmaintained-risk.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- telegram-nearby-map
- maltego
aliases:
- maltego-telegram
- vognik telegram transforms
tags:
- telegram
- maltego
- messaging
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Maltego Telegram

> A set of open-source Maltego transforms for Telegram investigations — pivot from a phone or username into users, groups, admins, channel authors, and forwarded-channel networks, visualized as a graph.

## When to use
You have a `phone` number, a Telegram `username`, or a channel/group and want to map the surrounding Telegram network graphically. Telegram is a key channel in many investigations; these transforms let you resolve a phone to a Telegram account, list a group's members/admins, identify channel authors, and follow forwards to related channels — surfacing `associate` clusters and alternate `username`s. Best when you already run Maltego and want Telegram nodes in the same graph.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Maltego (community edition is fine) and clone `https://github.com/vognik/maltego-telegram`.
2. `pip install` the Python dependencies; create Telegram API credentials (`api_id`/`api_hash`) on a **sock-puppet** account and put them in `config.ini` (plus a bot token where required).
3. Authenticate with `login.py`, generate the transform files with `project.py`, and import them into Maltego.
4. Drop a phone/username/channel entity onto the Maltego graph and run the relevant transforms (phone→user, group→members/admins, channel→authors/forwards).
5. Read the graph and pivot: members/admins are `associate` leads; discovered usernames feed cross-platform username tools; forwarded channels map an information network.

## Inputs → Outputs
- **In:** `phone`, Telegram `username`, or channel/group
- **Out:** `social-profile` (Telegram user info), `associate` links (group members, admins, channel authors), alternate `username`s, related/forwarded channels
- **Empty/negative result looks like:** phone→user resolves to nothing (the number isn't on Telegram, or privacy settings hide it), or a group returns no members (admin-restricted visibility) — absence reflects Telegram privacy settings, not necessarily a real negative.

## Gotchas & OpSec
- **Active and attributable:** transforms run under your Telegram account. Resolving a phone typically adds it to your contacts and may expose your sock-puppet to the target — segregate identity and infrastructure.
- Requires API credentials and setup steps; keep everything on burner accounts.
- Telegram privacy settings (hidden phone, restricted membership lists) limit results; don't over-read gaps.
- OpSec: treat as **active** throughout.

## Overlaps ("do both")
- Pairs with [[telegram-nearby-map]] (geolocation of nearby users) and the broader [[maltego]] transform ecosystem — combine Telegram graph data with other selectors in one investigation canvas.

## Trust & verifiability
`trust: community` — an unofficial open-source transform set built on Telegram's own API. The underlying data is authoritative (from Telegram); the tooling is community-maintained, so verify critical findings directly in a Telegram client.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maltego-telegram |
| category | messaging |
| selectorsIn → selectorsOut | phone, username → social-profile, associate, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | yes (api-key) |
