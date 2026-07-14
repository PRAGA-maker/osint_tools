---
id: spiderfoot-poppopjmp-fork
name: SpiderFoot (poppopjmp fork)
description: Use when you have a `name`, `email`, `username`, `domain`, `ip-address`, or `phone` and want automated multi-source enrichment across 200+ modules — returns `email`, `social-profile`, `domain`, `ip-address`, and `address` correlations.
url: https://github.com/poppopjmp/spiderfoot
category: search-engines
path:
- search-engines
bestFor: Automated, correlated OSINT enrichment of a seed selector across hundreds of data sources in one run.
selectorsIn:
- name
- email
- phone
- domain
- ip-address
- username
selectorsOut:
- email
- social-profile
- domain
- ip-address
- address
status: live
pricing: free
costNote: Free and open-source. Many modules work with no key; others (Shodan, Hunter, HaveIBeenPwned, etc.) need your own API keys to activate — some of those are paid.
opsec: active
opsecNote: SpiderFoot can run ACTIVE modules that touch the target directly — DNS lookups, port/banner scans, web crawling — which are logged by the target's infrastructure. For OPSEC-sensitive work, explicitly select a passive-only module set (or "passive" scan mode) so you never touch the subject. Your own IP and API keys are exposed to the data sources you enable.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: A maintained community fork of the well-known SpiderFoot framework; the core engine is mature and widely used, though this specific fork's currency should be checked against upstream.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- spiderfoot
- SpiderFoot HX fork
tags:
- automation
- framework
- enrichment
source: gh-topic-osint-resources
lastVerified: '2026-07-14'
enrichment: full
---

# SpiderFoot (poppopjmp fork)

> The Swiss-army enrichment engine of OSINT — feed it one selector and 200+ modules fan out across data sources, correlating everything they find into a single graph.

## When to use
You have a seed selector — a `name`, `email`, `username`, `domain`, `ip-address`, or `phone` — and want breadth fast: instead of running dozens of tools by hand, SpiderFoot queries hundreds of sources and correlates the results (which email ties to which domain, which username appears where, which IP resolves to what). Ideal early in an investigation to surface leads and connections you'd otherwise miss, then follow the strongest threads with focused tools.

## How to use it (`bestInteractionPattern`: cli)
1. Install locally (clone the repo; `pip install -r requirements.txt`) and launch — it offers a web UI (`python sf.py -l 127.0.0.1:5001`) and a CLI (`sfcli`/`sf.py -s <target>`).
2. Add API keys for the modules you want (Settings) — many free sources work keyless; premium sources need keys.
3. **Choose scan mode / modules deliberately:** for OPSEC-sensitive cases select a **passive-only** module set so nothing touches the target.
4. Enter the seed selector and run; watch the correlations graph and per-module results.
5. Read outputs: linked `email`s, `social-profile`s, `domain`s, `ip-address`es, and `address` data, with source attribution per finding.
6. Pivot: promising leads feed dedicated tools (a discovered email → breach/account-existence checks; a username → cross-platform enumeration).

## Inputs → Outputs
- **In:** `name`, `email`, `phone`, `domain`, `ip-address`, or `username` (seed target)
- **Out:** correlated `email`, `social-profile`, `domain`, `ip-address`, `address`, and many other data types, each with the source module noted
- **Empty/negative result looks like:** modules returning nothing or erroring — often missing API keys, a target with a thin footprint, or a passive-only run that skipped active checks. Sparse output isn't proof of absence; check which modules actually ran.

## Gotchas & OpSec
- **Active by default in places:** without care, SpiderFoot will directly probe the target (DNS, ports, crawl). Use passive mode for stealth; assume active modules are logged by the target.
- Coverage depends heavily on which API keys you supply — a keyless run is far thinner than a fully configured one.
- It generates volume; treat findings as leads to verify, not confirmed facts, and mind source reliability per module.
- Verify this fork tracks upstream SpiderFoot; core is trusted, fork currency varies.

## Overlaps ("do both")
- Pairs with focused single-purpose tools and other frameworks (Recon-ng, Maltego) — SpiderFoot casts the wide automated net, while dedicated tools (breach checks, username enumerators, people-search) go deep on the specific leads it surfaces. Automate for breadth, then hand-verify for depth.

## Trust & verifiability
`trust: community` — the SpiderFoot core is a mature, widely trusted framework; this is a community fork, so confirm it's current with upstream. SpiderFoot aggregates third-party sources of varying quality, so always attribute and verify each finding at its source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spiderfoot-poppopjmp-fork |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, phone, domain, ip-address, username → email, social-profile, domain, ip-address, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
