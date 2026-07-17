---
id: ripe
name: RIPE NCC Database
description: Use when you have an `ip-address` or netblock in Europe/Middle East/Central Asia and want its registered holder — returns the organisation, `address`, and abuse/admin contacts for that IP range.
url: https://apps.db.ripe.net/db-web-ui/query
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: WHOIS lookup of who is allocated an IP address or network block in the RIPE region (Europe, Middle East, Central Asia).
selectorsIn:
- ip-address
- domain
selectorsOut:
- employer-org
- address
- email
status: live
pricing: free
costNote: Free public WHOIS database run by the RIPE NCC; no account needed to query. An account is only required to register/maintain your own objects.
opsec: passive
opsecNote: Querying the RIPE database hits RIPE's servers, not the target's network, so the subject is not alerted. RIPE applies anti-abuse query rate limits per IP; heavy automated querying may get you throttled. Personal data in objects is minimised under GDPR.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: One of the five authoritative Regional Internet Registries; allocation data is the system of record for who holds an IP range in its region.
missingPersonsRelevance: medium
coverage:
- eu
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- arin
- whois-arin
- ipinfo-io
aliases:
- RIPE NCC
- RIPE Database
- ripe.net whois
tags:
- domainsandips
- whois
- rir
- ip-allocation
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# RIPE NCC Database

> The authoritative registry for who holds IP address space across Europe, the Middle East and Central Asia — the RIR-level WHOIS behind any EMEA IP.

## When to use
You have an `ip-address` (or ASN/netblock) that geolocates to Europe, the Middle East, or Central Asia and you want to know the registered holder — the ISP, hosting company, or organisation allocated that range — plus its abuse/admin contact. Use it to attribute infrastructure (which provider hosts a site or sent an email), to find the org and `address` behind a netblock, and to identify the right abuse contact. It resolves *infrastructure* ownership, not individual end-users.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the RIPE Database query at https://apps.db.ripe.net/db-web-ui/query (or use `whois -h whois.ripe.net <IP>` on the CLI).
2. Enter the `ip-address`, netblock, ASN, or org handle.
3. Read the returned objects: `inetnum`/`inet6num` (the allocation and its holder), `organisation` (org name + `address`), and `role`/`person` objects for admin-c/abuse-c contacts.
4. Confirm the region: if RIPE says the range is administered by another RIR, follow the pointer (ARIN for North America, APNIC for Asia-Pacific, etc.).
5. Pivot: the holder org and abuse `email` feed corporate-records and email tools; the netblock scopes further reverse-DNS and hosting-neighbor lookups.

## Inputs → Outputs
- **In:** `ip-address` (or ASN/netblock/org handle) in the RIPE region
- **Out:** `employer-org` (holding organisation), `address`, admin/abuse `email` contacts
- **Empty/negative result looks like:** "no entries found" or a referral to another RIR means the IP isn't administered by RIPE — re-query the correct registry rather than concluding there's no record.

## Gotchas & OpSec
- Region-scoped: only EMEA/Central Asia ranges live here; North American IPs are in ARIN, Asia-Pacific in APNIC, etc.
- Personal details are heavily minimised for GDPR; expect an organisation and role contacts, rarely a named individual.
- OpSec: passive, but respect RIPE's per-source query rate limits to avoid throttling; use the API with care for bulk work.

## Overlaps ("do both")
- Pairs with `[[arin]]` / `[[whois-arin]]` (the North American RIR) — always query the RIR that actually administers the range. Combine with `[[ipinfo-io]]` for a quick geolocation/ASN sanity check before diving into the raw RIPE objects.

## Trust & verifiability
`trust: trusted` — the RIPE NCC is an authoritative Regional Internet Registry; its allocation records are the definitive source for IP-range holdership in its region.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ripe |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → employer-org, address, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
