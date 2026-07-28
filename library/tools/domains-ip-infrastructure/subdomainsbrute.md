---
id: subdomainsbrute
name: SubDomainsBrute
description: Use when you have a `domain` and want to enumerate its live subdomains fast via dictionary brute-force — returns discovered subdomain `domain`s and their `ip-address`es.
url: https://github.com/lijiejie/subDomainsBrute
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast, high-concurrency subdomain brute-forcing to map an organization's web footprint.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free, open-source Python CLI (MIT); no account or key.
opsec: active
opsecNote: Brute-forcing sends a large volume of DNS queries to public resolvers to resolve candidate names — it does not hit the target's own servers directly, but the query burst is noisy and can be rate-limited or logged by the resolvers you use. Run from a sock-puppet host and throttle if you need to stay quiet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Popular community pentest tool by lijiejie (thousands of GitHub stars); widely used but unaudited, so validate discovered hosts before acting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- subDomainsBrute
- lijiejie subdomain brute
tags:
- Domain/IP/Links
- Subdomains scan/brute
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# SubDomainsBrute

> A fast Python CLI that dictionary-brute-forces subdomains at high concurrency — feed it a domain, get back the live hosts and their IPs in seconds.

## When to use
You have a `domain` (an organization, a subject's personal site, a business tied to your case) and want to map its wider web footprint by discovering subdomains that aren't linked anywhere public — dev/staging panels, mail hosts, VPN gateways, legacy apps. Those hosts often expose additional infrastructure, contact points, or misconfigurations worth pivoting on.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/lijiejie/subDomainsBrute && cd subDomainsBrute && pip install -r requirements.txt` (needs Python 3.8+).
2. Run: `python subDomainsBrute.py example.com` (add `-t` to tune concurrency, `-f wordlist.txt` for a custom dictionary).
3. It resolves candidate names concurrently, detects wildcard DNS, and pulls names from HTTPS certificates; results are written to `example.com.txt`.
4. Read the output: each line is a live subdomain plus its resolved `ip-address`.
5. Pivot: feed discovered hosts into WHOIS/ASN, port-scan, or historical-DNS tools; group by IP to find shared hosting.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` (live subdomains), `ip-address` (their resolved addresses), written to a text file
- **Empty/negative result looks like:** an empty/near-empty output file means few brute-forceable names resolved — try a larger wordlist or a passive source; it does not prove the domain has no other hosts.

## Gotchas & OpSec
- **Active and noisy:** the query burst can be throttled or logged by the resolvers. Throttle concurrency and use a disposable host if stealth matters.
- Brute-force only finds names in your wordlist — combine with passive certificate-transparency/DNS sources to catch the rest.
- Wildcard DNS can produce false positives; the tool tries to detect it, but verify surprising hits manually.

## Overlaps ("do both")
- Pairs with passive subdomain sources (certificate transparency, DNS aggregators) — do both, because brute-force finds guessable names the passive sources miss and vice versa.

## Trust & verifiability
`trust: unverified` — a widely used community pentest tool, but unaudited; the *results* are live DNS resolutions you can re-verify independently, so confirm each discovered host before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | subdomainsbrute |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
