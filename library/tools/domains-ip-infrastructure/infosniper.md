---
id: infosniper
name: Infosniper
description: Use when you have an `ip-address` and want its approximate geographic location and network operator — returns `geolocation` plus ISP/host details.
url: http://www.infosniper.net
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quick IP-to-location lookup showing country/region/city, coordinates on a map, and the ISP behind an address.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: A handful of free lookups per day (≈5); full detail (city, coordinates, provider) and higher volume need a Pro pass (≈$7) or an API key.
opsec: passive
opsecNote: Query hits Infosniper's geolocation database, not the target host — the subject is not contacted or alerted. Never confuse the ISP's registered city with the person's real location.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent third-party geolocation aggregator; accuracy is database-derived and coarse (often only correct to country/region), not authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- infosniper.net
tags:
- domain-and-ip-research
- ip-geolocation
source: awesome-osint
lastVerified: '2026-07-23'
relatedTools:
- info-sniper
- infosniper-net
---

# Infosniper

> A lightweight web IP-geolocation lookup: paste an address, get its country/region/city, map pin, and ISP.

## When to use
You have an `ip-address` — from an email header, server log, chat metadata, or another OSINT tool — and want a fast read on where it geolocates and which network operator controls it. Use it to sanity-check an IP's claimed origin or to identify the hosting/ISP behind infrastructure, not to pin a person to a street.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.infosniper.net.
2. Enter the target IPv4 or IPv6 address (leave blank to see your own).
3. Read the result: country, region, city, latitude/longitude on a map, timezone, and the ISP/organization. Detailed fields may be gated behind Pro/API.
4. Pivot: the ISP/org feeds WHOIS and ASN lookups; the coarse location narrows (not fixes) a region; cross-check against a second geolocation source before relying on it.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** `geolocation` (country/region/city, coordinates), ISP/organization
- **Empty/negative result looks like:** private/reserved IP, or a result that resolves only to a country with no city — treat low-granularity hits as "unknown city", not as evidence.

## Gotchas & OpSec
- Free tier is limited to a few lookups per day and masks detail; the cost note applies.
- Geolocation reflects the IP registration/allocation, which can be the ISP's headquarters or a datacenter — often tens or hundreds of miles from the actual user, and useless for VPN/proxy/mobile-CGNAT addresses.
- OpSec: **passive** — you query Infosniper's DB, not the subject's host.

## Overlaps ("do both")
- Pairs with WHOIS/ASN and a second geolocation provider — IP geolocation databases disagree, so corroborate before drawing a conclusion.

## Trust & verifiability
`trust: community` — a serviceable independent aggregator, but its data is estimated and should never be presented as a precise or authoritative location.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infosniper |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
