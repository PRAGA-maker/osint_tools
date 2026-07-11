---
id: osintgraph
name: Osintgraph
description: Use when you have an Instagram `username` and want to map the subject's follower/followee network to surface close ties — returns a Neo4j graph of connections and AI-summarized profiles.
url: https://github.com/XD-MHLOO/Osintgraph
category: social-networks
path:
- social-networks
bestFor: Building and visualizing a target's Instagram social graph to find mutual connections and close associates.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- name
status: live
pricing: free
costNote: Free open-source tool. Neo4j has a free tier; optional Gemini AI analysis needs your own (free-tier-capable) API key.
opsec: active
opsecNote: Scraping requires logging into Instagram; the account you use follows/reads targets and WILL be rate-limited or banned, and Instagram may flag the activity to the target's account. Use a dedicated sock-puppet Instagram account, a residential-looking User-Agent, and slow collection — never your real account.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source project on GitHub (XD-MHLOO); code is inspectable but unofficial, relies on scraping that breaks when Instagram changes, and carries account-ban risk.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
aliases:
- OSINTGraph
- Instagram graph OSINT
tags:
- instagram
- social-graph
- neo4j
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Osintgraph

> A self-hosted tool that scrapes an Instagram target's followers/followees into a Neo4j graph — use it to see the *shape* of a subject's network and surface the people closest to them.

## When to use
You have an Instagram `username` and want more than a profile snapshot — you want the relationship graph: who they follow, who follows back, and which accounts sit at the center of their circle. Mutual connections and tightly-linked nodes are strong `associate` leads for a locate case, where the fastest route to a missing person is often the people around them. Reach for this when a single-profile view has stalled and you need the network.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/XD-MHLOO/Osintgraph` and install its Python dependencies; stand up a Neo4j instance (free tier works).
2. Configure a **sock-puppet Instagram account** (not your primary), optionally a custom User-Agent, and optionally a Gemini API key for AI analysis.
3. Phase 1 (recon): run the collector against the target `username` — it scrapes profile metadata, followers, followees, posts, and comments into Neo4j.
4. Phase 2 (analysis): explore the graph directly in Neo4j's browser, or query it via the tool's natural-language AI agent. Look for dense clusters and mutual-follow pairs.
5. Pivot: promising `associate` nodes and `name`s from bios feed people-search, face, and other social tools.

## Inputs → Outputs
- **In:** `username` (Instagram)
- **Out:** a graph of `social-profile` nodes and follow relationships, candidate `associate`s, and `name`s / AI summaries from profiles
- **Empty/negative result looks like:** collection stalls or returns almost nothing — usually a private target, a rate-limited/banned sock account, or Instagram changing its endpoints. Not proof the network is small; re-run with a fresh account and slower pacing.

## Gotchas & OpSec
- Human-in-the-loop: requires an Instagram **login** and (for AI features) an **API key**; setup is technical (Neo4j, Python).
- OpSec: **active and account-risky** — scraping violates Instagram's ToS, gets accounts limited/banned, and the follows/views can surface to the target. Sock puppet only, slow collection, expect to burn accounts.
- Scraping tools rot fast; if collection breaks, check the repo for updates before assuming the target has no data.

## Overlaps ("do both")
- Pairs with single-profile Instagram tools and `[[dolphin-radar]]`-style analytics — those describe one account; this maps the surrounding network to find who matters.

## Trust & verifiability
`trust: community` — open-source and inspectable, but unofficial, scraping-dependent, and fragile; verify any specific relationship by viewing it directly on Instagram before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintgraph |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, api-key) |
