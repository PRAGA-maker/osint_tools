---
id: ip-2-geolocation
name: IP 2 Geolocation
description: Use when you have an `ip-address` or `domain` and want its estimated location plus the owning ISP/company — returns geolocation, ip-address, employer-org.
url: http://ip2geolocation.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Free IP/domain geolocation with ISP and owner details.
selectorsIn:
- ip-address
- domain
selectorsOut:
- geolocation
- ip-address
- employer-org
status: live
pricing: free
costNote: Free web lookup indexing 4B+ IPs; no account or payment.
opsec: passive
opsecNote: Passive — the lookup runs against the service's own geolocation database; nothing is sent to the subject or the host whose IP you enter.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Consumer IP-geolocation site; results are database estimates that can be off by city/region and resolve VPN/proxy IPs to the operator — treat as approximate.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- IP2GeoLocation
- ip2geolocation.com
tags:
- domain-and-ip-research
- geolocation
- ip
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# IP 2 Geolocation

> A no-frills free lookup that turns an IP or domain into an estimated location plus the owning ISP/company — a quick corroborating geo check.

## When to use
You have an `ip-address` or a `domain` and want a one-shot estimate of **where it resolves and who owns the network** — continent, country, region, city, lat/long, ZIP, time zone, and the ISP or company name. Use it as one of two or three independent geolocation reads on an address, not as authoritative location for an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://ip2geolocation.com and enter an IP address, domain, or website.
2. If you enter a domain, it resolves the IP for you first.
3. Read the returned fields: country/region/city, latitude/longitude, ZIP/postal code, time zone, and the ISP/company (`employer-org`) that owns the address.
4. Pivot: the ISP/company name feeds a business/registry lookup; compare the location against `[[utrace]]` or `[[geo-data-tool]]` before trusting it; feed the IP into `[[bgpview-io]]` for authoritative ASN ownership.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** estimated `geolocation` (country → city, lat/long, ZIP, time zone), resolved `ip-address`, ISP/company `employer-org`
- **Empty/negative result looks like:** a private/reserved IP, no match, or a location that maps to a hosting/VPN provider — meaning the address is infrastructure and the point is a database estimate, not a residence.

## Gotchas & OpSec
- No login, CAPTCHA, or human-in-the-loop.
- Passive; nothing reaches the subject.
- Not to be confused with the commercial **IP2Location** family — this is a free consumer lookup, and its city/region precision is best-effort. VPN, proxy and mobile-carrier IPs resolve to the operator, never the person.

## Overlaps ("do both")
- Pairs with `[[utrace]]` and `[[geo-data-tool]]` — three independent geo databases disagree often enough that running more than one is the point.
- Pairs with `[[bgpview-io]]` for the authoritative network owner behind the estimated location.

## Trust & verifiability
`trust: community` — a widely-used free geo site with undocumented data sourcing; corroborate any location that matters against a second provider and the RIR WHOIS.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip-2-geolocation |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → geolocation, ip-address, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
