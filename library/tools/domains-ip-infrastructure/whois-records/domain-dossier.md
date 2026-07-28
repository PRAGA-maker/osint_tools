---
id: domain-dossier
name: Domain Dossier
description: Use when you have a `domain` or `ip-address` and want a one-page recon report — WHOIS, DNS records, network whois, and optional traceroute/service scan — returns domain, ip-address.
url: https://centralops.net/co/DomainDossier.aspx
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: A fast, free, single-page WHOIS + DNS + network-whois report for a domain or IP.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free web tool from CentralOps.net; no account needed for the standard report. Heavy/automated use is throttled toward their paid API.
opsec: passive
opsecNote: WHOIS, DNS and registry lookups are queried by CentralOps' servers, not from your IP, so the target site doesn't see you. Enabling the optional "traceroute" or "service scan" makes CentralOps actively probe the target host — still from their infrastructure, but it is active reconnaissance; leave those off for a purely passive pass.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: CentralOps.net (Hexillion) is a long-established network-tools provider; results are pulled live from authoritative registries and DNS, not a stale cache.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- central-ops
- email-dossier
- free-online-network-tools
- viewdns-info
tags:
- whois
- dns-recon
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Domain Dossier

> CentralOps' one-shot recon page: paste a domain or IP and get WHOIS, DNS records, network-whois ownership, and (optionally) traceroute/service-scan — all on a single results page.

## When to use
You have a `domain` or `ip-address` surfaced in an investigation (from an email header, a website, a breach record) and want its registration, hosting, and DNS footprint in one look — who registered it, when, on what nameservers, and which network/ASN the IP belongs to. Good first stop before deeper infrastructure pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://centralops.net/co/DomainDossier.aspx.
2. Enter the `domain` or `ip-address`.
3. Tick the datasets you want: **domain whois record**, **DNS records**, **network whois record** are passive; **traceroute** and **service scan** actively probe the host — leave them unchecked for a stealthy pass.
4. Submit and read the combined report: registrant/registrar and dates, MX/NS/A records, and the IP's owning network/ASN.
5. Pivot: registrant email/name → people & reverse-whois search; IP/ASN → hosting neighbours; MX host → mail-provider intel; feed the domain into `[[viewdns-info]]` for reverse-IP/history.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** `domain` (nameservers, MX, related hosts), `ip-address` (resolved A records, owning network), plus WHOIS registrant/registrar/dates
- **Empty/negative result looks like:** redacted/privacy WHOIS (common post-GDPR, showing a privacy service instead of a person), NXDOMAIN for a dead domain, or a bogon/private IP with no network record.

## Gotchas & OpSec
- Registrant details are widely redacted now; expect a privacy proxy rather than a name on most modern domains — use registration *dates* and nameserver patterns as the pivot instead.
- The optional **traceroute/service scan** cross the line into active probing of the target host (done from CentralOps' servers); omit them if you want purely passive recon.
- Automated/bulk querying is rate-limited and nudged toward the paid Hexillion API.

## Overlaps ("do both")
- Pairs with `[[email-dossier]]` (same provider, validates an email/mail server) and `[[central-ops]]` for the broader toolset.
- Cross-check with `[[viewdns-info]]` for reverse-IP, DNS history, and reverse-whois that this single-page report doesn't provide.

## Trust & verifiability
`trust: trusted` — a long-running, reputable network-tools service querying authoritative registries and DNS live. The data is only as complete as public WHOIS/DNS allow (hence heavy redaction), but what it returns is reliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | domain-dossier |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
