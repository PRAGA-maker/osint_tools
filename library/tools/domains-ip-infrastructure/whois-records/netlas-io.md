---
id: netlas-io
name: Netlas.io
description: Use when you have a `domain`, `ip-address`, or ASN and want WHOIS/DNS, open ports, certificates, and historical infrastructure data — returns `domain`, `ip-address`, and attack-surface records.
url: https://app.netlas.io/whois_domains/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: Internet-wide asset search — WHOIS/DNS lookups, attack-surface mapping, and historical infrastructure data for a domain or IP.
input: Domain name, IP address, ASN, DNS records
output: DNS records, WHOIS data, open ports, SSL certificates, service information, historical data
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- address
status: live
pricing: freemium
costNote: Free registered tier with a modest daily request quota (~50/day historically); larger volume and API access are paid.
opsec: passive
opsecNote: Queries Netlas's own cached internet-scan data — you never scan or touch the target's servers, so the lookup is invisible to them. A free account (email) is needed for full features.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established internet-intelligence search engine (Netlas), comparable to Shodan/Censys; data is scan-derived and periodically refreshed.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Netlas
- netlas.io
tags:
- whois
- dns
- attack-surface
- internet-scan
source: arf-seed
lastVerified: '2026-07-23'
---

# Netlas.io

> An internet-wide asset search engine: query a domain, IP, or ASN and get its WHOIS/DNS, open ports, certificates, running services, and historical records from Netlas's cached scans.

## When to use
You have a `domain` or `ip-address` tied to a subject or organisation and want a full infrastructure picture without touching their servers: registration/WHOIS details (registrant, dates, contacts where public), DNS records, hosting IPs and open ports, SSL certificates, and — crucially — historical data showing how the infrastructure changed over time. Strong for corroborating ownership and mapping a target's digital footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in (free account) at https://app.netlas.io/ and pick the relevant search — WHOIS, DNS, or host/response search.
2. Enter the `domain`, `ip-address`, or ASN.
3. Read the result: WHOIS registrant/contacts and dates, DNS records, hosting IP and ports, certificates, and prior states in the historical view.
4. Pivot: registrant email/name feeds people search; a hosting IP feeds reverse-IP to co-hosted domains; certificate SANs feed subdomain discovery.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or ASN
- **Out:** `domain`/`ip-address` infrastructure, WHOIS contacts (possible `name`/`email`/`address`), certificates, ports, historical records
- **Empty/negative result looks like:** privacy-protected WHOIS (registrant redacted) or no scan data for an obscure host — redaction hides the registrant but the DNS/cert/host data is usually still informative.

## Gotchas & OpSec
- Free tier caps daily requests; heavy work needs a paid plan or API key.
- WHOIS is frequently privacy-masked; lean on certificates, DNS history, and reverse-IP when the registrant is hidden.
- OpSec: **passive** — cached scan data, no packets to the target; your account ties queries to you, so use a dedicated one for sensitive work.

## Overlaps ("do both")
- Pairs with Shodan/Censys and `[[certificate-search]]` — different scanners see different ports/certs and refresh on different schedules, so cross-check.

## Trust & verifiability
`trust: community` — a reputable internet-intelligence engine; scan/WHOIS data can lag reality, so confirm a live host directly before acting on a port or service claim.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | netlas-io |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
