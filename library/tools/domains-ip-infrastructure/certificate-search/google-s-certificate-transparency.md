---
id: google-s-certificate-transparency
name: Google's Certificate Transparency
description: Use when you need to understand or access the Certificate Transparency ecosystem — the reference for CT logs that record every TLS cert, enabling subdomain and cert discovery.
url: https://www.certificate-transparency.org/known-logs
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- certificate-search
bestFor: Understanding the CT log ecosystem and finding the logs that back cert-search tools like crt.sh.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public reference/infrastructure (Google's Certificate Transparency project); the logs themselves are openly queryable.
opsec: passive
opsecNote: CT logs are public append-only records — querying them (directly or via a search front-end) is passive and never touches the target. This is how you enumerate a domain's certificates/subdomains without probing the target itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's official Certificate Transparency project; the authoritative reference for the CT standard and the list of known, trusted logs.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Certificate Transparency
- CT logs
tags:
- domains-ip-infrastructure
- certificate-transparency
- subdomains
- passive-recon
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Google's Certificate Transparency

> The reference hub for Certificate Transparency — the public, append-only logs of every TLS certificate issued, which make passive subdomain and certificate discovery possible.

## When to use
You want to enumerate a `domain`'s certificates and sub`domain`s *passively* — without sending a single packet to the target — by reading the public CT logs that CAs must publish to. This page documents the CT ecosystem and the list of known logs; in practice you query those logs through a search front-end, but understanding CT is what tells you why (and how completely) that works.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read https://www.certificate-transparency.org/known-logs to see the trusted CT logs and how the system works.
2. To actually search certs for a domain, use a CT front-end (e.g. crt.sh, Censys) that indexes these logs — query the `domain` to list issued certificates.
3. Extract the subject/SAN entries: every hostname a cert covers is a discovered sub`domain`.
4. Pivot: discovered sub`domain`s feed DNS/IP resolution (`[[dnsrecon]]`) and service enumeration; unexpected certs can reveal staging/internal hosts and even planned domains.

## Inputs → Outputs
- **In:** `domain` (queried against CT logs via a front-end)
- **Out:** issued certificates and the sub`domain`s (SANs) they cover
- **Empty/negative result looks like:** few/no certs — the domain uses a private CA, wildcard-only certs (hiding subdomains), or is new; wildcards limit what CT reveals.

## Gotchas & OpSec
- This URL is the CT *project/reference*; for searching, pair it with a log front-end like crt.sh — it isn't a search box itself.
- Wildcard certs (`*.example.com`) hide specific subdomains from CT.
- CT shows certs that were *logged* — some internal/private-CA hosts never appear.

## Overlaps ("do both")
- Pairs with crt.sh/Censys (query the logs) and `[[dnsrecon]]`/`[[anubis]]` — CT gives passive subdomain discovery; DNS tools then resolve and validate the hosts actively.

## Trust & verifiability
`trust: trusted` — Google's official CT project; the logs are cryptographically append-only public records, so certificate data sourced from them is authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-s-certificate-transparency |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
