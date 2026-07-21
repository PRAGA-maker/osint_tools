---
id: myip-ip-address
name: MyIP.ms
description: Use when you have an `ip-address` or `domain` and want its geolocation, hosting/ISP owner, WHOIS and reverse-IP neighbors — returns `geolocation`, hosting `employer-org`, and co-hosted `domain`s.
url: https://myip.ms
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Enriching an IP or domain with geolocation, hosting owner, WHOIS and reverse-IP neighbors from a large IP-intelligence database.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
- geolocation
status: live
pricing: freemium
costNote: Basic IP/domain lookup (location, ISP, blacklist status, WHOIS) is free; downloadable databases, API access and bulk/Excel exports are paid.
opsec: passive
opsecNote: Queries run against MyIP.ms's own database, so the target host never sees you. Only MyIP.ms sees the IP/domain you look up; no login needed for the free lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Large commercial IP-intelligence database (hundreds of millions of sites indexed); geolocation and hosting data are good but, like all IP data, approximate and occasionally stale.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- myip.ms
- MyIP world IP database
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- reverse-ip
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# MyIP.ms

> A large free-tier IP-intelligence database: paste an IP or domain and get its location, hosting owner, WHOIS, blacklist status and reverse-IP neighbors on one page.

## When to use
You have an `ip-address` (from an email header, a server log, a website) or a `domain` and want to know *where* it sits and *who* runs it — country/city geolocation, the ISP or hosting `employer-org`, WHOIS registration, and other domains sharing the same IP. Useful for grounding a digital trail in a physical location and hosting provider, and for clustering a subject's web properties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://myip.ms (it also shows *your* own IP on the landing page — ignore that).
2. Enter the target `ip-address` or `domain` in the lookup box and submit.
3. Read the enrichment card: geolocation (country/state/city + map), ISP/hosting organization, WHOIS/owner details, blacklist status, and a reverse-IP list of other sites on the same server.
4. Follow the "Other Websites on this IP" and WHOIS links to expand the picture.
5. Pivot: the hosting `employer-org` and abuse/registrant contacts feed provider-side inquiries; the geolocation narrows a physical region; co-hosted domains feed further reverse-IP/WHOIS work.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** `geolocation` (country/city), hosting/ISP `employer-org`, `ip-address` ↔ `domain` resolution, and reverse-IP `domain` neighbors
- **Empty/negative result looks like:** a bare record with location but no owner/WHOIS detail (privacy-protected or thinly indexed), or "no data" for very new/obscure IPs. IP geolocation resolves to the ISP's routing point, not a street address — never treat the city as the person's home.

## Gotchas & OpSec
- Geolocation is provider-level: it reflects where the ISP routes the IP, often a data-center or regional hub, not the user's residence.
- The richest exports (bulk reverse-IP, historical data, API) are behind the paywall; the free page still gives the core lookup.
- OpSec: **passive** — you query MyIP.ms's dataset, not the target's server.

## Overlaps ("do both")
- Pairs with `[[yougetsignal-com]]` for reverse-IP cross-checking and with any dedicated WHOIS tool — MyIP.ms bundles geolocation + hosting + neighbors in one view, but confirm ownership claims against a primary WHOIS source.

## Trust & verifiability
`trust: community` — a large, commercially maintained IP database. Coverage is broad and generally reliable, but individual records can be stale and geolocation is approximate, so corroborate location and ownership before acting on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myip-ip-address |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
