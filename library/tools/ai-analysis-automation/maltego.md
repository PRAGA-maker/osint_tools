---
id: maltego
name: Maltego
description: Use when you have any entity (`name`, `email`, `username`, `phone`, `domain`, `ip-address`) and want to build and expand a link-analysis graph via transforms — returns connected names, emails, social-profiles, associates, domains and IPs.
url: https://maltego.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Visual link analysis — connecting people, emails, domains, social profiles, phones and infrastructure into an entity-relationship graph using transforms.
selectorsIn:
- name
- email
- username
- phone
- domain
- ip-address
- social-profile
selectorsOut:
- name
- email
- social-profile
- associate
- domain
- ip-address
status: live
pricing: freemium
costNote: Community Edition (CE) is free but limited (registration required, ~12 results per transform, no commercial use). Maltego Pro/Enterprise and many premium transform hubs are paid subscriptions, sometimes with per-query API costs from data providers.
opsec: active
opsecNote: Transforms call out to external data providers and target infrastructure (DNS, WHOIS, social APIs), so queries leave your environment and some touch the target's assets. Run from a research environment/VPN, mind which transform hubs you enable (they send your selectors to third parties), and avoid transforms that actively probe a target you shouldn't touch.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Industry-standard link-analysis platform used across OSINT, security and law-enforcement; the app is trusted, though the quality of any result depends on the specific transform/data provider behind it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
aliases:
- Maltego CE
- Maltego Community Edition
tags:
- link-analysis
- graph
- transforms
- entity-mapping
source: gh-topic-footprinting
lastVerified: '2026-07-10'
enrichment: full
---

# Maltego

> The industry-standard link-analysis platform — drop in a person, email, domain or handle and run "transforms" to expand it into a visual graph of connected people, accounts and infrastructure.

## When to use
You have one or more selectors on a subject and want to see and expand the relationships between them: from an `email` to linked social accounts, from a `name` to associates, from a `domain` to its infrastructure and registrants. Maltego shines when a case has grown beyond a checklist and you need a graph to spot connections, overlaps and pivots across many data sources at once — the classic "map the whole network around a missing person" task.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Maltego, register a free Community Edition account (or use a paid tier for higher limits).
2. Enable relevant transform hubs (many free ones exist; premium hubs need keys/subscriptions).
3. Drag an entity onto the graph (e.g. an `email`, `name`, `domain`) and run transforms to expand it.
4. Iterate: run transforms on the new nodes to grow the graph; use the graph to spot shared infrastructure, mutual associates, and cross-links.
5. Extract findings — connected `social-profile`s, `associate`s, `domain`s, `ip-address`es — and export the graph for reporting.

## Inputs → Outputs
- **In:** `name`, `email`, `username`, `phone`, `domain`, `ip-address`, `social-profile`
- **Out:** `name`, `email`, `social-profile`, `associate`, `domain`, `ip-address` (connected entities revealed by transforms)
- **Empty/negative result looks like:** transforms return no new nodes — usually because you haven't enabled a data source that covers that selector, or the entity genuinely has no linked data in the queried providers; try more/other transform hubs before concluding.

## Gotchas & OpSec
- **CE limits:** free edition caps results per transform and forbids commercial use; deep work needs a paid tier.
- Results are only as good as the transforms/providers enabled — coverage is modular, so a "nothing found" may just mean the right hub isn't installed.
- **Active:** transforms send your selectors to third parties and some probe target infrastructure — control which hubs are enabled and run from a research environment.

## Overlaps ("do both")
- Pairs with SpiderFoot (automated collection) and the individual selector tools in this library — use those to gather raw leads, then Maltego to visualise and connect them into one graph.

## Trust & verifiability
`trust: trusted` — a mature, standard platform; the app is reliable, but always attribute and verify a finding to the specific transform/data source that produced it, since provider data quality varies.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maltego |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, email, username, phone, domain, ip-address, social-profile → name, email, social-profile, associate, domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | yes (account-login) |
