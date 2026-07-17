---
id: fofa
name: FOFA
description: Use when you have a `domain`, `ip-address`, or favicon and want to map internet-facing assets — returns hosts, services, and banners across the internet (Shodan-style).
url: https://en.fofa.info/
category: search-engines
path:
- search-engines
bestFor: Mapping internet-exposed hosts/services tied to a domain, IP, or favicon — infrastructure and asset discovery.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
status: live
pricing: freemium
costNote: Free tier after registration (limited results/queries per day); paid plans unlock more results, advanced operators, and API volume.
opsec: passive
opsecNote: FOFA queries its own pre-scanned index, so you don't touch the target's servers directly — passive toward the subject. However you must register/log in, so your account (and its email) is tied to your searches; FOFA is a China-based service, so use a dedicated account and consider that the operator sees your queries.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known cyberspace search engine operated by Beijing Huashun Xin'an (BAIMAOHUI); reputable in the security community but a commercial third-party scanner, not an authority on ownership.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- shodan
- censys
- zoomeye
aliases:
- fofa.info
- FOFA search
tags:
- speciality-search-engines
- attack-surface
- infrastructure
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# FOFA

> A cyberspace search engine (Shodan/Censys peer) that indexes internet-facing hosts and services — for mapping the infrastructure behind a domain or IP.

## When to use
You're investigating the online infrastructure connected to a case — a `domain`, an `ip-address`, a distinctive site favicon — and want to find related hosts, exposed services, and other assets sharing fingerprints. FOFA has particularly strong coverage of Asian infrastructure and a powerful favicon/icon search that can cluster sites reusing the same icon. This is infrastructure recon (low direct missing-persons relevance), useful when a subject or a suspicious service ties to specific web/network assets.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register/log in at https://en.fofa.info/ (free tier available; use a dedicated account).
2. Query with operators, e.g. `domain="example.com"`, `ip="1.2.3.4"`, `host="sub.example.com"`, or `icon_hash="..."` for favicon clustering.
3. Read results: matched hosts, ports/services, banners, titles, certificates, and locations.
4. Combine operators (`&&`, `||`) to pivot — e.g. same favicon across different IPs reveals related sites.
5. Pivot: discovered hosts/IPs → `[[shodan]]` / `[[censys]]` to cross-validate; a shared favicon or cert → other domains run by the same operator.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, favicon/icon hash, or service fingerprint
- **Out:** matching hosts (`ip-address`/`domain`), open services, banners, certs, geolocation of hosts
- **Empty/negative result looks like:** no results — the asset isn't in FOFA's index (coverage gaps exist), the free-tier result cap hid deeper hits, or your operator syntax was off; cross-check on Shodan/Censys before concluding.

## Gotchas & OpSec
- Registration required; the free tier caps results and hides some data behind paid plans — a sparse free-tier result may not be the full picture.
- China-based operator: your account and queries are visible to it; use a throwaway account and don't tie searches to your real identity.
- Passive toward the *target* (FOFA pre-scans), but banner data can be stale — verify a live host before acting.

## Overlaps ("do both")
- Pairs with `[[shodan]]` and `[[censys]]` — overlapping but differently-sourced indexes; FOFA is strong on Asian assets and favicon search. Run the same asset across all three for coverage.
- Pairs with `[[zoomeye]]` as another peer scanner for cross-validation.

## Trust & verifiability
`trust: community` — a reputable commercial scanner widely used in security research. Its banners/fingerprints are real observations but can be outdated and are not authoritative on *ownership*; confirm findings independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fofa |
| category | search-engines |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
