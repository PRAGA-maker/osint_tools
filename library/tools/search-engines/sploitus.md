---
id: sploitus
name: Sploitus
description: Use when you have a software/product `name` or CVE and want to find public exploits and PoC tools for it — a technical-research search engine, not a people-finder.
url: https://sploitus.com/
category: search-engines
path:
- search-engines
bestFor: Quickly finding published exploits, PoCs, and security tools for a given software, version, or CVE.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free public exploit/PoC search; no account needed for basic queries. It aggregates public exploit databases and security repos.
opsec: passive
opsecNote: Searching Sploitus only queries its own index of public exploit data; no target system is touched and nothing is sent to any subject. Fully passive research; still use a VPN if you prefer not to associate exploit searches with your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known exploit/PoC search aggregator; it indexes third-party exploit sources, so the exploits' quality/safety is the original authors', not Sploitus's.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- sploitus.com
tags:
- exploits
- vulnerability
- security-research
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Sploitus

> A search engine for exploits and proof-of-concept code: enter a product, version, or CVE and it returns published exploits, PoCs, and tools from across public exploit databases.

## When to use
This is a technical-research tool, not a person-finder. In an investigation with an infrastructure/technical angle — profiling a server, understanding what a piece of software is vulnerable to, or researching a tool a subject uses — Sploitus quickly aggregates the public exploits and PoCs tied to a `name`/CVE. Treat outputs as security-research references (`document-id`), not attribution to any individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sploitus.com/.
2. Search a software name, version, or CVE identifier.
3. Review the ranked results — each links to an exploit/PoC with its source (Exploit-DB, GitHub, etc.), date, and type.
4. Follow a result to its source repo/database to read the code and confirm applicability.
5. Pivot: a PoC's author/repo can itself be a `social-profile` lead if the investigation concerns the researcher, not just the vuln.

## Inputs → Outputs
- **In:** software `name` / version / CVE
- **Out:** published exploits and PoCs (`document-id` references) with sources and dates.
- **Empty/negative result looks like:** no results for the query — no public exploit is indexed for that term (which is not proof none exists privately).

## Gotchas & OpSec
- Exploit code is third-party and unvetted — never run it outside an authorized, isolated lab.
- Coverage is limited to *public* exploit sources; absence here is not proof of security.
- Marginal for people-search; use it only when your case has a genuine technical/infrastructure dimension.

## Overlaps ("do both")
- Complements CVE/vulnerability databases and code-search engines — Sploitus is fastest for "is there a PoC," those give authoritative advisory detail.

## Trust & verifiability
`trust: community` — a reputable aggregator of public exploit data; the index is reliable but the underlying exploits are authored by third parties, so verify each at its source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sploitus |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
