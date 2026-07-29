---
id: shadowscatcher-shodan
name: shadowscatcher/shodan
description: Use when you have an `ip-address` or `domain` and want to query Shodan programmatically for exposed services/devices from Go — returns ip-address and domain infrastructure detail.
url: https://github.com/shadowscatcher/shodan
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Type-safe Go client for scripting Shodan.io device/service lookups at scale.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: freemium
costNote: The library is free/open-source, but it calls the Shodan API, which requires a Shodan account and API key. Shodan's free tier is limited; deeper filters/queries need a paid Shodan membership.
opsec: passive
opsecNote: Passive toward the subject — you query Shodan's pre-collected scan data, not the target's host directly. Your API key ties every query to your Shodan account, so use a dedicated research account for sensitive work.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: python-lib
trust: community
trustNote: Community Go SDK (~119 stars) wrapping the official Shodan REST API; it is a client, so data authority rests with Shodan, not this wrapper.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools: []
aliases:
- go-shodan
tags:
- shodan
- go
- internet-scanning
- iot
source: gh-topic-intelligence-gathering
lastVerified: '2026-07-29'
enrichment: full
---

# shadowscatcher/shodan

> A well-documented Go SDK for the Shodan.io internet-scan search engine, for scripting device/service lookups instead of clicking the web UI.

## When to use
You have an `ip-address` or `domain` (or an ASN/product filter) and want to enumerate the internet-exposed services, banners, certificates and open ports Shodan has already observed — and you want to do it in code, at scale, from a Go program. Pure infrastructure/attack-surface work; minimal direct people-finding value, but useful for tying a subject's server/domain to its hosting footprint.

## How to use it (`bestInteractionPattern`: python-lib)
1. Register at shodan.io and copy your API key (this is the human-in-the-loop step — a key is mandatory).
2. In a Go project, `go get github.com/shadowscatcher/shodan` and construct a client with your key.
3. Build a query using the SDK's structured search objects (filter by product, ASN, port, SSL/cert expiry, etc.) rather than raw strings.
4. Execute the search/host lookup and iterate the rich result models (services, certs, config data).
5. Pivot: discovered hostnames/certs/co-located IPs feed reverse-DNS and domain-mapping tools; an exposed service banner can corroborate ownership.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, or Shodan filter query
- **Out:** `ip-address` (host details, open ports/services), `domain` (associated hostnames, certificates)
- **Empty/negative result looks like:** an empty match set or a rate-limit/401 error — Shodan only returns what it has scanned, so "no results" means unobserved, not necessarily unexposed.

## Gotchas & OpSec
- Human-in-the-loop: you must obtain and supply a Shodan API key (`api-key`); registration required.
- OpSec: passive toward the target (Shodan already scanned it), but every query is logged against your Shodan account — segregate research identities.
- Language: this is a **Go** library, not Python; the `python-lib` tag here only marks it as a code-import SDK. Free-tier Shodan gates many filters behind a paid membership.

## Overlaps ("do both")
- Complements web-based Shodan and other internet-scan indexes — script this SDK when you need repeatable, bulk lookups that a browser UI can't sustain.

## Trust & verifiability
`trust: community` — the wrapper is community-maintained; the underlying data is Shodan's authoritative scan corpus. Cross-check any exposed-service finding directly against Shodan's own record before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shadowscatcher-shodan |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | yes (api-key) |
