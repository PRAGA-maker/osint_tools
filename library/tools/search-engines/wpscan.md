---
id: wpscan
name: WPScan
description: Use when you have a `domain` running WordPress and want to enumerate its author users, plugins and version — returns `username` handles and site fingerprint.
url: https://wpscan.com
category: search-engines
path:
- search-engines
bestFor: Enumerating WordPress author usernames and the plugin/theme stack of a target site.
selectorsIn:
- domain
selectorsOut:
- username
- name
status: live
pricing: freemium
costNote: The CLI scanner is free and open source (GPL). The vulnerability-database API has a free tier of 25 requests/day; higher volume is paid. You do not need the API to enumerate users.
opsec: active
opsecNote: Scanning sends many HTTP requests directly to the target's web server from your IP; it appears in their access logs and can trip WAF/rate limits. Only scan sites you are authorised to test, or route through a VPN/sock-puppet host. User enumeration alone is lightweight but still logged.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by Automattic (owners of WordPress.com); the scanner is widely used and open source.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools: []
aliases:
- wpscan cli
- WordPress security scanner
tags:
- speciality-search-engines
- wordpress
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# WPScan

> A black-box WordPress scanner whose OSINT value is author-username enumeration: it turns a WordPress `domain` into the login handles (and often display names) of the people who post on it.

## When to use
You have a `domain` that runs WordPress and you want to know who writes for it. WordPress exposes author archives (`/?author=1`, `/wp-json/wp/v2/users`), and WPScan harvests these into a list of usernames and display names — a direct pivot from a blog to the real people behind it. Also use it to fingerprint the site's WordPress core version, plugins and themes when profiling infrastructure.

## How to use it (`bestInteractionPattern`: cli)
1. Install the scanner: `gem install wpscan` (or run the official Docker image `wpscanteam/wpscan`).
2. Enumerate users: `wpscan --url https://target.com --enumerate u`. This lists author IDs, login slugs (`username`) and public display names (`name`).
3. Optionally add plugin/theme enumeration: `--enumerate ap,at,vp`. Supplying a free API token via `--api-token <token>` cross-references findings against the vulnerability database.
4. Read the output: the `[i] User(s) Identified` block is the OSINT payload — each entry is a login handle to pivot on.
5. Pivot: feed harvested `username` values into username-search tooling to find the same handle on other platforms; feed a display `name` into people search.

## Inputs → Outputs
- **In:** `domain` (a WordPress site)
- **Out:** `username` (author login slugs), `name` (display names), plus site version/plugin fingerprint
- **Empty/negative result looks like:** "The URL supplied seems to be down" or no `User(s) Identified` block — the site may not be WordPress, may block REST/author endpoints, or may sit behind a WAF that dropped the scan.

## Gotchas & OpSec
- Human-in-the-loop: register a free account to obtain an API token if you want vulnerability data; user enumeration works without one.
- OpSec: this is **active** — requests hit the target's server from your IP and are logged. Scan only with authorisation; otherwise proxy through a disposable host.
- Hardened sites disable author enumeration and the REST users endpoint; a clean result is not proof of no authors.

## Overlaps ("do both")
- Pairs with any `username`-pivot tool: WPScan produces the handle, those confirm where else it exists.

## Trust & verifiability
`trust: trusted` — the scanner is open source and maintained by Automattic; output is drawn live from the target's own endpoints, so usernames are authoritative for that site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wpscan |
| category | search-engines |
| selectorsIn → selectorsOut | domain → username, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
