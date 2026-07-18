---
id: infosniper-net
name: infosniper.net
description: Use when you have an `ip-address` or `domain` and want its approximate geolocation — returns country/region/city, ISP and coordinates plotted on a map.
url: https://www.infosniper.net/index.php?lang=1
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quick IP/domain geolocation with ISP, coordinates and a map view.
selectorsIn:
- ip-address
- domain
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: A few free lookups per day (≈5) with basic detail; a low-cost Pro tier removes ads and unlocks fuller ISP/hostname data.
opsec: passive
opsecNote: InfoSniper geolocates from its own databases, so the target IP/host isn't contacted by you. Only InfoSniper logs the value you looked up; a clean session is enough.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party aggregator of commercial IP-geolocation databases; results are approximate (ISP/city level at best) and can be defeated by VPN/proxy/mobile networks.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- info-sniper
- infosniper
aliases:
- InfoSniper
- infosniper.net
tags:
- domainsandips
- Domains & IPs
- ip-geolocation
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# infosniper.net

> A quick IP/domain geolocation lookup — country, region, city, ISP and coordinates on a map, with a handful of free checks a day.

## When to use
You have an `ip-address` (from an email header trace, a server log, a link) or a `domain` and want a fast read on **where it's hosted/located** and which ISP/organisation runs it. Useful for corroborating a claimed location, spotting a mismatch, or getting an ISP/city to feed into further work. Treat the location as approximate — IP geolocation places the *network*, not necessarily the person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.infosniper.net/.
2. Enter the `ip-address` or `domain` and run the lookup (you have a small number of free lookups per day).
3. Read: country/region/**city**, **ISP/organisation**, hostname, timezone, and latitude/longitude on the map.
4. Cross-check the result against a second geolocation source — providers disagree, especially at city level.
5. Pivot: ISP/org feeds infrastructure work (WHOIS, HE BGP); the coordinates give a coarse map anchor, not an address.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** `geolocation` — country/region/city, ISP/org, coordinates, timezone
- **Empty/negative result looks like:** only a country (no city), or a datacentre/hosting location rather than a user — typical for cloud, VPN, proxy, or mobile CGNAT IPs. The IP was never the person's home.

## Gotchas & OpSec
- Human-in-the-loop: **rate-limit** — only ~5 free lookups/day; heavier use needs the paid tier.
- OpSec: **passive** — InfoSniper does the geolocating; the target host isn't touched.
- **Approximate by nature:** IP geolocation is often accurate only to country/region; city-level is a guess and VPN/proxy/mobile networks routinely mislocate. Never treat the city as the subject's location without corroboration.
- Free-tier detail is limited; the pinpoint on the map is the database centroid, not a precise address.

## Overlaps ("do both")
- Do both with another geolocation source (e.g. `[[ip2location-free-email-header-tracer]]` for the IP, or MaxMind/ipinfo) and with `[[hurricane-electric-internet-services]]` for the network/ASN — geolocation databases disagree, so consensus across tools is the reliable signal.

## Trust & verifiability
`trust: community` — an aggregator of commercial geolocation data; dependable for country and ISP, unreliable for precise location, so corroborate before acting on a city-level result.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infosniper-net |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
