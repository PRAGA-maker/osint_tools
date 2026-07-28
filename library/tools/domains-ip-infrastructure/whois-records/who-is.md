---
id: who-is
name: Who.is
description: Use when you have a `domain` or `ip-address` and want registration, DNS and network ownership data — returns WHOIS/RDAP registrant details, nameservers, DNS records and IP ownership.
url: https://who.is/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: Fast web WHOIS/RDAP + DNS lookup for a domain or IP, with historical records behind a paid tier.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- name
- email
- address
status: live
pricing: freemium
costNote: Free WHOIS, RDAP, DNS and IP lookups; Domain History reports and Pro monitoring are paid add-ons.
opsec: passive
opsecNote: Queries public WHOIS/RDAP/DNS registries via who.is, not the target's own server, so the subject is not contacted. Your query is seen by who.is; use a sock-puppet if you don't want it logged against you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running third-party WHOIS/RDAP front-end. Data quality depends on the underlying registries; it presents, it does not vouch.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- icann-whois-lookup
aliases:
- who.is
tags:
- whois
- domain-registration
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Who.is

> A clean web front-end for WHOIS, RDAP, DNS and IP lookups — the fast way to pull a domain's registration and network footprint in one page.

## When to use
You have a `domain` or `ip-address` tied to a subject (a personal site, a business, an email domain, an IP from a header/log) and want to know who registered it, where it resolves, and what network owns it. Where WHOIS is un-redacted, this can surface a registrant `name`, `email` or `address`; even when redacted, nameservers, creation date and hosting IP are useful pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://who.is/ and enter the `domain` (or `ip-address`).
2. Read the WHOIS/RDAP block: registrar, registrant (if public), created/updated/expiry dates, nameservers.
3. Open the DNS tab for A/AAAA/MX/TXT/NS records — MX reveals the mail provider, A/AAAA the hosting IP.
4. For an IP, use the IP lookup to get the owning org/ASN and network range.
5. Pivot: hosting IP → other domains on that IP (reverse-IP); registrant email → other domains by the same registrant; nameserver → domains sharing infrastructure.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** `domain`/`ip-address` infrastructure, nameservers, DNS records, and — when unredacted — registrant `name`, `email`, `address`
- **Empty/negative result looks like:** WHOIS fields showing "REDACTED FOR PRIVACY", GDPR masking, or a WHOIS-privacy proxy registrant — common for personal domains; fall back to DNS/hosting pivots and historical records.

## Gotchas & OpSec
- Human-in-the-loop: none for the free lookups.
- OpSec: **passive** — you query registries via who.is, never the target's server. Still a burner session is wise for sensitive work.
- Modern WHOIS is heavily redacted; the richest registrant data is often in *historical* records (paid here, or via other archives), not the current record.

## Overlaps ("do both")
- Pairs with `[[icann-whois-lookup]]` — ICANN's lookup is the authoritative registry front-end for the current record; who.is adds DNS/IP tabs and a historical (paid) view alongside it.

## Trust & verifiability
`trust: community` — a reputable third-party presenter of registry data; treat the registration facts as coming from the registry, and corroborate names/emails before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | who-is |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, name, email, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
