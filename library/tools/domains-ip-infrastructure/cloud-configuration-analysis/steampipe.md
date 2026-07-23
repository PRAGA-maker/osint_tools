---
id: steampipe
name: Steampipe
description: Use when you want to query cloud accounts, SaaS, and OSINT APIs with SQL — returns tabular results (domains, IPs, org/infra metadata) from live provider data via plugins.
url: https://github.com/turbot/steampipe
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- cloud-configuration-analysis
bestFor: Running SQL against cloud/SaaS/OSINT APIs (via plugins) to inventory and cross-reference infrastructure at scale.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Core CLI is free and open-source (AGPL 3.0); Turbot Pipes is the optional paid cloud/team service. Most OSINT plugins (whois, dns, shodan, censys, crtsh, virustotal) are free (some need your own API key).
opsec: active
opsecNote: Depends on the plugin. Passive OSINT plugins (whois/dns/crtsh) don't touch the target, but net/http/nmap-style or authenticated cloud plugins actively query targets or your own accounts. Know which plugin you're running and route active queries through infrastructure you control.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: trusted
trustNote: Actively maintained open-source project by Turbot (thousands of stars, frequent releases); code and plugins are public and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- turbot steampipe
tags:
- cloud
- sql
- infrastructure
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Steampipe

> "SQL for APIs" — query cloud accounts, SaaS, and OSINT services through plugins and join the results like database tables.

## When to use
You want to inventory or cross-reference infrastructure programmatically: enumerate a cloud account's assets, or pull OSINT data (WHOIS, DNS, certificate transparency, Shodan/Censys) and JOIN it in SQL. For OSINT specifically, its `whois`, `net`/`dns`, `crtsh`, `shodan`, `censys`, and `virustotal` plugins turn a `domain`/`ip-address` into structured, queryable results. It's infrastructure/security tooling, not people-search.

## How to use it (`bestInteractionPattern`: cli)
1. Install the CLI (`brew install turbot/tap/steampipe` or the install script) — a single Go binary.
2. Install the plugins you need: `steampipe plugin install whois net crtsh shodan` (add API keys in the plugin config where required).
3. Start querying: `select * from whois_domain where domain = 'example.com';` or `select * from crtsh_certificate where domain = 'example.com';`.
4. JOIN across plugins to correlate (e.g. certs → resolved IPs → Shodan services) and export to CSV/JSON.
5. Pivot: results feed the same follow-ups as their underlying sources ([[certkit-certificate-transparency-log-search]], [[ipvoid]], [[whois-arin]]).

## Inputs → Outputs
- **In:** SQL queries plus a `domain`/`ip-address` (and any needed API keys); or cloud credentials for infra inventory.
- **Out:** tabular results — `domain`s, `ip-address`es, certificates, service banners, org/asset metadata — joinable in SQL.
- **Empty/negative result looks like:** an empty result set (no matching records, or a plugin missing its API key/permission) — check the plugin config before concluding the data doesn't exist.

## Gotchas & OpSec
- **Know your plugin's opsec:** passive OSINT plugins are safe, but active/network or authenticated-cloud plugins reach out to targets or accounts — this is why it's marked `active`.
- Many plugins need your own API keys and inherit those services' rate limits and terms.
- It's power-user tooling — SQL fluency and plugin setup are prerequisites.

## Overlaps ("do both")
- Wraps sources you may also use directly ([[certkit-certificate-transparency-log-search]], [[ipvoid]], [[whois-arin]]): Steampipe's value is joining them in one SQL workflow at scale, versus one-off manual lookups.

## Trust & verifiability
`trust: trusted` — actively maintained, widely-used open-source project; every result traces to a public plugin querying an authoritative upstream source you can re-check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steampipe |
