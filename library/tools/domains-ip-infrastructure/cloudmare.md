---
id: cloudmare
name: Cloudmare
description: Use when you have a `domain` behind Cloudflare/Sucuri/Incapsula and want to uncover its real origin server IP via DNS/history misconfigurations — returns ip-address, domain.
url: https://github.com/MrH0wl/Cloudmare
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Finding the origin server IP hidden behind a CDN/WAF (Cloudflare, Sucuri, Incapsula).
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free and open-source (Python CLI). Some data-source lookups (e.g. SecurityTrails/Shodan) work better with free API keys added to the config.
opsec: active
opsecNote: Cloudmare queries historical DNS, cert transparency, subdomains, and can directly probe candidate IPs to confirm the origin — that verification traffic hits the target's real server and may be logged there. Run passive-only sources first; use a VPN/disposable host before any confirmation probes.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by MrH0wl. Community-maintained; effectiveness depends entirely on the target having a real misconfiguration (leaked historical IP, exposed subdomain), so results are opportunistic.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- domain-dossier
- dnsdumpster
- shodan
tags:
- Domain/IP/Links
- Cloudfare
- origin-ip
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Cloudmare

> A CLI that tries to strip away Cloudflare/Sucuri/Incapsula and reveal a site's real origin-server IP by exploiting DNS history and misconfigurations.

## When to use
You have a `domain` fronted by a CDN/WAF and need the true hosting `ip-address` — for example to geolocate the real server, find co-hosted sites, or move past the CDN's anonymity. Infrastructure-focused; low relevance to a person-centric case unless the subject runs a hidden site.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install requirements (Python).
2. (Optional) add free API keys (SecurityTrails, Shodan, etc.) to the config to widen the source coverage.
3. Run against the target: `python cloudmare.py -u <domain>` (add subdomain brute/scan flags as needed).
4. Read output: candidate origin IPs (from historical DNS records, cert transparency, and direct subdomains) and any that verify as the true backend.
5. Pivot: a confirmed origin `ip-address` → `[[shodan]]`/reverse-IP to find co-hosted domains and open services; geolocate the host.

## Inputs → Outputs
- **In:** `domain` (CDN-fronted)
- **Out:** `ip-address` (candidate/confirmed origin server), plus related `domain`s/subdomains
- **Empty/negative result looks like:** only CDN edge IPs returned and no candidate origin — meaning the target is correctly configured (no leaked history, origin firewalled to CDN only). That's a real negative, not a tool failure.

## Gotchas & OpSec
- Success is **entirely opportunistic**: it only works if the target leaked its IP historically or exposes a non-proxied subdomain. A clean target yields nothing.
- The confirmation step actively connects to candidate IPs — that traffic reaches the real server and can be logged. Keep to passive sources unless you accept that exposure.
- API keys materially improve results; without them coverage is thin.

## Overlaps ("do both")
- Pairs with `[[dnsdumpster]]` and `[[domain-dossier]]` for the passive DNS/subdomain groundwork, and with `[[shodan]]` to validate and enrich a discovered origin IP.

## Trust & verifiability
`trust: community` — an open-source tool; inspect the code before running. Treat unconfirmed candidate IPs as leads and verify (e.g. host header check) before asserting an origin.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloudmare |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
