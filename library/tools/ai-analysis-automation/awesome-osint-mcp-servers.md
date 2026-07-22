---
id: awesome-osint-mcp-servers
name: awesome-osint-mcp-servers
description: Use when you are building or extending an AI-agent OSINT workflow and want ready-made MCP servers that expose OSINT tools to an LLM — returns a categorised directory of installable capabilities.
url: https://github.com/soxoj/awesome-osint-mcp-servers
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Finding MCP servers to wire OSINT tools (SOCMINT, network, records, blockchain) into an AI agent.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, MIT-licensed catalogue on GitHub; individual servers it lists vary (open-source, free-tier, or paid) and are labelled as such.
opsec: passive
opsecNote: Reading the list is a plain GitHub visit and leaks nothing about a target. Note that any MCP server you then install runs code and may make queries against targets — vet each server's provenance and network behaviour before wiring it into an agent.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: Maintained by soxoj (author of Maigret and a well-known OSINT toolmaker); actively curated, ~300 stars, open to PRs.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases: []
tags:
- mcp
- ai
- automation
- catalog
source: gh-topic-osint-resources
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- 1c-database-converter
- counter-osint-guide-for-russians
- fravia-soxoj
- gitcolombo
- maigret
- maigret-via-socid-extractor-soxoj-ecosystem
- mailto-analyzer
- marple
- osint-namecheckers-list
- socid-extractor
- username-generation-guide
---

# awesome-osint-mcp-servers

> A curated GitHub directory of OSINT MCP servers — the shortlist for turning OSINT tools into capabilities an LLM agent can call directly.

## When to use
You are assembling an AI-driven OSINT pipeline (an agent that queries tools and writes reports) and need to discover which OSINT capabilities already ship as Model Context Protocol servers — so you can plug them into Claude, Cursor, Windsurf, or your own agent instead of scripting each tool by hand. Reach for it at the tooling/design stage, not during an active lookup on a subject.

## How to use it (`bestInteractionPattern`: api)
1. Open https://github.com/soxoj/awesome-osint-mcp-servers and read the README.
2. Browse the 10 categories — SOCMINT, Network Scanning, Web Scraping, Company Intelligence, Public Records & Compliance, Threat Intelligence, Research Intelligence, Meta/Discovery, Blockchain Intelligence, Market & Trading — to find a server matching the capability you need.
3. Note each entry's availability label (open-source / free-tier / paid) and follow the link to the server's own repo.
4. Install/configure the chosen MCP server in your agent host (its repo documents the transport, env vars, and any API keys).
5. Pivot: an installed server becomes a live tool your agent invokes; use this catalogue again to fill capability gaps as an investigation's needs change.

## Inputs → Outputs
- **In:** none (a reference/discovery resource, not a selector-driven lookup)
- **Out:** a categorised list of MCP servers with descriptions and availability tiers
- **Empty/negative result looks like:** a category with no server for the capability you want — meaning no MCP wrapper exists yet, so you'd fall back to calling that tool directly.

## Gotchas & OpSec
- It is a catalogue, not the tools themselves — value depends on the linked servers, some of which are paid or require API keys.
- Installing any MCP server executes third-party code inside your agent; review provenance, permissions, and what each server sends over the network before trusting it in an investigation.
- OpSec: browsing the list is passive; the servers you install are where real query footprints get created.

## Overlaps ("do both")
- Pairs with `[[maigret]]` and `[[socid-extractor]]` — this list points to MCP wrappers, while those are concrete soxoj-ecosystem tools you might run directly or find wrapped here.

## Trust & verifiability
`trust: trusted` — curated by a recognised OSINT tool author (soxoj), openly on GitHub with visible commit history and community PRs, so the catalogue itself is dependable; judge each linked server on its own merits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-osint-mcp-servers |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
