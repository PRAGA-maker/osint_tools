---
id: harpoon
name: Harpoon
description: Use when you have a `domain`, `ip-address`, `email`, or `username` and want to run many threat-intel/OSINT lookups from one CLI — 70+ plugins return infrastructure, reputation, and some social data.
url: https://github.com/Te-k/harpoon
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Threat-intel-flavored OSINT lookups (domains, IPs, some social platforms) from a single plugin-based CLI.
selectorsIn:
- domain
- ip-address
- email
- username
selectorsOut:
- domain
- ip-address
- social-profile
status: live
pricing: free
opsec: passive
opsecNote: Most plugins query third-party services/APIs (Shodan, VirusTotal, Censys, DNS/CT databases), so lookups are passive toward the target — but they run under YOUR API keys and are logged by those providers. Use dedicated keys and a controlled network. A few plugins (e.g. direct DNS/HTTP) touch the target; know which command you're running.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: trusted
trustNote: Mature CLI by Te-k (GPLv3, actively developed, 70+ commands); broad, well-regarded plugin set.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- harpoon
- Te-k/harpoon
tags:
- cli
- threat-intel
- plugins
source: gh-topic-osint-framework
lastVerified: '2026-07-23'
enrichment: full
---

# Harpoon

> A plugin-based OSINT / threat-intel CLI — 70+ subcommands wrapping Shodan, VirusTotal, Censys, DNS/certificate databases, and social platforms, so one tool orchestrates many lookups.

## When to use
You have an infrastructure or account selector — `domain`, `ip-address`, `email`, or `username` — and want to run it through many intel sources without visiting each site. Harpoon shines for CTI/infrastructure work (reputation, passive DNS, certificates, Shodan) and has Twitter/Telegram/Instagram plugins that extend it toward people-side leads. Good as a scriptable hub when you already hold API keys.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install harpoon`, then `harpoon config` to add your API keys for the services you'll use.
2. List capabilities with `harpoon --help`; each plugin is a subcommand (e.g. `harpoon dns`, `harpoon ip`, `harpoon domain`, `harpoon shodan`).
3. Run a plugin against your selector, e.g. `harpoon ip <ip>` or `harpoon domain <domain>` (`selectorsIn`).
4. Read the aggregated output (`selectorsOut`) and pivot new domains/IPs/profiles into further plugins.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, `email`, `username`
- **Out:** `domain`/`ip-address` infrastructure + reputation, `social-profile` (via social plugins), certificate/DNS/threat data
- **Empty/negative result looks like:** a plugin returns nothing or errors on a missing key — often means the source has no data or you haven't configured that API; check `harpoon config`.

## Gotchas & OpSec
- Human-in-the-loop: many plugins require your own service API keys (`api-key`).
- OpSec: mostly passive (third-party APIs), but a few plugins query the target directly; know each command. Lookups are logged by the API providers under your keys — isolate them.
- Coverage depends entirely on which keys you've added; without keys many commands are inert.

## Overlaps ("do both")
- Overlaps with [[sn0int]] (both orchestrate many sources) and with the underlying services directly (Shodan, Censys, VirusTotal) — use Harpoon to script routine multi-source lookups, and go to a service's own UI for depth.

## Trust & verifiability
`trust: trusted` — a mature, actively-maintained GPLv3 CLI with a broad plugin set. Results are only as authoritative as the upstream service each plugin calls, so attribute findings to their source and corroborate the important ones.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | harpoon |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, ip-address, email, username → domain, ip-address, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
