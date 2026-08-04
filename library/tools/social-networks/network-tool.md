---
id: network-tool
name: OSoMeNet (OSoMe Network Tool)
description: Use when you have a hashtag, keyword, or `username` and want to see how content spreads between accounts — returns an interactive diffusion/co-occurrence network of social-profiles and associates.
url: https://osome.iu.edu/tools/networks/#/
category: social-networks
path:
- social-networks
bestFor: Visualizing who amplifies whom around a topic or account to spot coordinated networks and key connectors.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free academic tool from Indiana University's Observatory on Social Media.
opsec: passive
opsecNote: OSoMeNet builds the graph via the platforms' own search APIs on the server side — you don't contact any subject directly, so it is passive toward targets. Your queries sit with a university research service; no login is required for the public tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by OSoMe at Indiana University, a reputable disinformation-research center; coverage depends on the platforms' search APIs, which can change and limit what's retrievable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- botometer
- botometer-by-osome
- botslayer
- covaxxy
- osome-iu-edu
- trends-tool
aliases:
- OSoMeNet
- OSoMe Networks
tags:
- network-analysis
- social-media
- diffusion
- disinformation
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# OSoMeNet (OSoMe Network Tool)

> An academic network-visualization tool that maps how a topic or account propagates across social media — turning a hashtag or username into a diffusion graph of who amplifies whom.

## When to use
You are investigating a topic, campaign, or account and want to see the *structure* around it: which accounts spread a hashtag, who mentions/replies to a target `username`, and which nodes act as hubs or bridges. This is the move for spotting coordinated amplification, bot clusters, and the key connectors linking a subject to `associate` accounts — the relationship view that a flat search can't give you.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osome.iu.edu/tools/networks/ (OSoMeNet).
2. Choose the platform and query type, then enter a hashtag/keyword or a target `username`.
3. Generate the network — OSoMeNet builds a **diffusion** network (edges = posts linking users, e.g. mentions/replies) or a **co-occurrence** network, rendered interactively.
4. Explore: hubs are high-influence amplifiers; tight clusters can indicate coordination; the timeline lets you scrub how the network grew and animate its evolution.
5. Pivot: pull the `social-profile`/`associate` accounts of interest (hubs, bridges) into profile-level OSINT and bot-scoring tools.

## Inputs → Outputs
- **In:** hashtag/keyword, or `username` / `social-profile`
- **Out:** an interactive network of `social-profile`s and their `associate` links, with a diffusion timeline
- **Empty/negative result looks like:** a sparse or empty graph — the query had little activity, or (more often) the platform's search API returned limited data; a thin graph is not proof the topic wasn't discussed.

## Gotchas & OpSec
- Human-in-the-loop: none; no login for the public tool.
- OpSec: **passive** — the graph is built server-side via platform APIs, so no request reaches the subject.
- API dependency: what OSoMeNet can retrieve is bounded by the social platforms' current search-API access, which has tightened over time — coverage and recency vary by platform. Treat gaps as data-access limits, not ground truth.

## Overlaps ("do both")
- Pairs with [[botometer]] / [[botslayer]] — OSoMeNet shows the *shape* of amplification while Botometer scores whether individual accounts in it are likely bots; run the graph first, then score the hubs. Also complements [[trends-tool]] for the volume-over-time view.

## Trust & verifiability
`trust: trusted` — an academic tool from Indiana University's OSoMe; the visualization faithfully reflects the API data it pulled, but that data is only as complete as the platform allows, so state coverage limits alongside any finding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | network-tool |
