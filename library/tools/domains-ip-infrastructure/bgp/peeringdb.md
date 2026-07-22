---
id: peeringdb
name: PeeringDB
description: Use when you have an ASN, network/org name or `ip-address` and want the operator behind it — org, facilities, IX presence and NOC contacts — returns `employer-org`, `ip-address` ranges and facility `address`.
url: https://www.peeringdb.com/advanced_search
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- bgp
bestFor: Mapping the organisation, physical facilities and peering contacts behind an autonomous system or network.
selectorsIn:
- ip-address
- domain
selectorsOut:
- employer-org
- ip-address
- address
status: live
pricing: free
costNote: Free public registry; a free account unlocks a few extra filter fields and contact visibility.
opsec: passive
opsecNote: Reads a public infrastructure registry — no contact with the target network. Only your connection to PeeringDB is exposed; a login is attributable, so use a research account if you want extra fields anonymously.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Community-maintained, industry-standard peering registry (since 2004); entries are self-published by network operators, so treat operator-supplied detail as authoritative-but-self-declared.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- PeeringDB
tags:
- bgp
- asn
- network-infrastructure
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# PeeringDB

> The industry-standard registry of networks, ASNs, exchanges and data centres — used in OSINT to attribute an IP/ASN to the operator behind it and to its physical facilities and contacts.

## When to use
You have an `ip-address`, ASN, network name or hosting `domain` and want to know who runs it: the operating organisation (`employer-org`), which internet exchanges and data centres (`address`) it's present in, its advertised IP ranges, peering policy, and NOC/peering contact details. A strong step in de-anonymising hosting/infrastructure and understanding an organisation's footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.peeringdb.com/advanced_search.
2. Search by ASN, organisation name, IX or facility (map an IP to its ASN first via a BGP/whois lookup).
3. Read the network record: operating org (`employer-org`), IRR/prefix info (`ip-address` ranges), IX and facility presence with locations (`address`), traffic level, peering policy and NOC contacts.
4. Pivot: take facility `address`es and contacts into further OSINT; use IX presence to understand connectivity and geography.

## Inputs → Outputs
- **In:** ASN / organisation name / IX / `ip-address` (resolve to ASN first) / hosting `domain`
- **Out:** `employer-org`, `ip-address` prefixes, facility/IX `address`es, peering contacts, policy
- **Empty/negative result looks like:** no record — many end-user networks and small hosts aren't in PeeringDB (it's biased toward networks that peer); absence isn't proof the ASN doesn't exist.

## Gotchas & OpSec
- Entries are self-maintained by operators, so they can be stale or incomplete — cross-check prefixes against RIR whois/BGP data.
- PeeringDB skews toward transit/peering networks; residential/enterprise ASNs are often absent.
- OpSec: passive; a logged-in session is attributable.

## Overlaps ("do both")
- Pairs with RIR whois (RIPE/ARIN) and BGP tools (bgp.he.net): resolve IP→ASN there, then PeeringDB adds the operator, facilities and human contacts.

## Trust & verifiability
`trust: trusted` — the de-facto community registry for interconnection data; authoritative for what operators publish, but verify prefixes/ownership against RIR records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peeringdb |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → employer-org, ip-address, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
