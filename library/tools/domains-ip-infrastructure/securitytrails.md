---
id: securitytrails
name: SecurityTrails
description: Use when you have a `domain` or `ip-address` and want its historical DNS records, current subdomains and WHOIS history — returns related `domain`s and `ip-address`es over time.
url: https://securitytrails.com/dns-trails
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Pivoting a domain/IP through historical DNS, subdomain enumeration and WHOIS-history to map infrastructure and past ownership.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free account gives limited web queries and a small API quota; deeper history, bulk subdomains and higher API limits are paid (SecurityTrails is now part of Recorded Future).
opsec: passive
opsecNote: Queries hit SecurityTrails' own historical datasets, not the target — the subject is never contacted. Searches are tied to your account, so use a dedicated investigative login.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established commercial DNS-intelligence provider (Recorded Future); data is first-party collected passive DNS and WHOIS history, widely used in threat intel.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- DNSTrails
- SecurityTrails DNS history
tags:
- domain-and-ip-research
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# SecurityTrails

> A DNS and domain-intelligence platform: historical DNS records, subdomain enumeration and WHOIS history that let you see how a domain's infrastructure and ownership changed over time.

## When to use
You have a `domain` or `ip-address` tied to a subject and need more than its current state: which IPs it *used to* resolve to, what subdomains exist, which other domains share its hosting or WHOIS details, and how registration data changed. That historical pivoting is how you connect a person's current site to older infrastructure they thought they'd abandoned.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free account at https://securitytrails.com and log in.
2. Search a `domain` (e.g. via the DNSTrails view) to see current + historical A/MX/NS records, subdomains, and WHOIS history.
3. Search an `ip-address` to see which domains have resolved to it (reverse/passive DNS).
4. Pivot: a historical IP, a shared name server, or an old WHOIS email/registrant becomes the next selector to chase.
5. For scale, use the API with your account key within the free quota, or a paid tier for bulk work.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** historical + current DNS records, subdomains (`domain`), reverse-DNS `ip-address`es, WHOIS history
- **Empty/negative result looks like:** a brand-new or low-profile domain may have thin history and few subdomains — sparse data is a real signal (young/obscure), not a failure.

## Gotchas & OpSec
- Human-in-the-loop: account login required; the free tier caps queries, history depth and subdomain counts.
- WHOIS history may be redacted (post-GDPR) for many domains — older records are often the useful ones.
- OpSec: passive toward the target; attributable to your SecurityTrails account.

## Overlaps ("do both")
- Pairs with passive-DNS and internet-scan tools like `[[onyphe]]` and certificate-transparency search — coverage and history windows differ, so cross-checking surfaces subdomains and past IPs any single source misses.

## Trust & verifiability
`trust: trusted` — a first-party DNS-intelligence dataset from an established provider; records are timestamped and can be corroborated against other passive-DNS sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | securitytrails |
