---
id: about-rdap-org
name: about.rdap.org
description: Use when you have a `domain`, `ip-address`, or ASN and want structured registration data via RDAP — returns a hosted RDAP query interface and the standardized JSON registration record.
url: https://about.rdap.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Querying RDAP (the modern, structured successor to WHOIS) for domains, IPs, and ASNs.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free informational hub and hosted RDAP client; RDAP itself is a free open protocol run by registries/RIRs. No account or key.
opsec: passive
opsecNote: RDAP queries hit the registry/RIR, not the target's server, so the domain/IP owner is not alerted. The query goes through the hosted client or the bootstrap service, which sees your IP; use a clean IP for sensitive lookups. Results are the same public data WHOIS exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: RDAP is the IETF/ICANN-standardized registration-data protocol; about.rdap.org is a community reference hub pointing to authoritative registry endpoints.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- viewdns-info
- whoxy
- team-cyru-ip-to-asn-lookup
aliases:
- RDAP
- rdap.org
tags:
- domainsandips
- Domains & IPs
- rdap
- whois
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# about.rdap.org

> The reference hub for RDAP — the structured JSON successor to WHOIS — with a hosted client that routes your domain/IP/ASN query to the authoritative registry and returns a machine-readable registration record.

## When to use
You have a `domain`, `ip-address`, or ASN and want its registration data in a clean, structured form rather than the inconsistent free-text of legacy WHOIS. RDAP returns standardized fields (registrar, status, nameservers, creation/expiry dates, and — where not privacy-redacted — registrant/abuse contacts) as JSON, which is easier to parse and cross-source. Use it when WHOIS output is messy or when you want to script registration lookups reliably.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://about.rdap.org/ — it explains RDAP and links to a hosted query client and the IANA bootstrap registry.
2. Enter the `domain`, `ip-address`, or ASN; the client routes the query to the correct authoritative RDAP server (via the bootstrap that maps TLD/IP-block → registry endpoint).
3. Read the JSON: `entities` (registrar/registrant where shown), `events` (registration/expiry/last-changed dates), `nameservers`, and `status` codes.
4. For automation, query the registry RDAP endpoint directly, e.g. `https://rdap.org/domain/example.com` or `https://rdap.org/ip/8.8.8.8`.
5. Pivot: nameservers and abuse contacts feed hosting/DNS clustering; dates and status corroborate a domain's age and standing.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or ASN
- **Out:** structured registration record — registrar, `domain` nameservers, dates, status, and any non-redacted contact `entities`
- **Empty/negative result looks like:** a 404 / "no RDAP server" for TLDs that don't yet support RDAP, or a record with contacts redacted for privacy/GDPR — the object exists but personal fields are withheld.

## Gotchas & OpSec
- Not every ccTLD publishes RDAP yet; for those you'll fall back to classic WHOIS. A missing RDAP endpoint is a coverage gap, not a nonexistent domain.
- Registrant personal data is usually GDPR-redacted just as in modern WHOIS — RDAP standardizes the *format*, it does not un-redact.
- OpSec: **passive** — the query goes to the registry, never to the target's infrastructure.

## Overlaps ("do both")
- Pairs with `[[viewdns-info]]` and `[[whoxy]]` — RDAP gives the clean current record, while those add historical/reverse WHOIS that RDAP does not; run both to get current + historical registration data.

## Trust & verifiability
`trust: trusted` — RDAP is an IETF/ICANN standard served by the authoritative registries and RIRs, so the record is as canonical as registration data gets.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | about-rdap-org |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
