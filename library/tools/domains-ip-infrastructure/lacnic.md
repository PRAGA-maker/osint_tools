---
id: lacnic
name: LACNIC
description: Use when you have an `ip-address` or `domain` in Latin America/Caribbean and want the allocation record — returns the holder org, contacts and `address`/country.
url: https://query.milacnic.lacnic.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: WHOIS-style lookups for IP ranges and ASNs registered in Latin America and the Caribbean — the authoritative RIR for that region.
selectorsIn:
- ip-address
- domain
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free public RIR WHOIS; no account. Rate limits apply to heavy automated querying.
opsec: passive
opsecNote: Querying the registry is passive and does not touch the target host; only LACNIC sees the lookup. Safe. (Resolving a domain to an IP first is also passive if you use public DNS.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: LACNIC is the official Regional Internet Registry for Latin America and the Caribbean; allocation records are authoritative for who holds an IP block/ASN in the region.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- LACNIC WHOIS
- lacnic.net
- milacnic
tags:
- domainsandips
- Domains & IPs
- rir-whois
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# LACNIC

> The Regional Internet Registry for Latin America and the Caribbean — authoritative WHOIS for IP allocations and ASNs in that region.

## When to use
You have an `ip-address` (or a `domain` you can resolve to one) that geolocates to Latin America or the Caribbean, and you want the authoritative allocation record: which organisation holds the block, its registered country/`address`, abuse and admin contacts, and the ASN. Use it to attribute infrastructure — a host, a mail server, a site — to a real regional entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. If you only have a `domain`, resolve it to an IP first (public DNS).
2. Open LACNIC's WHOIS query at https://query.milacnic.lacnic.net/ and enter the IP or ASN.
3. Read the record: the holder `employer-org`, country/`address`, allocation dates, and contact objects (abuse/admin/tech).
4. Pivot: take the org and contacts into corporate registries and reverse-WHOIS; if the block is sub-allocated, note the downstream ISP/customer; use the ASN to map the org's other ranges.

## Inputs → Outputs
- **In:** `ip-address` or ASN (or a resolved `domain`)
- **Out:** holder `employer-org`, registered country/`address`, contacts, ASN
- **Empty/negative result looks like:** "not found" / referral — the IP isn't in LACNIC's region; the other RIRs (ARIN, RIPE, APNIC, AFRINIC) manage other regions, so follow the referral to the right registry.

## Gotchas & OpSec
- **Region-scoped:** LACNIC only covers Latin America/Caribbean. For a non-regional IP you'll be referred elsewhere — use the matching RIR.
- Contacts are often role/abuse addresses for an ISP, not the end user of the IP; treat as the network operator, not necessarily your subject.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with the other RIR WHOIS services (ARIN/RIPE/APNIC/AFRINIC) and with IP-geolocation/Shodan — the RIR gives authoritative ownership, the others add geolocation and what's running.

## Trust & verifiability
`trust: trusted` — an official RIR; allocation data is authoritative. Remember it identifies the network *holder*, which for shared/ISP ranges is not the individual end-user — corroborate before attributing to a person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lacnic |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
