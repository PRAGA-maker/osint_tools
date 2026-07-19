---
id: webdork
name: webdork
description: Use when you have a `domain` or `employer-org` and want to automate Google-dorking for exposed data — a Python CLI that runs dork queries to surface information disclosures.
url: https://github.com/HACKE-RC/webdork
category: search-engines
path:
- search-engines
bestFor: Automating a batch of Google dorks against a target domain/organization to find exposed files, tools and internal info.
selectorsIn:
- domain
selectorsOut:
- domain
- document-id
status: live
pricing: free
costNote: Free and open-source; Python 3.9+. Runs your searches through a normal search engine.
opsec: active
opsecNote: webdork issues automated search queries tied to your IP; heavy dorking can trip CAPTCHAs or rate limits and is attributable to whoever runs it. Use a proxy/VPN (it supports proxies), throttle, and only dork targets you are authorized to investigate — findings require manual verification and lawful handling.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An open-source OSINT dorking CLI (HACKE-RC/webdork) with an explicit ethical-use disclaimer. Community-maintained; results are raw search hits that must be verified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- HACKE-RC/webdork
tags:
- dorking
- cli
- osint
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# webdork

> A Python command-line tool that automates Google-dorking — fire a set of crafted queries at a target domain/organization to surface exposed files, backends, and internal info.

## When to use
You have a `domain` or `employer-org` and want to sweep for publicly-exposed but not-obvious material — misconfigured directories, leaked documents, internal tools, backup files — without hand-typing dozens of dork operators. webdork scripts that process, running the queries and collecting hits, which can reveal a target's infrastructure, exposed contact/personnel documents, and disclosures useful for pivoting.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install (Linux: `sudo python3 setup.py`; Termux/iSH variants provided); needs Python 3.9+.
2. Run it against the target with the desired flags — browser-search mode, verbose output, a proxy, and export-to-file are supported.
3. Review the returned search hits; every result requires manual verification before you rely on or act on it.
4. Refine the dorks for your target (domain, filetypes, keywords) and re-run to narrow disclosures.
5. Pivot: exposed documents (`document-id`) may carry `metadata-exif`; discovered subdomains/hosts feed infrastructure OSINT.

## Inputs → Outputs
- **In:** `domain` / `employer-org` (target to dork)
- **Out:** search hits → exposed `document-id`s, related `domain`s/subdomains, information disclosures
- **Empty/negative result looks like:** few or no hits — the target may be well-configured, or the search engine rate-limited/blocked you; adjust dorks, add a proxy, and retry.

## Gotchas & OpSec
- Human-in-the-loop: none to run, but findings are unverified search results — confirm each manually.
- OpSec: **active** — queries are attributable and can hit CAPTCHAs/rate limits. Use the proxy support, throttle, and stay within authorized scope; heed the repo's ethical-use disclaimer.
- It automates public search operators; it does not bypass access controls — treat "exposed" hits as leads, and handle any sensitive data lawfully.

## Overlaps ("do both")
- Pairs with manual operator references like [[bing-advanced-search-options]] and other dorking workflows — automation for breadth, manual dorks for precision.

## Trust & verifiability
`trust: community` — an auditable open-source tool; its output is raw search-engine hits, so verifiability comes from you checking each result at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webdork |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
