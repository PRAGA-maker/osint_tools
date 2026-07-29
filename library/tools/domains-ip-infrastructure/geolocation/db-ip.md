---
id: db-ip
name: DB-IP
description: Use when you have an `ip-address` and want its approximate location and network owner — returns country/city, ISP/ASN, and organisation.
url: https://db-ip.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- geolocation
bestFor: Geolocating an IP to country/city and identifying its ISP/ASN/organisation, via a free web lookup, downloadable databases, or an API.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
- employer-org
status: live
pricing: freemium
costNote: Free web demo lookup and a free "IP to Country Lite" database; higher-accuracy city-level data and the API need a paid plan (free trial available). Free tier is fine for coarse geolocation.
opsec: passive
opsecNote: You query DB-IP's dataset, not the IP's owner — nothing is sent to the target. Only DB-IP sees your lookup. IP geolocation is approximate and can be wrong by city/region; never treat it as a person's precise location.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established IP-geolocation provider used by large firms; accurate at country level, approximate at city level. Like all IP geo, it locates the network/ISP node, not necessarily the user.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- ipinfo-io
- maxmind-geoip
- viewdns-info
aliases:
- DB-IP
- db-ip.com
tags:
- ip-geolocation
- asn
- network-intel
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# DB-IP

> An IP-geolocation service: enter an IP and get its approximate country/city plus the ISP/ASN and organisation behind it — available as a free lookup, downloadable DB, or API.

## When to use
You have an `ip-address` — from an email header, a server log, a WHOIS record, a login trace — and want to know roughly where it is and who runs the network. DB-IP returns country and (paid, more accurate) city, plus the ISP/ASN and organisation. It's a coarse "where and whose network" answer, useful for orienting a lead; it is not a precise locator of a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://db-ip.com/ and enter the IP in the demo lookup (or use the API/downloadable DB for volume).
2. Read: country/region/city (city is approximate and best on paid tiers), ISP, ASN, and organisation.
3. Judge the ISP/org type — a residential ISP hints at a home connection area; a datacentre/hosting ASN or a VPN/proxy provider means the IP is *not* a person's location at all.
4. Cross-check the geo against a second provider, since city-level answers disagree between databases.
5. Pivot: the ASN/org feeds infrastructure lookups (`[[viewdns-info]]`, Shodan); a hosting/VPN result tells you to stop treating the IP as a location and chase the service instead.

## Inputs → Outputs
- **In:** `ip-address`.
- **Out:** `geolocation` (country/city, approximate) and `employer-org` (ISP/ASN/organisation).
- **Empty/negative result looks like:** country-only or "unknown" city — common for VPNs, mobile carriers (CGNAT), and datacentre ranges; a datacentre/anonymiser result means the IP hides the real user.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — the IP's owner isn't contacted; only DB-IP logs your query.
- Accuracy caveat: IP geolocation locates the network node, not the person. City-level is an estimate (often off by tens of km), mobile IPs can geolocate to the carrier's hub, and VPN/proxy IPs are deliberately misleading. Never present it as a precise address.
- Best free data is country-level; city accuracy is a paid feature.

## Overlaps ("do both")
- Overlaps with `[[ipinfo-io]]` and `[[maxmind-geoip]]` — different providers disagree on city/ISP; query 2–3 and look for consensus rather than trusting one.
- Feeds `[[viewdns-info]]` — take the ASN/org onward for reverse-IP and infrastructure mapping.

## Trust & verifiability
`trust: community` — a reputable provider, reliable at country level. Treat city-level results as estimates and confirm against another database; remember it geolocates the network, not the individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | db-ip |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → geolocation, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
