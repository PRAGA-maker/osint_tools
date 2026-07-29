---
id: hosthunter
name: HostHunter
description: Use when you have one or more `ip-address` targets and want the virtual hostnames served on them — returns discovered FQDNs/hostnames (plus optional screenshots) mapped to each IP.
url: https://github.com/SpiderLabs/HostHunter
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Turning a list of IPs into the hostnames/virtual hosts they serve, using SSL-cert and passive OSINT sources, for reverse-IP and attack-surface mapping.
selectorsIn:
- ip-address
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (MIT). Python 3 CLI; no paid tier. Some enrichment sources may want free API keys.
opsec: active
opsecNote: By default HostHunter pulls hostnames from passive sources (SSL certificates, reverse DNS, third-party APIs), but its screenshot/verify features actively connect to the target IPs — which touches the target's infrastructure and can be logged. Run reconnaissance-only mode for passive use, or route active checks through a sock-puppet host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by Trustwave SpiderLabs (a reputable security team); popular, MIT-licensed, actively developed. Community-trusted but still a third-party recon tool — verify hostnames it returns.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- hostil1y-hakrevdns
- shodan
- crt-sh
aliases:
- HostHunter SpiderLabs
- hosthunter.py
tags:
- Domain/IP/Links
- Domain/IP investigation
- reverse-ip
- hostname-discovery
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# HostHunter

> A Python recon tool by Trustwave SpiderLabs that maps IP addresses to the virtual hostnames they serve — reverse-IP discovery driven by SSL certs and OSINT, with optional endpoint screenshots.

## When to use
You have an `ip-address` (or a whole file of them — a netblock, a set of resolved IPs, a target's hosting range) and you need to know which hostnames/domains actually live on each. HostHunter extracts hostnames from SSL certificates, reverse DNS, and OSINT sources, and can screenshot the HTTP(S) endpoints, giving you a fast attack-surface / infrastructure map. It's a domain-infra tool; for a missing-persons case it matters only when a subject's server/hosting is in scope.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/SpiderLabs/HostHunter && pip3 install -r requirements.txt`.
2. Put your target IPs (one per line) in `targets.txt`.
3. Run: `python3 hosthunter.py targets.txt -f csv -o results.csv` (use `-t <ip>` for a single IP, `-g` to pick SSL ports, `-v` to verify).
4. Read the output CSV/TXT: each IP is mapped to the hostnames/FQDNs found, with optional screenshots saved locally (`screen_capture` mode) and a Nessus-format export if you asked for it.
5. Pivot: feed discovered `domain`s into `[[crt-sh]]` (more certs → more subdomains) and `[[shodan]]` (what services those hosts run), then WHOIS for ownership.

## Inputs → Outputs
- **In:** `ip-address` (single via `-t`, or a `targets.txt` list).
- **Out:** `domain` — hostnames/FQDNs mapped per IP, optionally with endpoint screenshots.
- **Empty/negative result looks like:** an IP resolves to no hostnames (bare/parked host, no SSL cert, no PTR record) — that's a genuine "nothing served here by name," not a tool failure.

## Gotchas & OpSec
- Human-in-the-loop: none — it's scripted CLI.
- OpSec: **active** when using verify/screenshot modes (it connects to the target IPs and can appear in their logs). For a purely passive footprint, stick to cert/OSINT extraction and skip live verification, or run active steps from a sock-puppet host/VPS.
- Depends on external sources whose availability and rate limits change; a thin result may mean a source was down, not that hostnames don't exist.
- Screenshots and hostnames are point-in-time; virtual hosting changes, so re-run for current state.

## Overlaps ("do both")
- Pairs with `[[crt-sh]]` — certificate transparency logs surface additional subdomains/hostnames that HostHunter's live cert grab may miss; run both to widen coverage.
- Overlaps with `[[shodan]]` and reverse-DNS tools like `[[hostil1y-hakrevdns]]` — Shodan tells you what's *running* on the hosts you discover.

## Trust & verifiability
`trust: community` — maintained by Trustwave SpiderLabs, MIT-licensed and widely used, but it's still an aggregator of third-party recon data. Confirm any hostname→IP mapping with an independent DNS/cert lookup before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hosthunter |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
