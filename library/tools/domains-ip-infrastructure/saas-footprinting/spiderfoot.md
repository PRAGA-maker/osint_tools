---
id: spiderfoot
name: SpiderFoot
description: Use when you have a `domain`, `ip-address`, `email`, `name`, or `phone` and want automated multi-source recon — 200+ modules correlate it into related domains, IPs, profiles, and breaches.
url: https://github.com/smicallef/spiderfoot
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- saas-footprinting
bestFor: Automated, multi-source OSINT recon that correlates a seed selector into a connected intelligence graph.
input: Domain, IP, email, name, phone, subnet
output: Correlated intelligence graph, structured findings across modules
selectorsIn:
- domain
- ip-address
- email
- name
- phone
selectorsOut:
- domain
- ip-address
- email
- social-profile
status: live
pricing: free
opsec: active
opsecNote: SpiderFoot runs many modules; MOST are passive (query third-party APIs/databases), but some ACTIVELY probe the target (DNS, port/banner, web crawl). Choose a passive-only scan or review the module set before running, or you will send attributable traffic to the target. Supply API keys via a dedicated account and run behind controlled infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Widely-used, long-maintained open-source framework (Steve Micallef); the engine is reliable, individual findings inherit their source module's quality.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- SpiderFoot
- smicallef/spiderfoot
tags:
- recon-automation
- attack-surface
- osint-framework
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# SpiderFoot

> An automation engine for OSINT — seed it a domain, IP, email, name, or phone and 200+ modules fan out across public sources, correlating everything into one connected findings graph.

## When to use
You have a starting selector and want breadth fast: SpiderFoot pulls from certificate transparency, passive DNS, WHOIS, breach data, search engines, social platforms, threat-intel feeds, and more, then links the results so a domain leads to IPs, IPs to certs, emails to breaches, names to profiles. Ideal for a comprehensive first-pass footprint of a person or organization's online presence, where running each source by hand would be impractical.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install spiderfoot` (or clone the repo/Docker); launch the web UI (`sf.py -l 127.0.0.1:5001`) or use the CLI (`sfcli.py`).
2. Add API keys under Settings for the sources you have (many modules work without, more with).
3. Start a scan: enter the seed (`selectorsIn`) and pick a scan type — **Passive** to avoid touching the target, or module-select to control exactly what runs.
4. Read the correlated results/graph by data type (`selectorsOut`); export CSV/JSON and pivot new entities into further scans or specialist tools.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, `email`, `name`, `phone` (or subnet)
- **Out:** correlated `domain`s, `ip-address`es, `email`s, `social-profile`s, breach hits, hosts, and more — as a linked graph
- **Empty/negative result looks like:** thin results — often means few API keys are configured or the seed has little public exposure; add sources rather than concluding nothing exists.

## Gotchas & OpSec
- Human-in-the-loop: none to run, but coverage scales with your own API keys.
- OpSec: **active by default unless you choose Passive** — some modules probe the target directly. Pick the Passive scan or curate modules; run keys/traffic through isolated infrastructure.
- Findings inherit each module's reliability; a hit is a lead to verify, not a fact.

## Overlaps ("do both")
- Overlaps with [[sn0int]] and [[harpoon]] (all orchestrate many sources) and feeds specialist tools ([[subfinder]], [[censys]], Sherlock) — use SpiderFoot for broad automated collection, then the specialists for depth on the leads it surfaces.

## Trust & verifiability
`trust: trusted` — a mature, widely-used open-source framework. The engine is dependable; because it aggregates 200+ sources of varying quality, attribute each finding to its module and corroborate the ones that matter.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spiderfoot |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, email, name, phone → domain, ip-address, email, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
