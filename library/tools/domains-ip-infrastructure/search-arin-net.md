---
id: search-arin-net
name: search.arin.net
description: Use when you have an `ip-address` or network in the Americas and want its official registration — returns the org, contacts, address, and netblock range from ARIN's authoritative RDAP/Whois.
url: https://search.arin.net/rdap/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Authoritative Whois/RDAP lookup of who an IP or network block in the Americas is registered to.
selectorsIn:
- ip-address
selectorsOut:
- employer-org
- address
- email
status: live
pricing: free
costNote: Free public registry service run by ARIN; no account needed for lookups.
opsec: passive
opsecNote: You query ARIN's registry database, not the IP's host, so the target is not contacted. ARIN logs queries and rate-limits heavy use. Fully passive for the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: ARIN is the official Regional Internet Registry for North America; its records are the authoritative registration source for IPs/ASNs in its region.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- arin
- whois-arin
aliases:
- ARIN Whois
- ARIN RDAP
- search.arin.net
tags:
- domainsandips
- Domains & IPs
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# search.arin.net

> ARIN's official Whois/RDAP search — the authoritative "who owns this IP/network" lookup for the Americas region.

## When to use
You have an `ip-address`, ASN, or network block and need to know who it's registered to. ARIN returns the registered organization, its postal `address`, abuse/technical `email` contacts, and the netblock range — establishing which ISP, hosting provider, company, or institution controls an address. This anchors an IP to a real-world entity, a key step when an IP appears in logs, headers, or metadata and you need to attribute or geolocate it (at the organizational level).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://search.arin.net/rdap/ and enter the `ip-address`, CIDR block, ASN, or org handle.
2. Read the record: registered organization/customer, address, registration and update dates, and point-of-contact emails/phones.
3. Note the parent netblock — a small allocation often rolls up to an ISP/hosting parent that identifies the real provider.
4. If the record says the range is administered by another registry (RIPE, APNIC, LACNIC, AfriNIC), follow the referral there — ARIN only authoritatively covers North America.
5. Pivot: the org → company records; abuse contacts (`email`) → email tools; the provider → understand whether the IP is residential, hosting, or corporate.

## Inputs → Outputs
- **In:** `ip-address`, CIDR, ASN, or org handle
- **Out:** registered `employer-org`/customer, `address`, contact `email`s, netblock range and dates
- **Empty/negative result looks like:** "no results" or a referral to another RIR — the address isn't ARIN-administered (it belongs to RIPE/APNIC/etc.); follow the referral. A record may also list only the ISP, not the end user (normal for residential IPs).

## Gotchas & OpSec
- **Region-bound:** ARIN is authoritative only for North America; for other regions use the RIR it refers you to.
- Residential/dynamic IPs resolve to the ISP, not the individual — ARIN gives you the provider, not the person; the subscriber requires legal process.
- OpSec: **passive** — a registry query; the IP's owner is not contacted.

## Overlaps ("do both")
- Pairs with [[whois-arin]] and the other RIRs' Whois/RDAP — same data model, different regions; and with IP-geolocation tools that estimate physical location where ARIN gives only registration.

## Trust & verifiability
`trust: trusted` — ARIN is the official Regional Internet Registry; its registration data is the authoritative record for IPs and networks in the Americas.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-arin-net |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → employer-org, address, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
