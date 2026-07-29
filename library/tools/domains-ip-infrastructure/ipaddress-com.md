---
id: ipaddress-com
name: IPAddress.com
description: Use when you have an `ip-address` or `domain` and want geolocation, WHOIS ownership, DNS records and blacklist status — returns geolocation, ip-address and domain infrastructure detail.
url: https://www.ipaddress.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-stop web console for IP/domain WHOIS, geolocation, DNS and blacklist checks.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- geolocation
- domain
status: live
pricing: free
costNote: Free browser tool; no account or payment required. Ad-supported.
opsec: passive
opsecNote: Passive — the subject is never contacted; you query IPAddress.com's own databases about an address. Your lookups are logged by the site, so use a clean/VPN IP for sensitive casework. Geolocation is ISP/registry-level, not a home address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial IP-tools portal aggregating public WHOIS/DNS/geo databases; data is only as fresh as its upstream sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ipaddress-tools
aliases:
- ipaddress.com
tags:
- ip
- dns
- geolocation
- whois
source: inteltechniques-tools
lastVerified: '2026-07-29'
enrichment: full
---

# IPAddress.com

> A free browser console that bundles IP/domain WHOIS, approximate geolocation, DNS records and blacklist checks in one place.

## When to use
You have an `ip-address` (e.g. one pulled from an email header, server log, or a chat leak) or a `domain` and want a fast, no-login read on who owns it, roughly where it sits, and what DNS/mail infrastructure sits behind it. Good as a first-pass triage before reaching for specialist WHOIS/DNS tooling.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ipaddress.com/ in a clean/sock-puppet browser session.
2. Paste the target `ip-address` or `domain` into the lookup box (or use the dedicated IP Lookup / WHOIS / DNS Lookup / Blacklist Check sub-tools linked on the page).
3. Read the output:
   - **IP** → owning organisation/ISP, ASN, country/region/city-level `geolocation`, reverse-DNS hostname.
   - **Domain** → registrar WHOIS, name servers, A/MX/NS records, hosting IP.
   - **Blacklist** → whether the IP appears on common spam/abuse block lists.
4. Pivot: the owning org/ASN and reverse-DNS feed infrastructure mapping; the hosting IP of a domain feeds reverse-IP lookups to find co-hosted sites.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** `geolocation` (country/region/city, ISP), `ip-address` (hosting/reverse-DNS), `domain` (WHOIS, DNS records)
- **Empty/negative result looks like:** WHOIS "no match"/redacted (GDPR-privacy) records, or a geolocation that resolves only to a country + datacenter — treat city-level geo as a lead, never a residential address.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a plain web form.
- OpSec: passive — you never touch the subject, only third-party databases. Geolocation for a residential/mobile IP is ISP-region accurate at best; datacenter/VPN IPs geolocate to the host, not the person.
- Registrar WHOIS is increasingly privacy-redacted, so a blank owner field is expected, not a failure.

## Overlaps ("do both")
- Pairs with `[[ipaddress-tools]]` — run both when one portal's geo/WHOIS source is stale or redacted; cross-checking IP geolocation across independent databases reduces false positives.

## Trust & verifiability
`trust: community` — a well-established commercial IP-tools site, but it merely surfaces upstream WHOIS/geo/DNS data; verify any actionable result against the authoritative registry (RIR WHOIS, registrar) before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipaddress-com |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, geolocation, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
