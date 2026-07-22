---
id: osint-toolkit-ayxkaddd
name: Osint-ToolKit (ayxkaddd)
description: Use when you have a `username`, `email`, `domain`, or GitHub handle and want a self-hosted web dashboard that runs several lookups (breach search, WHOIS history, DNS/GitHub recon) in one place — returns social-profile, email, domain.
url: https://github.com/ayxkaddd/Osint-ToolKit
category: people-search
path:
- people-search
bestFor: Self-hosted web UI bundling breach, WHOIS-history, DNS and GitHub-profile lookups behind one dashboard.
selectorsIn:
- username
- email
- domain
selectorsOut:
- social-profile
- email
- domain
status: live
pricing: free
costNote: Free, open-source; self-hosted (FastAPI + Tailwind). Some modules need third-party API keys (HackerTarget, WhoisXMLAPI free tier, osint.industries, SecurityTrails/VirusTotal optional); a few (DoxBin/Cavalier search) work with no setup.
opsec: passive
opsecNote: You self-host it, so lookups originate from your server and hit third-party APIs (breach DBs, WHOIS, DNS) rather than the target directly — no subject notification. Anything you enter is sent to those upstream APIs under your keys; use a dedicated key set and host on infrastructure you control.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Small community project (ayxkaddd, ~18 stars); it's a front-end orchestrating other services, so results are only as good as the upstream APIs it calls.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
aliases:
- osint toolkit
tags:
- web-ui
- multi-tool
- self-hosted
source: gh-topic-osint-framework
lastVerified: '2026-07-22'
enrichment: full
---

# Osint-ToolKit (ayxkaddd)

> A self-hosted web dashboard that wires several OSINT lookups — breach search, WHOIS history, DNS recon, GitHub profiling — behind one FastAPI UI.

## When to use
You want a single browser dashboard (rather than a pile of CLIs) to run common lookups on a `username`, `email`, `domain`, or GitHub handle: check breach databases, pull WHOIS history, do DNS recon, or profile a GitHub account. Best when you'll reuse it across cases and don't mind standing up a small self-hosted service and plugging in a few API keys.

## How to use it (`bestInteractionPattern`: web-manual)
1. Clone `github.com/ayxkaddd/Osint-ToolKit` and run the FastAPI backend + web UI locally (per the repo's README).
2. Add API keys for the modules you want: HackerTarget (NS lookup), WhoisXMLAPI (WHOIS history, 1k free requests), osint.industries, optional SecurityTrails/VirusTotal for DNS recon, GitFive for GitHub analysis.
3. In the web UI, pick a module and enter the selector (email/username/domain).
4. Read results per module: breach hits (`email`/`social-profile`), WHOIS history (`domain` ownership over time), DNS records, GitHub profile intel.
5. Pivot: a breach hit feeds credential/email-OSINT; WHOIS history feeds infrastructure attribution.

## Inputs → Outputs
- **In:** `username`, `email`, `domain` (and GitHub handle)
- **Out:** `social-profile` (breach/GitHub hits), `email` (breach records), `domain` (WHOIS history / DNS)
- **Empty/negative result looks like:** a module returning nothing — often because its API key is missing or the free quota is exhausted, so check configuration before treating a blank as "no data."

## Gotchas & OpSec
- It's a thin orchestration layer: value depends entirely on the upstream APIs and whether you've supplied keys; the no-key modules (DoxBin/Cavalier search) are the only ones usable out of the box.
- Human-in-the-loop: several modules require API keys and self-hosting setup.
- OpSec: passive toward the target, but your queries and keys route through third-party services — host it yourself and use dedicated keys.

## Overlaps ("do both")
- Pairs with standalone versions of the same services (HaveIBeenPwned-style breach tools, WHOIS-history providers, GitFive): the toolkit is convenient, but for a definitive answer query the authoritative source directly.

## Trust & verifiability
`trust: community` — a small open-source project acting as a UI over external APIs, so treat it as convenience tooling; confirm any material finding at the underlying service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-toolkit-ayxkaddd |
| category | people-search |
| selectorsIn → selectorsOut | username, email, domain → social-profile, email, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (api-key) |
