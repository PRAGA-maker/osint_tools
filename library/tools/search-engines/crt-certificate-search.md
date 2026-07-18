---
id: crt-certificate-search
name: crt.sh Certificate Search
description: Use when you have a `domain` and want every TLS certificate ever issued for it — returns subdomains, issuance dates, issuing CA and any `email`/org in the certificate.
url: https://crt.sh
category: search-engines
path:
- search-engines
bestFor: Enumerating a domain's subdomains and certificate history from public Certificate Transparency logs.
selectorsIn:
- domain
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free public search interface over Certificate Transparency logs; no account, no payment.
opsec: passive
opsecNote: Queries hit crt.sh's aggregated CT-log database, not the target's servers, so the domain owner is not alerted. Fully passive; no sock puppet needed for a lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Sectigo (a public CA); data comes directly from append-only Certificate Transparency logs, which are authoritative and tamper-evident.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- crt-sh-certificate-search
aliases:
- crt.sh
- Certificate Transparency search
tags:
- speciality-search-engines
- subdomain-enumeration
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# crt.sh Certificate Search

> A free front-end to Certificate Transparency logs: type a domain and get every TLS certificate ever issued for it — the fastest passive way to enumerate subdomains.

## When to use
You have a `domain` linked to a subject or their organisation and want to map its infrastructure. Because every publicly-trusted certificate is logged in CT, crt.sh reveals subdomains (dev, mail, vpn, staging, internal-looking hosts) that DNS brute-forcing would miss, plus the issuing CA and any organisation/`email` embedded in the certificate subject — all without touching the target's own servers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://crt.sh and enter the domain. Use `%` as a wildcard: `%.example.com` returns certs for all subdomains; `example.com` matches the apex.
2. Read the results table: each row is a logged certificate with its issuance/expiry dates, issuer CA, and the identities (CN and SANs) it covers.
3. Click a `crt.sh?id=` entry to see the full certificate, including any organisation, locality, or contact `email` in the subject/SAN fields.
4. Pivot: newly-found subdomains feed DNS/IP tools and web recon; an org or email in a cert feeds email/company OSINT. (crt.sh also supports JSON output by appending `&output=json`.)

## Inputs → Outputs
- **In:** `domain` (optionally with `%` wildcards)
- **Out:** `domain` (subdomains and alternate names from certs), `email`/org identities embedded in certificates, plus issuer and validity dates
- **Empty/negative result looks like:** "None" / no rows — no certificate for that pattern is in the CT logs (very new, internal-only, or self-signed hosts won't appear); absence doesn't prove the host doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none; large wildcard queries can be slow — narrow the pattern if it times out.
- OpSec: passive — you query CT logs, never the target. Nothing is sent to the subject's infrastructure.
- Wildcard certificates (`*.example.com`) hide specific hostnames; combine with active DNS enumeration to resolve which subdomains actually exist.

## Overlaps ("do both")
- Pairs with `[[crt-sh-certificate-search]]` (same source) and with active DNS/subdomain tools — CT logs list names that were certified, while DNS resolution confirms which are live now; run both to separate historical from active infrastructure.

## Trust & verifiability
`trust: trusted` — crt.sh is run by Sectigo and serves data straight from append-only Certificate Transparency logs, so results are authoritative and independently verifiable against the logs themselves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crt-certificate-search |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
