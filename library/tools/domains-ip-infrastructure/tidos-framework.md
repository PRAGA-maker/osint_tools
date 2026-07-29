---
id: tidos-framework
name: TIDoS-Framework
description: Use when you have a `domain` and want a scripted recon sweep — a modular web-recon/pentest framework whose passive OSINT modules return subdomains, DNS, WHOIS, breach hits, and more.
url: https://github.com/0xInfection/TIDoS-Framework
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Running bundled passive/active reconnaissance modules (DNS, subdomains, reverse IP, Wayback, breach checks) against a target domain.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
- email
status: degraded
pricing: free
costNote: Free and open-source (GPL-3.0), Python 3. Some modules are marked BROKEN:DEP (broken dependencies), so expect to skip or fix individual modules.
opsec: passive
opsecNote: Its passive-recon modules query third-party sources (CT logs, Wayback, breach APIs) and do not touch the target. The active-recon and later attack phases DO connect to and probe the target's server — only run those against systems you are explicitly authorized to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A known open-source offensive framework (0xInfection); powerful but only partially maintained, with some broken modules — verify each module's output before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- TIDoS
- TIDoS Framework
tags:
- Code
- web-recon
- pentest
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# TIDoS-Framework

> A modular, Metasploit-style web-recon and pentest framework — for OSINT, its passive footprinting phase bundles DNS, subdomain, reverse-IP, Wayback, and breach-check modules against a domain.

## When to use
You have a `domain` and want a menu of recon modules in one place for a first-pass footprint: enumerate subdomains, pull DNS/WHOIS, reverse-IP, check the Wayback Machine, and run breach-email checks. TIDoS packages ~100 modules across recon → scanning → exploitation; for investigative OSINT you stay in the **passive reconnaissance** phase and ignore the offensive later phases unless you have authorization to test the target.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `github.com/0xInfection/TIDoS-Framework` and install Python 3 requirements (some modules need extra deps).
2. Launch the framework and set your target `domain`.
3. Enter the **Passive Reconnaissance / OSINT** phase and run the modules you want (DNS lookup, subdomain enum, reverse IP, Wayback, breach email).
4. Read each module's output; skip any module flagged `BROKEN:DEP`.
5. Pivot: discovered subdomains/`ip-address`es feed infrastructure OSINT (`[[certgraph]]`, MaxMind); breach `email`s feed email-OSINT. **Do not** run active/exploit phases without written authorization.

## Inputs → Outputs
- **In:** a target `domain`
- **Out:** subdomains and related `domain`s, `ip-address`es, DNS/WHOIS data, Wayback captures, breach `email` hits
- **Empty/negative result looks like:** a module returns nothing or errors on a dependency — either the target genuinely has no such data or (often) the module is broken/rate-limited; confirm with a dedicated tool.

## Gotchas & OpSec
- Human-in-the-loop: none required, but you must consciously stay in passive phases for pure OSINT.
- OpSec: passive modules are safe (third-party queries); **active/exploit modules probe and attack the target** and are only lawful against systems you are authorized to test. Misuse can be illegal.
- Partial maintenance means broken modules — treat TIDoS as a convenient aggregator, and corroborate any finding with the authoritative single-purpose tool.
- It wraps other services, so reliability tracks those upstreams.

## Overlaps ("do both")
- Overlaps with dedicated recon tools (Amass/subfinder for subdomains, `[[certgraph]]` for cert pivots, holehe for breach emails). Use TIDoS to triage quickly, then confirm each thread with the specialized, better-maintained tool.

## Trust & verifiability
`trust: community` — open-source and capable but only partially maintained; because modules can be stale or broken, never treat a single TIDoS output as authoritative — verify against the primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tidos-framework |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
