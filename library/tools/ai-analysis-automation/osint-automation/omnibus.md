---
id: omnibus
name: Omnibus
description: Use when you have mixed artifacts (`ip-address`, `domain`, `email`, `username`, hash, wallet) and want a session-based CLI to enrich them across sources — returns aggregated intel per artifact.
url: https://github.com/InQuest/omnibus
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: Running an interactive CLI "investigation session" that collects and enriches technical indicators (IPs, domains, emails, usernames, hashes, BTC addresses) from multiple modules.
selectorsIn:
- ip-address
- domain
- email
- username
- crypto-wallet
selectorsOut:
- ip-address
- domain
- email
status: degraded
pricing: free
costNote: Free and open-source (MIT).
opsec: active
opsecNote: Modules reach out to third-party APIs/services to enrich each artifact, so queries about the target leave your machine to those providers. Some modules need API keys tied to accounts. Run from attributable-safe infrastructure and review which modules are active before a run.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source project by InQuest (a reputable security vendor), but written for Python 2.7 and only lightly maintained — expect setup friction and some dead modules on modern systems.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
aliases:
- InQuest Omnibus
- omnibus-cli
tags:
- osint-automation
- artifact-enrichment
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Omnibus

> An open-source CLI that treats indicators as "artifacts" inside an investigation session and enriches them across many modules — powerful in concept, but aging (Python 2.7).

## When to use
You have a bag of technical indicators — `ip-address`es, `domain`s, `email`s, `username`s, file hashes, Bitcoin `crypto-wallet`s — and want to load them into one session, run a battery of enrichment modules, and keep the results together. Best suited to infrastructure/indicator investigations where you'd otherwise query a dozen services by hand.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo (`github.com/InQuest/omnibus`) and `pip install -r requirements.txt` — note it targets Python 2.7, so use a matching environment or expect to patch.
2. Launch `python omnibus-cli.py` to enter the interactive console.
3. Create a session and add artifacts (`new <artifact>`), then run modules against them to enrich.
4. Add API keys in the config for modules that need them (Shodan, VirusTotal, etc.).
5. Review the aggregated results per artifact and export the session; pivot enriched IPs/domains into other tools.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, `email`, `username`, hash, or Bitcoin `crypto-wallet`
- **Out:** aggregated per-artifact enrichment (related `ip-address`/`domain`/`email`, reputation, WHOIS, etc.)
- **Empty/negative result looks like:** modules erroring out or returning nothing — often an expired module/API or a Python 2 incompatibility rather than a true negative; verify the module ran.

## Gotchas & OpSec
- **Legacy code:** Python 2.7 and light maintenance mean setup friction and some non-functional modules on current OSes. Consider it a reference/last-resort rather than a daily driver.
- Human-in-the-loop: several modules require API keys (accounts).
- OpSec: **active** — enrichment queries hit third-party services; the artifacts (your target's indicators) are disclosed to them.

## Overlaps ("do both")
- Overlaps with modern all-in-one enrichment frameworks and with single-purpose lookups (Shodan, VirusTotal, WHOIS) — those are better maintained; use Omnibus only if its session model specifically helps.

## Trust & verifiability
`trust: community` — reputable origin (InQuest) and MIT-licensed/auditable, but its age means results should be spot-checked and it may not run cleanly today.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | omnibus |
