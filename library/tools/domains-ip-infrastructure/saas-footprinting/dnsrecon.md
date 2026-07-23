---
id: dnsrecon
name: dnsrecon
description: Use when you have a `domain` and want thorough DNS enumeration — returns records (A/MX/NS/SOA/TXT/SRV), subdomains, PTR ranges, and zone-transfer results.
url: https://github.com/darkoperator/dnsrecon
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- saas-footprinting
bestFor: Comprehensive DNS reconnaissance of a domain from the command line.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (GPL-2.0); Python CLI, actively maintained. In Kali by default.
opsec: active
opsecNote: Standard record lookups are low-noise, but subdomain brute-forcing and zone-transfer attempts send traffic to the target's DNS and can be logged. Only run against authorised targets; use a resolver/VPN and scope the brute-force wordlist.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Long-running, widely-used open-source tool (darkoperator); a staple of DNS recon shipped in security distros.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- DNSRecon
tags:
- domains-ip-infrastructure
- dns
- recon
- cli
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- dns-recon
---

# dnsrecon

> A thorough command-line DNS enumerator — records, subdomains, zone transfers, PTR sweeps — for footprinting a domain's DNS surface.

## When to use
You have a `domain` and want its DNS picture: all record types, discoverable sub`domain`s (dictionary or brute-force), reverse-PTR ranges, SRV services, cached records, and any misconfigured zone transfer (AXFR) that dumps the whole zone. A core infrastructure-mapping step that turns one domain into hosts and `ip-address`es.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install dnsrecon` or use the Kali package; `git clone https://github.com/darkoperator/dnsrecon`.
2. Run standard enumeration: `dnsrecon -d example.com`; add `-t axfr` for zone-transfer tests or `-D wordlist.txt -t brt` for subdomain brute-forcing.
3. Read the enumerated records and hosts; export with `--json`/`--csv`.
4. Pivot: discovered sub`domain`s and `ip-address`es feed reverse-IP, cert-transparency, and service enumeration; an open AXFR is a significant finding.

## Inputs → Outputs
- **In:** `domain` (+ optional wordlist)
- **Out:** DNS records, sub`domain`s, PTR ranges, `ip-address`es, zone-transfer dumps
- **Empty/negative result looks like:** only the basic records resolve, no extra subdomains found, AXFR refused — expected for a well-configured domain; broaden the wordlist before concluding.

## Gotchas & OpSec
- Brute-forcing and AXFR attempts are active and logged — get authorisation.
- Subdomain results depend on your wordlist; a miss isn't proof of absence.
- Respect rate limits; aggressive brute-forcing can trip defenses.

## Overlaps ("do both")
- Overlaps with `[[finalrecon]]` (broader all-in-one) and `[[anubis]]`/passive subdomain sources — use passive cert-transparency first, then dnsrecon for active depth.

## Trust & verifiability
`trust: trusted` — a mature, widely-trusted open-source tool; it queries DNS directly, so results are authoritative for what DNS actually returns at scan time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnsrecon |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
