---
id: maltego-transforms-m0m0sms-osint
name: Maltego transforms (M0m0SMS-OSINT)
description: Use when you are running link analysis in Maltego and want a big curated index of community transforms to install — returns a menu of transform repos that turn selectors into graphed relationships.
url: https://github.com/M0m0SMS-OSINT/Maltego
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Extending Maltego with community transforms so selectors (domain, email, IP, handle) expand into graphed entities and relationships.
selectorsIn:
- domain
- email
- ip-address
- username
selectorsOut:
- domain
- email
- ip-address
- associate
- social-profile
status: live
pricing: freemium
costNote: The transform index is a free GitHub repo; running it needs Maltego (Community Edition is free with entity/result limits; commercial tiers are paid).
opsec: active
opsecNote: Transforms make live queries to third-party APIs/services about your selectors (Shodan, VirusTotal, crt.sh, social APIs, etc.). Those lookups can be logged by each provider and some touch the target's infrastructure — know what each transform does before running it, and use API keys/accounts that aren't attributable.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: desktop-app
trust: community
trustNote: A community-maintained meta-index (100+ submodules, ~159 stars) of third-party Maltego transforms; last major update 2018, so many linked transforms need vetting and may be outdated.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
aliases:
- M0m0SMS-OSINT Maltego
- Maltego transform collection
tags:
- maltego
- transforms
- link-analysis
- graph
source: gh-topic-osint-framework
lastVerified: '2026-07-21'
enrichment: full
---

# Maltego transforms (M0m0SMS-OSINT)

> A curated index of 100+ community Maltego transform repositories — the shopping list for turning Maltego into a link-analysis powerhouse across infrastructure, breach, blockchain, and social selectors.

## When to use
You do (or want to do) graph-based link analysis in Maltego and need transforms beyond the built-ins — Shodan/Censys for infrastructure, crt.sh/PDNS for domains, blockchain explorers for crypto, social transforms for handles. This repo aggregates the community's transforms so you can find and install the ones that expand your specific selector. Reach for it when a case has many interlinked entities (domains ↔ emails ↔ people ↔ infra) and you want them mapped visually.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Maltego (Community Edition is free; register an account).
2. Browse https://github.com/M0m0SMS-OSINT/Maltego and pick transform repos matching your need (each is a submodule/link).
3. Follow that transform's own README to install it (local transform or TDS) and supply any required API keys.
4. In Maltego, drop your starting entity (a `domain`, `email`, `ip-address`, `username`) and run the transform to expand related entities.
5. Pivot: graphed relationships surface new `associate`s, linked `domain`s/`email`s, and `social-profile`s to run further transforms on.

## Inputs → Outputs
- **In:** a seed selector — `domain`, `email`, `ip-address`, `username`
- **Out:** a relationship graph → linked `domain`s, `email`s, `ip-address`es, `associate`s, `social-profile`s
- **Empty/negative result looks like:** a transform returns no new entities — the selector may have no data at that source, the transform may be outdated/broken, or you're missing an API key (many silently fail without one).

## Gotchas & OpSec
- Aggregation, not code: it's an index of third-party transforms — each has its own install steps, maintenance state, and trust profile; vet before running.
- Dated (2018): expect broken links and deprecated transforms; verify each still works.
- Many transforms need API keys (human-in-the-loop) and make live external queries — some touch the target's infra (active). Understand each before firing it.
- Maltego CE has entity/result caps that limit large graphs.

## Overlaps ("do both")
- Pairs with standalone recon tools (Shodan, crt.sh, breach-search) and other OSINT frameworks — the transforms wrap many such services into one graph; use the standalone tool when you need depth a transform doesn't expose.

## Trust & verifiability
`trust: community` — a community meta-index of third-party transforms; the transforms' outputs are only as reliable as their upstream data sources, so verify graph findings against the underlying tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maltego-transforms-m0m0sms-osint |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, email, ip-address, username → domain, email, ip-address, associate, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | yes (api-key) |
