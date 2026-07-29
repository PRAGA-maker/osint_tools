---
id: dirscraper
name: dirscraper
description: Use when you have a `domain`/website and want to surface hidden endpoints and subdomains referenced in its JavaScript — returns directories/paths and subdomains found in JS source.
url: https://github.com/Cillian-Collins/dirscraper
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Extracting undocumented endpoints, paths, and subdomains embedded in a site's JavaScript files.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open-source Python tool; no account or key.
opsec: active
opsecNote: dirscraper fetches the target's pages and JavaScript files directly from your machine, so the target's server logs your requests — this is active reconnaissance. Probing the discovered endpoints afterward is more active still. Run from a VPN/sock-puppet and avoid hammering the host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small but well-regarded open-source recon tool (200+ stars); the technique (parsing JS for endpoints) is standard, results depend on the target's code.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- turbolist3r
aliases:
- dirscraper
tags:
- recon
- javascript
- endpoint-discovery
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# dirscraper

> A recon tool that reads a website's JavaScript files and pulls out the directories, endpoints, and subdomains referenced inside them — surfacing paths that aren't linked anywhere visible.

## When to use
You have a `domain`/website connected to a subject or org and want to map its non-obvious surface. Modern sites embed API endpoints, admin paths, and subdomains in their JS bundles; dirscraper harvests script tags, parses the JavaScript, and extracts those references. That can reveal staging hosts, internal endpoints, or subdomains carrying more identifying content than the public pages — an infrastructure-mapping step, not a people lookup.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/Cillian-Collins/dirscraper` and install its Python requirements.
2. Run: `python dirscraper.py -u https://target.com` (`-o out.txt` to save, `-s` for silent).
3. It loads the page, finds script tags, and parses the JS for endpoints/paths/subdomains.
4. Review the output; feed discovered sub-`domain`s and paths into your other infra tooling — carefully, since visiting them is active.
5. Corroborate subdomains with a dedicated enumerator like `[[turbolist3r]]`.

## Inputs → Outputs
- **In:** `domain` / target URL
- **Out:** endpoints/directories and sub-`domain`s referenced in the site's JavaScript
- **Empty/negative result looks like:** little or nothing extracted — the site may have minimal/obfuscated JS or block automated fetches; not proof there are no hidden endpoints.

## Gotchas & OpSec
- **Active recon:** you fetch the target's assets directly — the server logs you. Use a VPN/sock-puppet; don't probe discovered endpoints without care.
- Results are only as rich as the target's JavaScript; single-page apps yield more than static sites.
- OpSec: **active** — this touches the target's infrastructure.

## Overlaps ("do both")
- Pairs with `[[turbolist3r]]` — dirscraper finds subdomains/endpoints *inside the site's own JS*, while a passive enumerator like Turbolist3r pulls subdomains from external OSINT sources. Run both to cover what each misses.

## Trust & verifiability
`trust: community` — a legitimate open-source tool using a standard technique; output is directly checkable (the endpoints either resolve or don't), so easy to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dirscraper |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
