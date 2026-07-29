---
id: viewdns-info
name: ViewDNS.info
description: Use when you have a `domain` or `ip-address` and want DNS/WHOIS intelligence — returns reverse-IP, reverse-WHOIS, IP history, DNS records, and more from one free toolkit.
url: https://viewdns.info/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: A one-stop free toolkit of DNS/IP reconnaissance lookups — reverse IP, reverse WHOIS, IP history, DNS records, port scan, and related domain-intel tools.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- address
status: live
pricing: freemium
costNote: The web tools are free to use (a free lookup allowance per tool); an API and bulk data products are paid. Reverse WHOIS/IP and history are usable free in the browser.
opsec: passive
opsecNote: Lookups run against ViewDNS's own datasets and public records, not the target's servers (except the optional port scanner, which actively probes the target). You disclose the queried domain/IP to ViewDNS. For the port scanner specifically, treat it as active and use a sock-puppet IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, widely used domain-intel site; dependable for quick lookups. Reverse-WHOIS and IP-history data are third-party snapshots — corroborate before drawing firm conclusions.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- reverse-domain
- crt-sh
- securitytrails
aliases:
- ViewDNS
- viewdns.info
tags:
- whois
- reverse-ip
- reverse-whois
- dns-recon
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# ViewDNS.info

> A free Swiss-army toolkit for domain/IP intelligence: reverse IP, reverse WHOIS, IP history, DNS records, port scan, and a dozen more lookups on one page.

## When to use
You have a `domain` or `ip-address` and want to pivot fast without stringing together separate tools. ViewDNS bundles the essentials: **Reverse IP** (other sites on a server), **Reverse WHOIS** (domains registered to a name/email/org), **IP History** (a domain's past IPs — great for piercing Cloudflare to find an origin), DNS records, reverse MX/NS, subdomain discovery, and HTTP headers. Reverse WHOIS in particular turns a registrant `name`/`email` into their other domains.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://viewdns.info/ and pick a tool from the grid.
2. Enter your input — a `domain`, an `ip-address`, or (for Reverse WHOIS) a registrant name/email/org.
3. Read results, e.g.:
   - **Reverse WHOIS** → list of domains tied to that registrant (`domain` leads + registrant `address`).
   - **IP History** → past IPs/dates (a pre-CDN origin IP is a prize).
   - **Reverse IP** → co-hosted domains.
4. Note free per-tool allowances; space out queries or use the API for volume.
5. Pivot: registrant domains feed `[[crt-sh]]`/`[[reverse-domain]]`; a discovered origin IP feeds Shodan/reverse-IP; confirm WHOIS ties against a second source.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or a registrant `name`/`email`/org (Reverse WHOIS).
- **Out:** `domain` (co-hosted/registrant domains, subdomains), `ip-address` (history, DNS), and registrant `address` fields.
- **Empty/negative result looks like:** no records — privacy-protected WHOIS (redacted registrant), a domain with no indexed history, or a big shared host that makes reverse-IP meaningless. Absence isn't proof of isolation.

## Gotchas & OpSec
- Human-in-the-loop: none for web tools.
- OpSec: **passive** for most lookups (ViewDNS queries its data), but the **port scanner actively probes the target** — treat that one as active and use a sock-puppet IP.
- Third-party snapshots: reverse-WHOIS and IP-history come from ViewDNS's collection, which can be incomplete or stale, and WHOIS privacy hides many registrants. Corroborate.
- Free allowances are limited; heavy use needs the paid API.

## Overlaps ("do both")
- Overlaps with `[[securitytrails]]` — SecurityTrails has deeper historical DNS/WHOIS (some paid); cross-check IP history and reverse WHOIS between them.
- Feeds `[[crt-sh]]` and `[[reverse-domain]]` to widen a registrant/infrastructure footprint.

## Trust & verifiability
`trust: community` — a reliable, long-standing lookup hub, but its reverse-WHOIS/IP-history data are third-party snapshots. Use hits as strong leads and confirm registrant/origin claims against an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | viewdns-info |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
