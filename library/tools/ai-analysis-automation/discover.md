---
id: discover
name: Discover
description: Use when you have a `name`, `domain` or `email` and want to run the standard passive/active recon playbook in one command — returns aggregated OSINT (subdomains, people, emails, hosts) as a report.
url: https://github.com/leebaird/discover
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: One-command orchestration of many recon/OSINT tools (domain, person, and network reconnaissance) on Kali/Ubuntu.
selectorsIn:
- name
- domain
- email
selectorsOut:
- email
- domain
- ip-address
- social-profile
status: live
pricing: free
costNote: Free and open-source (MIT); it wraps other free tools you install alongside it.
opsec: active
opsecNote: The active recon modules (Nmap scans, host enumeration) touch the target directly and are noisy; the passive/person-OSINT modules query third parties. Choose passive modes and route through a VPN when you must stay quiet, and only run active scans against infrastructure you're authorised to test.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: trusted
trustNote: Long-maintained, widely used pentest/OSINT automation suite by Lee Baird (bundled in many Kali workflows); 1,700+ commits and active upkeep.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- discover.sh
- Lee Baird discover
tags:
- recon
- automation
- Tools collections/toolkits
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Discover

> Lee Baird's menu-driven recon suite: it chains dozens of OSINT and scanning tools so a single choice runs a whole passive-or-active reconnaissance workflow and hands you a consolidated report.

## When to use
You're starting a case with a `name`, a `domain`, or an `email` and want the routine recon done fast and consistently — subdomain and host enumeration, people/email harvesting, and (optionally) active scanning — without invoking each underlying tool by hand.

## How to use it (`bestInteractionPattern`: cli)
1. On Kali/Ubuntu: `git clone https://github.com/leebaird/discover && cd discover && ./update.sh` (installs the tools it orchestrates).
2. Run `./discover.sh` for the interactive menu.
3. Pick a workflow: **Domain** (passive/active) for an org, or **Person** for name/email OSINT; enter the target selector when prompted.
4. Read the aggregated report; pivot the harvested `email`/`subdomain`/`ip-address`/`social-profile` results into targeted tools.

## Inputs → Outputs
- **In:** `name`, `domain`, or `email`
- **Out:** `email`, `domain` (subdomains), `ip-address`, `social-profile` (aggregated recon)
- **Empty/negative result looks like:** thin output usually means missing API keys for the wrapped services or a target with little public footprint — supply keys and try again before concluding there's nothing.

## Gotchas & OpSec
- Human-in-the-loop: choose passive vs active deliberately — active modules scan the target and are loud/authorised-only.
- It's an orchestrator: results are only as good as the underlying tools and any API keys you configure.
- Kali/Ubuntu-oriented; expect setup friction elsewhere.

## Overlaps ("do both")
- Complements SpiderFoot/Recon-ng-class frameworks: Discover is fast menu-driven orchestration; the frameworks offer deeper, module-by-module control and correlation.

## Trust & verifiability
`trust: trusted` — an established, actively maintained open-source suite; it aggregates other tools, so verify individual findings at their source before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discover |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, domain, email → email, domain, ip-address, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (manual-review) |
