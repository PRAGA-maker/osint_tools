---
id: certkit-certificate-transparency-log-search
name: CertKit — Certificate Transparency Log Search
description: Use when you have a domain and want its issued TLS certificates to enumerate subdomains — returns domain (subdomains via SANs) from public Certificate Transparency logs.
url: https://www.certkit.io/tools/ct-logs/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- certificate-search
bestFor: Passive subdomain enumeration by mining a domain's certificates from Certificate Transparency logs.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free tier returns up to 100 certificates per query; unlimited results, brand monitoring, and API access require a paid Business account.
opsec: passive
opsecNote: CT logs are public and CertKit queries them on its servers, so the target domain is never contacted — fully passive with no footprint on the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial certificate-monitoring service; the CT data itself is authoritative (public append-only logs), the free web tool is a convenient front-end.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- CertKit CT logs
tags:
- certificate-transparency
- subdomain
- passive-dns
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# CertKit — Certificate Transparency Log Search

> A browser front-end over Certificate Transparency logs — enter a domain and get the TLS certificates issued for it, exposing subdomains via their Subject Alternative Names.

## When to use
You have a `domain` and want to discover its subdomains and infrastructure **passively** — every publicly-trusted TLS certificate is logged to CT, and the SAN field routinely leaks `dev.`, `vpn.`, `mail.`, and other hosts an org never advertised. Use it to widen the attack/footprint surface without ever touching the target. Infrastructure recon, not people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.certkit.io/tools/ct-logs/ and enter the `domain` (child domains are included automatically).
2. Read the returned certificates: issuing CA, issuance/expiry dates, and the SAN list — each SAN is a candidate `domain`/subdomain.
3. Collect the unique hostnames; recent certs highlight currently-active infrastructure, expired ones show history.
4. If you hit the 100-cert free cap on a large org, cross-check with another CT source (crt.sh) to fill gaps.
5. Pivot: resolve discovered subdomains ([[aiodnsbrute]] for brute-forced ones) → IPs → [[ipvoid]]/[[whois-arin]].

## Inputs → Outputs
- **In:** a `domain`.
- **Out:** issued TLS certificates with issuance/expiry dates and SAN `domain`s (subdomains).
- **Empty/negative result looks like:** no certificates (a domain that has never had a publicly-trusted cert, or uses only internal CAs) — meaning CT can't help here, not that the domain is inactive.

## Gotchas & OpSec
- Free tier caps at 100 certificates — big orgs will overflow it; corroborate with crt.sh or the CT logs directly.
- CT only captures publicly-trusted certificates; internal/self-signed hosts won't appear.
- SANs can include retired hosts; verify a subdomain still resolves before treating it as live.

## Overlaps ("do both")
- Pairs with [[aiodnsbrute]] (brute-forced subdomains) and [[dns-history-lookup]]: CT finds historically-issued names, brute-forcing finds guessable ones, passive-DNS finds resolved ones — the union is far more complete.

## Trust & verifiability
`trust: community` — a commercial front-end, but the underlying CT logs are authoritative append-only records; any certificate it shows is independently checkable in the public logs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | certkit-certificate-transparency-log-search |
