---
id: pygreynoise
name: pygreynoise
description: Use when you have an `ip-address` and want to know if it's mass internet-scanning "noise" or targeted — GreyNoise's official Python client/CLI; returns classification and actor context.
url: https://github.com/GreyNoise-Intelligence/pygreynoise
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Enriching IPs via GreyNoise to distinguish benign internet background scanners from targeted activity.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: freemium
costNote: The library is free/open-source; it calls the GreyNoise API, which has a free "Community" tier and paid plans for full features.
opsec: passive
opsecNote: You query GreyNoise's dataset about an IP, not the IP itself — passive, no packets to the target. Requires a GreyNoise API key (register with a sock-puppet identity). Community-tier queries are logged by GreyNoise.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: trusted
trustNote: The official Python SDK/CLI from GreyNoise Intelligence, a reputable internet-scanning-intelligence company; classifications are well-regarded in the security community.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools: []
aliases:
- pygreynoise
- greynoise python
tags: []
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# pygreynoise

> GreyNoise's official Python library and CLI — enrich an IP to learn whether it's part of the internet's mass background scanning ("noise") or something more targeted, plus who's behind it.

## When to use
You have an `ip-address` (from a log, an alert, an email header) and need context: is it a benign/opportunistic mass scanner (Shodan, Censys, botnet sweeps) that hits everyone, or is it targeted/anomalous? GreyNoise classifies internet-wide scanning activity, so it quickly tells you whether an IP is worth investigating or is just noise — a triage tool in a technical/security investigation.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install greynoise`.
2. Configure your API key: `greynoise setup -k <API_KEY>` (free Community-tier key from greynoise.io).
3. Query: `greynoise ip 1.2.3.4` (or `greynoise quick`, or use the Python API `GreyNoise().ip("1.2.3.4")`).
4. Read the result: classification (benign / malicious / unknown), whether it's a known scanner, tags (what it scans for), and actor/first-last-seen context.
5. Pivot: a "noise" verdict deprioritizes the IP; a targeted/unknown verdict routes it to deeper IP-attribution (WHOIS/ASN, passive DNS).

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** `ip-address` enrichment (noise classification, scanner tags, actor/RIOT context, first/last seen)
- **Empty/negative result looks like:** "IP not observed" means GreyNoise hasn't seen it scanning — often a good sign (not a mass scanner), but it says nothing about targeted activity; combine with other signals.

## Gotchas & OpSec
- Human-in-the-loop: needs a **GreyNoise API key** (free Community tier is limited; register with a sock puppet).
- "Not seen" ≠ safe — GreyNoise tracks internet-wide *scanning*, not all malice; absence isn't clearance.
- Passive: enriches from GreyNoise's data, so the target IP is never contacted.

## Overlaps ("do both")
- Pairs with WHOIS/ASN and passive-DNS tools and with `[[whatismyipaddress]]` — GreyNoise tells you *what kind of activity* an IP does across the internet; the others tell you *where it lives and who owns it*.

## Trust & verifiability
`trust: trusted` — the official SDK from a reputable internet-intelligence vendor; classifications are well-regarded, though (as with any single source) corroborate a consequential verdict with additional IP context.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pygreynoise |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
