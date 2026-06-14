---
id: robtex-com
name: Robtex.com
description: Use when you have a domain or IP (e.g. from an email's mail server or a registered domain) and want its DNS, hosting, and related-domain graph.
url: https://www.robtex.com
category: email
path:
- email
bestFor: DNS/IP/WHOIS research — mapping a domain or IP to its name servers, MX/mail hosts, hosting, and other domains on the same infrastructure.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
- metadata-exif
status: live
pricing: freemium
costNote: Free web lookups; paid Robtex Pro/API for higher limits and historical data.
opsec: passive
opsecNote: Queries passive DNS / public records — no contact with the subject's infrastructure from your IP. You do submit the query to Robtex.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established, well-regarded DNS/IP research service. NOTE — this is a network/infrastructure tool, not an email-lookup tool; it is miscategorized under email. Use it on the DOMAIN behind an email, not on the address itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases: []
tags:
- dns
- ip
- whois
- infrastructure
source: metaosint
lastVerified: ''
enrichment: full
---

# Robtex.com

> Robtex is a veteran DNS/IP research engine — feed it a `domain` or `ip-address` and it maps name servers, mail hosts, hosting, and co-located domains. It is infrastructure tooling, not an email-owner lookup.

## When to use
You have a `domain` (e.g. the part after the @ of a subject's custom-domain email, or a domain found via reverse-WHOIS) or an `ip-address` and want to understand its DNS, who hosts it, its MX/mail servers, and what other domains share the same infrastructure. It does NOT take a person's email address and return their identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to robtex.com and enter the domain or IP.
2. Review the DNS graph: A/AAAA, MX (mail hosts), NS, related domains on the same IP/host.
3. Pivot co-hosted domains and the mail host into further WHOIS/reverse-WHOIS work.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** DNS records, hosting IPs, MX/mail servers, co-located `domain`s, route/ASN metadata (`metadata-exif`).
- **Empty/negative result looks like:** sparse graph or "no data" for a freshly registered or parked domain.

## Gotchas & OpSec
- Human-in-the-loop: free tier is rate-limited; deep/historical data needs Robtex Pro.
- OpSec: passive — uses passive DNS, not active probing of the target's servers. Useful for confirming whether a custom email domain is self-hosted vs. a shared provider.

## Overlaps ("do both")
- Pairs with `[[reverse-whois]]`: reverse-WHOIS gives the person's domains; Robtex turns each domain into hosting/DNS/co-tenant intelligence.

## Trust & verifiability
`trust: community` — long-standing, reputable infrastructure tool. Rated for accuracy of DNS data; flagged as miscategorized under email (it is a domain/IP tool).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | robtex-com |
| category | email |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
