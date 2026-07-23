---
id: qualys-ssl-check
name: Qualys SSL Check
description: Use when you have a `domain` and want its TLS/certificate posture — returns the SSL cert chain (names, issuer, validity, SANs) and server configuration grade.
url: https://www.ssllabs.com/ssltest/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Inspecting a domain's TLS certificate details and server SSL configuration in depth.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free public service from Qualys SSL Labs; no account needed.
opsec: active
opsecNote: "SSL Labs actively connects to the target host on port 443 to test its TLS config, so the request originates from Qualys's scanners (not your IP), which shields you — but the target's server does log a connection from a known SSL Labs scanner. There's also an option to make results public; keep 'Do not show results on the boards' checked for sensitive targets."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Qualys SSL Labs is the industry-standard TLS testing service; certificate and configuration data is authoritative (read live from the server).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- SSL Labs
- Qualys SSL Test
- ssllabs.com
tags:
- domain-and-ip-research
- tls
- certificates
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Qualys SSL Check

> The industry-standard TLS tester: enter a domain and get a deep report on its certificate (names, issuer, SANs, validity) and server SSL configuration, graded A–F.

## When to use
You have a `domain` and want its certificate details — most usefully the **Subject Alternative Names (SANs)**, which often reveal other `domain`s/subdomains sharing the same certificate, and the issuer/validity dates that help fingerprint an operator. Also gives the resolving `ip-address` and full protocol/cipher config. A precise infrastructure step, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ssllabs.com/ssltest/ and enter the target `domain`.
2. **Check "Do not show the results on the boards"** before scanning a sensitive target.
3. Wait for the scan; read the certificate section: Common Name, **SANs** (pivot list of related domains), issuer, serial, validity window.
4. Note the resolving `ip-address`(es) and the config grade/protocol support.
5. Pivot: feed SAN domains into subdomain/passive-DNS tools; use issuer + validity to correlate with other hosts by the same operator.

## Inputs → Outputs
- **In:** `domain`
- **Out:** certificate details incl. **SANs** (`domain`s), issuer/validity, resolving `ip-address`, TLS config grade
- **Empty/negative result looks like:** "Assessment failed" / no TLS — the host may not serve HTTPS, be behind a WAF blocking the scanner, or be down; a failure isn't proof of anything about the subject.

## Gotchas & OpSec
- The scan actively connects to the target from an SSL-Labs scanner (logged); it does shield your own IP.
- Results can be posted to public boards — opt out for sensitive work.
- A Cloudflare/CDN cert reflects the CDN, not the origin; SANs then describe the CDN's shared cert, not the target's own.

## Overlaps ("do both")
- Pairs with certificate-transparency and passive-DNS tools like [[dns-dumpster]] and the overview from [[web-check]] — SSL Labs gives the deepest single-cert detail (SANs, config), CT logs give historical certs, passive-DNS ties them to hosts.

## Trust & verifiability
`trust: trusted` — Qualys SSL Labs is the authoritative TLS scanner; certificate data is read live from the server, so it's as reliable as the handshake itself.
