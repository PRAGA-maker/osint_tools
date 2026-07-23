---
id: subdomain-finder
name: Subdomain Finder
description: Use when you have a `domain` and want its subdomains discovered passively — returns subdomain hosts and their resolved ip-address.
url: https://osint.sh/subdomain/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast passive subdomain enumeration of a domain from a free web tool — no install.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free browser tool, part of the osint.sh suite. No account or payment; generous but subject to soft rate limits.
opsec: passive
opsecNote: Enumeration is done by osint.sh from certificate-transparency logs and passive DNS, not by probing the target, so the subject's servers see nothing. Only osint.sh sees the domain you queried; use a VPN if that matters to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Popular free OSINT toolbox; results are as complete as its passive sources (CT logs / passive DNS) and can miss subdomains that never appeared in a certificate. Corroborate with a second enumerator for coverage.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- osint.sh subdomain finder
- osint.sh subdomain
tags:
- Domain/IP/Links
- subdomain-enumeration
- passive-recon
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Subdomain Finder

> osint.sh's free passive subdomain finder — paste a domain, get its known subdomains from certificate-transparency and passive-DNS sources without touching the target.

## When to use
You have a target `domain` and want to map its attack/footprint surface — dev, staging, mail, VPN, admin, or vanity subdomains that often reveal internal naming, hosting, or a personal side-project tied to the subject. Passive enumeration means you find these without sending traffic to the target's own servers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://osint.sh/subdomain/ .
2. Enter the root `domain` (e.g. `example.com`) and run the search.
3. Read the returned subdomain list, typically with resolved IPs. Skim for interesting hostnames — `dev.`, `staging.`, `mail.`, `admin.`, `vpn.`, or personal-looking names.
4. Because CT-log-based enumeration misses hosts that never got a public cert, run a second tool for anything important (active brute-force or another aggregator).
5. Pivot: resolved `ip-address` values feed reverse-IP / infrastructure mapping; an interesting subdomain feeds a fresh WHOIS or content review.

## Inputs → Outputs
- **In:** root `domain`
- **Out:** list of `domain` subdomains and their resolved `ip-address`
- **Empty/negative result looks like:** no subdomains returned — usually a domain with no public certificates or passive-DNS history, not proof it has none. Confirm with another enumerator before concluding.

## Gotchas & OpSec
- Coverage is bounded by passive sources: subdomains that never appeared in a CT log or passive-DNS record won't show. It is a floor, not a complete map.
- Heavy use may hit soft rate limits on the free service.
- OpSec: **passive** — nothing is sent to the target; only osint.sh sees your query.

## Overlaps ("do both")
- Complements active enumerators (e.g. amass/subfinder brute-force modes) and crt.sh — passive finds the easy wins fast, active fills the gaps. Combine for a fuller picture.

## Trust & verifiability
`trust: community` — a widely used free tool. Reliable for what its passive sources contain; treat the list as a strong starting set, not an exhaustive one, and verify live hosts before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | subdomain-finder |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
