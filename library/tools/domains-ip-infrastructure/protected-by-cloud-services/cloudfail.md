---
id: cloudfail
name: CloudFail
description: Use when you have a Cloudflare-fronted `domain` and want to uncover the real origin server — returns candidate origin `ip-address`(es) and subdomains.
url: https://github.com/m0rtem/CloudFail
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- protected-by-cloud-services
bestFor: Finding the origin IP behind Cloudflare via DNS history, the Crimeflare DB, and subdomain brute-forcing.
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free, open-source (MIT) Python3 CLI tool on GitHub; no account.
opsec: active
opsecNote: This is ACTIVE — the subdomain brute-force phase sends thousands of DNS/HTTP requests that can hit the target's infrastructure and be logged. Run it through Tor (`--tor`) and only against systems you are authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely-used community tool (2.7k+ stars) but no formal releases and reliant on third-party datasets (DNSDumpster, Crimeflare) whose freshness varies.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- m0rtem CloudFail
tags:
- domains-ip-infrastructure
- cloudflare
- origin-ip
- cli
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# CloudFail

> A CLI reconnaissance tool that tries to strip away Cloudflare and reveal the origin server's real IP behind a protected domain.

## When to use
You have a `domain` that resolves to Cloudflare IPs and you need the true origin `ip-address` — to attribute hosting, correlate infrastructure, or map a target's real servers. CloudFail chains three approaches: misconfigured-DNS discovery (via DNSDumpster), the Crimeflare historical database, and a brute-force over 2,500+ subdomains that may resolve directly to the origin.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/m0rtem/CloudFail && cd CloudFail && pip3 install -r requirements.txt`.
2. Run against the target: `python3 cloudfail.py --target example.com`.
3. For OpSec, route through Tor: `python3 cloudfail.py --target example.com --tor` (requires Tor running).
4. Read the output: any subdomain or DNS-history record that resolves to a non-Cloudflare IP is a candidate origin. Pivot the candidate `ip-address` into reverse-DNS, passive-DNS, and hosting lookups to confirm.

## Inputs → Outputs
- **In:** `domain` (Cloudflare-fronted)
- **Out:** candidate origin `ip-address`(es) and discovered sub`domain`s
- **Empty/negative result looks like:** every result still points to Cloudflare ranges and no historical record leaks — the origin is well-hidden (or datasets are stale); absence is not proof.

## Gotchas & OpSec
- ACTIVE and noisy: the brute-force phase can trigger WAF/rate-limit logging on the target. Only run with authorisation; use `--tor`.
- Relies on third-party data (DNSDumpster, Crimeflare) that can be outdated — a "found" IP may be a former origin.
- No signed releases; review the code before running.

## Overlaps ("do both")
- Complements passive origin-hunting via certificate transparency and passive-DNS — do those first (passive), then use CloudFail's active brute-force only if needed.

## Trust & verifiability
`trust: community` — a popular open-source tool, but unmaintained-looking (no releases) and only as good as its upstream datasets; always confirm a candidate origin independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloudfail |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
