---
id: hacker-target-reverse-dns
name: Hacker Target - Reverse DNS
description: Use when you have an `ip-address` (or range) and want the domains/PTR records that resolve to it — returns `domain` leads.
url: https://hackertarget.com/reverse-dns-lookup/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ipv4
bestFor: Reverse-DNS / PTR lookup to find the domain(s) associated with an IP address or range.
selectorsIn:
- ip-address
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free web lookup and a free, rate-limited API tier (a few unauthenticated queries/day); a paid membership raises the limits.
opsec: passive
opsecNote: HackerTarget resolves the query from its own infrastructure against public DNS — no packet reaches the target host, so it's passive. The IP you submit is logged by HackerTarget; use a research session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, widely used hosted recon service; results reflect public DNS/PTR data at query time and can lag real changes.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- hacker-target
- hackertarget-com
- online-tool-to-extract-links-from-any-web-page
aliases:
- HackerTarget reverse DNS
tags:
- reverse-dns
- ptr
- dns
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Hacker Target - Reverse DNS

> A hosted reverse-DNS/PTR lookup: give it an IP (or range) and it returns the domain names that point back to it.

## When to use
You have an `ip-address` — from mail headers, a server log, a WHOIS record, or a hosting lookup — and want to know which domains resolve to it. Reverse DNS helps attribute an IP to a person's or organization's web/mail infrastructure and can surface co-hosted domains worth pivoting on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://hackertarget.com/reverse-dns-lookup/.
2. Enter the target `ip-address` (or an IP range) and run the lookup.
3. Read the returned PTR records / associated `domain` names.
4. For scripting, hit the free API: `https://api.hackertarget.com/reversedns/?q=<IP>` (rate-limited unauthenticated; add a key for higher limits).
5. Pivot: a returned domain feeds WHOIS, passive-DNS, and subdomain enumeration; a shared-hosting IP with many unrelated domains is a caution flag against over-attributing it to your subject.

## Inputs → Outputs
- **In:** `ip-address` (single or range)
- **Out:** `domain`(s) / PTR records mapped to that IP
- **Empty/negative result looks like:** no PTR record returned — the IP has no reverse DNS set (common for residential/dynamic IPs), which is itself a signal it may not be dedicated hosting.

## Gotchas & OpSec
- Reverse DNS is set by the IP owner and is often absent or generic (`ISP-pool-x.example.net`) — absence isn't proof of anything.
- The free API is rate-limited; heavy use needs a keyed/paid tier.
- OpSec: passive — the lookup runs on HackerTarget's side, nothing touches the target.

## Overlaps ("do both")
- Pair with forward-DNS/passive-DNS and WHOIS tools — reverse DNS gives you a candidate domain, those confirm ownership and history. Same-provider siblings: [[hacker-target]], [[hackertarget-com]].

## Trust & verifiability
`trust: community` — a reputable, long-established hosted tool; it simply relays public DNS, so accuracy depends on the current PTR configuration, not on HackerTarget itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hacker-target-reverse-dns |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
