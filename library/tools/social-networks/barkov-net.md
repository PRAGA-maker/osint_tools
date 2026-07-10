---
id: barkov-net
name: Barkov.net (VK Target Audience Tools)
description: Use when you have a VKontakte/OK/Telegram community, user list or profile criteria and want to enumerate and filter users — returns `social-profile`s and `associate` links, filtered by age/location/interests.
url: http://vk.barkov.net
category: social-networks
path:
- social-networks
bestFor: Large-scale VKontakte (and OK/Telegram) audience analysis — finding users across communities, filtering by profile attributes, and cross-referencing linked accounts.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Free tier covers small tasks; larger audience pulls and advanced scripts require a paid subscription. Requires a VK login to run most tools.
opsec: active
opsecNote: Running tools requires connecting a VK account, which ties activity to that identity and can trip VK's automation defenses. Use a sock-puppet VK account, never your own. It is a Russian-jurisdiction marketing service that processes VK data at scale.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established (since 2014) Russian VK-marketing toolkit with 1M+ users; repurposed for OSINT. Data comes from VK's own API, so it's as good as VK's data, but the interface is Russian and marketing-oriented.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- vk.barkov.net
- Barkov target audience
tags:
- vkontakte
- vk
- social-networks
- russia
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Barkov.net (VK Target Audience Tools)

> A 300-tool Russian marketing suite for VKontakte (plus OK and Telegram) — built to find and filter audiences, which doubles as powerful VK people-enumeration for OSINT.

## When to use
Your subject has a VKontakte presence (or you're mapping a VK community they belong to) and you want to enumerate members, filter users by profile attributes (age, city, relationship status, interests), or find which communities a user belongs to. VK is the dominant social network across the Russian-speaking world, so this is high-value for locating Russian/CIS subjects and mapping their social graph. Best when you need scale beyond manual VK browsing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://vk.barkov.net (Russian interface — use a translation layer). Register and connect a **sock-puppet VK account**.
2. Pick a tool: "find users in communities," "filter users by criteria," "find a user's communities/friends," or cross-account linking (VK↔Instagram/Twitter/Skype).
3. Provide input: a community URL/ID, a list of user IDs, or filter criteria; run the tool (free tier limits result size).
4. Read/export the structured output: user IDs, profiles (`social-profile`), and links between them (`associate`).
5. Pivot: filtered users → individual VK profiles; a subject's communities → interests/location; linked Instagram/Twitter → cross-platform enumeration.

## Inputs → Outputs
- **In:** `username`/VK ID, community, or filter criteria (`name`, city, age, interests)
- **Out:** `social-profile` (VK/OK users), `associate` (members, friends, co-community links), exportable lists
- **Empty/negative result looks like:** an empty export or a paywall/limit prompt on the free tier. Empty can mean the criteria are too narrow, the community is closed, or you've hit free-tier caps — not that no users exist.

## Gotchas & OpSec
- **Russian-only** interface and marketing framing — expect a learning curve and translation friction.
- **Login required** and rate-sensitive — VK may flag automation; puppet account essential.
- Free tier is capped; large pulls need payment.
- OpSec: **active** — tools run under your connected VK account.

## Overlaps ("do both")
- Pairs with VK's native search and other VK-OSINT tools (`[[vk-community-search]]`-style) — Barkov adds scale/filtering the native UI lacks.

## Trust & verifiability
`trust: community` — a mature, widely used VK toolkit drawing on VK's own API, so data quality tracks VK. Cross-check individual profiles directly on VK, and be mindful of the Russian-jurisdiction data handling.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | barkov-net |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
