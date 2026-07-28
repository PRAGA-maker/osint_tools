---
id: open-dns
name: OpenDNS
description: Use when you want a free filtering DNS resolver to harden your own recon setup (block malware/phishing) — an OpSec/privacy resolver, not a target-lookup tool.
url: https://www.opendns.com/home-internet-security
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A free public DNS resolver with malware/phishing filtering to protect the machine you investigate from.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: freemium
costNote: Free public resolvers (208.67.222.222 / 208.67.220.220) and free Home filtering; business-grade threat intelligence (Cisco Umbrella Investigate) is a separate paid product.
opsec: passive
opsecNote: This protects/routes YOUR DNS; it doesn't query anything about a target. Note that using OpenDNS means Cisco sees your resolver traffic — a trade-off: filtering and reliability in exchange for DNS visibility to the provider. Use with a VPN if that matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Cisco (OpenDNS/Umbrella); an established, reputable DNS security provider. The free tier is a resolver/filter, not an investigative data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Cisco OpenDNS
tags:
- dns
- privacy
- opsec
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# OpenDNS

> A free, Cisco-run public DNS resolver with built-in malware/phishing filtering — an OpSec/hardening choice for your own recon environment, not a lookup tool for targets.

## When to use
You want to harden the machine you run investigations from by pointing it at a filtering resolver that blocks known malware/phishing domains, or you want a reliable public DNS alternative to your ISP's. This is defensive plumbing: it protects and routes *your* DNS. It does not enrich a target — for domain intelligence (passive DNS, WHOIS history) you want dedicated recon tools, and Cisco's own investigative product (Umbrella Investigate) is paid.

## How to use it (`bestInteractionPattern`: web-manual)
1. Point your device/router DNS at OpenDNS resolvers (`208.67.222.222`, `208.67.220.220`), or set up a free OpenDNS Home account for custom filtering.
2. Optionally configure category/domain filtering in the dashboard.
3. Browse/investigate as normal; known-malicious domains are blocked at resolution.
4. Be aware Cisco now sees your resolver traffic — layer a VPN if you don't want that visibility.
5. Pivot: for actual domain OSINT (passive DNS, historical records), use `domains-ip-infrastructure` tools rather than the resolver itself.

## Inputs → Outputs
- **In:** n/a for target work — you configure it as your resolver (a `domain` you visit is filtered, not investigated).
- **Out:** filtered DNS resolution / blocked-domain protection. No person- or target-level `selectorsOut`.
- **Empty/negative result looks like:** n/a. If a legitimate site is blocked, it's a false-positive category filter — allowlist it.

## Gotchas & OpSec
- Direction: this is a defensive resolver, not an investigative lookup. Don't mistake it for a passive-DNS/threat-intel source (that's the paid Umbrella Investigate).
- Provider visibility: Cisco sees your DNS queries. Filtering vs. privacy is the trade-off; combine with a VPN if needed.
- Category filtering can over-block; tune it so it doesn't hide legitimate research targets.

## Overlaps ("do both")
- Complements `domains-ip-infrastructure` recon tools — those investigate a target domain; OpenDNS just hardens and routes your own resolution while you do so.

## Trust & verifiability
`trust: trusted` — an established Cisco service; trustworthy as a resolver/filter, but understand it's infrastructure hardening, not an OSINT data source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-dns |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → — |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
