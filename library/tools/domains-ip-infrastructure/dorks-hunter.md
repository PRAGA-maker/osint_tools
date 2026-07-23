---
id: dorks-hunter
name: Dorks Hunter
description: Use when you have a `domain` and want to auto-run a battery of Google dorks against it — returns exposed URLs, documents, login pages and error leaks (`domain`/`document-id`) worth chasing.
url: https://github.com/six2dez/dorks_hunter
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-command Google-dork sweep of a target domain for exposed files, panels and leaks.
selectorsIn:
- domain
selectorsOut:
- domain
- document-id
status: live
pricing: free
costNote: Free and open-source Python script (six2dez); no API key required for the core run.
opsec: active
opsecNote: The script fires many automated search-engine queries about the target domain from your IP. Google will throttle/CAPTCHA aggressive querying, and the searches themselves are attributable — run from a sock-puppet IP/VPN and pace the queries.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Part of the well-known six2dez recon tooling (reconftw author); widely used in bug-bounty/recon workflows, code is public.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- dorks_hunter
- six2dez/dorks_hunter
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- google-dorks
- recon
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- reconftw
---

# Dorks Hunter

> A one-command Google-dork runner: point it at a domain and it sweeps for exposed files, login pages and error leaks automatically.

## When to use
You have a target `domain` and want the low-hanging exposed surface without typing dozens of `site:` dorks by hand. Dorks Hunter runs a curated battery of Google dorks — backup files, database dumps, exposed documents, sub-subdomains, login/admin panels, SQL/PHP error pages — and collects the hits. Useful for quickly finding leaked documents, forgotten portals and misconfigurations tied to a person's or organisation's domain.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/six2dez/dorks_hunter && cd dorks_hunter && pip install -r requirements.txt` (Python 3.8+; also installs its dork backend).
2. Run against a domain: `python3 dorks_hunter.py -d example.com -o results.txt`.
3. Let it iterate the dork categories; results print to the terminal and save to the output file.
4. Review the hits — each is a live Google result URL worth opening manually.
5. Pivot: exposed documents feed metadata/`document-id` analysis; discovered subdomains and panels feed further infrastructure recon (e.g. `[[reconftw]]`).

## Inputs → Outputs
- **In:** a target `domain`
- **Out:** categorised search hits — exposed `document-id`/files, backup/DB files, login pages, error leaks, extra sub-subdomains (`domain`)
- **Empty/negative result looks like:** few or no results — either the domain is clean, or (more often) Google rate-limited/CAPTCHA'd the run; slow down, change IP, and retry before assuming clean.

## Gotchas & OpSec
- Human-in-the-loop: Google throttles and CAPTCHAs automated dorking; you'll need to pace queries and possibly rotate IPs.
- Results are only as fresh as Google's index and can include stale/cached pages — verify each hit manually.
- OpSec: **active** — you are querying a search engine repeatedly about the target from your IP; use a sock-puppet VPN and don't hammer it.

## Overlaps ("do both")
- Pairs with `[[reconftw]]` (same author ecosystem) — Dorks Hunter finds indexed exposures via search engines, while reconftw enumerates the live attack surface directly; together they cover indexed and unindexed assets.

## Trust & verifiability
`trust: community` — an open, widely-used script from the reputable six2dez recon toolset; it only surfaces what search engines already index, so treat each hit as a lead to verify at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dorks-hunter |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (rate-limit) |
