---
id: aiodnsbrute
name: aiodnsbrute
description: Use when you have a domain and want to enumerate its live subdomains fast — returns domain (subdomains) and their ip-address records.
url: https://github.com/blark/aiodnsbrute
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: High-speed asynchronous subdomain brute-forcing to map an organization's or subject's web infrastructure.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (Python, pip-installable); no account or key.
opsec: active
opsecNote: This is ACTIVE recon — it fires thousands of DNS queries whose answers (and, for resolved hosts, follow-on traffic) touch the target's and resolvers' logs. Route through a resolver/VPN you control, throttle the rate, and never point it at infrastructure you are not authorized to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Established, well-starred open-source DNS tool (blark/aiodnsbrute); community-maintained rather than vendor-backed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- aio dns brute
tags:
- dns
- subdomain
- recon
source: gh-topic-osint-resources
lastVerified: '2026-07-23'
enrichment: full
---

# aiodnsbrute

> A fast asyncio-based DNS brute-forcer: throw a wordlist at a domain and get back the subdomains that actually resolve, with their IPs.

## When to use
You have a `domain` (a company, a personal vanity domain, a project) and want to discover its non-obvious subdomains — `mail.`, `vpn.`, `dev.`, `staging.`, internal-looking hosts — to widen the infrastructure picture. This is infrastructure recon that maps an org's attack/footprint surface; it does not identify a person and is not a people-search step.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install aiodnsbrute` (Python 3).
2. Run against the target zone: `aiodnsbrute -w wordlist.txt example.com` — it asynchronously resolves `word.example.com` for every entry.
3. Tune concurrency/`-t` and supply a good wordlist for coverage vs. speed; results list each resolving subdomain and its A/AAAA `ip-address`.
4. Export findings and feed resolved hosts into further checks (WHOIS, reverse-DNS, port/service tooling).
5. Pivot: a discovered `ip-address` → reverse-DNS/geolocation; a discovered `domain` → certificate-transparency or WHOIS enrichment.

## Inputs → Outputs
- **In:** a base `domain` plus a subdomain wordlist.
- **Out:** the subset of guessed `domain`s that resolve, each with its `ip-address`(es).
- **Empty/negative result looks like:** all guesses NXDOMAIN (nothing resolves) — either the zone is sparse, uses wildcard DNS (everything resolves, a false positive to filter), or your resolver is rate-limiting. Wildcard responses should be detected and discarded.

## Gotchas & OpSec
- Brute-forcing only finds names in your wordlist — pair it with passive sources (certificate transparency) to catch the rest.
- Wildcard DNS makes every guess "resolve"; verify hits independently before trusting them.
- High query volume is loud and can trip rate limits or IDS — this is **active**, so use authorized targets and a resolver you control.

## Overlaps ("do both")
- Pairs with passive subdomain sources (crt.sh / certificate transparency): brute-forcing finds guessable hosts, passive sources find historically-seen ones — the union is far more complete than either alone.

## Trust & verifiability
`trust: community` — mature open-source project, but community-maintained; every result is directly verifiable by re-resolving the name yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aiodnsbrute |
