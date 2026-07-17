---
id: arin
name: ARIN
description: Use when you have an `ip-address` or ASN and want the North American registrant org, address and abuse contacts — returns `employer-org`, `address`, `email`, `phone`.
url: https://www.arin.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Resolving who an IPv4/IPv6 block or ASN in North America is registered to.
selectorsIn:
- ip-address
- employer-org
selectorsOut:
- employer-org
- address
- email
- phone
- name
status: live
pricing: free
costNote: Free public registry lookups via Whois-RWS and RDAP; no account needed. Bulk Whois access requires a signed AUP.
opsec: passive
opsecNote: A Whois/RDAP query hits ARIN's public registry, not the target's own infrastructure, so it does not touch or alert the subject. Rate limits apply per source IP; heavy automated querying can get you throttled.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: ARIN is the authoritative Regional Internet Registry for North America; registration records are first-party and definitive for allocation ownership.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- account-arin-net
- arin-net
- search-arin-net
- whois-arin
- whois-arin-online
aliases:
- American Registry for Internet Numbers
- ARIN Whois-RWS
- ARIN RDAP
tags:
- domainsandips
- Domains & IPs
- whois
- ip-address
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# ARIN

> The authoritative registry for North American IP address and ASN allocations — the ground truth for "who owns this IP block?"

## When to use
You have an `ip-address` (or an ASN, or a network operator's org name) that geolocates to or is allocated within North America, and you need the registrant organization, its mailing address, and abuse/technical contact details. This is the definitive source when a lower-tier tool gives you a hosting provider but you want the underlying registrant of record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.arin.net/ and use the Whois-RWS search box, or hit the RDAP/Whois-RWS endpoints directly (e.g. `https://whois.arin.net/rest/ip/8.8.8.8` or `https://rdap.arin.net/registry/ip/8.8.8.8`).
2. Enter the `ip-address`, ASN (e.g. `AS15169`), or organization name.
3. Read the record: registrant `employer-org` (OrgName), postal `address`, abuse and technical POC `email`/`phone`, and the allocation range/parent block.
4. If the IP is registered outside North America, ARIN returns a referral to the correct RIR (RIPE for Europe/ME, APNIC for Asia-Pacific, LACNIC for Latin America, AFRINIC for Africa) — follow the referral there.
5. Pivot: the OrgName and POC email/domain feed WHOIS-on-the-registrant, and the abuse contact tells you who to escalate to.

## Inputs → Outputs
- **In:** `ip-address`, ASN, or `employer-org` name
- **Out:** `employer-org` (registrant), `address`, abuse/tech `email` and `phone`, allocation range, POC handles
- **Empty/negative result looks like:** "no records found" for private/reserved ranges, or a referral pointing you to another RIR when the block is not ARIN-administered — that referral is the answer, not a dead end.

## Gotchas & OpSec
- Human-in-the-loop: none for standard lookups. Bulk Whois or Reg-RWS automation requires agreeing to ARIN's AUP.
- OpSec: **passive** — you query ARIN, not the subject; no alert reaches the target. Aggressive automated querying is rate-limited by source IP.
- Registrant is the org that holds the allocation, which for cloud/hosting IPs is the provider (AWS, Cloudflare), not the end user — combine with the provider's own abuse process to reach the actual customer.

## Overlaps ("do both")
- Pairs with `[[whois-arin]]` and `[[search-arin-net]]` — same registry, different front ends; use whichever exposes the field you need.
- Do the equivalent RIR lookup elsewhere when ARIN referrals you (RIPE/APNIC/LACNIC/AFRINIC) for non-North-American blocks.

## Trust & verifiability
`trust: trusted` — ARIN is the RIR that actually issues these allocations, so its records are the primary source, not a scraped copy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arin |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
