---
id: maxmind-demo
name: MaxMind Demo
description: Use when you have an `ip-address` and want a quick country/region/city/ASN geolocation estimate — returns approximate `geolocation` and network owner.
url: https://www.maxmind.com/en/geoip-demo
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- geolocation
bestFor: A fast, single-IP geolocation and ASN lookup against MaxMind's GeoIP2 database via their web demo.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
- domain
status: live
pricing: free
costNote: The web demo is free; a MaxMind account/login is required to run it, and bulk/programmatic use needs a paid GeoIP2 subscription or the free GeoLite2 database.
opsec: passive
opsecNote: You query MaxMind's database, not the target host, so the subject's IP is never contacted — but the lookup is tied to your MaxMind account. Use a dedicated account for investigative work.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: MaxMind is the industry-standard commercial IP-geolocation provider; its GeoIP2 data underpins many other tools, though city-level accuracy is an estimate.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- maxmind
aliases:
- MaxMind GeoIP demo
- GeoIP2 demo
tags:
- ip-geolocation
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# MaxMind Demo

> MaxMind's own GeoIP2 web demo — paste an IP and get the country/region/city and network (ASN) that the industry-standard geolocation database attributes to it.

## When to use
You have an `ip-address` from an email header, a log, a website visit, or another tool and want a quick, reputable estimate of where it geolocates and who owns the network. Because MaxMind's GeoIP2 is the reference dataset many other services resell, the demo is a good sanity check on an IP's location and ASN.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in with a (dedicated) MaxMind account and open https://www.maxmind.com/en/geoip-demo.
2. Enter the `ip-address` and submit.
3. Read the result: country, region, city, approximate coordinates, ASN/ISP, and connection-type where available.
4. Treat city-level as an estimate — country/ASN is reliable, precise street location is not.
5. Pivot: the ASN/ISP (`domain`) and rough `geolocation` guide which region and provider to pursue; for automation, use GeoLite2 (free DB) or the paid API rather than the demo.

## Inputs → Outputs
- **In:** an `ip-address`
- **Out:** country/region/city `geolocation` estimate, coordinates, ASN/ISP (`domain`)
- **Empty/negative result looks like:** private/reserved ranges (10.x, 192.168.x) or unallocated IPs return no meaningful location — that's expected, not a lookup failure.

## Gotchas & OpSec
- Human-in-the-loop: MaxMind requires account login to use the demo; it also rate-limits demo queries.
- City-level geolocation is approximate and can be wrong by tens of kilometres or reflect the ISP's hub, not the user — never treat it as a person's address; VPNs/proxies further distort it.
- OpSec: passive toward the target; attributable to your MaxMind account.

## Overlaps ("do both")
- Pairs with `[[maxmind]]` and other IP-geolocation services — cross-check one IP across two providers, since geolocation databases disagree and none is ground truth.

## Trust & verifiability
`trust: trusted` — MaxMind is the canonical commercial GeoIP source; country/ASN attribution is authoritative, while city precision remains a best-effort estimate to be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maxmind-demo |
