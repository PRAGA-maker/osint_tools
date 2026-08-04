---
id: ipfingerprints
name: IPFingerprints
description: Use when you have an `ip-address` or `domain` and want geolocation plus a live network profile (open ports, reverse DNS, WHOIS, mail auth) — returns location, host details, and open-service data.
url: http://www.ipfingerprints.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-stop web console for IP geolocation, port scanning, reverse DNS, WHOIS and mail-auth checks on an IP or domain.
selectorsIn:
- ip-address
- domain
selectorsOut:
- geolocation
- ip-address
- domain
status: live
pricing: free
costNote: Free browser tools; no account required.
opsec: active
opsecNote: The port scanner and ping probes send real packets to the target host from IPFingerprints' servers — that is active recon the target can log. Geolocation/WHOIS/DNS lookups are passive. Never point the scanner at infrastructure you are not authorized to probe; scan sparingly and assume it may be attributed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing free network-tools site; geolocation/WHOIS are drawn from standard databases (accuracy typical of GeoIP), reliable but not authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ip-finger-prints
- ip-fingerprints
- ip-fingerprints-reverse-ip-lookup
aliases:
- ipfingerprints.com
tags:
- domain-and-ip-research
- geolocation
- port-scan
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# IPFingerprints

> A free web console bundling IP geolocation, port scanning, reverse DNS, WHOIS, and email-auth checks — profile a host from one page.

## When to use
You have an `ip-address` (from an email header, a server log, a chat leak) or a `domain` and want to know where it sits and what it exposes: approximate `geolocation`, ISP/host, reverse DNS name, WHOIS registrant, and — via its port scanner — which services the host is running. Useful for characterising infrastructure a subject uses or corroborating an IP's claimed location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ipfingerprints.com in a sock-puppet browser over a VPN.
2. Pick a tool: **IP/Geo lookup** and **WHOIS/Reverse DNS** for passive profiling; **Port Scanner**/**Ping** for active probing.
3. Enter the `ip-address` or `domain` and run.
4. Read: geolocation (country/city/coords), ISP/ASN, reverse DNS hostname, WHOIS, and (for a scan) the list of open ports/services.
5. Pivot: reverse DNS/WHOIS → related `domain`s; open ports → service fingerprinting; geolocation → corroborate or contradict a claimed location.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** `geolocation`, host/ISP details, reverse DNS `domain`, WHOIS, open-port list
- **Empty/negative result looks like:** geolocation resolving only to a country (or to the datacenter, not a person), or a port scan showing all-filtered/closed — a hardened or proxied host reveals little; GeoIP city-level data is often imprecise, so never treat it as a street address.

## Gotchas & OpSec
- Human-in-the-loop: none, but the **port scan is active** — packets hit the target and can be logged/attributed. Only scan hosts you are authorized to, and prefer the passive tools first.
- OpSec: geolocation is datacenter/ISP-level, not person-level; VPN/hosting IPs will geolocate to the provider, not the subject.
- Accuracy of GeoIP and WHOIS varies; corroborate against a second source before drawing conclusions.

## Overlaps ("do both")
- Pairs with dedicated lookups like `[[shodan]]` (deeper service/banner data) and `[[whois-lookup]]` — IPFingerprints is a fast all-in-one first pass; those go deeper on ports/registration.

## Trust & verifiability
`trust: community` — an established free tools site pulling from standard GeoIP/WHOIS/DNS databases; results are reliable for a first pass but carry the usual GeoIP imprecision, so verify anything decision-critical elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipfingerprints |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → geolocation, ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
