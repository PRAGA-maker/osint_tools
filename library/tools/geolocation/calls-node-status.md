---
id: calls-node-status
name: Calls Node Status
description: Use when you have a `geolocation` or a radio system of interest and want to see which Broadcastify Calls ingest nodes are live and recently active — returns geolocation and device-id (node) leads.
url: https://www.broadcastify.com/calls/status/
category: geolocation
path:
- geolocation
bestFor: Checking which Broadcastify Calls ingest nodes are online and when each last relayed radio traffic.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- device-id
status: live
pricing: freemium
costNote: The status page is free to view. Listening to some Calls feeds/archives may require a free account or Premium subscription.
opsec: passive
opsecNote: Read-only public dashboard; viewing it reveals nothing about your target and touches only Broadcastify's own infrastructure. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: First-party status page operated by Broadcastify (RadioReference); the node list itself is authoritative for their network, though coverage depends on volunteer ingest operators.
missingPersonsRelevance: low
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- broadcastify
aliases:
- Broadcastify Calls Node Status
tags:
- radio
- scanner
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Calls Node Status

> Broadcastify's live dashboard of Calls ingest nodes — a quick way to see whether radio-call coverage exists and is currently active for a given area or trunked system.

## When to use
You're using Broadcastify Calls (recorded public-safety/land-mobile radio calls) to place activity in a `geolocation`, and you need to confirm that a covering ingest node is actually online and relaying — not stale. The status page lists 900+ trunked and 100+ conventional nodes with last-active timestamps, so you can tell whether the silence you're hearing means "nothing happening" versus "the feed for that area is down". Also useful to identify which node/system covers a region before diving into archives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.broadcastify.com/calls/status/.
2. Scan the trunked-systems and conventional-systems lists for the node/system covering your area of interest.
3. Read each node's **last active** timestamp — a recent time means live coverage; a stale one means the volunteer feed is offline.
4. Follow through to the Calls coverage map / archives / playlists for the live or recorded audio itself.
5. Pivot: a confirmed live node → monitor `[[broadcastify]]` Calls feeds/archives for that system; correlate call timing with your subject's known location/timeline.

## Inputs → Outputs
- **In:** a `geolocation` / region or a known radio system
- **Out:** node online/offline state, last-active timestamp, node type (trunked vs conventional) — a coverage/`device-id` indicator per ingest node
- **Empty/negative result looks like:** no node listed for your area, or a node with a very old last-active time — means there is no usable Broadcastify Calls coverage there, not that no radio activity exists.

## Gotchas & OpSec
- No login needed to view status; listening to certain feeds/archives may require a free account or Premium.
- OpSec: fully passive — a public read-only dashboard about Broadcastify's own network; nothing reaches your target.
- Coverage is volunteer-driven and patchy; absence of a node is common in rural areas.

## Overlaps ("do both")
- Pairs with `[[broadcastify]]` — this tells you whether a node is live; Broadcastify Calls itself gives you the audio/archives for that node.

## Trust & verifiability
`trust: community` — first-party Broadcastify status page (authoritative for their node network), but the underlying coverage depends on volunteer ingest operators, so treat gaps as coverage gaps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | calls-node-status |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, device-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
