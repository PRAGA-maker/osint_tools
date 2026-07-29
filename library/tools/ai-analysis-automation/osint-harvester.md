---
id: osint-harvester
name: Osint-Harvester
description: Use when you have a `domain`/`ip-address`/URL and want a scripted collect-and-normalize of DNS, WHOIS, HTTP headers, and IP reputation into one JSON output.
url: https://github.com/Kubenew/Osint-Harvester
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Automating basic domain/IP footprinting (DNS, WHOIS, headers, IP reputation) into normalized JSON/STIX-like output.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free, open source (pip-installable Python CLI/library); no account.
opsec: active
opsecNote: WHOIS and DNS lookups are low-noise, but HTTP header fingerprinting and IP-reputation checks make direct requests to the target/third parties from your IP. Run from sock-puppet infrastructure for target work, and review what each module actually contacts before pointing it at a sensitive host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A very small early-stage GitHub project (Kubenew/Osint-Harvester, ~1 star, v0.1.0, few commits); functional but unproven — read the source before trusting its output or running it against sensitive targets.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Osint-Harvester
tags:
- aggregator
- normalization
- domain-footprinting
source: gh-topic-footprinting
lastVerified: '2026-07-29'
enrichment: full
---

# Osint-Harvester

> A lightweight CLI that runs DNS/WHOIS/header/IP-reputation lookups on a domain or IP and normalizes them into one JSON blob — early-stage, but handy for scripted footprinting.

## When to use
You have a `domain`, `ip-address`, or URL and want a single command to gather the basic infrastructure facts — DNS records, WHOIS, HTTP header fingerprint, IP reputation — as normalized JSON you can pipe into a pipeline, rather than running four tools by hand. Best for repeatable bulk footprinting where uniform output matters. It does **not** do email/username/social enumeration despite the "harvester" name.

## How to use it (`bestInteractionPattern`: cli)
1. Install from the repo (`pip install` per its README) into an isolated environment.
2. Run against a target: `osint-harvester domain example.com` (also accepts IPs/URLs).
3. Read the normalized output (standard JSON or a STIX-like format) for DNS/WHOIS/header/reputation fields.
4. Pivot: the resolved `ip-address`/hosting `domain` feeds passive-DNS, reputation scanners (`[[vurl-online]]`), and WHOIS-history tools.

## Inputs → Outputs
- **In:** `domain` / `ip-address` / URL
- **Out:** normalized JSON of DNS, WHOIS, HTTP headers, IP reputation → resolved `domain`/`ip-address`
- **Empty/negative result looks like:** empty/error fields — the host doesn't resolve, WHOIS is privacy-protected, or a module failed; confirm with a standalone `whois`/`dig`.

## Gotchas & OpSec
- **Unproven, tiny project:** ~1 star, v0.1.0 — read the code, pin the version, and validate its output against known-good tools before relying on it.
- Header/IP-reputation modules make **active** requests from your IP; use sock-puppet egress for target work.
- Output quality is only as good as the free data sources it wraps — treat it as a convenience layer, not an authority.

## Overlaps ("do both")
- Wraps the same lookups you'd otherwise run individually; pairs with `[[vurl-online]]` (safe URL dissection) and dedicated WHOIS/passive-DNS tools for verification and depth.

## Trust & verifiability
`trust: unverified` — a small early-stage script; useful for automation but validate its results with established tools before acting on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-harvester |
