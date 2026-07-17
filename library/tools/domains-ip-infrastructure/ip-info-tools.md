---
id: ip-info-tools
name: IP Info Tools (ipinfo.info)
description: Use when you have an `ip-address` or `domain` and want a bundle of free network checks (geolocation, WHOIS, blacklist, email-header trace) — returns `geolocation`, `domain`, ISP leads.
url: https://ipinfo.info/index.php
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A grab-bag of free IP/domain utilities in one place — IP location, WHOIS, reverse lookup, blacklist check, and email-header analysis.
selectorsIn:
- ip-address
- domain
selectorsOut:
- geolocation
- domain
status: live
pricing: free
costNote: Free web tools; no account. Ad-supported.
opsec: passive
opsecNote: The utilities query databases about an IP/domain — they don't contact the target (except tools you explicitly point at a host). Reading WHOIS/geolocation is passive; avoid any "ping"/"traceroute" utility if you need to stay non-contacting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An older ad-supported tools portal aggregating third-party data; convenient but not authoritative — verify anything important against a primary source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ipinfo.info
- IP Info Tools
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# IP Info Tools (ipinfo.info)

> A one-stop portal of free IP/domain utilities — geolocation, WHOIS, reverse DNS, blacklist checks, and email-header tracing — handy for a quick multi-angle read on an address.

## When to use
You have an `ip-address` or `domain` and want several quick checks without hopping between sites: where the IP geolocates, who owns it (WHOIS), what hostnames it resolves to, whether it's on spam blacklists, and — via the email-header tool — the origin IP of a message. Good for a fast first-pass characterisation of infrastructure or a suspicious email before deeper work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ipinfo.info/ and pick a utility (IP location, WHOIS, reverse lookup, blacklist check, email-header analyzer).
2. Enter the IP/domain (or paste raw email headers into the header tool).
3. Read the output — geolocation, registrant/ISP, resolved hosts, or the extracted originating IP from headers.
4. Pivot: an origin IP from an email feeds geolocation/WHOIS; an ISP feeds abuse-contact work; a blacklist hit flags a malicious host.

## Inputs → Outputs
- **In:** `ip-address` or `domain` (or raw email headers)
- **Out:** `geolocation`, WHOIS/ISP details, resolved `domain`/hostnames, and blacklist status.
- **Empty/negative result looks like:** a stale or thin WHOIS/geolocation answer (the site aggregates older data sources) — corroborate on a primary/registrar source before relying on it.

## Gotchas & OpSec
- It's an ageing aggregator — data can lag; treat results as a convenient first look, not authoritative, and confirm key facts against the registrar/RIR and a current geolocation provider.
- Ad-heavy interface; avoid mistaken clicks.
- OpSec: passive for lookup tools; steer clear of any active "ping/traceroute" utility if non-contact matters.

## Overlaps ("do both")
- Complements `[[ip2location-free-ip-location-search]]` and dedicated WHOIS tools — use ipinfo.info for a fast bundle, then confirm the specifics on authoritative single-purpose sources.

## Trust & verifiability
`trust: community` — a third-party aggregator; useful and free, but verify important geolocation/WHOIS/header findings against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip-info-tools |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → geolocation, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
