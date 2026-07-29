---
id: dnspop
name: dnspop
description: Use when you have a `domain` and want the most effective subdomain-guessing wordlists — returns ranked lists of common subdomain labels for brute-forcing.
url: https://github.com/bitquark/dnspop
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Seeding subdomain brute-force tools with data-driven "most popular subdomain" wordlists.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open-source on GitHub; download the prebuilt wordlists or run the scripts. No account.
opsec: passive
opsecNote: The wordlists and analysis scripts are inert — building or reading them touches no target. The brute-force you feed them into (against a subject's domain) does send DNS queries and, if the resolver is the target's, may be observable. Prefer a public/passive resolver first; treat active enumeration as mildly noisy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Created by bitquark from analysis of large domain datasets; the "popular subdomains" list is widely used and bundled into other recon tools. Data is a few years old but subdomain naming conventions are durable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- seclists-dns-subdomains
- amass
- subfinder
aliases:
- bitquark dnspop
- popular-subdomains
tags:
- wordlist
- subdomain-enumeration
- dns-recon
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# dnspop

> Data-driven subdomain wordlists — bitquark analysed huge datasets to rank the subdomain labels that actually occur most, so a brute-force finds hosts faster.

## When to use
You are mapping a subject's `domain` and want to discover its subdomains (mail, vpn, dev, staging, admin, internal apps) by brute-force. dnspop gives you a high-yield wordlist ordered by real-world frequency, so a shorter run hits more live hosts than a generic list. Use it to expand attack surface and find non-obvious infrastructure tied to a person or org.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/bitquark/dnspop` and use the prebuilt lists in `results/` (e.g. the popular-subdomains list), or run its scripts to build your own from a dataset.
2. Feed a list into a subdomain brute-forcer: `amass enum -brute -w results/bitquark_20160227_subdomains_popular_1000 -d target.example`, or use it with `subfinder`, `gobuster dns`, `massdns`, etc.
3. Resolve candidates and keep the ones that return records; validate they belong to the target (not wildcard/parked responses).
4. Enrich: run discovered hosts through infrastructure/service tools.
5. Pivot: new subdomains feed `[[amass]]`/`[[subfinder]]` passive enrichment and `[[shodan]]`-style service scans.

## Inputs → Outputs
- **In:** `domain` (target to enumerate against)
- **Out:** additional `domain`s (live subdomains) discovered via the wordlist
- **Empty/negative result looks like:** all guesses NXDOMAIN or all resolving to one wildcard IP — the domain has few brute-forceable subdomains or uses a wildcard; switch to passive sources (CT logs) instead.

## Gotchas & OpSec
- Watch for wildcard DNS: a domain that answers every label will produce false positives — detect and filter wildcards first.
- The lists are a snapshot (mid-2010s) but subdomain naming is stable; pair with passive sources for coverage of unusual names.
- Brute-forcing is active DNS traffic; use a public resolver and reasonable rate to stay quiet.

## Overlaps ("do both")
- Pairs with `[[seclists-dns-subdomains]]` (broader/larger lists) and passive tools `[[amass]]` / `[[subfinder]]`. Do both: passive enumeration for known hosts, dnspop brute-force for the ones only guessing will reveal.

## Trust & verifiability
`trust: community` — a well-regarded, widely reused wordlist from a known researcher. Results are self-verifying (a subdomain either resolves or not); confirm ownership before treating a host as the subject's.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnspop |
