---
id: kali-intelligence-suite-kis
name: Kali Intelligence Suite (KIS)
description: Use when you have a `domain`/`ip-address` scope and want one framework to run and centralise dozens of recon/pentest tools — orchestrates nmap, dnsrecon, gobuster, Shodan, Censys etc. into a PostgreSQL DB, returning `domain`, `ip-address`, `email`.
url: https://github.com/chopicalqui/KaliIntelligenceSuite
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Automating and centralising the output of many Kali recon/pentest tools against a target scope into one queryable database.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- email
status: live
pricing: free
costNote: Free, open-source framework (chopicalqui/KaliIntelligenceSuite); runs via Docker, needs the underlying Kali tools and optional API keys (Shodan/Censys) for those modules.
opsec: active
opsecNote: This is an active-scanning orchestrator — it runs nmap, gobuster, hydra and similar directly against target infrastructure, generating heavy, obvious traffic in the target's logs. Use ONLY within an authorised engagement scope, from controlled infrastructure; it is emphatically not a passive people-finder.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Active, reasonably popular open-source project; it wraps standard, trusted tools, so results are as reliable as those tools — the value it adds is orchestration and storage, not new data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- dome
- orb
aliases:
- KIS
tags:
- kali
- pentest-orchestration
- automation
- recon
source: gh-topic-intelligence-gathering
lastVerified: '2026-07-23'
enrichment: full
---

# Kali Intelligence Suite (KIS)

> A recon orchestrator: point it at a scope and it runs dozens of Kali tools and API lookups on a schedule, funnelling everything into a PostgreSQL database you can query and re-use across scans.

## When to use
You're doing **authorised** infrastructure recon against an organisation's `domain`/`ip-address` scope and want to stop juggling nmap, dnsrecon, gobuster, hydra, Censys, and Shodan by hand. KIS coordinates them, dedups and stores results centrally, and lets each new scan build on prior findings. It's for adversarial-infrastructure mapping and pentest workflows — heavy, active, and out of place for locating a missing person.

## How to use it (`bestInteractionPattern`: docker)
1. Deploy via Docker (image on Docker Hub); the container bundles the tool dependencies and a PostgreSQL backend.
2. Define scope and manage the workspace with `kismanage` (add domains, networks, hosts, credentials, API keys).
3. Collect with `kiscollect` — it runs the selected Kali tools and API queries against the scope, populating the DB tables.
4. Query/report with `kisreport` — export to CSV, Excel, JSON, or raw text; re-run collection to enrich the same dataset over time.
5. Pivot the structured results (subdomains → IPs → services → harvested emails) into targeted follow-up.

## Inputs → Outputs
- **In:** `domain`, `ip-address`/network, hostnames, credentials (scope definition)
- **Out:** `domain` (subdomains/hosts), `ip-address`, open services, and harvested `email` addresses — all stored and queryable
- **Empty/negative result looks like:** sparse DB tables — a locked-down/CDN-fronted scope or a tool that found nothing; not a KIS failure.

## Gotchas & OpSec
- **Loud and legally gated:** it actively scans/brute-forces; running it outside an authorised, scoped engagement can be illegal. Confirm authorisation first.
- Heavy footprint — expect it to be detected; run from engagement infrastructure, not your own IP.
- Setup is non-trivial (Docker + tool deps + API keys); budget time before it's productive.
- It only orchestrates existing tools — accuracy and coverage come from them.

## Overlaps ("do both")
- A superset-style orchestrator over point tools like [[dome]] and [[orb]] — use those for quick single-purpose runs, and KIS when a large scope justifies a persistent, centralised, repeatable collection pipeline.

## Trust & verifiability
`trust: community` — an active open-source framework wrapping standard, trusted tools; it adds orchestration and storage rather than data, so verifiability inherits from the tools and APIs it drives.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kali-intelligence-suite-kis |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | active |
| human-in-loop | no |
