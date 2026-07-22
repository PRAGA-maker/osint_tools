---
id: nmap-formatter
name: Nmap Formatter
description: Use when you have Nmap XML scan output for an `ip-address`/`domain` and want a readable report — converts it to HTML, CSV, JSON, Markdown, SQLite or Graphviz.
url: https://github.com/vdjagilev/nmap-formatter
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Turning raw Nmap XML into shareable/searchable formats (HTML report, CSV, JSON, Graphviz graph) for infrastructure investigations.
selectorsIn:
- ip-address
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (MIT). No account, no API key.
opsec: passive
opsecNote: The formatter itself only processes a local XML file you already have — it makes no network connection and reveals nothing. Any OpSec exposure comes from the Nmap scan that produced the XML, not from this tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source Go utility on GitHub (MIT-licensed); the code is auditable and it performs no external calls.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- nmap-formatter
- vdjagilev/nmap-formatter
tags:
- Domain/IP/Links
- Domain/IP investigation
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Nmap Formatter

> A small open-source CLI that turns Nmap's clunky XML into HTML, CSV, JSON, Markdown, SQLite, Excel or a Graphviz graph.

## When to use
You have run an Nmap scan against a subject's infrastructure (an `ip-address`, CIDR, or `domain`'s hosts) and produced XML output that is painful to read. You want it as a clean HTML report to attach to a case, a CSV/SQLite you can query, or a Graphviz diagram to visualise host/port relationships.

## How to use it (`bestInteractionPattern`: cli)
1. Install with Go: `go install github.com/vdjagilev/nmap-formatter/v3@latest` (or grab a release binary).
2. Run your Nmap scan with XML output: `nmap -oX scan.xml <target>`.
3. Convert: `nmap-formatter html scan.xml > report.html` (swap `html` for `csv`, `json`, `markdown`, `dot`, `sqlite`, `excel`).
4. For a graph: `cat scan.xml | nmap-formatter dot | dot -Tsvg > hosts.svg`.
5. Pivot: the structured output makes it easy to extract open-service banners, hostnames and `domain`/`ip-address` mappings that feed further infrastructure lookups.

## Inputs → Outputs
- **In:** Nmap XML (the scan of an `ip-address`/`domain`)
- **Out:** the same host/port data in a chosen readable format; effectively a cleaner list of `domain`/`ip-address` and services
- **Empty/negative result looks like:** an empty table/report — the underlying scan found no hosts or ports, not a tool failure.

## Gotchas & OpSec
- This is a formatter, not a scanner — it adds no data; the intelligence quality is entirely from your Nmap scan.
- The scan itself is **active** and noisy against the target; run it from infrastructure you're willing to burn. The formatting step is offline and safe.

## Overlaps ("do both")
- Pairs with the rest of the domain/IP infrastructure suite — use it to make Nmap output diff-able and searchable alongside WHOIS/DNS enrichment tools.

## Trust & verifiability
`trust: community` — auditable MIT-licensed code that only transforms your local file; there is no data-quality risk introduced by the tool itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nmap-formatter |
