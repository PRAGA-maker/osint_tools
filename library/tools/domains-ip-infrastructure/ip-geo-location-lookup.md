---
id: ip-geo-location-lookup
name: IP GEO Location Lookup
description: Use when you have an `ip-address` and want its approximate location and network owner — returns country/region/city, coordinates, ISP and ASN.
url: https://osint.sh/ip/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quickly geolocating an IP address to country/region/city plus its ISP and ASN, as part of the free OSINT.SH tool suite.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
- employer-org
status: live
pricing: freemium
costNote: Free to use with no account for the web lookup; part of the donation-supported OSINT.SH suite.
opsec: passive
opsecNote: The lookup resolves the IP against geolocation databases held by OSINT.SH — it does not connect to the target IP, so the subject is not alerted. OSINT.SH sees which IP you queried; use a research session for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of the well-known free OSINT.SH toolset; results come from commercial/open IP-geolocation databases, which are accurate to city level at best and often only to country/ISP.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatismyipaddress
- criminal-ip-search
- radb
aliases:
- osint.sh ip lookup
- IP geolocation
tags:
- Domain/IP investigation
- geolocation
- osint4all
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# IP GEO Location Lookup

> The IP-geolocation tool in the free OSINT.SH suite: paste an IP and get its country/region/city, map coordinates, ISP and ASN in one view.

## When to use
You have an `ip-address` — from an email header, a server log, a chat leak, a website's hosting — and want a fast read on where it's located and which network owns it. This gives you approximate `geolocation` (country → region → city) plus the ISP/ASN, enough to sanity-check a claimed location or to hand off to deeper infrastructure tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/ip/.
2. Enter the target `ip-address` (IPv4 or IPv6) and submit.
3. Read the result: country, region, city, latitude/longitude (often on a small map), plus ISP/organisation and ASN.
4. Treat the location as **approximate** — accurate to country/ISP reliably, to city only sometimes, and never to a street address.
5. Pivot: the ISP/ASN feeds routing and org lookups (`[[radb]]`); the IP feeds exposure scanners (`[[criminal-ip-search]]`); explore the rest of the OSINT.SH suite (reverse IP, WHOIS history, tech stack) for the same target.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** `geolocation` (country/region/city + coordinates), `employer-org` (ISP/hosting org + ASN)
- **Empty/negative result looks like:** a bogon/private/reserved IP (e.g. `10.x`, `192.168.x`) returns no meaningful location; a datacenter/VPN/mobile-carrier IP geolocates to the provider's hub, not the user — treat those as "provider location, not person location".

## Gotchas & OpSec
- IP geolocation is **inference from databases**, not GPS — city-level accuracy is unreliable and VPNs/proxies/mobile CGNAT routinely mislead it.
- A hosting/VPN/Tor exit IP tells you about the infrastructure, not the individual behind it.
- Passive: nothing touches the target IP; only OSINT.SH sees the query.

## Overlaps ("do both")
- Pairs with `[[whatismyipaddress]]` — a second geolocation source to cross-check the city/ISP, since databases disagree.
- Feeds `[[radb]]` (routing/AS owner) and `[[criminal-ip-search]]` (what the host exposes) once you have the IP and its ASN.

## Trust & verifiability
`trust: community` — OSINT.SH is a reputable free suite, but the underlying geolocation is only as good as the commercial/open databases it draws on; confirm any location-critical claim against a second geolocation provider and the routing registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip-geo-location-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → geolocation, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
