---
id: clatscope-info-tool
name: ClatScope Info Tool
description: Use when you have any of a name/email/phone/IP/domain and want a one-stop recon sweep — a Python CLI that runs 70+ lookups (breach, WHOIS, DNS, geolocation, skip-trace) via external APIs.
url: https://github.com/Clats97/ClatScope
category: search-engines
path:
- search-engines
bestFor: Fast multi-selector pivoting — throw in an email/phone/IP/domain/name and get aggregated recon across many APIs at once.
selectorsIn:
- name
- email
- ip-address
- domain
- geolocation
- phone
selectorsOut:
- address
- geolocation
- domain
status: live
pricing: freemium
costNote: The tool is free and open-source, but most of its 70+ features call third-party APIs that need your own keys (Have I Been Pwned, Hunter, Hudson Rock, RapidAPI, Perplexity, etc.) — or a paid ClatScope subscription (~$29–$99/mo) that pre-configures them. Without keys, only a subset works.
opsec: passive
opsecNote: It doesn't contact the target directly, but every lookup discloses your query (email/phone/IP/domain) to the third-party API providers, who log it. Use dedicated API keys and a research environment; be aware some providers may retain or share submitted selectors.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Popular community recon aggregator (1.5k+ stars, active through 2025); quality of each result depends entirely on the underlying third-party API.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- ClatScope
tags:
- recon
- all-in-one
- python
source: gh-topic-osint-resources
lastVerified: '2026-07-11'
enrichment: full
---

# ClatScope Info Tool

> A Python "Swiss-army" recon CLI: one selector in, dozens of API-backed lookups out — breach, WHOIS, DNS, geolocation, phone, and skip-trace in a single run.

## When to use
You have a selector — `email`, `phone`, `ip-address`, `domain`, `name`, or `geolocation` — and want a broad first-pass sweep instead of visiting a dozen sites. ClatScope orchestrates 70+ lookups (breach checks, MX/DNS/WHOIS, IP geolocation, carrier detection, reverse lookups, person/skip-trace) and returns them together, which is efficient for early pivoting when you don't yet know which thread will pay off.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/Clats97/ClatScope.git` and `pip install` the listed dependencies.
2. Provide API keys for the services you want (HIBP, Hunter, Hudson Rock, RapidAPI, etc.) — or use the paid subscription that ships keys pre-configured.
3. Run the tool and choose the lookup for your selector.
4. Read the aggregated output; treat each section as a lead from that specific API, not gospel.
5. Pivot: an IP → `geolocation`/ISP; an email → breach hits and linked domains; a phone → carrier/reverse; feed confirmed threads to dedicated tools.

## Inputs → Outputs
- **In:** `name`, `email`, `phone`, `ip-address`, `domain`, or `geolocation`
- **Out:** aggregated `address`/`geolocation`, `domain`/DNS/WHOIS, breach and reverse-lookup findings
- **Empty/negative result looks like:** many features silently return nothing without their API key, or an API returns no data. A blank section often means "no key / quota exhausted," not "nothing exists" — check your key config before trusting an empty result.

## Gotchas & OpSec
- Key-gated: without your own API keys (or the paid tier) most of the 70+ features are inert — the "free" label is the code, not the data.
- Result quality is only as good as each third-party API; verify important findings at the source.
- OpSec: **passive** to the target, but you're disclosing selectors to many API vendors that log queries — use dedicated keys and mind provider data-retention.

## Overlaps ("do both")
- Pairs with focused tools (`[[holehe]]` for email, phone-OSINT libs, WHOIS/DNS tools) — ClatScope is the broad orchestrator, the specialists go deeper and let you verify what the aggregator surfaced.

## Trust & verifiability
`trust: community` — an actively maintained community aggregator; it's a convenient front-end, so trust flows from the underlying APIs — confirm each finding against its authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | clatscope-info-tool |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, ip-address, domain, geolocation, phone → address, geolocation, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
