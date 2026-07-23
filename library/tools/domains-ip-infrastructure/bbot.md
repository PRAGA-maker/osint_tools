---
id: bbot
name: BBOT
description: Use when you have a `domain`, `ip-address` or `email` and want deep recursive attack-surface enumeration — chains modules to return subdomains (`domain`s), `ip-address`es, `email`s and occasional `social-profile`s.
url: https://github.com/blacklanternsecurity/bbot
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Recursive, module-chaining enumeration of an organization's subdomains, IPs, emails and attack surface.
selectorsIn:
- domain
- ip-address
- email
selectorsOut:
- domain
- ip-address
- email
- social-profile
status: live
pricing: free
costNote: Free and open source (Python); install via `pipx install bbot`. Some modules use third-party APIs that need free keys for full coverage.
opsec: active
opsecNote: BBOT's default recursive scans include active modules that directly probe the target (DNS brute-force, port scans, web requests), so traffic hits the target from your host. Use passive-only presets, proxies and API-backed sources when you need to stay off the target's radar.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by Black Lantern Security (9k+ GitHub stars); reputable, widely-used, auditable open-source recon framework.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- bbot
- blacklanternsecurity/bbot
tags:
- recursive-scanner
- subdomains
- emails
- modules
source: gh-topic-osint-framework
lastVerified: '2026-07-23'
enrichment: full
---

# BBOT

> A recursive, module-chaining OSINT/recon scanner: feed it a seed (`domain`/`ip`/`email`) and it self-expands — each discovery becomes input to the next module — mapping an organization's full external attack surface.

## When to use
You're profiling an organization's internet footprint and want breadth without hand-running twenty tools. BBOT chains subdomain enumeration, DNS, port scanning, web spidering, email harvesting and dozens of other modules recursively, so a single `domain` seed cascades into subdomains, IPs, open ports, emails and sometimes linked social profiles. It's infra-first — for people work it occasionally surfaces staff emails/accounts as a side effect, not as its purpose.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pipx install bbot`.
2. Run a scan with a preset, e.g. passive-only recon: `bbot -t example.com -p subdomain-enum -rf passive`; or a fuller active sweep: `bbot -t example.com -f subdomain-enum web-basic`.
3. Add API keys (in the config) for modules like SecurityTrails, Shodan, etc. to widen passive coverage.
4. Read the output/exported results — the graph of subdomains, IPs, ports, emails and findings.
5. Pivot: harvested emails feed breach/account tooling; subdomains feed web recon; the IP/port map feeds service fingerprinting.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or `email` seed(s)
- **Out:** subdomain `domain`s, `ip-address`es, open ports/services, `email`s, occasional `social-profile`s
- **Empty/negative result looks like:** a thin result set — often means passive-only mode with no API keys, or a small target with little external surface. Add keys or enable active modules (mind OpSec) to go deeper.

## Gotchas & OpSec
- Default scans are **active** and noisy (brute-force DNS, port scans, web hits) — for stealth use the passive presets/flags and API-backed sources so you never touch the target directly.
- Full passive coverage depends on third-party API keys you supply; without them, breadth drops.
- OpSec: choose the preset deliberately — active recursion will appear in the target's logs; proxy and scope carefully.

## Overlaps ("do both")
- Pairs with focused enumerators (amass, subfinder) and service scanners (Shodan) — BBOT orchestrates broadly and recursively, while single-purpose tools go deeper on one facet; run BBOT to map, then drill in with the specialist.

## Trust & verifiability
`trust: trusted` — actively maintained, widely-adopted open-source framework from a reputable security firm; the code and modules are auditable, and results are reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bbot |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, email → domain, ip-address, email, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
