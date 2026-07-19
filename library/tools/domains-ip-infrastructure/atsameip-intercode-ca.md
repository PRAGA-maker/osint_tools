---
id: atsameip-intercode-ca
name: AtSameIP
description: Use when you have an `ip-address` or `domain` and want to find other websites hosted on the same IP — returns a reverse-IP list of co-hosted domains that can reveal a subject's related sites.
url: https://atsameip.intercode.ca/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reverse-IP lookup — listing other domains sharing the same server/IP as a target site.
selectorsIn:
- ip-address
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free reverse-IP lookup; no account. (The tool has migrated hosts — the intercode.ca address now redirects to its current home, atsameip.com / intercode.info.)
opsec: passive
opsecNote: The lookup runs from the service against passive DNS/hosting data, not the target's server, so the subject isn't alerted. Reverse-IP results on shared/CDN hosting can be noisy and don't prove common ownership.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small free web utility (Intercode); reverse-IP data is only as complete as its source and, on shared hosting/CDNs, co-location does not imply the same owner — corroborate before drawing conclusions.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- atsameip
- atsameip.com
tags:
- reverse-ip
- domains
- hosting
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# AtSameIP

> A free reverse-IP lookup: give it an IP or domain and it lists other sites hosted on the same address — a quick way to surface a subject's other websites when they share a server, or to understand a host.

## When to use
You have an `ip-address` or a `domain` tied to your subject and want to find what else lives on the same IP. On dedicated or small shared hosting, co-hosted domains are often the same owner's other projects, aliases, or businesses — a strong pivot. On large shared hosts or CDNs, co-location is meaningless, so it's most useful once you've confirmed the host isn't a big shared provider.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://atsameip.intercode.ca/ (it redirects to the tool's current home if the host has moved).
2. Enter the `ip-address`, or a `domain` (it resolves to the IP first), and run the lookup.
3. Read the returned list of domains sharing that IP.
4. Judge the hosting context: a handful of related-looking domains on one IP is a real lead; hundreds of unrelated domains means shared hosting/CDN — discount it.
5. Pivot: promising co-hosted domains feed WHOIS/[[dnsquery]]/[[cqcounter-site-info]] to check for a common registrant, and content review to confirm the subject's link.

## Inputs → Outputs
- **In:** `ip-address` or `domain`
- **Out:** `domain` list (other sites on the same IP)
- **Empty/negative result looks like:** an empty list, a single domain, or a huge unrelated list — empty/single may mean dedicated hosting or incomplete data; a huge list means shared hosting where co-location proves nothing. Neither is a clean "answer" without context.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — the query hits the service's data, not the target's server.
- Key caveat: **shared hosting and CDNs** put unrelated sites on one IP, so co-location ≠ common ownership. Always confirm a suspected link with WHOIS/registrant overlap or content, and cross-check against another reverse-IP source (results vary by provider).

## Overlaps ("do both")
- Pairs with other reverse-IP services (ViewDNS, SecurityTrails) and with [[dnsquery]]/[[cqcounter-site-info]] — different reverse-IP datasets surface different co-hosted domains, and the WHOIS/DNS tools then test whether a co-hosted domain shares a registrant with the target.

## Trust & verifiability
`trust: community` — a small free utility whose reverse-IP data is partial and context-dependent; treat co-hosting as a lead to verify (via registrant/content overlap and a second source), not as proof of common ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | atsameip-intercode-ca |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
