---
id: cloudunflare
name: CloudUnflare
description: Use when a target `domain` sits behind Cloudflare and you want to find its real origin `ip-address` — returns candidate origin IPs and historical DNS records.
url: https://github.com/greycatz/CloudUnflare
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reconnaissance to uncover the origin server IP hidden behind Cloudflare via historical DNS.
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free and open source (BSD); requires a free CompleteDNS account for the historical-DNS API it queries.
opsec: active
opsecNote: The script queries the CompleteDNS API and resolves records; if you then connect to a discovered origin IP to confirm it, that contact comes from your IP and can be logged by the target. Verify candidate origins from a disposable IP, and never treat an unmasked origin as licence to attack it.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source bash script (greycatz); results are only as good as the historical-DNS data source and require manual verification of each candidate IP.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: true
relatedTools: []
aliases:
- CloudUnflare
- Cloudflare bypass recon
tags:
- Domain/IP/Links
- Cloudfare
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# CloudUnflare

> A bash reconnaissance script that hunts for the real origin IP behind a Cloudflare-fronted domain by mining historical DNS records.

## When to use
A target `domain` is proxied through Cloudflare, so a normal DNS lookup only returns Cloudflare's IPs and hides where the site is actually hosted. CloudUnflare tries to recover the origin `ip-address` — the true host — by pulling historical DNS records (from before Cloudflare was enabled, or misconfigured subdomains that leak it), which can reveal the hosting provider and other infrastructure the operator controls.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/greycatz/CloudUnflare`.
2. Ensure `curl`, `dig` and `whois` are installed; create a free CompleteDNS account and put its credentials/API details into the script's config.
3. Run: `bash cloudunflare.bash` and enter the target domain when prompted.
4. Read the candidate origin IPs and historical records it returns.
5. **Verify** each candidate (e.g. request the site directly by IP with the Host header) from a disposable IP before believing it — historical records go stale.

## Inputs → Outputs
- **In:** a Cloudflare-fronted `domain`
- **Out:** candidate origin `ip-address`(es) and historical DNS `domain`/record data
- **Empty/negative result looks like:** a domain that has *always* been behind Cloudflare (no pre-proxy history, no leaking subdomains) yields no real origin — that means the technique didn't work here, not that no origin exists.

## Gotchas & OpSec
- Requires a CompleteDNS account/API access for the historical-DNS lookups (`humanInLoop: api-key`).
- Candidates are guesses from historical data — always confirm before relying on one; many will be stale or shared-hosting IPs.
- OpSec: **active** if you probe a candidate origin directly; do that only from a throwaway IP, and never use an unmasked origin to bypass protections or attack the host.

## Overlaps ("do both")
- Complements internet-scan engines and passive-DNS tools — those index certificates and historical resolutions that can independently corroborate a candidate origin CloudUnflare surfaces.

## Trust & verifiability
`trust: community` — an open-source script whose accuracy depends on a third-party historical-DNS source; every candidate origin must be manually verified, so treat outputs as leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloudunflare |
