---
id: search-censys-io
name: search.censys.io
description: Use when you have a `domain` or `ip-address` and want its internet-facing infrastructure, certificates, and services — returns linked domains, IPs, and hosting details.
url: https://search.censys.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fingerprinting a target's hosts, open services, and TLS certificates to pivot between IPs and domains.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Unauthenticated search works on a limited dataset; a free non-commercial account raises the cap to ~250 queries/month. Full history and API volume are paid.
opsec: passive
opsecNote: Passive against the target — Censys serves results from its own internet-wide scans, so you never touch the subject's infrastructure directly. Your queries are, however, logged to your Censys account; use a research account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Censys, Inc. (spun out of University of Michigan scans.io research); a widely cited, reputable internet-measurement provider.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- censys
- censys-certificates
- censys-ipv4
aliases:
- Censys Search
- censys.io
tags:
- domainsandips
- infrastructure
- certificate-transparency
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# search.censys.io

> A search engine over internet-wide scans and Certificate Transparency logs — turn a domain or IP into the full picture of the infrastructure behind it.

## When to use
You have a `domain` or `ip-address` tied to a subject (a personal site, a small-business server, a mentioned IP) and want to expand it: what other hosts share the same TLS certificate, what services and ports are exposed, what hostnames resolve to that IP, and who the hosting provider is. In a missing-persons context this is a niche/technical pivot — most useful when the subject ran their own site, server, or online business and you need to link infrastructure together.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search.censys.io/ and (recommended) log into a free research account to lift the guest limits.
2. Choose the dataset: **Hosts** (IPs/services) or **Certificates** (TLS certs from CT logs).
3. Enter the `domain` or `ip-address`, or a Censys query (e.g. `services.tls.certificates.leaf_data.names: example.com`).
4. Read the results: for a host, the open ports, service banners, software versions, and location; for a certificate, the subject/issuer DNs and every hostname it covers.
5. Pivot: a shared certificate or ASN links seemingly separate `domain`s and `ip-address`es; feed those back into WHOIS, DNS, and domain-history tools.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** related `domain`s (cert SANs, resolved hostnames), related `ip-address`es (hosts sharing certs/infrastructure), plus service/hosting metadata
- **Empty/negative result looks like:** "No results" — the host may be firewalled, behind a CDN (you'll see the CDN's edge, not the origin), or simply not in Censys's last scan; absence does not prove the asset is offline.

## Gotchas & OpSec
- Human-in-the-loop: full search and history require a (free) account login.
- CDN/cloud fronting hides the true origin — a Cloudflare-fronted site shows Cloudflare IPs, not the subject's server.
- Data reflects Censys's most recent scan, which can be days stale; use paid history for point-in-time analysis.
- OpSec: passive toward the target, but your queries are attributable to your Censys account.

## Overlaps ("do both")
- Pairs with `[[censys-certificates]]` and `[[censys-ipv4]]` (the certificate- and host-focused entries for the same platform) and complements `[[censys]]`; run the same selector through each view — certificates surface sibling domains, host search surfaces exposed services.

## Trust & verifiability
`trust: trusted` — Censys is a reputable, widely-cited internet-measurement company; scan data is empirical, though always time-bounded to the last scan.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-censys-io |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
