---
id: dns-recon
name: DNS Recon
description: Use when you have a `domain` and want its full DNS footprint — returns records, discovered subdomains, zone-transfer and PTR results.
url: https://github.com/darkoperator/dnsrecon
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Comprehensive DNS enumeration of a domain — records, subdomain brute-force, zone-transfer testing, and reverse-DNS sweeps.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open source (dnsrecon by darkoperator). pip-installable / ships in Kali.
opsec: active
opsecNote: dnsrecon sends real DNS queries — brute-forcing subdomains generates many lookups that the target's authoritative DNS (and passive-DNS collectors) can see. It doesn't touch the target's web services, but the query volume is observable; use a resolver that doesn't attribute back to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Long-standing, widely-used open-source DNS enumeration tool (darkoperator); a staple of the recon toolkit, bundled in Kali Linux.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- dnsrecon
aliases:
- dnsrecon
tags:
- dns
- subdomain-enumeration
- recon
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# DNS Recon

> The Swiss-army knife of DNS enumeration: hand it a domain and it pulls records, brute-forces subdomains, tests for zone transfers, and sweeps reverse DNS.

## When to use
You have a `domain` and want to map its DNS footprint as part of infrastructure recon — all standard records (NS/SOA/MX/A/AAAA/TXT/SRV), subdomains via wordlist brute-force, misconfigured zone transfers (AXFR), and PTR records across an IP range. It expands a single domain into a list of hosts and `ip-address`es to investigate further. Infrastructure mapping; missing-persons relevance is low and indirect (enumerating a suspect organisation's or site's hosts).

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install dnsrecon` (or use the copy in Kali Linux).
2. Run enumeration modes:
   ```
   dnsrecon -d example.com                     # standard records + checks
   dnsrecon -d example.com -t brt -D words.txt # brute-force subdomains
   dnsrecon -d example.com -t axfr             # test zone transfer
   dnsrecon -r 192.0.2.0/24                     # reverse-DNS sweep of a range
   ```
3. Read the output: record types, discovered subdomains with their `ip-address`es, any successful zone transfer (a jackpot that dumps the whole zone), wildcard status.
4. Pivot: resolved subdomains/`ip-address`es feed passive DNS, port/service scanning, and favicon/asset clustering (`[[favfreak]]`); a working AXFR hands you the full host inventory.

## Inputs → Outputs
- **In:** `domain` (or an IP range for reverse lookups)
- **Out:** DNS records, discovered subdomain `domain`s + `ip-address`es, zone-transfer dump, PTR records
- **Empty/negative result looks like:** only the base records and no brute-forced subdomains — either the wordlist missed them, wildcard DNS is masking results, or the domain genuinely has few hosts; absence isn't proof there are no other subdomains (try passive sources).

## Gotchas & OpSec
- **Active** — brute-force mode fires many DNS queries; noisy and observable. Combine with *passive* subdomain sources first to reduce the brute-force set.
- Wildcard DNS produces false positives (everything "resolves"); dnsrecon flags wildcards — heed it.
- Zone transfers rarely succeed on well-configured DNS, but always worth testing.
- OpSec: use non-attributable resolvers; the target's DNS logs your pattern.

## Overlaps ("do both")
- Pairs with passive enumerators (Amass, subfinder) and permutation generators (`[[mksub]]`) — passive finds known hosts quietly, dnsrecon brute-forces unlisted ones; run passive first, then dnsrecon to fill gaps. Resolved hosts feed asset-clustering and scanning.

## Trust & verifiability
`trust: trusted` — a mature, auditable open-source tool that simply reports DNS responses, so results are authoritative for what the resolver returned (mind wildcards and resolver caching).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dns-recon |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
