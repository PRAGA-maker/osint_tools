---
id: onyphe
name: Onyphe
description: Use when you have an `ip-address` or `domain` and want its exposed services, open ports, certificates and passive-DNS history — returns infrastructure `domain`s and `ip-address`es.
url: https://www.onyphe.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ipv4
bestFor: Pivoting an IP or domain across internet-wide scan data, passive DNS and certificate history to map related infrastructure.
selectorsIn:
- ip-address
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free tier available after registration with a limited daily query quota and history depth; deeper history, exports and higher API limits are paid.
opsec: passive
opsecNote: Queries hit Onyphe's own scan/passive-DNS datasets, not the target, so the subject sees nothing — but you must log in, so the search is tied to your account. Use a dedicated investigative account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established commercial cyber-intelligence provider (France-based) that runs its own internet-wide scanners; data is first-party collected, not resold scraping.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- onyphe.io
- ONYPHE
tags:
- internet-scanning
- passive-dns
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Onyphe

> An internet-wide scanning and cyber-intelligence engine (a Shodan/Censys peer) that turns an IP or domain into its exposed services, certificates and passive-DNS history.

## When to use
You have an `ip-address` or `domain` connected to a subject — a server hosting their site, an IP from a log or email header — and you want to expand it: what services and ports are exposed, what TLS certificates it presents (revealing other hostnames), and what domains have historically resolved to it. That certificate and passive-DNS overlap is how you find *other* infrastructure the same person or org controls.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://search.onyphe.io/ and log in.
2. Search a selector, e.g. `ip:203.0.113.10` or `domain:example.com`, optionally scoping to a category (geoloc, threatlist, resolver, datascan).
3. Read the returned records: open ports/protocols, software banners, TLS certificate subjects/SANs, ASN/geolocation, and passive-DNS resolutions.
4. Pivot: a certificate SAN or a co-resolving hostname becomes the next `domain` to search; a shared ASN/subnet clusters related hosts.
5. For bulk/automated work, use the REST API with your account key (respecting the free-tier quota).

## Inputs → Outputs
- **In:** `ip-address`, `domain` (also ASN, subnet, CVE)
- **Out:** exposed services/ports, TLS certificates, passive-DNS `domain`s, related `ip-address`es, geolocation and ASN
- **Empty/negative result looks like:** an obscure or newly-provisioned host may return few or no scan records — absence of data means "not seen in our scans," not that the host is clean or offline.

## Gotchas & OpSec
- Human-in-the-loop: account login is required; the free tier caps queries per day and how far back history goes.
- Scan data has a collection lag — a service shown may be stale, and one not shown may simply be missed between scan cycles; confirm live if it matters.
- OpSec: passive toward the target (you query Onyphe, not the subject), but tie searches to a dedicated investigative account.

## Overlaps ("do both")
- Run alongside another internet-scan engine (Shodan/Censys) — coverage and scan timing differ, so each surfaces hosts and certificates the other misses; the union is your real infrastructure map.

## Trust & verifiability
`trust: trusted` — Onyphe operates its own scanners and passive-DNS collection, so results are first-party observations with timestamps you can cross-check against another scanner.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onyphe |
