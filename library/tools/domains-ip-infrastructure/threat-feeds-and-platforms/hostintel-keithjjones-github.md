---
id: hostintel-keithjjones-github
name: hostintel - keithjjones Github
description: Use when you have an `ip-address` or `domain` and want to bulk-enrich it against many reputation/geolocation feeds at once — returns geolocation, resolved hosts, and threat-reputation data as CSV.
url: https://github.com/keithjjones/hostintel
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Bulk host enrichment — feed a list of IPs/domains and get a merged CSV of geo, DNS and reputation from several sources.
selectorsIn:
- ip-address
- domain
selectorsOut:
- geolocation
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (CC BY-SA 4.0). You supply your own free-tier API keys for the sources you enable.
opsec: passive
opsecNote: Enrichment queries third-party reputation APIs, not the target host, so the target host itself is not touched. But every IP/domain you submit is disclosed to VirusTotal, Shodan, Censys, PassiveTotal, OTX, ISC, etc.; use dedicated research API keys not tied to your identity, and assume those providers log your queries.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Independent open-source project by security researcher Keith J. Jones; ~150 commits, no formal releases. Read the code before running.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- hostintel
- keithjjones hostintel
tags:
- host-enrichment
- threat-intel
- csv
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# hostintel - keithjjones Github

> A modular Python CLI that fans a list of IPs/domains out across several intelligence feeds and merges the answers into one CSV.

## When to use
You have one or many `ip-address` / `domain` values (e.g. infrastructure pulled from an email header, a scam site, or the servers a subject's accounts touched) and want a single consolidated enrichment table instead of pasting each host into ten web lookups. Best when you already hold free API keys for the underlying services.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/keithjjones/hostintel && cd hostintel && pip install -r requirements.txt`.
2. Copy the example config and add your API keys (VirusTotal, Shodan, Censys, PassiveTotal, OTX/AlienVault, ISC). GeoLite2 geolocation and plain DNS work with no key.
3. Put one IP/FQDN/domain per line in an input file.
4. Run `python hostintel.py config.conf inputfile.txt -a > output.csv` (flags select which modules run; `-a` = all configured).
5. Open the CSV in a spreadsheet and pivot on geolocation, resolved hosts, and reputation hits to cluster related infrastructure.

## Inputs → Outputs
- **In:** `ip-address` (IPv4), `domain`, or FQDN — one per line.
- **Out:** CSV rows of `geolocation` (city/country/ASN), resolved `domain`/`ip-address`, and per-source reputation/threat verdicts.
- **Empty/negative result looks like:** blank cells for a given source column (no data or missing key for that module) — not proof the host is clean, just that that feed had nothing.

## Gotchas & OpSec
- Human-in-the-loop: you must register for and paste each source's API key; free tiers impose rate limits, so large input files can stall or partially fail.
- IPv4 only; IPv6 and bare hostnames without DNS records return empty.
- The project is old (Python 2/3 era) — pin dependencies in a venv and expect some modules to need patching.

## Overlaps ("do both")
- Pairs with a live-recon framework like `[[recon-ng]]` — hostintel is a one-shot batch enricher, while recon-ng lets you iteratively expand and store results in a workspace.

## Trust & verifiability
`trust: community` — a single-maintainer open-source repo with no releases; the data is only as good as the third-party feeds behind it, and you should audit the code before feeding it sensitive selectors.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hostintel-keithjjones-github |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → geolocation, domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
