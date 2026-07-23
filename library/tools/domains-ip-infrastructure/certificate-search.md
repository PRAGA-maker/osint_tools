---
id: certificate-search
name: Certificate Search
description: Use when you have a `domain` and want to discover its subdomains and related hostnames from Certificate Transparency logs — returns additional `domain` values.
url: https://osint.sh/crt/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Passive subdomain and hostname discovery for a domain by mining public TLS-certificate (CT) logs.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free to use as part of the osint.sh toolkit; no account required for the web lookup.
opsec: passive
opsecNote: Reads public Certificate Transparency logs — you never touch the target's own infrastructure, so subdomain discovery here is invisible to the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: One of the free tools on osint.sh; it surfaces CT-log data (the same public source as crt.sh), so results are as reliable as the certificates that were logged.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- osint.sh certificate search
- crt osint.sh
tags:
- domain-and-ip-research
- certificate-transparency
- subdomain-enumeration
source: osint4all
lastVerified: '2026-07-23'
---

# Certificate Search

> The certificate-transparency lookup in the osint.sh toolkit: give it a domain and it lists the subdomains and hostnames that appear in publicly logged TLS certificates.

## When to use
You have a `domain` tied to a person or organization and want to map its infrastructure — staging servers, mail hosts, internal tools, and other subdomains that never appear in ordinary DNS enumeration but were named on a TLS certificate. This is a clean, passive first step before you send any request to the target's own servers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/crt/.
2. Enter the base `domain` (e.g. `example.com`).
3. Read the result: a list of hostnames/subdomains drawn from Certificate Transparency logs, often with issuer and validity dates.
4. Pivot: resolve the discovered subdomains to IPs, feed them to WHOIS/DNS tools, or check archived copies — a forgotten subdomain frequently exposes the most.

## Inputs → Outputs
- **In:** `domain`
- **Out:** additional `domain` values (subdomains / SAN hostnames)
- **Empty/negative result looks like:** no certificates logged for the domain (common for brand-new or never-HTTPS domains) — absence in CT logs is not proof a subdomain doesn't exist, only that none was publicly logged.

## Gotchas & OpSec
- CT logs are historical: some listed hostnames are decommissioned, and some live subdomains (using wildcard certs or no public cert) won't appear — pair with active enumeration when completeness matters.
- OpSec: **passive** — you read public logs; the target sees nothing.

## Overlaps ("do both")
- Pairs with `crt.sh`, `[[google-subdomains]]`, and dedicated subdomain finders — CT-log search and search-index dorking surface different hostnames, so run both.

## Trust & verifiability
`trust: community` — a convenient front-end over public CT-log data; verify any critical hostname by resolving it yourself rather than trusting the listing alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | certificate-search |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
