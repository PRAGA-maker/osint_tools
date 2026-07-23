---
id: fast-google-dorks-scan
name: Fast Google Dorks Scan
description: Use when you have a `domain` and want an automated sweep of 45+ Google-dork categories against it — returns exposed admin panels, sensitive file types and path-traversal `domain`/URL hits.
url: https://github.com/IvanGlinkin/Fast-Google-Dorks-Scan
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Automated multi-category Google-dork scan of a domain for exposed panels and sensitive files.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (IvanGlinkin); a Bash script, optional Docker. No API key for the core run.
opsec: active
opsecNote: It issues many automated Google queries about the target domain from your IP; Google will CAPTCHA/throttle aggressive dorking, and the queries are attributable. Use a sock-puppet IP/VPN or the built-in proxy option, and pace it.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source dorking script (1.7k+ stars); it only surfaces search-indexed content, so results are leads to verify.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- IvanGlinkin/Fast-Google-Dorks-Scan
- FGDS
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- google-dorks
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- dorks-hunter
---

# Fast Google Dorks Scan

> Bash-driven dork sweep: point it at a domain and it runs dozens of Google-dork categories to surface exposed panels, files and traversal points.

## When to use
You have a target `domain` and want its search-indexed exposures without hand-typing dorks: admin/login panels, sensitive file types (configs, backups, documents), and path-traversal artefacts. FGDS automates 45+ dork categories and collects the hits, giving you a fast map of what Google already knows about the site's soft spots — useful for scoping an org's or person's web exposure.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/IvanGlinkin/Fast-Google-Dorks-Scan`.
2. Run: `bash ./FGDS.sh example.com` (or with a proxy: `bash ./FGDS.sh example.com 192.168.1.1 8080`; Docker also supported).
3. It iterates the dork categories and outputs a report of matching Google result URLs.
4. Open each hit manually to confirm — a dork match is a candidate, not a confirmed exposure.
5. Pivot: exposed documents feed metadata analysis; panels/subdomains feed further recon.

## Inputs → Outputs
- **In:** a target `domain`
- **Out:** categorised Google-dork hits — admin panels, sensitive files, traversal points (`domain`/URLs)
- **Empty/negative result looks like:** few/no hits — a clean domain OR (more often) Google throttled/CAPTCHA'd the run; slow down, add a proxy, and retry before assuming clean.

## Gotchas & OpSec
- Human-in-the-loop: Google rate-limits automated dorking; expect CAPTCHAs and pace the queries.
- Results reflect Google's index and may be stale/cached — verify each hit live.
- OpSec: **active** — many search queries about the target from your IP; use a sock puppet/proxy.

## Overlaps ("do both")
- Pairs with `[[dorks-hunter]]` — both automate Google dorking with different dork sets and engines; running both broadens the exposed surface you find.

## Trust & verifiability
`trust: community` — a well-known open-source dork runner; it only reveals what search engines already index, so treat every hit as a lead to confirm at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fast-google-dorks-scan |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (rate-limit) |
