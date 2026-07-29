---
id: fierce
name: Fierce
description: Use when you have a `domain` and want to discover its subdomains and non-contiguous IP space via DNS reconnaissance — returns domain, ip-address.
url: https://github.com/mschwager/fierce
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: DNS recon — subdomain and non-contiguous IP-space discovery for a domain.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (GPL); install via pip (`pip install fierce`) or use the copy bundled in Kali/pentest distros.
opsec: active
opsecNote: Active — Fierce sends DNS queries and can brute-force subdomains against the target's name servers, generating traffic that shows in their DNS logs. Only run it against domains you're authorised to enumerate, and consider running from a disposable VPS rather than your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: A classic, long-standing DNS reconnaissance tool bundled in Kali; open-source, so its behaviour is auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- fierce
- mschwager/fierce
tags:
- dns
- subdomains
- recon
source: gh-topic-footprinting
lastVerified: '2026-07-29'
enrichment: full
---

# Fierce

> A command-line DNS reconnaissance tool that walks a domain's name servers to find subdomains and the scattered IP ranges an organisation actually uses — a fast footprinting first step.

## When to use
You have a `domain` (a subject's business or organisation) and want to map its **DNS footprint**: which subdomains exist and what IP space they resolve to, including non-contiguous ranges you wouldn't guess from the main site's IP. Each discovered host/IP is a fresh pivot — more infrastructure to fingerprint, more content to search, and a sense of how big the target's online presence is.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install fierce` (or use the version in Kali).
2. Run against a domain: `fierce --domain example.com`.
3. Optionally supply a wordlist for subdomain brute-forcing (`--subdomains` / `--subdomain-file`) and tune DNS servers with `--dns-servers`.
4. Read the output: discovered hostnames, their IPs, and nearby IP-space hints.
5. Pivot: resolved IPs feed `[[bgpview-io]]` for ownership; discovered subdomains feed content search and history lookups; cross-check with a passive aggregator like `[[subdomainradar-io]]`.

## Inputs → Outputs
- **In:** `domain`
- **Out:** sub`domain`s and their resolved `ip-address`es, plus non-contiguous IP-range indicators
- **Empty/negative result looks like:** only the apex and `www` resolve, or brute-forcing finds nothing — a small footprint, a domain fully behind a CDN, or a name server that resists enumeration (not proof there's nothing there).

## Gotchas & OpSec
- **Active and logged:** brute-forcing subdomains hammers the target's DNS; it's noisy and attributable to your IP. Get authorisation and run from a VPS.
- Results depend on the wordlist and DNS behaviour; combine with passive sources for coverage.
- CDN/wildcard DNS can produce misleading resolutions — validate that discovered hosts are really distinct.

## Overlaps ("do both")
- Pairs with `[[subdomainradar-io]]` and certificate-transparency search — Fierce actively probes DNS while those pull from passive datasets, and each surfaces hosts the other misses.
- Feeds `[[bgpview-io]]` for the network/owner behind discovered IPs.

## Trust & verifiability
`trust: trusted` — a well-known open-source recon tool; its findings are live DNS facts you can re-resolve independently to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fierce |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
