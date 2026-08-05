---
id: paterva-maltego
name: Maltego (Paterva)
description: Use when you have a seed selector (`email`, `domain`, `ip-address`, `name`, `phone`) and want to fan out and map its relationships across many data providers — returns a visual link graph of connected entities.
url: https://www.maltego.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Visual link-analysis of a subject across many data sources — mapping how emails, domains, people, and infrastructure connect.
selectorsIn:
- email
- domain
- ip-address
- name
- phone
selectorsOut:
- email
- domain
- ip-address
- social-profile
- associate
status: live
pricing: freemium
costNote: Free Community Edition (account required) with capped transform results and no commercial use; paid Pro/Enterprise unlock more transforms, higher limits, and premium data providers.
opsec: active
opsecNote: Transforms query external data providers about your entities — many are passive OSINT lookups, but some touch the target's own infrastructure (DNS, ports, active checks), and the results pass through Maltego/provider servers. Run sensitive investigations with care over which transforms you fire, and use a controlled network.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: desktop-app
trust: trusted
trustNote: The de-facto standard OSINT link-analysis platform (originally Paterva); the tool is reputable, but output quality depends on which third-party transforms/data providers you enable.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- maltego
- opengraph-intel-ogi
aliases:
- Paterva
- Maltego CE
- Maltego Community Edition
tags:
- link-analysis
- graph
- osint-platform
- relationship-mapping
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Maltego (Paterva)

> The flagship OSINT link-analysis platform: drop a seed entity onto a graph, run "transforms" that pull from scores of data providers, and watch the relationships between people, accounts, domains, and infrastructure resolve into a visual web.

## When to use
When an investigation has enough interconnected selectors — an `email`, `domain`, `ip-address`, `name`, or `phone` and the entities around them — that you need to *see* the relationships, not track them in notes. Maltego is the tool for correlation-heavy cases: mapping a subject's infrastructure, linking accounts and associates, and spotting the non-obvious connection. The free Community Edition covers learning and light casework.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Maltego (desktop client) from https://www.maltego.com/ and sign in — the free Community Edition requires an account and caps transform results (~12 per run).
2. Drop a seed entity (email, domain, IP, person, phone) onto a new graph.
3. Run transforms on it — each queries a data provider and adds connected entities/edges (DNS, WHOIS, breach data, social, etc.). Enable the transform hubs/providers you need.
4. Iterate outward from promising nodes; read the graph for clusters and bridges. Export the graph/report.
5. Pivot: a surfaced account, domain, or associate becomes the next seed, or a handoff to a specialist tool.

## Inputs → Outputs
- **In:** a seed `email`/`domain`/`ip-address`/`name`/`phone`
- **Out:** a visual relationship graph of connected `email`s, `domain`s, `ip-address`es, `social-profile`s, and `associate`s
- **Empty/negative result looks like:** transforms return no new entities — either the seed is genuinely isolated, or you have not enabled a data provider that covers it (CE's limits also cap breadth); try more/different transforms before concluding.

## Gotchas & OpSec
- Human-in-the-loop: account login required; Community Edition throttles results and forbids commercial use.
- OpSec: **mixed** — most transforms are passive OSINT, but some make active queries against the target's infrastructure, and all pass through Maltego/provider servers. Choose transforms deliberately on sensitive cases.
- Output quality = transform/provider quality; some premium data needs paid subscriptions, and free transforms vary — verify key edges at their source.

## Overlaps ("do both")
- Pairs with the open-source [[opengraph-intel-ogi]] — Maltego has the deepest transform ecosystem, OGI is a free self-hosted alternative when you cannot send data through third-party providers; use OGI for privacy-sensitive graphs, Maltego for reach.

## Trust & verifiability
`trust: trusted` — the mature, widely adopted standard for OSINT link analysis. The platform is reputable; the caveat is that each edge is only as good as the transform/provider that produced it, so confirm decisive links at the primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | paterva-maltego |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | email, domain, ip-address, name, phone → email, domain, ip-address, social-profile, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | yes (account-login) |
