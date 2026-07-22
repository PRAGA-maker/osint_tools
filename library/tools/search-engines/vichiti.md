---
id: vichiti
name: Vichiti
description: Use when you have a single selector (`email`, `username`, `phone`, `ip-address`, `domain`, or crypto wallet) and want a fast multi-module recon sweep from one CLI — returns social-profile, geolocation, domain, crypto-wallet.
url: https://github.com/umair9747/vichiti
category: search-engines
path:
- search-engines
bestFor: One-command cross-platform OSINT enrichment (username/email/IP/domain/wallet) from a single Node.js tool.
selectorsIn:
- email
- username
- phone
- ip-address
- domain
- crypto-wallet
selectorsOut:
- social-profile
- geolocation
- domain
- crypto-wallet
status: live
pricing: free
costNote: Free, open-source (MIT); Node.js install, no paid tier.
opsec: active
opsecNote: Several modules make direct requests to third-party services against the target (IP geolocation, port scanning, URL expansion, WHOIS, wallet balance checks). Port scanning in particular is an active probe that touches the target's infrastructure and may be logged — run from a VPS/sock-puppet network and avoid it against systems you're not authorised to probe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source Node.js OSINT tool by umair9747 (~99 stars, MIT); it aggregates public sources, so per-module accuracy depends on the upstream service.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- vichiti
tags:
- nodejs
- enrichment
- multi-tool
source: gh-topic-osint-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Vichiti

> A cross-platform Node.js OSINT multi-tool: feed it one selector and it fans out across a dozen recon modules — usernames, email validation, WHOIS, IP geolocation, port scan, wallet balance, and more.

## When to use
You hold a single `email`, `username`, `phone`, `ip-address`, `domain`, or crypto-wallet address and want a quick, scriptable first-pass enrichment without stitching together separate tools. Good as an early triage step to see which pivots light up before you dig deeper with specialised tools.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `github.com/umair9747/vichiti` and install via Node.js (works on Windows, Linux, Termux; macOS untested).
2. Run the CLI with your selector and the module(s) you want (e.g. Instagram username investigation, email validation, WHOIS, IP identification/geolocation, port scan, URL expander, MAC lookup, wallet balance).
3. Read the aggregated output: profile hits, ownership/WHOIS records, `geolocation` for an IP, wallet balance, etc.
4. Treat it as breadth-first triage: confirm any interesting hit in a dedicated, authoritative tool.
5. Pivot: a validated email/username feeds account-enumeration; an IP's geolocation and WHOIS feed infrastructure mapping.

## Inputs → Outputs
- **In:** `email`, `username`, `phone`, `ip-address`, `domain`, or `crypto-wallet`
- **Out:** `social-profile` (username hits), `geolocation` (IP), `domain` (WHOIS/URL data), `crypto-wallet` (balance) among other module results
- **Empty/negative result looks like:** a module returning "not found"/no data — a signal per-module, not a verdict; upstream rate limits or API changes can also blank a module.

## Gotchas & OpSec
- Quality varies by module because each wraps a different public source that can change or rate-limit; verify important findings elsewhere.
- The port-scan and probing modules are **active** — only use them against infrastructure you're authorised to test.
- OpSec: run from an isolated/sock-puppet network; several modules disclose your requests to third-party services and to the target.

## Overlaps ("do both")
- Pairs with focused single-purpose tools (dedicated username enumerators, WHOIS, IP-geolocation): Vichiti finds where to look fast, while the specialists give authoritative, complete results for the selector that lit up.

## Trust & verifiability
`trust: community` — open-source and MIT-licensed, but it's an aggregator: each result is only as reliable as the upstream service the module calls, so corroborate before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vichiti |
| category | search-engines |
| selectorsIn → selectorsOut | email, username, phone, ip-address, domain, crypto-wallet → social-profile, geolocation, domain, crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
