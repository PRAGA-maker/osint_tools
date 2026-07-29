---
id: cert4recon
name: Cert4Recon
description: Use when you have a `domain` and want fast passive subdomain enumeration from certificate-transparency logs (crt.sh) — returns domain (subdomains) leads.
url: https://github.com/mathis2001/Cert4Recon
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quick passive subdomain enumeration for a domain by querying crt.sh certificate-transparency data.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open-source Python 3 script. No API key; relies on the public crt.sh service.
opsec: passive
opsecNote: Passive against the target — subdomains come from public certificate-transparency logs via crt.sh, so you never touch the target's infrastructure. The optional "-a" alive check DOES connect to each subdomain (active); skip it, or run it through a proxy, if you must stay fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small open-source recon script (mathis2001); simple wrapper over crt.sh, so results are only as complete as certificate-transparency coverage.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- webhackurls
aliases:
- Cert4Recon
tags:
- Domain/IP/Links
- Domain/IP investigation
- subdomain-enumeration
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Cert4Recon

> A tiny Python recon script that pulls a domain's subdomains straight from certificate-transparency logs (crt.sh) — passive, fast, no API key.

## When to use
You have a `domain` and want to map its attack surface / infrastructure by enumerating subdomains without actively probing the target. Certificate-transparency logs record every TLS cert issued, so hosts that ever got a cert (including internal-sounding ones like `vpn.`, `mail.`, `dev.`) show up. Good first pass before active tooling, or when you must keep collection passive.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/mathis2001/Cert4Recon` (Python 3, no extra install).
2. Run: `./cert4recon.py -t example.com` — queries crt.sh for subdomains of the target.
3. Optionally `-o out.txt` to save results, and `-a` to filter to only "alive" (responding) subdomains.
4. Review the subdomain list.
5. Pivot: resolve each subdomain to IPs (DNS), feed into port/service scanning or `[[webhackurls]]`, and map hosting/ASN infrastructure.

## Inputs → Outputs
- **In:** a `domain`
- **Out:** list of subdomains (`domain`) found in certificate-transparency logs, optionally filtered to live hosts
- **Empty/negative result looks like:** an empty list — the domain has no CT-logged certs for subdomains (rare for active domains), or crt.sh is temporarily down; absence in CT ≠ no subdomains (hosts without public certs won't appear).

## Gotchas & OpSec
- CT-only: subdomains that never received a public cert are invisible — combine with DNS brute-force/other sources for completeness.
- The `-a` alive check is **active** (it connects to each host) — omit it to stay passive.
- Depends on crt.sh uptime and rate limits.

## Overlaps ("do both")
- Complements DNS brute-forcers (Amass, subfinder) and `[[webhackurls]]` — CT enumeration catches what wordlists miss and vice-versa; run both for full subdomain coverage.

## Trust & verifiability
`trust: community` — simple open-source wrapper over authoritative crt.sh CT data; results trace to public certificate-transparency logs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cert4recon |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
