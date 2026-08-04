---
id: domainrecon
name: DomainRecon
description: Use when you have a `domain` and want a one-shot recon report — DNS records, WHOIS/RDAP, SSL certs and discovered subdomains — returns infrastructure `domain`/`ip-address` data.
url: https://kriztalz.sh/domain-recon/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Getting a fast consolidated domain recon report (DNS + WHOIS + certs + subdomains) from one web query.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free online tool; no account required.
opsec: passive
opsecNote: DNS, WHOIS/RDAP and certificate-transparency data are pulled from public registries and CT logs, so the query does not touch the subject's own web server — passive. Subdomain discovery here is CT/passive-sourced rather than active brute force, keeping your footprint off the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent developer-hosted recon front-end aggregating authoritative sources (registry WHOIS/RDAP, DNS, CT logs); the underlying data is verifiable, the aggregator is community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- faviconhash
- githubrecon
- metadata-viewer
- pgpkeyanalyser
- searchdorks
- traceroutevisualizer
aliases:
- kriztalz domain-recon
tags:
- domains-ip-infrastructure
- dns
- whois
- subdomains
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# DomainRecon

> A free web front-end that bundles the core domain-recon lookups — DNS, WHOIS/RDAP, SSL certificates and passively-discovered subdomains — into one report.

## When to use
You have a `domain` and want the standard first-pass recon without running separate tools: full DNS record set (A/AAAA/MX/TXT/NS/SOA), live WHOIS/RDAP registration data, SSL certificate details, and a list of discovered subdomains. Good as a quick consolidated snapshot at the start of infrastructure work, or to sanity-check ownership and mail configuration for a subject's domain.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://kriztalz.sh/domain-recon/.
2. Enter the target `domain` (or URL) and run the report.
3. Read the sections: DNS records, WHOIS/RDAP registrant/dates, SSL certificate (issuer, SANs), and discovered subdomains.
4. Mine the details — SAN entries and subdomains expand the attack/investigation surface; MX/TXT reveal the mail and verification providers; RDAP dates anchor a timeline.
5. Pivot: feed subdomains and `ip-address`es into reverse-IP (`[[tcp-ip-utils-domain-neighbors]]`) and tech-fingerprinting (`[[wappalyzer]]`); take registrant details into WHOIS-history tools.

## Inputs → Outputs
- **In:** `domain`
- **Out:** DNS records, WHOIS/RDAP data, SSL certificate details, subdomains, resolved `ip-address`es
- **Empty/negative result looks like:** redacted WHOIS (GDPR/privacy proxy), few subdomains found, or a domain that doesn't resolve. Redacted registrant data is normal now — pivot to certificate SANs and DNS instead.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — WHOIS/RDAP and DNS come from registries and CT logs, not the subject's server; subdomain discovery is passive (CT-based), so no brute-force noise reaches the target.
- Data currency: WHOIS/RDAP is live but DNS is briefly cached and CT-based subdomain lists only show names that ever got a certificate — combine with a wordlist enumerator for completeness.

## Overlaps ("do both")
- Overlaps with dedicated WHOIS, DNS and subdomain tools — DomainRecon is the fast all-in-one first look; pair it with `[[wappalyzer]]` and reverse-IP for attribution, and with brute-force enumerators (fed by `[[seclists-dns-subdomains]]`) for subdomains CT logs miss.

## Trust & verifiability
`trust: community` — an independent aggregator, but it surfaces authoritative primary data (registry WHOIS/RDAP, live DNS, public CT logs) that you can re-verify with `dig`, `whois`, and crt.sh.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | domainrecon |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
