---
id: censys-certificates
name: Censys Certificates
description: Use when you have a `domain`, org name, or cert detail and want to search TLS/SSL certificates for related hosts — returns certificates, their SANs (other `domain`s), and issuing hosts.
url: https://search.censys.io/certificates
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Certificate-transparency search to map a target's infrastructure via shared/related TLS certificates.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Requires a free Censys account to search; generous free tier, with paid plans for higher volume/API and historical depth.
opsec: passive
opsecNote: You query Censys's scanned certificate dataset, not the target — no probe reaches the subject's host. Note searches are tied to your logged-in Censys account; use a dedicated research account, not a personal one, if attribution matters.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Censys is a reputable internet-scanning company with an academic lineage (University of Michigan); its certificate data is authoritative, sourced from its own scans and CT logs.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- censys
- censys-ipv4
- search-censys-io
aliases:
- Censys certificate search
tags:
- certificate-transparency
- tls
- infrastructure-mapping
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Censys Certificates

> Censys's TLS/SSL certificate search: pivot from one domain or certificate to every related host and hostname that shares its certificate chain.

## When to use
You have a `domain` tied to your subject and want to expand their infrastructure map. TLS certificates leak relationships: a single cert's Subject Alternative Names (SANs) list every hostname it covers, and searching by organisation/issuer/fingerprint surfaces sibling domains and the hosts serving them. Great for finding a person's other websites, staging/dev subdomains, and hosts they'd rather keep unlinked.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in at https://search.censys.io/certificates (free Censys account).
2. Search by `domain`, SAN, organisation, or certificate fingerprint.
3. Read matching certificates: SANs (additional `domain`s), issuer, validity, and the hosts (`ip-address`) presenting them.
4. Pivot: SAN hostnames become new domains to investigate; associated hosts feed IP/infrastructure lookups; a self-signed/reused cert can tie disparate hosts to one operator.

## Inputs → Outputs
- **In:** `domain` (or SAN / org / cert fingerprint)
- **Out:** certificates, SAN `domain`s, issuer, and serving `ip-address`(es)
- **Empty/negative result looks like:** no certificates — the domain never had a public TLS cert Censys observed, or you searched a private/internal name; not proof no site exists.

## Gotchas & OpSec
- **Account required** — anonymous cert search was retired; use a research Censys account.
- Certificate data is historical/point-in-time; a SAN may list hosts no longer live.
- Wildcard and CDN (Cloudflare) certs can be shared by many unrelated sites — don't over-attribute.

## Overlaps ("do both")
- Pairs with `[[censys]]`/`[[search-censys-io]]` (host search) and crt.sh (CT logs) — certificate search finds related hostnames, host search shows what those IPs run; run both plus crt.sh, as each indexes CT slightly differently.

## Trust & verifiability
`trust: trusted` — Censys is an authoritative scanner with transparent data provenance (its own scans + CT logs); certificate facts are verifiable, though relationship *inferences* need corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | censys-certificates |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
