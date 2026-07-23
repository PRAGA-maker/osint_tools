---
id: whois-arin-online
name: Whois ARIN Online
description: Use when you have an `ip-address` (or ASN) in North America and want to know which organization owns that network block — returns the registered org `name`, `address` and abuse/technical contacts.
url: https://whois.arin.net
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Resolving a North American IP/network block to its registered owning organization and contact/address.
selectorsIn:
- ip-address
selectorsOut:
- employer-org
- address
- email
status: live
pricing: free
costNote: Free official ARIN Whois-RWS lookup; no account.
opsec: passive
opsecNote: You query ARIN's registry, not the target host, so the IP's user sees nothing. Standard registry logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by ARIN, the Regional Internet Registry for North America; the network-ownership and allocation data is authoritative registry record.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- account-arin-net
- arin
- arin-net
- search-arin-net
- whois-arin
aliases:
- ARIN Whois
- whois.arin.net
tags:
- domain-and-ip-research
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Whois ARIN Online

> ARIN's authoritative Whois for North America: turn an `ip-address` or ASN into the organization that owns that network block, with its registered address and abuse/technical contacts.

## When to use
You have an `ip-address` (from a log, an email header, a connection, a passive-DNS hit) that geolocates to North America and you need to know who actually owns the network it belongs to — the hosting provider, ISP, or the end-organization that holds the allocation. ARIN gives the registered owner org, the allocation range, and the abuse/tech contact addresses, which are the starting point for attribution and for filing abuse reports.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://whois.arin.net and enter the `ip-address`, CIDR block, ASN, or org handle.
2. Read the record: the network name and range, the registered organization (`name`), its mailing `address`, and POC (point-of-contact) `email`s for abuse/technical roles.
3. If the block is a downstream reassignment, follow the "parent"/"customer" references to distinguish the hosting provider from the end-org.
4. Pivot: the owning org feeds corporate-registry lookups; the abuse contact feeds a report; for IPs outside ARIN's region, follow the referral to RIPE/APNIC/LACNIC/AFRINIC.

## Inputs → Outputs
- **In:** `ip-address` / CIDR / ASN / org handle
- **Out:** owning organization `name`, registered `address`, abuse/tech contact `email`s, allocation range
- **Empty/negative result looks like:** a referral to another RIR ("this IP is managed by RIPE/APNIC…") — meaning the IP isn't in ARIN's region; follow the referral. A sparse record can mean a large provider that hasn't reassigned the sub-block to the end customer.

## Gotchas & OpSec
- ARIN only covers North America; IPs elsewhere resolve at RIPE/APNIC/LACNIC/AFRINIC — follow the referral rather than assuming no data.
- The registered org is often the hosting provider, not the site operator — a reassignment/customer record (if present) is what points to the actual tenant.
- OpSec: passive — you query the registry, never the host.

## Overlaps ("do both")
- Pairs with the other RIRs' Whois and with reverse-DNS/passive-DNS tools like `[[mnemonic]]` — ARIN names the network owner, while passive-DNS ties specific domains to the IP over time.

## Trust & verifiability
`trust: trusted` — ARIN is the official Regional Internet Registry for North America; allocation and ownership data is authoritative, with the standard caveat that the listed org may be an upstream provider rather than the end user.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whois-arin-online |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → employer-org, address, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
