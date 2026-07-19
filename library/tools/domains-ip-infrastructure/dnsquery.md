---
id: dnsquery
name: DNSQuery
description: Use when you have a `domain` or `ip-address` and want registration and DNS infrastructure detail — returns WHOIS, nameservers, DNS records, reverse DNS, geolocation, and blocklist (RBL) status.
url: https://dnsquery.org
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-stop web console for WHOIS, DNS records, reverse DNS, IP geolocation, and RBL checks on a domain or IP.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- geolocation
status: live
pricing: free
costNote: Free to use, funded by donations; no account or API key required.
opsec: passive
opsecNote: Queries run from DNSQuery's servers against public DNS/WHOIS/RBL data, so the lookup is not attributed to you and does not touch the target's host directly (except the standard traceroute/ping tools, which do send packets to the target — avoid those if you need to stay fully passive).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent community-run diagnostic site; results mirror authoritative WHOIS/DNS/RBL sources and can be cross-checked, but the site itself is unverified as an organisation.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- dnsquery.org
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# DNSQuery

> A free browser console that bundles WHOIS, DNS-record, reverse-DNS, IP-geolocation, and blocklist lookups — a quick way to fingerprint the infrastructure behind a domain or IP tied to a subject.

## When to use
You have a `domain` (e.g. from a subject's website, email address, or a social bio link) or an `ip-address` and want to map the infrastructure around it: who registered it and when, which nameservers and mail servers it uses, what other records exist, where the IP geolocates, and whether it appears on spam blocklists. Useful for corroborating that a site belongs to the subject, dating when they registered a domain, or pivoting from an IP to a hosting region.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://dnsquery.org.
2. Pick the relevant tool group: **Domain** (WHOIS, nameserver info, zone health, Punycode), **IP** (IP WHOIS, geolocation, reverse DNS, RBL status), or **Hostname** (DNS records, DNS traversal, traceroute, ping).
3. Enter the `domain` or `ip-address` and run the query.
4. Read the output: registrant/registrar and dates from WHOIS (often redacted for privacy), the record set (A/MX/NS/TXT), the reverse-DNS PTR for an IP, the geolocated country/region, and any RBL listings.
5. Pivot: a registrant email/name feeds email- and people-search tools; an MX host or shared IP feeds reverse-IP/co-hosting lookups; registration dates help build a timeline.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** `domain`/`ip-address` infrastructure detail (WHOIS, DNS records, reverse DNS), `geolocation` of the IP, RBL status
- **Empty/negative result looks like:** WHOIS returning a privacy-proxy registrant (GDPR/redaction) rather than a real name, or an NXDOMAIN/"no records" for a domain that does not resolve — the tool worked, the data is simply protected or absent.

## Gotchas & OpSec
- Human-in-the-loop: none; direct web forms.
- OpSec: the WHOIS/DNS/RBL/geolocation lookups are **passive** (run server-side, not attributed to you). The **traceroute and ping** utilities, however, send packets directly to the target host — skip those if the subject controls the host and might notice.
- Modern WHOIS is heavily redacted; a proxy registrant is the norm now, not a dead end — pivot to historical WHOIS tools for pre-redaction records.

## Overlaps ("do both")
- Pairs with historical-WHOIS and reverse-IP tools because DNSQuery shows the *current* state; those recover the pre-privacy registrant and other domains sharing the same host, which is where the identifying leads usually are.

## Trust & verifiability
`trust: community` — DNSQuery is an independent diagnostic site of unverified ownership, but every value it returns (WHOIS, DNS records, RBL entries) comes from authoritative public sources and can be re-checked with `dig`/`whois` or another lookup, so accuracy is easy to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnsquery |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
