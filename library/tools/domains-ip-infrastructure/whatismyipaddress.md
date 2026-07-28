---
id: whatismyipaddress
name: WhatIsMyIPAddress
description: Use when you have an `ip-address` and want quick geolocation, ISP/hostname, and blacklist context — returns `geolocation`, `domain`, and network attribution.
url: http://whatismyipaddress.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast lookup of an IP's approximate location, ISP/hostname, and whether it's a known proxy/blacklisted.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
- domain
- ip-address
status: live
pricing: free
costNote: Free web lookups; the site upsells a VPN but the IP tools require no payment or account.
opsec: passive
opsecNote: You are querying a third-party database about an IP, not contacting the IP itself, so the target is not alerted. If you leave the input blank it reveals YOUR OWN public IP — always type the target IP in explicitly when investigating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial IP-info site; geolocation is database-derived and approximate (city/ISP level, not a street address).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatismyipaddress-blacklist-checker
- whatismyipaddress-com
aliases:
- whatismyipaddress.com
- what is my ip address
tags:
- domain-and-ip-research
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# WhatIsMyIPAddress

> A one-stop IP-info site: paste an address and get its city-level geolocation, ISP/hostname, and proxy/blacklist reputation.

## When to use
You have an `ip-address` — from an email header, server log, chat metadata, or another tool — and want a fast read on where it geolocates, who the ISP/host is, and whether it's a known proxy/VPN or blacklisted. Useful to sanity-check an IP's plausibility (e.g. does the claimed location match) before deeper attribution work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://whatismyipaddress.com and open the "IP Lookup" tool (not the homepage, which shows *your* IP).
2. Enter the target `ip-address` and submit.
3. Read the returned card: approximate `geolocation` (country/region/city, lat-long), ISP and organization, reverse-DNS `domain`/hostname, and connection type.
4. Optionally run the site's Blacklist Check and Hide-My-IP (proxy detection) tools on the same address.
5. Pivot: feed the ISP/hostname into WHOIS/ASN tools; use the geolocation only as a coarse hint, never as a precise address.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** `geolocation` (city/ISP level), `domain` (reverse-DNS hostname), `ip-address` attribution (ISP, ASN, proxy/blacklist flags)
- **Empty/negative result looks like:** "No results / invalid IP" for a malformed address; a valid IP with only country-level data (no city) means the geolocation DB has coarse coverage there — not an error.

## Gotchas & OpSec
- Geolocation is **database-derived and approximate** — often the ISP's hub city, not the user's actual location. Never treat it as a home address.
- Leaving the box empty returns *your* IP; always type the target's address so you don't confuse the two.
- Passive: the target IP is not contacted, so no alert is generated.

## Overlaps ("do both")
- Pairs with `[[whatismyipaddress-blacklist-checker]]` (reputation) and `[[whatismyipaddress-com]]`, and with independent geo/ASN sources — cross-check because IP databases disagree on city and proxy status.

## Trust & verifiability
`trust: community` — a well-established commercial site, but its geolocation and proxy flags come from third-party databases; corroborate location claims with at least one other provider.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatismyipaddress |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → geolocation, domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
