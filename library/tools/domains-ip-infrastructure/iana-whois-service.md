---
id: iana-whois-service
name: IANA Whois Service
description: Use when you have a `domain`, TLD, or `ip-address` block and want the authoritative registry/whois-server pointer for it — returns the sponsoring org and where to query next.
url: https://www.iana.org/whois
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Finding the authoritative registry, sponsoring organisation, and correct whois server for a TLD, root-level domain, or IP allocation.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- employer-org
status: live
pricing: free
costNote: Free authoritative service run by IANA (the Internet Assigned Numbers Authority); no account needed.
opsec: passive
opsecNote: Querying IANA hits IANA's servers, not the target domain's infrastructure, so the subject is never notified. Fully passive. Standard web logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: IANA is the top-level authority for the DNS root, TLDs, and IP-block delegations; its whois is the definitive pointer to the responsible registry.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- iana-root-zone-database
- ripe
- arin
aliases:
- iana.org/whois
- IANA WHOIS
tags:
- whois
- iana
- dns
- registry
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# IANA Whois Service

> The root-level whois: it doesn't give you a registrant's name — it tells you which registry/authority is responsible for a TLD or IP block, and which whois server to query next.

## When to use
You have a `domain` (especially an unusual TLD), a bare TLD, or an `ip-address`/allocation and you need to find the *authoritative* source for it. IANA's whois returns the sponsoring organisation and the delegated registry/whois server responsible — the correct next hop when a generic whois is ambiguous or a ccTLD/new-gTLD needs its specific registry. It's a routing/attribution step in domain and IP research, not a registrant-data lookup itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.iana.org/whois.
2. Enter the TLD (e.g. `.io`), a domain, or an IP/AS number.
3. Read the result: the sponsoring organisation, administrative/technical contacts for the delegation, and the authoritative whois server / registry URL.
4. Follow the pointer — query that registry's whois (or the right RIR) for the detailed registrant/allocation data.
5. Pivot: the authoritative whois server feeds a full domain-whois lookup; an IP delegation points you to the correct RIR (`[[ripe]]`, `[[arin]]`, etc.) for holder details.

## Inputs → Outputs
- **In:** `domain`, TLD, or `ip-address`/allocation
- **Out:** sponsoring `employer-org` (registry/authority), authoritative whois server / `domain` to query next
- **Empty/negative result looks like:** no delegation record — an invalid/unassigned TLD or block. It won't return individual registrant details; that's expected — IANA operates one level up.

## Gotchas & OpSec
- Root-level only: IANA tells you *who is responsible*, not who registered a specific second-level domain — you then query the registry it names.
- Best value is for exotic TLDs, ccTLDs, and IP-block delegations where the right whois server isn't obvious.
- OpSec: passive; nothing touches the target.

## Overlaps ("do both")
- Pairs with `[[iana-root-zone-database]]` (the TLD delegation records) and the RIRs `[[ripe]]` / `[[arin]]` — IANA routes you to the authority, those give the detailed domain or IP-allocation data.

## Trust & verifiability
`trust: trusted` — IANA is the authoritative operator of the DNS root and IP/AS number registries; its delegation and whois-server pointers are definitive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iana-whois-service |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
