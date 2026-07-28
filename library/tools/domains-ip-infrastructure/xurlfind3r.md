---
id: xurlfind3r
name: xurlfind3r
description: Use when you have a `domain` and want every URL ever seen for it from passive archives (Wayback, Common Crawl, OTX, URLScan, etc.) — returns a deduplicated list of known URLs.
url: https://github.com/hueristiq/xurlfind3r
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Passively harvesting a domain's historically known URLs from multiple archive/threat-intel sources at once.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open-source Go CLI. Some sources (Intelligence X, URLScan, GitHub) return more when you add their free API keys.
opsec: passive
opsecNote: Fully passive — it pulls from third-party archives (Wayback, Common Crawl, AlienVault OTX, URLScan, IntelX) and never sends traffic to the target domain, so the subject sees nothing. Add API keys via config for fuller results.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained open-source tool by hueristiq (700+ stars); results are only as complete/fresh as the underlying archives.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- xurlfind3r
- hueristiq xurlfind3r
tags:
- Domain/IP/Links
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# xurlfind3r

> A fast Go CLI that gathers a domain's known URLs from passive sources — Wayback Machine, Common Crawl, AlienVault OTX, URLScan, Intelligence X, GitHub — without ever touching the target.

## When to use
You have a `domain` (a subject's site, a business, a suspicious host) and want to see everything about it that's been publicly indexed over time — old pages, endpoints, parameters, subdirectories, files. Great for surfacing deleted or unlinked content, mapping a site's history, and finding paths worth investigating, all passively.

## How to use it (`bestInteractionPattern`: cli)
1. Install (Go): `go install github.com/hueristiq/xurlfind3r/cmd/xurlfind3r@latest` (or grab a release binary).
2. Optionally add free API keys (IntelX, URLScan, GitHub) to the config file for richer results.
3. Run: `xurlfind3r -d example.com` (add `-o urls.txt` to save, or `--include-subdomains`).
4. Read the deduplicated URL list; grep it for interesting paths (`admin`, `login`, `.pdf`, `?id=`, etc.).
5. Pivot: feed live-looking URLs into archive viewers or a browser (sock-puppet); pair with a subdomain tool for full coverage.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` (a list of known URLs/paths for that domain)
- **Empty/negative result looks like:** few or no URLs means the archives haven't indexed much for that domain (new/obscure site) — not proof the site is empty; combine with active crawling if authorized.

## Gotchas & OpSec
- Results are **historical** — many listed URLs may 404 now; that's expected, and dead URLs can still reveal past structure.
- Completeness depends on the source archives and any API keys you configure; without keys some sources return limited data.
- Passive: no packets to the target, so safe for stealthy recon.

## Overlaps ("do both")
- Pairs with subdomain tools like `[[subdomainsbrute]]` and with the Wayback Machine UI — do both, since URL discovery and subdomain discovery surface different parts of a target's footprint.

## Trust & verifiability
`trust: community` — an actively maintained open-source tool; the URLs come from reputable third-party archives you can re-query independently, so verify any specific URL before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xurlfind3r |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
