---
id: maxmind
name: MaxMind
description: Use when you have an `ip-address` and want its likely geolocation and network — returns country/region/city, ASN, and ISP/organization from MaxMind's GeoIP databases.
url: https://www.maxmind.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: IP-to-location and IP-to-ISP/ASN lookups via the industry-standard GeoIP databases (free GeoLite2 tier).
selectorsIn:
- ip-address
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: GeoLite2 databases and a limited GeoLite2 web/API lookup are free with a (free) MaxMind account; the higher-accuracy GeoIP2 databases and API are paid.
opsec: passive
opsecNote: You query MaxMind's local database (or their API) about an IP — you never touch the target's host, so the lookup is invisible to the subject. Downloading the GeoLite2 DB for offline use is the most private option.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: api
trust: trusted
trustNote: MaxMind is the de-facto industry standard for IP geolocation; widely used, well-documented, with published accuracy figures.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
invitationOnly: false
relatedTools:
- maxmind-demo
aliases:
- GeoIP
- GeoLite2
- GeoIP2
tags:
- ip-geolocation
- geoip
- asn
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# MaxMind

> The industry-standard GeoIP databases: resolve an `ip-address` to a country/region/city estimate plus its ASN and ISP/organization — free at the GeoLite2 tier.

## When to use
You have an `ip-address` (from an email header, a server log, a connection, a breach record) and want to place it geographically and identify the network behind it. MaxMind maps the IP to an approximate `geolocation` (country → city) and to its ASN/ISP, letting you gauge where a connection likely originated and whether it is a residential ISP, hosting provider, or VPN/proxy range.

## How to use it (`bestInteractionPattern`: api)
1. Create a free MaxMind account and get a license key.
2. Choose your path:
   - **Offline (most private):** download the free GeoLite2 City/ASN databases and query them locally with a MaxMind reader library (Python `geoip2`, etc.).
   - **API/web:** use the GeoLite2 web service (free, rate-limited) or paid GeoIP2 for higher precision.
3. Look up the IP; read the returned country/region/city, coordinates (with an accuracy radius), ASN, and organization.
4. Judge confidence: city-level results are estimates with an accuracy radius — treat country/ASN as strong, city as indicative.
5. Pivot: the ASN/ISP feeds infrastructure OSINT (is this a hosting/VPN provider?); the location narrows a subject's likely region for other tools.

## Inputs → Outputs
- **In:** an `ip-address`
- **Out:** `geolocation` (country/region/city + accuracy radius), ASN, ISP/organization (`address`-level network attribution)
- **Empty/negative result looks like:** the IP resolves only to a country (or "anonymous proxy"/hosting range) with no meaningful city — common for VPNs, mobile carriers, and CGNAT; do not over-read a coarse result.

## Gotchas & OpSec
- Human-in-the-loop: a free account/license key is required to download DBs or use the API.
- OpSec: passive — you query MaxMind, not the target's host. Offline DB use leaks nothing at all.
- Accuracy varies widely: country-level is reliable, city-level is an estimate, and VPN/mobile/CGNAT IPs frequently mislocate. Never treat a MaxMind city as a person's address.
- The free GeoLite2 is less precise than paid GeoIP2; state which you used when reporting.

## Overlaps ("do both")
- Pairs with other IP-intelligence sources (Shodan, ipinfo, threat feeds): MaxMind is the baseline geo/ASN layer; cross-check VPN/proxy detection and open-port data from those to interpret the IP correctly.

## Trust & verifiability
`trust: trusted` — the reference implementation for IP geolocation, transparent about accuracy limits; the numbers are authoritative *as estimates*, and you can reproduce any lookup against the same database version.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maxmind |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → geolocation, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (account-login) |
