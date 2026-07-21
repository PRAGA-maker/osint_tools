---
id: ipanalyzer-privacy-test
name: IPalyzer
description: Use when you have an `ip-address` (or `domain`) and want its geolocation, network owner, reverse DNS, open services and blacklist status in one report — returns `geolocation`, `domain`, `address`.
url: https://www.ipalyzer.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-page enrichment of an IP or domain — location, owner/ASN, rDNS, running services and spam-blacklist status.
selectorsIn:
- ip-address
- domain
selectorsOut:
- geolocation
- domain
- address
status: live
pricing: free
costNote: Free, donation-supported (PayPal donate link); no account required.
opsec: passive
opsecNote: The lookup runs on IPalyzer's servers against public databases (MaxMind, WHOIS, blacklists), so the target is not contacted directly — but the third-party operator sees which IP/domain you query; use a sock puppet for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent hobby/donation tool aggregating MaxMind GeoIP, WHOIS and Spamhaus/Barracuda/SpamCop blacklists; the underlying sources are reputable but geolocation is ISP-level (city at best), never a street address of a person.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- geobytes-ip-locator
- censys-ipv4
- iana-whois-service
aliases:
- ipalyzer.com
- IP Analyzer
tags:
- domains-ip-infrastructure
- ip-lookup
- geoip
- blacklist
- toddington
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# IPalyzer

> A single-page IP/domain profiler: feed it an address and get location, network owner, reverse DNS, exposed services and spam-blacklist hits together.

## When to use
You have an `ip-address` (from an email header, server log, chat metadata, or a WHOIS record) or a `domain`, and want a fast, consolidated picture: what network and country/city it sits in, who owns the block (ASN/ISP/org), what its reverse DNS name is, what services it exposes, and whether it's flagged on major spam blacklists. Useful for grounding an IP to a rough location and owner before deeper infrastructure work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ipalyzer.com in a clean/sock-puppet browser.
2. Enter the `ip-address` or `domain` and run the lookup.
3. Read the report: geolocation (country/region/city + coords), network owner/ASN/CIDR, reverse DNS host, running services, and blacklist status (Spamhaus/Barracuda/SpamCop).
4. Note the ISP/org and rDNS host — these are the pivot points (an rDNS name can reveal a hosting provider, a corporate netblock, or a residential ISP).
5. Pivot: confirm/expand with `[[iana-whois-service]]` for authoritative registration, `[[censys-ipv4]]` for exposed-service and certificate detail, or `[[geobytes-ip-locator]]` for a second geolocation opinion.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** `geolocation` (ISP-level city/region + coordinates), `domain` (reverse DNS / hostnames), `address` (registered org/owner of the netblock)
- **Empty/negative result looks like:** a private/reserved IP, an unrouted address, or a lookup that returns only "unknown" fields — meaning no public registration/geo data, not a wrong target.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — no packets to the target; the operator logs your query, so sock-puppet for sensitive cases.
- Geolocation is at the ISP/city level and can be off by a wide margin (especially mobile carriers, VPNs, and CDNs). It is **never** a person's home address — the "address" it shows is the network owner's registration, not the subject's.

## Overlaps ("do both")
- Pairs with `[[iana-whois-service]]` — that gives the authoritative registrant/ASN record, while IPalyzer bundles geo + blacklist + rDNS in one view.
- Pairs with `[[censys-ipv4]]` for a deeper look at exposed services and TLS certificates on the same host.

## Trust & verifiability
`trust: unverified` — an independent donation-supported aggregator; its inputs (MaxMind, WHOIS, major blacklists) are reputable, but cross-check anything decisive against the primary source rather than relying on the aggregated page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipanalyzer-privacy-test |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → geolocation, domain, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
