---
id: recon-ng
name: Recon-ng
description: Use when you have a `domain`, `employer-org`, `email` or `ip-address` and want a scripted, modular framework to harvest hosts, subdomains, contacts and breach data — returns domains, ip-addresses, names, emails and social-profiles into a stored workspace.
url: https://github.com/lanmaster53/recon-ng
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Reproducible, workspace-based web recon that chains many API-driven modules over a domain or organisation.
selectorsIn:
- domain
- employer-org
- email
- ip-address
selectorsOut:
- domain
- ip-address
- email
- name
- social-profile
status: live
pricing: free
costNote: Free and open-source. Core is free; several marketplace modules need free/paid third-party API keys stored in recon-ng's key store.
opsec: passive
opsecNote: Most modules pull from third-party APIs and datasets rather than probing the target directly, so the target host usually isn't touched — but each module discloses your selectors to services like Shodan, HIBP, Hunter, Censys, etc., which log queries. Use dedicated research keys and a controlled IP.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: trusted
trustNote: Long-standing, widely used framework by Tim Tomes (lanmaster53); a de-facto standard taught in recon/pentest training.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- reconng
- recon-ng framework
tags:
- recon-framework
- subdomains
- osint-automation
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Recon-ng

> A modular, interactive reconnaissance framework — think Metasploit-style console, but for open-source data collection over a domain or organisation.

## When to use
You have a `domain`, `employer-org`, `email`, or `ip-address` and want to systematically expand it: enumerate subdomains and hosts, harvest employee names/emails, resolve infrastructure, and check breaches — with every result stored in a workspace you can re-query and export. Best when you want repeatability and scale beyond ad-hoc web lookups.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pipx install recon-ng` (or clone the repo and `pip install -r REQUIREMENTS`), then run `recon-ng`.
2. Create a workspace: `workspaces create <case>`.
3. Install modules from the marketplace: `marketplace install all` (or selectively), and add API keys with `keys add <name> <value>`.
4. Seed the target: `db insert domains` (or `companies`), then load and run modules, e.g. `modules load recon/domains-hosts/hackertarget; run`.
5. Review and export: `show hosts`, `show contacts`, then `modules load reporting/html; run` for a report. Pivot the harvested hosts/emails/names into other tools.

## Inputs → Outputs
- **In:** `domain`, `employer-org`, `email`, or `ip-address` seeded into the workspace tables.
- **Out:** `domain`/subdomains, resolved `ip-address`, `name` and `email` contacts, and some `social-profile` links — accumulated and de-duplicated in the DB.
- **Empty/negative result looks like:** a module completing with "0 results added" — usually a missing/expired API key or a low-footprint target, not a definitive negative.

## Gotchas & OpSec
- Human-in-the-loop: the most productive modules require API keys you must register for; without keys, coverage is thin.
- The marketplace changes over time — module names and availability shift between versions; check `marketplace search` if a module is missing.
- Results are aggregated from third parties and can be stale or wrong; verify contacts/hosts before acting.

## Overlaps ("do both")
- Complements one-shot enrichers like `[[hostintel-keithjjones-github]]` (batch CSV over a host list) and broad platforms like `[[prism]]`; recon-ng is the choice when you want an iterative, stored, scriptable workflow.

## Trust & verifiability
`trust: trusted` — a mature, well-known open-source framework with a long track record; the framework is reliable, though the quality of any given finding depends on the third-party module behind it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | recon-ng |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, employer-org, email, ip-address → domain, ip-address, email, name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
