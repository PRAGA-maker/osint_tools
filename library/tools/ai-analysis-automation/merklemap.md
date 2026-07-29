---
id: merklemap
name: Merklemap
description: Use when you have a `domain` and want to enumerate its subdomains and TLS certificates from certificate-transparency logs — returns linked sub`domain`s and cert data.
url: https://www.merklemap.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Fast subdomain discovery and certificate-transparency search for a domain.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free web search of subdomains/certificates with limits; higher-volume search, historical data, and the live-domains API are paid.
opsec: passive
opsecNote: It queries public certificate-transparency logs and its own index, not the target's servers, so no subdomain scan touches the subject's infrastructure and nothing is alerted. Standard passive recon — VPN for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Certificate-transparency data is publicly logged and authoritative; Merklemap indexes it. Coverage of very new/very obscure subdomains varies, so cross-check with another CT source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- MerkleMap
tags:
- dns
- subdomains
- certificate-transparency
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Merklemap

> A subdomain and certificate-transparency search engine — enter a domain and get its known subdomains and TLS certificates, with historical data and a live newly-issued-hostname stream on paid tiers.

## When to use
You have a `domain` and want to map its attack surface: enumerate subdomains (often revealing dev/staging/admin hosts and forgotten services) and inspect its TLS certificates. Useful for the infrastructure phase of profiling an organisation or a subject's site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.merklemap.com/ and search the target `domain`.
2. Review the enumerated subdomains and the certificates issued for them (certs often expose additional hostnames via Subject Alternative Names).
3. For bulk/automated use or historical/live-stream data, use the paid API.
4. Note interesting subdomains (mail, VPN, admin, staging) for follow-up.
5. Pivot: discovered sub`domain`s feed host-scan tools (`[[censys-ipv4]]`), WHOIS, and passive-DNS enrichment.

## Inputs → Outputs
- **In:** `domain`
- **Out:** enumerated sub`domain`s and TLS certificate data (SAN hostnames, issuers, validity)
- **Empty/negative result looks like:** few/no subdomains — the domain may genuinely be flat, or certs use wildcards that hide hostnames; cross-check another CT source before concluding.

## Gotchas & OpSec
- Freemium limits apply to the free web search; historical and live-stream data are paid.
- CT logs only show hosts that got a logged certificate — internal hosts without public certs won't appear.
- OpSec: **passive**; you query public CT logs/index, never the target's servers.

## Overlaps ("do both")
- Do both with other CT/subdomain tools (crt.sh-class sources) and `[[censys-ipv4]]` — each CT index and scanner captures a slightly different set of hostnames.

## Trust & verifiability
`trust: trusted` — built on publicly-verifiable certificate-transparency data; corroborate a specific subdomain's liveness with a resolver/host scan.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | merklemap |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
