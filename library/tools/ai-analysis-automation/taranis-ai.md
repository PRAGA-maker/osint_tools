---
id: taranis-ai
name: Taranis AI
description: Use when you want to continuously collect and AI-summarize open-source news/feeds into structured intelligence reports — returns a self-hosted OSINT/threat-intel workflow.
url: https://github.com/taranis-ai/taranis-ai
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Self-hosted, AI-assisted aggregation of news/RSS/social sources into deduplicated, analyst-ready threat-intelligence reports.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (EUPL-1.2); no license fee. You supply the hosting (Docker) and any LLM/NLP compute it uses.
opsec: active
opsecNote: This is your own server that fetches configured sources on a schedule — those fetches originate from wherever you host it, so give it an egress you control (VPS/proxy) if source sites shouldn't see your organization's IP. Data stays in your instance, which is good for sensitive collection.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: docker
trust: community
trustNote: Actively developed open-source project (taranis-ai on GitHub, successor to Taranis NG) under EUPL-1.2; auditable code and public releases, community-maintained rather than a commercial vendor.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- Taranis NG
tags:
- threat-intelligence
- news-monitoring
- self-hosted
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Taranis AI

> A self-hosted OSINT collection-and-analysis platform: it ingests news/RSS/social sources, applies NLP/AI to cluster and enrich them, and helps an analyst turn the stream into structured reports.

## When to use
You need standing, repeatable open-source monitoring across many sources — websites, web feeds, email, social/RSS — and want the raw firehose deduplicated, tagged, and summarized so a human can produce intelligence products instead of hand-reading everything. It's infrastructure for continuous SOCMINT/threat-intel monitoring, not a one-off selector lookup; useful when a case needs ongoing coverage of a topic, region, or set of sources.

## How to use it (`bestInteractionPattern`: docker)
1. Deploy from https://github.com/taranis-ai/taranis-ai using the docker-compose deployment guide (core REST API, web frontend, worker, PostgreSQL/SQLite, Redis).
2. Configure collectors: point them at the sources you want (site/`domain` feeds, RSS/Atom, email, social).
3. Let workers gather and the NLP/AI layer cluster, deduplicate, and enrich incoming articles.
4. In the web UI, review the enhanced items, group them into analysis products, and export structured reports/PDFs.
5. Pivot: a clustered story surfaces a name/org/event → hand off to targeted people/records tools; export reports feed a case file.

## Inputs → Outputs
- **In:** configured source feeds (site `domain`s, RSS/Atom, email, social)
- **Out:** deduplicated, AI-enriched news items and analyst-built structured reports/PDFs
- **Empty/negative result looks like:** collectors returning nothing — misconfigured sources, blocked feeds, or a source that stopped publishing; check collector logs rather than assuming no activity.

## Gotchas & OpSec
- Human-in-the-loop: manual-review — the AI enriches and clusters, but analysts must curate and author the final product; also expect real setup/hosting effort (Docker, services).
- Quality: AI summaries can mislead — treat them as triage, verify claims against the original articles before reporting.
- OpSec: active — your instance actively fetches sources; control its egress so monitoring doesn't fingerprint you.

## Overlaps ("do both")
- Pairs with lightweight RSS readers like [[the-old-reader]] and hosted change-detection — those are quick and manual; Taranis AI is heavyweight, automated, and self-hosted for teams needing scale and structured output.

## Trust & verifiability
`trust: community` — open-source under EUPL-1.2 with a public codebase and release history; you can audit and self-host it, but it's community-maintained, so validate its AI outputs against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | taranis-ai |
