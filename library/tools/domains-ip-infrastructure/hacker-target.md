---
id: hacker-target
name: HackerTarget
description: Use when you have a `domain` or `ip-address` and want fast recon (WHOIS, DNS, reverse-IP, reverse-DNS) — returns linked domains, IPs and hosting infrastructure.
url: https://hackertarget.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-stop web recon on a domain or IP — WHOIS, DNS, reverse IP (co-hosted sites), reverse DNS, traceroute and more from a browser or API.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free web tools and a free API tier (daily query limits); paid membership raises limits and unlocks the full toolset. The free tier is enough for ad-hoc recon.
opsec: passive
opsecNote: HackerTarget queries the target's public infrastructure (DNS/WHOIS/reverse-IP) from ITS servers, not yours — so the lookup isn't attributable to your IP. This is passive recon; it doesn't probe the subject's own devices. Still, treat active scanning tools (port/URL scans) with care and authorization.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established, widely used web-recon service; results mirror authoritative DNS/WHOIS data, so reliability tracks the underlying registries.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- hacker-target-reverse-dns
- hackertarget-com
aliases:
- hackertarget.com
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- dns-recon
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# HackerTarget

> A browser-and-API recon hub for domains and IPs — WHOIS, DNS, reverse-IP (what else is hosted on this server), reverse-DNS and traceroute, run from HackerTarget's infrastructure so the lookup isn't tied to you.

## When to use
You have a `domain` or `ip-address` connected to your subject — a personal site, a small business, a mail server, an IP from a header/log — and want to map the infrastructure around it: who registered it, where it resolves, what other domains share the same server (reverse IP), and its DNS records. Reverse-IP in particular can tie a person's several sites together when they're co-hosted. Useful for pivoting from a web presence to an owner or to associated properties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://hackertarget.com and pick a tool (WHOIS, DNS lookup, Reverse IP, Reverse DNS, traceroute, etc.).
2. Enter the `domain` or `ip-address` and run it; read the result.
   - Reverse IP → list of other domains on the same server (possible same-owner sites).
   - WHOIS → registrant/organization, dates, registrar (often privacy-masked now).
   - DNS → mail (MX), name servers, and hosting clues.
3. For batch/automation, use the free API endpoints (e.g. `https://api.hackertarget.com/reverseiplookup/?q=<ip>`) within the daily limit.
4. Pivot: co-hosted domains → repeat WHOIS/recon on each; a registrant org/email → `[[hackertarget-com]]` and email/domain OSINT; an IP → geolocation and hosting provider.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** related `domain`s (reverse IP), resolved `ip-address`es, DNS/WHOIS records, hosting/route info
- **Empty/negative result looks like:** reverse-IP returns only the one domain (dedicated host) or a huge shared-hosting list (thousands of unrelated sites — not useful for attribution); WHOIS masked by privacy proxy. Rate-limit messages mean you hit the free quota.

## Gotchas & OpSec
- Reverse IP on shared/CDN hosting (Cloudflare, big hosts) returns noise — only meaningful on dedicated/small servers.
- WHOIS is increasingly privacy-redacted (GDPR/privacy proxies) — expect masked registrants.
- Human-in-the-loop: free tier has daily rate limits; space queries or use the API key.
- OpSec: passive and non-attributable (runs server-side), but don't point active scan tools at systems you're not authorized to test.

## Overlaps ("do both")
- Pairs with `[[hackertarget-com]]` / `[[hacker-target-reverse-dns]]` and dedicated WHOIS-history and passive-DNS services — HackerTarget gives the current snapshot; historical DNS/WHOIS shows what changed and unmasks older registrants.

## Trust & verifiability
`trust: community` — a reputable, long-running recon service; its output reflects authoritative DNS/WHOIS data, so accuracy tracks those sources (and their redactions).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hacker-target |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
