---
id: ghostintel
name: GhostIntel
description: Use when you have a `username`, `email`, `domain`, `ip-address` or `phone` and want a one-command recon sweep across public sources — returns `social-profile`, `email`, `ip-address`, `phone`, `geolocation`.
url: https://github.com/ruyynn/GhostIntel
category: people-search
path:
- people-search
bestFor: Running fast multi-selector lookups (username across 100+ sites, email breach, domain, IP, phone) from one Python CLI with no API keys.
selectorsIn:
- username
- email
- domain
- ip-address
- phone
selectorsOut:
- social-profile
- email
- ip-address
- phone
- geolocation
status: live
pricing: free
costNote: Free and open-source (MIT); runs on public data sources with zero API keys required.
opsec: passive
opsecNote: It queries public profile pages and open data sources, not the subject directly, so it's passive toward the target — but all requests leave your IP; run behind a VPN/sock puppet and expect username-enumeration false positives to verify by hand.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small but actively-maintained open-source framework (MIT, ~50 stars, v2.5 in 2026); read the source before trusting output and corroborate every hit at the primary source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- gosint-ruyynn
aliases:
- GhostIntel framework
tags:
- osint
- framework
- multi-selector
- username-enumeration
- cli
source: gh-topic-osint-framework
lastVerified: '2026-07-21'
enrichment: full
---

# GhostIntel

> A no-API-key Python OSINT framework — hand it a username, email, domain, IP or phone and it sweeps public sources in one run, checking 100+ platforms for accounts.

## When to use
Early-stage breadth from a single selector. GhostIntel bundles common recon steps: username enumeration across 100+ social/gaming/developer platforms, email breach detection with risk scoring, domain DNS/tech/SSL analysis, IP geolocation and threat/proxy checks, and phone-number analysis for several countries. Because it needs no API keys, it's a quick first pass to generate leads you then verify with focused tooling.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/ruyynn/GhostIntel and install Python 3 dependencies (see the README).
2. Run it with the selector you have — a `username`, `email`, `domain`, `ip-address` or `phone`.
3. Read the output (CLI, and a web-UI dashboard in recent versions): per-platform account hits, breach appearances, DNS/tech for a domain, geo/threat data for an IP, carrier/region for a phone.
4. Verify each account hit manually (open the profile, confirm it's the same person) before relying on it.
5. Pivot: feed confirmed accounts into per-platform tools, breach hits into email-OSINT, and IP/geo into infrastructure tooling.

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, `ip-address`, or `phone`
- **Out:** `social-profile` (candidate accounts), `email` (breach exposure), `ip-address`/`geolocation` (IP + geo), `phone` (carrier/region)
- **Empty/negative result looks like:** rows of "not found," or account hits that turn out to be a different person — username enumeration is noisy, so treat unconfirmed hits as leads only.

## Gotchas & OpSec
- Human-in-the-loop: none required (no API keys), but you must verify results yourself.
- OpSec: passive toward the target, but your IP makes every request — use a VPN/sock puppet.
- It's an aggregator: platform coverage drifts as sites change and false positives are common. Keep it updated and confirm everything downstream. Phone support is limited to a handful of countries.

## Overlaps ("do both")
- Overlaps with dedicated username-enumerators (Sherlock-class), breach-check services, and IP/phone tools — GhostIntel is the quick combined sweep; the specialised tools verify and deepen each lead. Pairs with `[[gosint-ruyynn]]` from the same author.

## Trust & verifiability
`trust: community` — an actively-maintained open-source project aggregating public sources; useful for breadth, but corroborate every finding at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghostintel |
| category | people-search |
| selectorsIn → selectorsOut | username, email, domain, ip-address, phone → social-profile, email, ip-address, phone, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
