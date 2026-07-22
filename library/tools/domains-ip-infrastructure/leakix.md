---
id: leakix
name: LeakIX
description: Use when you have an `ip-address` or `domain` and want to see its exposed/misconfigured services and indexed leaks — returns exposed services, host details and related `domain`s.
url: https://leakix.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Searching internet-wide indexed data on exposed services, misconfigurations and leaks by IP, host, ASN or protocol.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: freemium
costNote: Free search and browsing with an account; higher-volume access, full leak details and API scale are paid tiers.
opsec: passive
opsecNote: Queries LeakIX's own scan index, not the target host, so the subject is never contacted. Note the ethical/legal weight of "leak" data — it may include sensitive exposed information; handle accordingly and stay within authorised scope.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A respected independent scan/leak-index project with public docs and an API; findings are first-party scan observations you can corroborate.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- onyphe
- securitytrails
aliases:
- leakix.net
tags:
- internet-scanning
- exposed-services
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# LeakIX

> A search engine over internet-wide scans of exposed and misconfigured services (open databases, dev panels, leaking endpoints) — index a target's IP/host to see what it's leaking to the world.

## When to use
You have an `ip-address` or `domain` tied to a subject or org and want to know what it exposes: open databases (MySQL/Elastic/Mongo), misconfigured services, dev/admin panels, and endpoints LeakIX has flagged as leaking. That surface both reveals security posture and can point to other hostnames/IPs the same operator runs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://leakix.net/ (register a free account for full search).
2. Search by host/IP, or use field queries like `protocol:mysql`, `port:3306`, `asn:...`, or a hostname.
3. Read results: exposed service banners, plugin/leak findings, host and geo/ASN details, and linked hostnames.
4. Use the graph view to see relationships between hosts.
5. Pivot: related `domain`s/`ip-address`es and ASNs feed further infrastructure mapping via `[[onyphe]]` and `[[securitytrails]]`.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, ASN, or a protocol/port query
- **Out:** exposed/misconfigured services, leak findings, host details, related `ip-address`/`domain`
- **Empty/negative result looks like:** a well-secured or unscanned host returns no findings — that's a clean/absent-from-index result, not proof of no exposure at any time; scan timing matters.

## Gotchas & OpSec
- Freemium: free account covers search/browse; full leak detail, bulk and API scale are paid.
- "Leak" results can include genuinely sensitive exposed data — mind the legal/ethical line and your authorised scope; don't access exposed systems.
- Scan data has a collection lag; a finding may be stale — confirm before acting.

## Overlaps ("do both")
- Pairs with `[[onyphe]]` and Shodan/Censys — coverage, scan timing and what each flags as a "leak" differ, so cross-checking surfaces exposures any single index misses.

## Trust & verifiability
`trust: community` — an independent scan/leak index with public documentation; findings are first-party observations you can corroborate against another scanner.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leakix |
