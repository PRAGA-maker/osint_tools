---
id: github-apurv-singh-gautam
name: Dark Web OSINT Tools (Apurv Singh Gautam)
description: Use when you're starting dark-web research and want a curated GitHub list of tools for finding, scraping, and monitoring Tor/onion services — returns pointers to tools, not data itself.
url: https://github.com/apurvsinghgautam/dark-web-osint-tools
category: dark-web
path:
- dark-web
bestFor: A curated catalog of dark-web/Tor OSINT tools for discovery, scraping, and monitoring.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open GitHub repository; the tools it lists vary (some free, some need setup/keys/Tor).
opsec: passive
opsecNote: Reading the list is passive. The tools it points to touch Tor/onion services — that activity must run through Tor from an isolated VM, never your real IP/host. Some listed tools actively crawl hidden services; treat each on its own OpSec terms before running it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-curated GitHub list by a known researcher (Apurv Singh Gautam); it indexes third-party tools whose quality/currency you must judge individually.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- dark-web-osint-tools
- Apurv Singh Gautam dark web tools
tags:
- darkweb
- Dark Web Links
source: uk-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Dark Web OSINT Tools (Apurv Singh Gautam)

> A curated GitHub catalog of dark-web/Tor OSINT tooling — the "what should I use to search, scrape, or monitor onion services" index.

## When to use
When an investigation moves onto the dark web and you need the right tooling: onion search engines, hidden-service crawlers/scrapers, marketplace monitors, and Tor-aware utilities. Rather than hunting for tools yourself, this list points you to maintained options for each task. It's a directory of tools, not a data source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/apurvsinghgautam/dark-web-osint-tools.
2. Find the section matching your need (search, scraping, monitoring, analysis).
3. Follow the linked tool's repo and set it up — most require Tor and run best from an isolated VM.
4. Route all onion activity through Tor from a disposable environment.
5. Pivot: onion `domain`s/content surfaced by the chosen tool → your dark-web analysis workflow.

## Inputs → Outputs
- **In:** none (a reference you read)
- **Out:** pointers to tools that yield onion `domain`s/content
- **Empty/negative result looks like:** no listed tool fits your exact need — the niche may require a bespoke crawler; check sibling dark-web tool lists.

## Gotchas & OpSec
- **Directory, not a tool** — nothing is found until you install and run a listed tool.
- Dark-web work is high-risk: always Tor + isolated VM, never your host/IP; expect illegal/harmful content.
- Listed tools drift (link rot, abandonment); verify each before relying on it.

## Overlaps ("do both")
- Complements other dark-web link/tool collections in this library; cross-reference, since each curator lists different tools and onion indexes.

## Trust & verifiability
`trust: community` — a credible curator's index; trust the curation, but vet each individual tool and treat any onion content it surfaces as unverified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-apurv-singh-gautam |
| category | dark-web |
| selectorsIn → selectorsOut |  → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
