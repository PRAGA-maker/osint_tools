---
id: ip-investigation-toolbox
name: Ip Investigation Toolbox
description: Use when you have an `ip-address` and want many lookups at once — returns `geolocation`, routing, open ports, and threat/host data from 15 services in one click.
url: https://cipher387.github.io/domain_investigation_toolbox/ip.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fanning a single IP address out to ~15 lookup services (geolocation, BGP, Shodan/Censys, threat intel) from one page.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- geolocation
- domain
status: live
pricing: free
costNote: Free static page (GitHub Pages) that opens each of ~15 third-party tools pre-filled with your IP; those tools are free for interactive use (a few, e.g. Shodan/Censys, gate deeper detail behind accounts).
opsec: passive
opsecNote: The page just builds links — most (geolocation, BGP, WHOIS, threat-intel lookups) query third-party databases and don't touch the IP's owner. Active scanners it links (Shodan/Censys show cached scans; check-host.net can probe live) may generate a request to the host. Prefer the database lookups; be aware which links do live checks.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by cipher387 (Cyber Detective), a well-known OSINT author; it's a launcher for reputable third-party services, so trust each destination on its own merits.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- central-ops
- ghost-eye
- website-information
aliases:
- IP Investigation Toolbox
- cipher387 ip toolbox
tags:
- domain/ip/links
- ip-lookup
- toolbox
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Ip Investigation Toolbox

> A one-page launcher by cipher387: paste an IP once and it opens ~15 lookup services (geolocation, BGP/routing, Shodan, Censys, threat-intel, host checks) each pre-filled — turning a batch of manual lookups into a single step.

## When to use
You have an `ip-address` from a lead — an email header, a server log, a suspicious link's host, a chat connection — and want the full picture fast: where it geolocates, which network/ASN owns it, what ports/services it exposes, and whether it appears in threat-intel. Instead of visiting fifteen sites by hand, this fans the IP out to all of them. Infrastructure-oriented, so direct missing-person value is low, but origin and hosting details help corroborate where a message or account came from.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cipher387.github.io/domain_investigation_toolbox/ip.html.
2. Enter the `ip-address` once in the input box.
3. Click through the generated links — geolocation (iplocation.net, ip2location), routing (bgp.he.net, bgp.tools), scans (Shodan, Censys), threat intel, and host checks — each opens pre-filled for that IP.
4. Read across the services: consistent `geolocation`/ASN, exposed services, any blacklist/threat hits.
5. Pivot: hosting/ASN and reverse-DNS `domain`s feed further domain recon; a residential vs datacenter/VPN classification informs how much weight to give the location.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** `geolocation` (approximate location), `ip-address` routing/ASN and open services, reverse-DNS `domain`s, threat-intel flags
- **Empty/negative result looks like:** an IP that geolocates to a datacenter/VPN with no reverse DNS and no scan data — meaning it's likely proxied, so the "location" isn't the person's.

## Gotchas & OpSec
- It's a link launcher: some destination services rot, rate-limit, or now require accounts (Shodan/Censys for depth); the underlying tool is the source of truth.
- IP `geolocation` is coarse and easily masked by VPN/proxy — never treat it as the subject's real location without corroboration.
- Mostly passive, but note the couple of links that can do a live host check before firing them at a sensitive target.

## Overlaps ("do both")
- Overlaps `[[central-ops]]` and `[[website-information]]` for the WHOIS/DNS side and `[[ghost-eye]]` for local scanning; use this as the fast IP-triage front end.

## Trust & verifiability
`trust: community` — a reputable author's convenience launcher; data quality is that of whichever third-party service you open, all of which expose verifiable public records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip-investigation-toolbox |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address, geolocation, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
