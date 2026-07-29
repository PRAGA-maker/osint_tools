---
id: fierce-domain-scanner
name: Fierce Domain Scanner
description: Use when you have a `domain` and want to enumerate its subdomains and map them to non-contiguous IP space — returns discovered `domain`s and resolved `ip-address`es.
url: https://github.com/davidpepper/fierce-domain-scanner
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: DNS reconnaissance — zone-transfer attempts and brute-force subdomain enumeration to find a target's IP footprint.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: degraded
pricing: free
costNote: Free and open-source. You provide the Perl runtime; no account or key needed.
opsec: active
opsecNote: Fierce performs direct DNS queries and brute-force lookups against the target's nameservers, which authoritative DNS operators can log. This is active recon — run it from controlled infrastructure (VPS/VPN), not your home IP, when the target could notice or object.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Legacy Perl fork (davidpepper) of RSnake's original fierce; 300+ stars but old and only lightly maintained — a modern Python rewrite (mschwager/fierce) exists and may be preferable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- fierce.pl
- fierce DNS scanner
tags:
- subdomains
- dns-recon
- recon
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Fierce Domain Scanner

> The classic Perl DNS-recon tool — attempts zone transfers and brute-forces subdomains to locate a domain's scattered IP space; legacy, but still illustrative.

## When to use
You have a `domain` and want to map its DNS attack surface: enumerate subdomains, attempt a zone transfer, and resolve the results to IPs so you can find non-contiguous hosting a target uses. Useful for the infrastructure phase of an investigation (linking a domain to its servers and neighbours). Being legacy, prefer the modern Python `fierce` for fresh work, but this fork still runs.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/davidpepper/fierce-domain-scanner` and run the Perl script (`fierce.pl`).
2. Point it at the target `domain`; optionally supply a custom wordlist and DNS-server options.
3. Let it attempt a zone transfer, then brute-force hostnames and resolve them.
4. Read the discovered subdomains and their resolved `ip-address`es.
5. Pivot: new IPs feed reverse-IP and ASN lookups; subdomains feed certificate-transparency and content OSINT.

## Inputs → Outputs
- **In:** `domain` (+ optional wordlist / DNS-server args)
- **Out:** enumerated subdomains (`domain`) and resolved `ip-address`es
- **Empty/negative result looks like:** few or no subdomains — the domain may use wildcard DNS, block brute-forcing, or the legacy tool's assumptions may not fit modern DNS; confirm with a current tool.

## Gotchas & OpSec
- **Legacy Perl**: unmaintained, so behaviour against modern DNS/wildcards may be imperfect — treat a thin result skeptically and re-run with a maintained scanner.
- **Active recon**: brute-forcing nameservers is noisy and loggable; use controlled infrastructure.
- Zone transfers rarely succeed on well-configured domains; the brute-force wordlist does most of the work.

## Overlaps ("do both")
- Pair with modern subdomain tools (amass, subfinder, crt.sh) — those use passive sources fierce can't, so combining passive enumeration with fierce's active brute-force gives fuller coverage.

## Trust & verifiability
`trust: community` — open-source and inspectable, but an old fork; verify its findings against a maintained enumeration tool before relying on completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fierce-domain-scanner |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
