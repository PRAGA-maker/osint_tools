---
id: ip2geo-dev
name: ip2geo.dev
description: Use when you have an `ip-address` and want programmatic geolocation — returns country/city `geolocation`, ISP and ASN via a REST API or SDK.
url: https://ip2geo.dev
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Scripting IPv4/IPv6 → country/city/ISP/ASN lookups from your own code.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
- employer-org
status: live
pricing: freemium
costNote: Free tier of 1,000 conversions/month with a signed-up API key; paid plans lift the quota.
opsec: passive
opsecNote: Passive — you send the target `ip-address` to ip2geo.dev's API, never to the target. The provider logs your queries against your API key; use a puppet account if attribution matters.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: unverified
trustNote: Commercial developer API; no independent audit of its geolocation database accuracy, and provenance of the underlying data is not disclosed.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- ip2geo
- ip2geo.dev API
tags:
- domain-and-ip-research
- ip-geolocation
- api
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# ip2geo.dev

> A developer-focused IP-geolocation API — turn any IPv4/IPv6 address into country, city, ISP, ASN and timezone via REST or typed SDKs.

## When to use
You need to geolocate `ip-address`es at scale or inside a pipeline (enriching log exports, header IPs, or a batch of addresses) rather than one-off in a browser. ip2geo.dev is built for that: an API key, SDKs, and a dashboard with usage analytics.

## How to use it (`bestInteractionPattern`: api)
1. Sign up at https://ip2geo.dev for the free plan and obtain an API key.
2. Call the REST endpoint (or install a language SDK) with the target `ip-address`.
3. Parse the JSON: country, city, ISP, ASN, timezone.
4. Watch your quota (1,000/mo free) in the dashboard; batch or cache to stay under it.
5. Pivot: feed the ASN/ISP into WHOIS/passive-DNS tooling and the city-level `geolocation` into your map/notes — never treat it as a precise address.

## Inputs → Outputs
- **In:** `ip-address` (IPv4 or IPv6)
- **Out:** `geolocation` (country/city/timezone), ISP + ASN (`employer-org`)
- **Empty/negative result looks like:** private/reserved ranges and some IPv6 blocks return null or country-only data; a city result is an ISP-routing estimate, not the user's location.

## Gotchas & OpSec
- Requires registration + API key even for the free tier.
- IP geolocation is inherently coarse: it locates the ISP/allocation, not the person — VPNs, mobile carriers and CGNAT routinely mislocate.
- Free quota is small (1k/mo); design for caching.
- Accuracy and data source are undisclosed — corroborate against a second provider (e.g. a local `checkip` run) before relying on a result.

## Overlaps ("do both")
- Pairs with [[checkip]] and other IP-reputation/geolocation services — ip2geo.dev is the clean API for bulk geolocation, while checkip adds reverse-DNS and threat-reputation in one CLI; cross-check their geolocation for confidence.

## Trust & verifiability
`trust: unverified` — a commercial API with no public audit of its geolocation database; useful for leads, but verify critical locations against an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip2geo-dev |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → geolocation, employer-org |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
