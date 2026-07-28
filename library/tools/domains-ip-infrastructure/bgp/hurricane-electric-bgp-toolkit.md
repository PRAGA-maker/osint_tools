---
id: hurricane-electric-bgp-toolkit
name: Hurricane Electric BGP Toolkit
description: Use when you have an `ip-address`, `domain` or ASN and want its routing, network owner, DNS and neighbouring infrastructure — returns ip-address, domain, employer-org.
url: https://bgp.he.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- bgp
bestFor: Mapping who owns/routes an IP or ASN and what other prefixes, DNS and hosts sit alongside it.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
- employer-org
status: live
pricing: free
costNote: Free, no account needed; Hurricane Electric provides it as a public service.
opsec: passive
opsecNote: Fully passive — it queries public BGP/RIR/DNS data, never the target's own servers. Nothing you look up reaches the subject. Safe without a sock puppet, though VPN hygiene is always fine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Hurricane Electric, a major global backbone/transit provider; the BGP and RIR data it surfaces is authoritative public routing information.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- hurricane-electric-internet-services
aliases:
- bgp.he.net
- HE BGP Toolkit
tags:
- bgp
- asn
- network-recon
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Hurricane Electric BGP Toolkit

> The go-to free lookup for internet infrastructure: point it at an IP, domain or ASN and see who owns and routes it, and what else lives on that network.

## When to use
You have an `ip-address`, `domain` or ASN tied to a target (a server hosting a site, an email header IP, a company's netblock) and you want to understand the infrastructure around it: which organisation owns/announces it, what prefixes and other IPs it controls, its DNS records, and its peering. This is the pivot from a single IP/domain to the wider network it belongs to — useful for attributing hosting, finding sibling servers, or mapping an organisation's online footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bgp.he.net/ and enter an `ip-address`, `domain`, ASN (e.g. `AS13335`) or company name.
2. For an IP/prefix: read the announcing ASN, the owning `employer-org`, and the surrounding netblock.
3. For an ASN: browse its announced prefixes, IPv4/IPv6 space, peers/upstreams, and originated routes.
4. For a domain: check the DNS tab for A/MX/NS records that expose more `ip-address`/`domain` pivots.
5. Pivot: an owning org → its other prefixes → other hosted domains; feed resolved IPs into geolocation/hosting tools.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, ASN, or org name
- **Out:** owning/announcing `employer-org`, related `ip-address` prefixes and `domain` DNS records, peering/routing
- **Empty/negative result looks like:** "no results" for a bogon/unrouted IP or an unregistered domain — the address isn't publicly announced or the name isn't in DNS/RIR data.

## Gotchas & OpSec
- OpSec: passive; queries public routing/RIR/DNS data, never the target — nothing leaks to the subject.
- Ownership is at the network/ASN level: the org that *routes* an IP (a hosting provider) is often not the org that *uses* it. Distinguish hosting from tenant.
- Data reflects public BGP/RIR/DNS state; very recent changes may lag.

## Overlaps ("do both")
- Do both with WHOIS/passive-DNS and geolocation tools — HE gives the routing/ownership backbone; WHOIS gives registrant detail and passive DNS gives historical resolution, together attributing infrastructure precisely.

## Trust & verifiability
`trust: trusted` — first-party public routing data from a major backbone provider; authoritative for BGP/ASN questions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hurricane-electric-bgp-toolkit |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
