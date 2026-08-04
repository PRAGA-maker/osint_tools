---
id: osint-analyser
name: OSINT Analyser
description: Use when you want to auto-collect and LLM-summarize open-source chatter (e.g. Telegram channels) — a self-hosted pipeline; returns translated summaries and analysis, not direct selectors.
url: https://github.com/joestanding/osint-analyser
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Standing up a self-hosted collector that ingests Telegram channels and produces translated, LLM-analysed summaries.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free and open-source (self-host via Docker). You supply your own LLM/API key (e.g. OpenAI), which is the practical cost.
opsec: active
opsecNote: Collecting from Telegram means an account/session pulls messages, and pasting collected text into a third-party LLM sends that content off-box. Use a dedicated collection account, and be deliberate about what data you feed to an external model — treat the LLM step as data leaving your control.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: docker
trust: community
trustNote: A small single-author open-source project with minimal commit history; usable but effectively unmaintained — read the code and pin dependencies before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- joestanding/osint-analyser
tags:
- automation
- telegram
- llm
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# OSINT Analyser

> A self-hosted collection-and-analysis pipeline: it ingests open sources (notably Telegram), translates, and runs an LLM over the text to produce summaries — a monitoring harness, not a selector lookup.

## When to use
You want to continuously watch a set of Telegram channels (or similar open feeds) and get translated, summarized, LLM-analysed output instead of reading everything by hand. OSINT Analyser is a Dockerized collector that stores messages in MySQL and applies GPT-style analysis. Reach for it when the task is *ongoing monitoring of chatter* and you can self-host. It returns analysis over `social-profile`/channel content rather than resolving a single selector.

## How to use it (`bestInteractionPattern`: docker)
1. Clone the repo: `git clone https://github.com/joestanding/osint-analyser` (review the code first — see Trust).
2. Configure your collection source (Telegram channels), database, and your LLM API key in the environment/config.
3. Bring the stack up: `docker compose up`.
4. Let the collector ingest messages into MySQL; read the generated translations and LLM summaries/analysis it produces.
5. Pivot: mine the summarized output for concrete selectors (handles, links, `domain`s, `crypto-wallet`s) and push those into the appropriate targeted tools.

## Inputs → Outputs
- **In:** source configuration (`social-profile`/channel identifiers) + an LLM API key
- **Out:** translated, LLM-summarized/analysed text derived from the ingested channels (`social-profile`-level intelligence)
- **Empty/negative result looks like:** no messages collected (misconfigured source or auth) or empty/low-value summaries. LLM output can also hallucinate — treat summaries as leads to verify against the raw messages it stored.

## Gotchas & OpSec
- Human-in-the-loop: yes — you must supply and manage an LLM API key and configure sources; it's infrastructure, not a website.
- OpSec: **active** — a collection account touches the source, and the LLM step ships text to a third party. Use a burner collection identity and control what leaves your box.
- **Maintenance:** the repo has minimal history and is effectively unmaintained; dependencies may drift and there's no support. Audit and pin before operational use.

## Overlaps ("do both")
- Complements dedicated Telegram-OSINT tools (channel search, member/scraper utilities) — those find and pull raw data; OSINT Analyser adds the translate-and-summarize layer on top for volume monitoring.

## Trust & verifiability
`trust: community` — a single-author open-source project with little activity. The code is short and auditable, but there are no guarantees; verify every LLM-generated summary against the underlying stored messages, since the analysis step can fabricate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-analyser |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | active |
| human-in-loop | yes (api-key) |
