---
id: afrinic
name: AFRINIC
description: Use when you have an `ip-address` or `domain` allocated in Africa and want the registered network holder, allocation, and abuse contacts — returns WHOIS org/`address`/`associate` contact records for African IP space.
url: https://www.afrinic.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: WHOIS lookups for African IP address ranges and ASNs — who holds a network and their registered/abuse contacts.
selectorsIn:
- ip-address
- domain
selectorsOut:
- employer-org
- address
- associate
- email
status: live
pricing: free
costNote: Free public WHOIS/registry lookups; no account needed. AFRINIC is the non-profit Regional Internet Registry for Africa.
opsec: passive
opsecNote: A WHOIS query hits AFRINIC's registry, not the target's server, so it is passive and the subject is not notified. Bulk/automated queries are rate-limited by AFRINIC; throttle to avoid blocks.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: AFRINIC is the official Regional Internet Registry for Africa — the authoritative source for who holds African IP allocations and ASNs.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- African Network Information Centre
- afrinic.net WHOIS
tags:
- whois
- rir
- ip-lookup
- africa
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# AFRINIC

> The Regional Internet Registry for Africa — the authoritative WHOIS for African IP ranges and ASNs: who was allocated a block, and their registered and abuse contacts.

## When to use
You have an `ip-address` (or an ASN/`domain`) that geolocates to Africa and you need the responsible network holder — the organisation that was allocated the block, the country, and the registered admin/abuse contacts. This attributes an IP seen in logs, an email header, or a photo-upload trace to a real African ISP, hosting provider, or enterprise, and can yield contact names, emails, and addresses to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.afrinic.net/ and open its WHOIS/"whois query" tool (or query the AFRINIC whois server directly: `whois -h whois.afrinic.net <IP-or-ASN>`).
2. Enter the `ip-address`, IP range, or ASN.
3. Read the record: `inetnum`/`netname`, the holding organisation, country, and `admin-c`/`tech-c`/abuse contacts (often names, emails, phone, address).
4. Pivot: the org name feeds business lookups; abuse/admin contacts feed email/phone OSINT; the country narrows geography. If the IP isn't African, AFRINIC will refer you to the correct RIR (ARIN/RIPE/APNIC/LACNIC).

## Inputs → Outputs
- **In:** `ip-address` / IP range / ASN (African allocations), sometimes a `domain`'s resolved IP.
- **Out:** holding `employer-org`, registered `address`, admin/abuse `associate` contacts and `email`.
- **Empty/negative result looks like:** "no entries found" or a referral to another RIR — the address isn't in AFRINIC's region; re-query the correct registry.

## Gotchas & OpSec
- Only covers African (AFRINIC-region) allocations; for other regions use the matching RIR.
- Contact records can be stale or point to an upstream provider rather than the end user — treat as the network holder, not necessarily the person behind a single IP.
- Rate-limited: heavy automated querying gets throttled.

## Overlaps ("do both")
- Pair with the other RIRs (ARIN/RIPE/APNIC/LACNIC) — an IP belongs to exactly one; if AFRINIC returns a referral, follow it. Combine with passive-DNS/domain WHOIS to link an IP to hostnames.

## Trust & verifiability
`trust: trusted` — AFRINIC is the official registry; allocation data is authoritative. Contact accuracy depends on what the network holder registered and keeps current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | afrinic |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → employer-org, address, associate, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
