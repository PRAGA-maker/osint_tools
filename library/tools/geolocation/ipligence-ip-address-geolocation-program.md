---
id: ipligence-ip-address-geolocation-program
name: IPligence IP Address Geolocation
description: Use when you have an `ip-address` or `domain`/hostname and want its approximate city/country location — returns geolocation and a coarse address (city, country).
url: http://www.ipligence.com/geolocation
category: geolocation
path:
- geolocation
bestFor: A quick free city/country lookup for an IP, hostname, or URL.
selectorsIn:
- ip-address
- domain
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Free web lookup capped at 50 personal queries per day; a paid "IPligence Max" database and API exist for volume/commercial use. Provided "as is" with no accuracy guarantee.
opsec: passive
opsecNote: You query a geolocation database, not the target — the IP's owner is never contacted or alerted. Purely a lookup of data you already hold. Beware the result quality, not exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing commercial IP-geolocation vendor. The location data is best-effort ISP/registry-derived (city-level at best), so treat it as a lead, not fact.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- IPligence geolocation
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- ip-geolocation
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# IPligence IP Address Geolocation

> A free web lookup that maps an IP address, hostname, or URL to an approximate city and country on a map.

## When to use
You've obtained an `ip-address` (from email headers, a logged connection, a link tracker) or a `domain`/hostname, and you want a fast, no-signup sense of where it geolocates. Use it to sanity-check a claimed location or narrow a region — not to pinpoint a person's home.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ipligence.com/geolocation.
2. Enter an `ip-address`, hostname, or URL and submit.
3. Read the returned city/country and map marker.
4. Pivot: corroborate the region with a second geolocation provider; the resolved ISP/org can feed WHOIS/domain OSINT.

## Inputs → Outputs
- **In:** `ip-address`, hostname, or URL (`domain`)
- **Out:** `geolocation` (approximate coordinates/map) and a coarse `address` (city, country)
- **Empty/negative result looks like:** a country-only or "unknown" result, or an obviously wrong city — common for mobile carriers, VPNs, proxies, and CDN IPs, which geolocate to a datacenter or ISP hub, not the user.

## Gotchas & OpSec
- OpSec: passive — nothing is sent to the target; you're querying a database.
- Accuracy: free IP geolocation is city-level *at best* and frequently wrong. VPN/proxy/mobile IPs defeat it entirely. Never treat a hit as a physical address.
- Free tier is limited to 50 lookups/day; heavy use needs the paid product.

## Overlaps ("do both")
- Always cross-check with at least one other IP-geolocation source — providers disagree, and agreement across two is the only real signal. Combine with WHOIS/RDAP on the owning netblock for the ISP/org behind the IP.

## Trust & verifiability
`trust: community` — an established commercial vendor, but the underlying geolocation is inference from registry/ISP data, not ground truth. Reliable for country, shaky for city, useless for a street address.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipligence-ip-address-geolocation-program |
| category | geolocation |
| selectorsIn → selectorsOut | ip-address, domain → geolocation, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
