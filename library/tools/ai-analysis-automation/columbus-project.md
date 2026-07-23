---
id: columbus-project
name: Columbus Project
description: Use when you have a `domain` and want a fast, passive list of its subdomains — an API-first service backed by Certificate Transparency and contributed DNS data — returns additional `domain` values.
url: https://github.com/elmasy-com/columbus
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Very fast, API-first subdomain enumeration for a domain, drawing on CT logs and a shared DNS dataset.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Open source (Apache-2.0); the public API at columbus.elmasy.com is free for basic lookups.
opsec: passive
opsecNote: Returns subdomains from Columbus's own dataset (CT logs + contributed DNS) — it does not brute-force or query the target's servers, so enumeration is invisible to the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: Open-source project (elmasy-com); results depend on CT-log and community-contributed DNS coverage, so completeness varies.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- Columbus
- columbus.elmasy.com
tags:
- dns
- subdomain-enumeration
source: awesome-osint
lastVerified: '2026-07-23'
---

# Columbus Project

> An API-first subdomain discovery service: query a domain and get its known subdomains back in a fraction of a second, sourced from Certificate Transparency logs and a shared DNS dataset.

## When to use
You have a `domain` and want its subdomains quickly and passively as part of infrastructure mapping. Columbus is optimised for speed and scripting — a single HTTP request returns the subdomain list — making it a good first pass before slower or more active enumeration.

## How to use it (`bestInteractionPattern`: api)
1. Query the public API: `https://columbus.elmasy.com/lookup/example.com` (JSON by default; send `Accept: text/plain` for newline-separated hostnames).
2. Or self-host from the GitHub source for private/bulk use.
3. Read the output: the list of known subdomains for the domain.
4. Pivot: resolve the subdomains to IPs, feed them to WHOIS/port tools, or check archives — a forgotten subdomain often exposes the most.

## Inputs → Outputs
- **In:** `domain`
- **Out:** additional `domain` values (subdomains)
- **Empty/negative result looks like:** an empty list — the domain has no subdomains in Columbus's dataset (no CT/DNS coverage yet), not proof none exist; corroborate with another source.

## Gotchas & OpSec
- Dataset-bound: it returns what CT logs and contributed DNS know — subdomains using wildcard certs or no public cert may be missing.
- Passive by design: for exhaustive coverage, combine with active enumeration and other passive sources.
- OpSec: **passive** — the target's servers are never touched.

## Overlaps ("do both")
- Pairs with `[[certificate-search]]`, `[[google-subdomains]]`, and subfinder — each source's coverage differs, so union the results for completeness.

## Trust & verifiability
`trust: community` — a solid open-source enumerator; verify a discovered subdomain by resolving it before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | columbus-project |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
