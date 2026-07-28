---
id: dnsviz
name: DNSViz
description: Use when you have a `domain` and want a visual, authoritative analysis of its DNS/DNSSEC chain and misconfigurations — returns a diagnosed `domain` DNS/DNSSEC map.
url: https://dnsviz.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- dnssec
bestFor: Visualizing and diagnosing a domain's DNSSEC chain of trust and DNS delegation problems.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public tool (and open-source; can be self-hosted/run as a CLI).
opsec: passive
opsecNote: DNSViz's servers perform the DNS queries against the authoritative nameservers, so you never contact the target directly — passive from your side. Only the domain name is submitted. Results are publicly viewable by URL, so don't treat a submitted domain as secret.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Widely used, well-regarded DNSSEC analysis tool (originated at Sandia National Labs, now community-maintained); its diagnostics are authoritative for DNS/DNSSEC.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- dnssec-analyzer
- verisign
aliases:
- dnsviz.net
tags:
- domain-and-ip-research
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# DNSViz

> A tool that renders a domain's DNS and DNSSEC chain as an interactive graph, pinpointing exactly where signing, delegation, or resolution breaks — the reference tool for DNSSEC diagnostics.

## When to use
You have a `domain` and want a deep, visual read on its DNS health and DNSSEC deployment — useful when profiling an organization's infrastructure security, diagnosing why a signed domain fails to resolve, or documenting misconfigurations. It's an infrastructure tool, so its link to person-finding is peripheral (context on a subject's website/employer).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dnsviz.net/ and enter the `domain` under "Analyze".
2. Wait for the analysis; DNSViz queries the authoritative servers and builds a graph.
3. Read the diagram: nodes are DNS records (DNSKEY, DS, RRSIG, delegations), edges show the chain of trust; warnings/errors are color-coded with detailed explanations.
4. For automation, install the open-source `dnsviz` CLI to probe/graph domains locally in bulk.
5. Pivot: DNSSEC/DNS errors are findings for a security writeup; nameserver/host details feed further infrastructure mapping.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` DNS/DNSSEC analysis (chain-of-trust graph, per-record status, specific warnings/errors)
- **Empty/negative result looks like:** a domain that isn't DNSSEC-signed shows a valid but unsigned delegation (not an error) — that's a legitimate finding, not a tool failure.

## Gotchas & OpSec
- Submitted analyses are viewable by URL — don't assume the domain you checked stays private.
- Focused on DNS/DNSSEC — pair with WHOIS/subdomain tools for the full infrastructure picture.
- Passive: DNSViz does the querying; the target sees DNSViz's resolvers, not you.

## Overlaps ("do both")
- Pairs with `[[dnssec-analyzer]]` and `[[verisign]]` — cross-check, since different validators/resolvers occasionally disagree on edge cases; DNSViz's graph is the most detailed for diagnosing *why* something breaks.

## Trust & verifiability
`trust: trusted` — a mature, widely trusted DNSSEC analysis tool with authoritative diagnostics; its findings are reproducible (re-run or use the CLI) and reliable for DNS/DNSSEC assessment.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnsviz |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
