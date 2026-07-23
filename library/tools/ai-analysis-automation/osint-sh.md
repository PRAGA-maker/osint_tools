---
id: osint-sh
name: OSINT.SH
description: Use when you have a `domain`, `ip-address`, `email`, or `username` and want a free no-login web toolkit — runs reverse-whois, DNS history, reverse-IP, subdomain, email and username lookups.
url: https://osint.sh/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A free browser suite of quick OSINT lookups (whois/DNS history, reverse IP, subdomains, username/email search) with no account.
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
opsecNote: Lookups run server-side against OSINT.SH's own data/back-end sources, so the target isn't contacted directly. But you disclose your query selectors to a third-party site whose operators/data providers are not fully transparent — avoid submitting your most sensitive targets, and don't rely on it as sole sourcing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A popular free aggregator of OSINT lookups; convenient, but of uncertain provenance and data quality — corroborate results elsewhere.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINT.SH
- osint.sh
tags:
- osint-toolkit
- multi-lookup
- domain-and-ip-research
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# OSINT.SH

> A free, no-signup hub of one-click OSINT lookups — whois and DNS history, reverse IP, subdomain finder, email and username search, certificate and metadata tools, all in the browser.

## When to use
You have a `domain`, `ip-address`, `email`, or `username` and want fast answers without installing anything or logging in. OSINT.SH bundles the common lookups an investigator reaches for early — reverse whois, DNS/IP history, reverse-IP (co-hosted domains), subdomain enumeration, username-across-sites, and metadata viewers — into a single free site. Good for quick triage and cross-checking; use dedicated tools/APIs when you need reliability and provenance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/ and pick the relevant tool tile (e.g. Reverse Whois, DNS History, Reverse IP, Subdomain, Username Search, Email search).
2. Enter your selector (`selectorsIn`) and run the lookup.
3. Read the result — co-hosted domains, historical DNS/IP, subdomains, or username hits (`selectorsOut`).
4. Pivot: feed discovered domains/IPs/handles into more authoritative tools (Censys, WHOIS history providers, Sherlock) to confirm.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, `email`, or `username` (tool-dependent)
- **Out:** `domain` (reverse-whois/IP, subdomains), `ip-address` (history), `social-profile` (username hits), plus DNS/cert/metadata data
- **Empty/negative result looks like:** no records for a lookup — the aggregator's back-end may lack coverage for that target; treat a blank as inconclusive and try a first-party source.

## Gotchas & OpSec
- Human-in-the-loop: none (no account).
- OpSec: passive toward the target, but you hand your selectors to a third-party site of unclear provenance — don't run your most sensitive targets through it.
- Data quality and freshness are uneven across the tiles; always corroborate an important finding with an authoritative source.

## Overlaps ("do both")
- Overlaps with dedicated tools it approximates — [[censys]] and Netcraft for infrastructure, WHOIS-history providers, and Sherlock/WhatsMyName for usernames — use OSINT.SH for a fast first look, then confirm with the specialist tool.

## Trust & verifiability
`trust: unverified` — a convenient free aggregator whose data sources and operators aren't fully transparent. Fine for quick, non-sensitive triage, but verify anything you'll act on against a tool with known provenance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-sh |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, ip-address, email, username → domain, ip-address, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
