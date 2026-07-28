---
id: mayorsecdnsscan
name: MayorSecDNSScan
description: Use when you have a `domain` and want its DNS records, zone-transfer exposure, and enumerated subdomains — returns subdomain `domain`s and their `ip-address`.
url: https://github.com/dievus/msdnsscan
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Enumerating DNS records, testing AXFR zone transfers, and discovering subdomains for a target domain.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source Python CLI.
opsec: active
opsecNote: Zone-transfer attempts and subdomain resolution query the target's authoritative nameservers directly, so this touches the target's infrastructure and can be logged. Use only in authorized work; for stealth, prefer passive-DNS datasets that don't hit the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by dievus (msdnsscan); wraps standard DNS enumeration (records, AXFR, subdomain brute) — dependable but only as thorough as its wordlist and the target's DNS hygiene.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- dork-dump
- geemail-user-finder
- oh365userfinder
aliases:
- msdnsscan
tags:
- Domain/IP/Links
- Domain/IP investigation
- dns
- subdomain-enumeration
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# MayorSecDNSScan

> A Python DNS-recon CLI: dump a domain's records, try a zone transfer, and enumerate its subdomains in one pass.

## When to use
You have a `domain` tied to a subject or organization and want to map its DNS surface — the A/MX/NS/TXT records, whether the nameservers foolishly allow a full AXFR zone transfer (which dumps every record at once), and what subdomains exist. Subdomains and their IPs expose additional infrastructure (mail, VPN, dev/staging, vanity hosts) worth pivoting on.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/dievus/msdnsscan` and install its Python requirements.
2. Run it against the target `domain` (see the repo's `-h` for flags controlling record lookups, zone-transfer testing, and the subdomain wordlist).
3. Read the output: DNS records, any successful zone transfer (a significant misconfiguration finding), and resolved subdomains with their IPs.
4. Pivot: each subdomain `domain` + `ip-address` feeds reverse-DNS, hosting, and passive-DNS lookups; an open AXFR hands you the whole namespace at once.

## Inputs → Outputs
- **In:** a target `domain`
- **Out:** DNS records, zone-transfer result, and enumerated subdomain `domain`s with `ip-address`
- **Empty/negative result looks like:** only the base records resolve, AXFR is refused (the healthy default), and the wordlist finds no subdomains — expected for a well-configured domain; try a larger wordlist or passive-DNS sources.

## Gotchas & OpSec
- **Active** reconnaissance — brute-force subdomain resolution and AXFR attempts hit the target's nameservers and may be logged/rate-limited. Only run it where you're authorized.
- Subdomain results are only as complete as the wordlist; absence isn't proof a subdomain doesn't exist.
- For a stealthy first pass, use passive-DNS (which queries a third-party dataset, not the target) before touching the target's DNS directly.

## Overlaps ("do both")
- Pair with passive-DNS and certificate-transparency search (stealthy, third-party) — those find subdomains without touching the target; MayorSecDNSScan adds active record/AXFR checks. Same-source siblings: [[dork-dump]], [[oh365userfinder]].

## Trust & verifiability
`trust: community` — a straightforward open-source wrapper around standard DNS techniques; results are directly verifiable by re-querying DNS yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mayorsecdnsscan |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
