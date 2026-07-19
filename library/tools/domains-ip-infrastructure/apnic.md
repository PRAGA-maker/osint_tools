---
id: apnic
name: APNIC
description: Use when you have an `ip-address` in the Asia-Pacific region and want to know who holds the block — returns the registered network operator, allocation details, and abuse/admin contacts.
url: https://www.apnic.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: WHOIS lookups on Asia-Pacific IP addresses/ranges to identify the operator and abuse contact behind an IP.
selectorsIn:
- ip-address
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free public WHOIS/registry service. No account needed for lookups; bulk/API access has fair-use limits.
opsec: passive
opsecNote: You query APNIC's registry database, not the target host — the subject's IP is never contacted, so nothing is disclosed to them. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: APNIC is one of the five Regional Internet Registries — the authoritative source of record for IP allocation across the Asia-Pacific.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Asia Pacific Network Information Centre
- apnic.net
- APNIC WHOIS
tags:
- domainsandips
- Domains & IPs
- whois
- rir
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# APNIC

> The Regional Internet Registry for the Asia-Pacific — authoritative WHOIS for who owns an IP block in that region.

## When to use
You have an `ip-address` (from an email header, a login/connection log, a website, a message's metadata) that geolocates to the Asia-Pacific, and you need to know which organisation holds it and how to reach its abuse/admin contact. APNIC's WHOIS turns a raw IP into a named network operator (ISP, hosting company, enterprise) and the allocation's registered details — the starting point for attributing where a connection came from.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.apnic.net/ and open the WHOIS search (or query `whois -h whois.apnic.net <ip>` from a terminal).
2. Enter the `ip-address` (or a range/AS number).
3. Read the record: the `inetnum`/`netname` (block and operator), the holding organisation and country, and the `abuse-c`/admin contacts.
4. If the IP is outside APNIC's region, the record will point you to the correct RIR (ARIN, RIPE, LACNIC, AFRINIC) — follow that referral.
5. Pivot: the operator/hosting org can be served or contacted; the AS/range feeds infrastructure mapping; a residential ISP narrows a coarse geolocation.

## Inputs → Outputs
- **In:** `ip-address` (or IP range / AS number)
- **Out:** registered network operator (`employer-org`), allocation country/details, abuse & admin contacts (`address`/email)
- **Empty/negative result looks like:** "no entries found" or a referral to another RIR means the IP isn't APNIC-managed — query the RIR the record points to instead of assuming the IP is unregistered.

## Gotchas & OpSec
- Human-in-the-loop: none; heavy automated querying is rate-limited (fair use).
- WHOIS names the *block holder* (often an ISP/host), not the end user — a residential ISP won't reveal the subscriber without legal process.
- Records can be out of date or list a downstream reseller; corroborate with routing/AS data before asserting attribution.

## Overlaps ("do both")
- Pairs with `[[ripe-stat]]` / ARIN / other RIR WHOIS and with IP-geolocation tools — APNIC is authoritative for the Asia-Pacific block holder; a geolocation service estimates the physical area, and the two together bound "who and where."

## Trust & verifiability
`trust: trusted` — APNIC is the official Regional Internet Registry for the Asia-Pacific; its allocation records are the source of record, so the operator attribution is authoritative (subscriber-level identity is not).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apnic |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
