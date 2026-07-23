---
id: whois-arin
name: Whois ARIN
description: Use when you have an ip-address or ASN in North America and want its registered owner and contacts — returns employer-org, address, and point-of-contact email/phone from the RIR registry.
url: https://whois.arin.net/ui/advanced.jsp
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: Authoritative ownership and contact lookup for North American IP ranges and ASNs.
selectorsIn:
- ip-address
selectorsOut:
- employer-org
- address
- email
- phone
status: live
pricing: free
costNote: Free public registry; no account. A free API key unlocks the REST/RWS interface for bulk queries.
opsec: passive
opsecNote: Queries ARIN's own registry database; the target network is not contacted and no active scanning occurs — fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: ARIN is the official Regional Internet Registry for North America; its WHOIS is the authoritative source for allocations in its region.
missingPersonsRelevance: low
coverage:
- us
- ca
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- arin
- account-arin-net
- whois-arin-online
aliases:
- ARIN Whois
- ARIN Whois-RWS
tags:
- whois
- ip-registry
- asn
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Whois ARIN

> The authoritative WHOIS for North American IP space — turn an IP or ASN into its registered organization, address, and points of contact.

## When to use
You have an `ip-address` or ASN (from a log, an email header, [[wireshark]], or another tool) that geolocates to North America and want the authoritative registrant: which `employer-org` holds the block, its registered `address`, and the technical/abuse point-of-contact `email`/`phone`. For IPs outside North America, use the sibling RIR (RIPE, APNIC, LACNIC, AFRINIC). It attributes infrastructure ownership, not individual people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://whois.arin.net and enter the `ip-address`, CIDR block, ASN, or org name (the advanced page allows field-specific search).
2. Read the record: the **Organization** (name + `address`), the parent allocation, and the **Points of Contact** (abuse/tech/admin with `email` and often `phone`).
3. Follow the org handle to see all networks/ASNs registered to that entity — useful for mapping an organization's footprint.
4. For automation, register a free API key and use ARIN's Whois-RWS REST endpoints.
5. Pivot: an org's abuse `email` → email-OSINT; a downstream customer name in the comments → company registry lookup.

## Inputs → Outputs
- **In:** an `ip-address`, CIDR, ASN, or organization name/handle.
- **Out:** registrant `employer-org`, registered `address`, and POC `email`/`phone`; parent allocation and related networks.
- **Empty/negative result looks like:** "no valid records" (the IP is not in ARIN's region — try RIPE/APNIC/etc.), or a record that resolves only to an upstream ISP with no downstream customer detail.

## Gotchas & OpSec
- ARIN only covers North America; querying a non-NA IP here yields nothing — pick the right RIR.
- Many IPs return only the upstream provider, not the actual end-user org (SWIP/reassignment may be absent).
- Points of contact are the registrant's admins, not the person using a given address at a moment in time.

## Overlaps ("do both")
- Pairs with [[ipvoid]] and [[netcraft]]: ARIN gives authoritative ownership/contacts, those add reputation and hosting-history context.

## Trust & verifiability
`trust: trusted` — ARIN is the official registry of record; the allocation data is authoritative and directly citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whois-arin |
