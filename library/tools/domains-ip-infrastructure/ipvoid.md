---
id: ipvoid
name: IPVoid
description: Use when you have an ip-address or domain and want reputation, geolocation, blacklist status, WHOIS and DNS details in one place — returns geolocation, domain, and reputation signals.
url: https://www.ipvoid.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-stop free web toolkit for IP/domain reputation, geolocation, blacklist checks, and DNS/WHOIS lookups.
selectorsIn:
- ip-address
- domain
selectorsOut:
- geolocation
- domain
- ip-address
status: live
pricing: free
costNote: Web tools are free with no account; the related APIVoid service (programmatic access) is the paid product, but the browser tools here are free.
opsec: passive
opsecNote: Lookups are made from IPVoid's servers against public reputation/DNS data, so the target does not see your query. Still avoid tools that actively probe (their port-scan/screenshot utilities touch the target host directly) unless that's intended.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running toolkit by NoVirusThanks Company; aggregates well-known public blacklists and DNS/WHOIS sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ipvoid-com
aliases:
- IP Void
- NoVirusThanks IPVoid
tags:
- domain-and-ip-research
- reputation
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# IPVoid

> A free browser toolkit for IP and domain intelligence — reputation, geolocation, blacklist status, WHOIS, DNS, and URL checks in one site.

## When to use
You have an `ip-address` or `domain` (from an email header, a server log, a suspicious link, a Wireshark capture) and want to characterize it quickly: where it geolocates, who owns it, whether it appears on spam/malware blacklists, and its DNS/WHOIS footprint. It's infrastructure attribution and triage — useful for corroborating a lead, not for identifying a person directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ipvoid.com/ and pick a tool: **IP Blacklist Check**, **IP Geolocation**, **WHOIS**, **Reverse DNS**, **MX Lookup**, **URL Reputation**, etc.
2. Paste the `ip-address` or `domain` and run the check.
3. Read the report: `geolocation` (country/region, ISP/ASN), blacklist hits, WHOIS registrant/registrar, and DNS records.
4. Cross-reference across tools — a blacklisted IP + a fresh WHOIS date + a mismatched geolocation is a strong "suspicious infrastructure" signal.
5. Pivot: an ISP/ASN or registrant → deeper WHOIS/BGP tooling; an `email` found in WHOIS → email-OSINT.

## Inputs → Outputs
- **In:** an `ip-address` or `domain`.
- **Out:** `geolocation` (country, ISP, ASN), blacklist/reputation status, WHOIS registrant, and DNS records.
- **Empty/negative result looks like:** an IP that is not on any blacklist and geolocates to a generic residential/cloud ISP with privacy-protected WHOIS — informative (clean, but anonymized), not a dead end.

## Gotchas & OpSec
- Geolocation is ISP-level, not a home address — never present it as a physical location of a person.
- Reputation aggregates third-party blacklists; a "clean" result is not proof of safety, and a listing can be stale.
- The port-scan/screenshot utilities actively contact the target host — use those deliberately, not by reflex.

## Overlaps ("do both")
- Pairs with [[ipvoid-com]] (the same provider's email-tracer): this covers IP/domain reputation while that one dissects email headers to the originating IP.

## Trust & verifiability
`trust: trusted` — established provider (NoVirusThanks) aggregating recognized public sources; each check is reproducible and traceable to its underlying blacklist/registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipvoid |
