---
id: prism
name: PRISM
description: Use when you have a `domain`, `ip-address`, `email`, `phone` or `username` and want a self-hosted platform to run 20+ recon modules and build a linked profile — returns social-profiles, geolocation, associated infrastructure and an OPSEC exposure report.
url: https://github.com/NovaCode37/Prism-platform
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Running many OSINT modules on one selector from a single dashboard and getting an auto-generated, linked report.
selectorsIn:
- domain
- ip-address
- email
- phone
- username
selectorsOut:
- social-profile
- geolocation
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source, self-hosted via Docker. Optional paid third-party API keys unlock more modules; 14 of 22 modules work with no keys at all.
opsec: active
opsecNote: Runs on your own infrastructure, but modules make live queries to WHOIS, DNS, certificate transparency, Shodan/Censys, breach and threat feeds — some of which log the selectors you submit. Self-host on a research VPS and use dedicated API keys. Its own OPSEC-exposure score is about the target's footprint, not your operational safety.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Active open-source project (v2.6, ~150 stars, Docker-based). Community-maintained; verify module outputs against primary sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- Prism-platform
- prism osint platform
tags:
- osint-platform
- self-hosted
- reconnaissance
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# PRISM

> A self-hosted OSINT dashboard that runs 20+ recon modules against one selector and stitches the results into an entity graph, maps and a report.

## When to use
You have a starting selector — `domain`, `ip-address`, `email`, `phone`, or `username` — and want a repeatable, all-in-one scan that pulls WHOIS/DNS, certificate transparency, Wayback, breach lookups, username searches, phone validation and geolocation into a single linked view, rather than running each tool by hand. Good for standing up a controlled, logged research environment.

## How to use it (`bestInteractionPattern`: docker)
1. `git clone https://github.com/NovaCode37/Prism-platform && cd Prism-platform`.
2. Copy the env template and (optionally) add API keys for Shodan, Censys, VirusTotal, AbuseIPDB, etc. — 14 of 22 modules run without any keys.
3. `docker compose up` and open the local dashboard (Next.js frontend, FastAPI backend).
4. Enter a selector, start a scan, and watch the real-time module progress; review the entity-relationship graph and GeoIP map.
5. Export the result as HTML/PDF/CSV/Markdown and pivot on the linked domains, profiles and locations it surfaces.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, `email`, `phone`, or `username`.
- **Out:** `social-profile` matches, `geolocation` (GeoIP markers), associated `domain`/`ip-address`, breach hits, and an OPSEC exposure score plus a formatted report.
- **Empty/negative result looks like:** modules returning "no data" or greyed-out (missing API key) — a thin report means the selector is low-footprint or you haven't enabled the paid modules, not that nothing exists.

## Gotchas & OpSec
- Requires Docker and a bit of setup; the richest modules (Shodan, Censys, threat feeds) need their own free/paid keys.
- Aggregated results still need primary-source verification — the graph will happily link entities that merely share a common value.
- Self-host it; do not point a hosted instance at sensitive targets without controlling who can see the stored scans.

## Overlaps ("do both")
- Use it to orchestrate what single-purpose tools do individually — e.g. its username module overlaps `[[slash]]`, and its host module overlaps `[[hostintel-keithjjones-github]]`; run the standalone tool when you need depth on one selector, PRISM when you want breadth in one pass.

## Trust & verifiability
`trust: community` — a maintained but community-run aggregator; treat its confidence scores and auto-links as leads, and confirm any actioned finding against the underlying source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | prism |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, ip-address, email, phone, username → social-profile, geolocation, domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | docker |
| opsec | active |
| human-in-loop | no |
