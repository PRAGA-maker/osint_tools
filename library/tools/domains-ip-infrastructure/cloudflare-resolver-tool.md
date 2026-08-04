---
id: cloudflare-resolver-tool
name: Cloudflare Resolver Tool (ShadowCrypt)
description: Use when you have a `domain` fronted by Cloudflare and want to uncover the real origin `ip-address` behind the proxy — returns candidate origin IP(s) to pivot on.
url: https://shadowcrypt.net/tools/cloudflare
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Attempting to reveal the true origin server IP of a domain hidden behind Cloudflare's proxy.
selectorsIn:
- domain
selectorsOut:
- ip-address
status: live
pricing: freemium
costNote: Free to use in-browser; part of the free ShadowCrypt network-analysis tool suite (no account needed for basic lookups).
opsec: active
opsecNote: This queries live infrastructure (DNS history, subdomains, SSL/SAN data) about the target domain and may probe the origin directly. Run it over a VPN/sock-puppet; confirming and connecting to a revealed origin IP touches the target's server, which its owner can log.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of ShadowCrypt's network-analysis toolset; results depend on historical/leaked DNS records, so treat any origin IP as a candidate to verify, not a certainty.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- geoip-tracker-tool
- nmap-checker-tool
- page-links-extractor-tool
- phone-number-lookup-tool
- shadowcrypt-tools
aliases:
- ShadowCrypt Cloudflare Resolver
- Cloudflare origin IP finder
tags:
- cloudflare
- origin-ip
- domain-infrastructure
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Cloudflare Resolver Tool (ShadowCrypt)

> A browser tool that tries to strip away Cloudflare's proxy and surface the real origin server IP behind a domain.

## When to use
You have a `domain` that resolves only to Cloudflare's edge IPs and you need the *real* server it hides — for example to geolocate a host, find the hosting provider, or link a suspicious site to other domains on the same box. Cloudflare masks the origin by design; this tool checks the angles that commonly leak it (DNS history, subdomains that bypass the proxy, SSL certificate data) and reports any origin IP it can infer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://shadowcrypt.net/tools/cloudflare in a sock-puppet browser over a VPN.
2. Enter the target `domain` (e.g. `example.com`) and run the resolver.
3. Read the output: a candidate origin `ip-address` (or a "not found / still behind Cloudflare" result), often with the hosting/ASN context.
4. Verify a candidate before trusting it — request the site directly at that IP (Host header set to the domain) and confirm it serves the same content; a match strongly suggests it is the true origin.
5. Pivot: feed a confirmed IP into `[[geoip-tracker-tool]]` for location/ASN, `[[nmap-checker-tool]]` for open services, or reverse-IP lookups to find co-hosted domains.

## Inputs → Outputs
- **In:** `domain`
- **Out:** candidate origin `ip-address` (plus hosting/ASN context when available)
- **Empty/negative result looks like:** "no origin found" / only Cloudflare edge IPs returned — the origin is well-hidden (no leaking subdomain, no historical DNS exposure). That is a genuine dead-end for this method, not a tool error; try passive DNS history or certificate-transparency sources instead.

## Gotchas & OpSec
- Human-in-the-loop: none in the form, but you must manually verify the candidate IP — resolvers frequently return stale or unrelated IPs from old DNS records.
- OpSec: **active** — it probes infrastructure tied to the target domain, and any direct connection you make to a revealed origin can be logged by that server. Never connect from an attributable IP.
- A returned IP can be a shared host, a former server, or a decoy; treat it as a lead requiring corroboration, not proof of ownership.

## Overlaps ("do both")
- Chain with `[[geoip-tracker-tool]]` and `[[nmap-checker-tool]]` from the same ShadowCrypt suite — this finds the origin, those two geolocate and fingerprint it — and cross-check the result against independent passive-DNS/cert-transparency lookups since no single resolver is authoritative.

## Trust & verifiability
`trust: community` — ShadowCrypt is a live community network-analysis toolset; the technique is legitimate but inherently probabilistic (it relies on records that leaked the origin), so every returned IP must be independently confirmed before you act on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloudflare-resolver-tool |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
