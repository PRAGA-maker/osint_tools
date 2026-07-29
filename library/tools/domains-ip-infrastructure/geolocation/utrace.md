---
id: utrace
name: utrace
description: Use when you have an `ip-address` or `domain` and want a fast approximate geolocation plus ASN/provider and route path — returns geolocation, ip-address.
url: https://en.utrace.de/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- geolocation
bestFor: Quick approximate IP/domain geolocation with ASN, provider and optional traceroute.
selectorsIn:
- ip-address
- domain
selectorsOut:
- geolocation
- ip-address
status: live
pricing: free
costNote: Free German geolocation service with a free public XML API (utrace.de/api.php); no key or account.
opsec: active
opsecNote: The geolocation lookup itself is passive (utrace's cached database). The optional traceroute runs from utrace's servers and sends probe packets toward the target IP — active toward the host, but it does not reveal you to the subject. Nothing identifies the investigator.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Consumer IP-geolocation site of unknown data provenance; results are database estimates and should be treated as approximate and corroborated elsewhere.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- utrace
- en.utrace.de
tags:
- domain-and-ip-research
- geolocation
- ip
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# utrace

> A lightweight, free IP/domain locator that maps an address to a country/region, its ASN and provider, and can trace the route to it — good for a first, low-effort geolocation pass.

## When to use
You have an `ip-address` (from an email header, server log, or another tool) or a `domain`, and you want a quick estimate of **where it sits and whose network it is on** before committing to heavier tooling. utrace returns an approximate country/region on a map plus the ASN, reverse DNS, and provider, and can run a traceroute to show the path. Use it as a fast corroborating check, not as authoritative location for a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.utrace.de/ and enter an IP address or hostname.
2. Read the result: estimated location (marked on a map), country, ASN/provider, and reverse DNS.
3. Optionally trigger the traceroute/route view to see the network path to the host.
4. For scripting, call the free XML API — `https://xml.utrace.de/?query=<ip>` (see `en.utrace.de/api.php`) — no key required.
5. Pivot: feed the ASN/provider into `[[bgpview-io]]` for authoritative ownership; compare the estimated location against a second geolocation source before trusting it.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** estimated `geolocation` (country/region, map point), resolved `ip-address`, ASN/provider, reverse DNS
- **Empty/negative result looks like:** a private/reserved IP, a "not found," or a location that lands on a datacentre/VPN provider — meaning the address is infrastructure, not a residence, and the point is only a database estimate.

## Gotchas & OpSec
- No login, no CAPTCHA, no human-in-the-loop.
- The site occasionally shows a transient "Can't connect to database" error — retry, or fall back to another geolocation source.
- The location is an **estimate** (often only accurate to country/region) and resolves VPN/proxy/mobile-carrier IPs to the operator, never to the actual person.

## Overlaps ("do both")
- Pairs with `[[geo-data-tool]]` and `[[ip-2-geolocation]]` — running two independent geo databases and comparing them catches the frequent case where one is badly wrong.
- Pairs with `[[bgpview-io]]` for the authoritative ASN/owner behind the estimated location.

## Trust & verifiability
`trust: unverified` — data provenance isn't documented and estimates vary between providers; never present a utrace location as a confirmed physical address without independent corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | utrace |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → geolocation, ip-address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
