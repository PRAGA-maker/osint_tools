---
id: torbot
name: TorBot
description: Use when you have a seed `domain` (.onion or clearnet) and want to crawl and map dark-web link structure — returns discovered `domain` links, page titles and metadata.
url: https://github.com/DedSecInside/TorBot
category: dark-web
path:
- dark-web
- discovery
bestFor: Automated .onion crawling from a seed link to build a link tree of connected dark-web sites and surface pages of interest.
selectorsIn:
- domain
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free and open-source (GPL); the only cost is running it yourself over Tor.
opsec: active
opsecNote: This is ACTIVE — TorBot makes real requests to every crawled site, which those hidden services can log. Always route through Tor (never crawl .onion clearnet-side), throttle depth, and run from an isolated VM/identity; deep crawls can be noisy and slow.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained open-source project (DedSecInside; v4.1.1 released 2026-07-19, 1000+ commits) — code is auditable, but crawl results are only as trustworthy as the hidden services visited.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- DedSecInside/TorBot
tags:
- dark-web
- onion-crawler
- cli
- open-source
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# TorBot

> An open-source Python CLI that crawls .onion sites from a seed link and maps the connected dark-web link graph — your discovery engine for what a hidden service links out to.

## When to use
You have a seed `domain` (an .onion address or a clearnet URL) tied to a lead — a marketplace, forum, or paste — and want to systematically enumerate what it links to, harvest page titles/metadata, and build a link tree to spot related hidden services, mirrors, or contact points (emails) worth investigating. Use it for breadth-first dark-web discovery rather than deep single-page analysis.

## How to use it (`bestInteractionPattern`: cli)
1. Have Python 3.9+ and a running Tor service (SOCKS proxy on 9050). Clone the repo, then `python -m pip install -r requirements.txt && python -m pip install -e .`.
2. Run a crawl: `python main.py -u <seed-url> --depth 2 --visualize table` (raise `--depth` cautiously; each level multiplies requests).
3. Read the output: page titles, host info, live-link status, and a JSON link tree you can save and pivot on.
4. Pivot: newly discovered `domain`s feed further crawls or manual review; harvested emails feed email-OSINT; the link tree feeds link/graph analysis.

## Inputs → Outputs
- **In:** `domain` (seed .onion/clearnet URL) + crawl config (depth, visualization)
- **Out:** discovered `domain` links, page titles, host metadata, live-link status, JSON link tree; sometimes `email` addresses scraped from pages
- **Empty/negative result looks like:** a dead seed (offline hidden service) or a crawl that returns no outbound links — common for single-page or access-gated .onion sites; means "no reachable graph," not that the site is unimportant.

## Gotchas & OpSec
- **Active and noisy:** every crawled page is a request the destination can log. Always run over Tor, keep depth low, and isolate the environment/identity.
- Requires a working Tor setup; misconfiguration can leak requests outside Tor — verify your SOCKS routing before crawling .onion.
- Hidden services go up and down constantly; re-run to confirm, and capture results immediately.

## Overlaps ("do both")
- Complements manual dark-web directories and .onion search engines — TorBot automates link enumeration from a seed, while directories give you seeds to start from.

## Trust & verifiability
`trust: community` — a well-maintained, auditable open-source tool; the crawler itself is reliable, but treat the *content* it discovers on hidden services as unverified and often adversarial.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | torbot |
| category | dark-web |
| selectorsIn → selectorsOut | domain → domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
