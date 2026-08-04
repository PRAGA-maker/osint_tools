---
id: voidaccess
name: VoidAccess
description: Use when you have a selector (email, username, domain) and want to sweep dark-web and open-source threat feeds for it — returns leaked credentials, IOCs, wallets, and actor mentions.
url: https://github.com/KatrielMoses/voidaccess
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Self-hosted threat-intelligence collection that parallel-searches Tor indexes, paste sites, code forges, and security feeds and extracts entities.
selectorsIn:
- email
- username
- domain
selectorsOut:
- email
- password
- crypto-wallet
- ip-address
- domain
- username
status: live
pricing: free
costNote: Free and open source (MIT); self-hosted via pip or Docker, no paid tier.
opsec: active
opsecNote: VoidAccess reaches out across Tor `.onion` seeds, paste sites, code forges, and security feeds — that is a lot of outbound connections, including to dark-web sources, from your host. Run it in an isolated VM/container over Tor, never from an attributable machine, and heed its own policy restricting use to authorized security/threat-intel work. Searching for a subject's data is passive toward them, but the collection footprint is broad.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community-authored, MIT-licensed, with meaningful adoption (hundreds of stars) and an explicit authorized-use policy; as with any aggregator, extracted entities are leads from third-party sources that must be independently verified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- mailaccess
aliases:
- VoidAccess threat-intel platform
tags:
- threat-intelligence
- dark-web
- breach-data
- self-hosted
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# VoidAccess

> A self-hosted threat-intelligence engine that fans a query out across Tor indexes, paste sites, code forges, and security feeds, then extracts the entities it finds.

## When to use
You have a selector — an `email`, `username`, or `domain` — and you want to know whether it surfaces in breach dumps, pastes, code leaks, or dark-web/security sources, along with related indicators (leaked `password`s, `crypto-wallet`s, `ip-address`es, messaging handles, CVEs, actor profiles). It's the automated, self-hosted alternative to manually checking a dozen paste/breach sources, aimed at authorized security research and threat intelligence.

## How to use it (`bestInteractionPattern`: cli)
1. Deploy in an isolated environment (VM/container, routed over Tor):
   - CLI: `pip install voidaccess` (local, SQLite-backed), or
   - Docker Compose for the full self-hosted stack with PostgreSQL.
2. Run a collection against your selector (`email`/`username`/`domain`); it queries sources in parallel.
3. Review the extracted entities: leaked credentials, IOCs (IPs, domains, hashes), `crypto-wallet`s, handles, CVEs, and actor intel, stored in the local DB.
4. Triage and verify: each hit is a third-party claim — confirm a leaked `password`/`email` pairing against the original breach context before acting on it.
5. Pivot: a `crypto-wallet` → blockchain OSINT; a leaked `email` → account-existence and people-search; an actor handle → messaging/dark-web tracing.

## Inputs → Outputs
- **In:** `email`, `username`, or `domain`
- **Out:** `email`/`password` leaks, `crypto-wallet`s, `ip-address`es/`domain`s (IOCs), handles, and actor mentions
- **Empty/negative result looks like:** no entities returned — the selector isn't present in the crawled sources (or a source was unreachable). Absence is not proof of no exposure; dark-web coverage is always partial.

## Gotchas & OpSec
- Human-in-the-loop: none in operation, but you must self-host it (`localInstall`/Docker).
- OpSec: **active/broad** — it opens many outbound connections including to Tor/dark-web sources. Run it isolated, over Tor, from a non-attributable host, and only for authorized work (the project mandates this).
- Legal/ethics: handling leaked credentials and dark-web data carries legal weight — stay within your authorization and jurisdiction.

## Overlaps ("do both")
- Pairs with a focused breach-lookup service and [[mailaccess]] — VoidAccess casts a wide dark-web/paste net, while a curated breach database gives cleaner, better-attributed hits on a single `email`; corroborate across both.

## Trust & verifiability
`trust: community` — open MIT code with real adoption, but it aggregates unverified third-party sources; treat every extracted entity as a lead to confirm at its origin.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | voidaccess |
