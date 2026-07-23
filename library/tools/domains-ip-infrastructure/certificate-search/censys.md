---
id: censys
name: Censys
description: Use when you have a `domain`, `ip-address`, or certificate detail and want internet-wide scan data on it — returns hosts, open ports, service banners, and TLS certificates that reveal related infrastructure.
url: https://censys.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- certificate-search
bestFor: Searching internet-wide host and certificate scan data to enumerate a target's infrastructure and find related assets.
input: Domain, IP, certificate fingerprint, search query
output: Host details, open ports, TLS certificates, service banners
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
- geolocation
status: live
pricing: freemium
opsec: passive
opsecNote: Censys serves results from its own internet-wide scans, so you never touch the target's host and it isn't alerted. A free account is required and its API/UI queries are logged against your account — use a dedicated investigative account and keep API keys isolated.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Censys (a reputable internet-measurement company, ex-University of Michigan); scan data is authoritative within scan cadence.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- censys-certificates
- censys-ipv4
- search-censys-io
aliases:
- Censys
- search.censys.io
tags:
- certificate-search
- host-enumeration
- attack-surface
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Censys

> An internet-wide scan database — query a domain, IP, or certificate and get the hosts, ports, services, and TLS certificates behind it, exposing infrastructure a subject would rather keep separate.

## When to use
You have a `domain` or `ip-address` and want its real attack surface, or you have a TLS certificate detail (SAN, fingerprint, org) and want every host that presents it. Censys's power is *pivoting on certificates and banners*: a shared self-signed cert, an unusual service banner, or a favicon hash can tie a subject's public site to hidden dev/staging boxes, other domains, or an origin server behind a CDN.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in at https://search.censys.io/ (free account required).
2. Search a `domain`/`ip-address`, or write a query on certificate/service fields (e.g. `services.tls.certificates.leaf_data.subject.organization: "Acme"`).
3. Read results: host IPs, open ports, service banners/software, TLS certificate details, and location/AS (`selectorsOut`).
4. Pivot: take a certificate fingerprint or org string and re-search to find all hosts sharing it; feed new IPs/domains back into DNS/WHOIS. API supports bulk work.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, certificate fingerprint, or a field query
- **Out:** `ip-address` (hosts), related `domain`s (via certs/SANs), `geolocation`/AS, open ports, service banners, TLS certificates
- **Empty/negative result looks like:** no hosts/certs match — the asset may be unscanned, behind a CDN masking the origin, or freshly stood up; absence isn't proof it doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: free account/login required (`account-login`); free tier has query/result caps.
- OpSec: passive — results come from Censys's scans, not a probe you send; the target sees nothing.
- Scan cadence means data can lag hours/days; CDN/proxy fronting hides origin hosts unless a leaked cert or misconfig exposes them.

## Overlaps ("do both")
- Pairs with [[search-censys-io]] / [[censys-certificates]] (same platform, focused views) and with Shodan and crt.sh — cross-run because each scanner's coverage and certificate indexing differ, and one often exposes an origin the others miss.

## Trust & verifiability
`trust: trusted` — Censys is a reputable internet-measurement provider with rigorous scanning; its data is authoritative within scan timing. Certificate/banner pivots are strong evidence of shared infrastructure, but confirm a link with a second source before asserting common ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | censys |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
