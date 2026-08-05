---
id: cdnstrip
name: CDNStrip
description: Use when you have a list of IP addresses and want to separate CDN/WAF-fronted IPs from real origin IPs — returns two lists (CDN vs non-CDN) so you can focus on true hosts.
url: https://github.com/j3ssie/cdnstrip
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Filtering a bulk IP list down to non-CDN origin addresses worth investigating.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free and open-source (MIT); build/run locally, no account or key.
opsec: passive
opsecNote: Passive — classification uses the ProjectDiscovery cdncheck data (known CDN/WAF ranges) and does not connect to the target IPs, so it leaks nothing to them. It merely sorts a list you already have.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small open-source Go utility by a known offensive-tooling author (j3ssie), built on ProjectDiscovery's maintained cdncheck library; the classification is only as current as that CDN-range dataset.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- metabigor
aliases:
- cdnstrip
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- cdn
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# CDNStrip

> A fast Go filter that splits a list of IPs into "behind a CDN/WAF" versus "probably the real host" — so you stop chasing Cloudflare edge nodes and focus on origin infrastructure.

## When to use
You have resolved a set of domains or subdomains to `ip-address`es and need to know which ones are just CDN/WAF front-ends (Cloudflare, Akamai, Fastly, etc.) and which are genuine origin servers. Cleaning CDN noise out of a bulk IP list before deeper infrastructure OSINT — reverse-IP, port scanning, host attribution — is where this saves time.

## How to use it (`bestInteractionPattern`: cli)
1. Install: clone `github.com/j3ssie/cdnstrip` and build with Go (`go install`/`go build`), or grab a release binary.
2. Pipe your IP list into it: `cat ips.txt | cdnstrip -cdn cdn.txt -n non-cdn.txt`.
3. Read the output: `non-cdn.txt` holds the addresses NOT matching known CDN/WAF ranges (your origin candidates); `cdn.txt` holds the CDN-fronted ones.
4. Feed `non-cdn.txt` into your next step — reverse-IP/PTR, port scan, or host lookup — since those addresses are more likely to be the true server.
5. Treat the split as a filter, not proof: a "non-CDN" IP is a candidate origin, still to be verified.

## Inputs → Outputs
- **In:** a list of `ip-address`es (stdin or file)
- **Out:** two `ip-address` lists — CDN/WAF vs non-CDN (origin candidates)
- **Empty/negative result looks like:** an empty non-CDN list means every input IP matched a known CDN/WAF range (the real origin is hidden behind the CDN and you'll need another technique to find it); an empty CDN list means none were recognised as CDN — possibly because the dataset lacks that provider.

## Gotchas & OpSec
- Accuracy depends entirely on the cdncheck range dataset; new or niche CDNs/WAFs may be misclassified as origins.
- It classifies IPs you provide — it does NOT discover the hidden origin behind a CDN; pair it with origin-finding techniques for that.
- Requires a Go toolchain / local install; not a hosted service.
- OpSec: passive and offline against the targets — no packets go to the IPs during classification.

## Overlaps ("do both")
- Pairs with `[[metabigor]]` and reverse-IP/ASN tooling: use those to gather and enrich IPs, then CDNStrip to prune the CDN noise before the expensive per-host work.

## Trust & verifiability
`trust: community` — a small, transparent open-source utility over a maintained CDN-range library; verify a "non-CDN" classification (e.g. by checking the ASN/PTR) before treating an IP as a confirmed origin.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cdnstrip |
