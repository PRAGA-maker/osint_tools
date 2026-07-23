---
id: dirhunt
name: Dirhunt
description: Use when you have a `domain` and want to discover and analyse its web directories — finds "index of" listings, hidden folders and files across many sources, returning `domain`/URL paths.
url: https://github.com/Nekmo/dirhunt
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Finding and analysing exposed/hidden web directories on a domain without brute force.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (MIT, Nekmo); a Python CLI (`pip3 install dirhunt`). No API key needed.
opsec: active
opsecNote: Dirhunt crawls the target site directly (it also pulls hints from Wayback/VirusTotal/crt.sh), so it generates real requests to the target from your IP. The project itself asks for the site owner's consent; use a sock-puppet IP/proxy and only scan what you're authorised to.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known open-source directory analyser; efficient and widely used, but findings are candidate paths to verify manually.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Nekmo/dirhunt
tags:
- Domain/IP/Links
- Find directories
- recon
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- waybackurls
---

# Dirhunt

> Smart directory finder: it analyses a site's folder structure, catches "index of" pages and fake-404 hidden directories, and pulls extra paths from public sources — without noisy brute force.

## When to use
You have a target `domain` and want to map its web directories and exposed folders — the classic "index of" listings that leak files, plus directories hidden behind empty index pages or false 404s. Dirhunt is efficient (it avoids brute force, finishing in seconds) and enriches its crawl with paths from robots.txt, VirusTotal, Google, CommonCrawl, SSL certs, crt.sh and the Wayback Machine, so it surfaces folders a simple crawl would miss.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install dirhunt`.
2. Run against a target: `dirhunt https://example.com/`.
3. Read the output: it flags interesting directories, "index of" pages, redirectors, and notable files, and can save to JSON.
4. Use `--proxies` for OpSec and resume support for large sites.
5. Pivot: exposed files feed metadata/document analysis; discovered paths feed further recon and `[[waybackurls]]` for historical versions.

## Inputs → Outputs
- **In:** a target `domain`/URL
- **Out:** discovered directories and files — "index of" listings, hidden folders, notable files (`domain`/paths), JSON-exportable
- **Empty/negative result looks like:** no interesting directories — the server has listing disabled and no exposed folders surfaced; not proof nothing exists, since dirhunt avoids brute force by design.

## Gotchas & OpSec
- OpSec: **active** — it requests pages from the target directly; get authorisation and use a proxy/sock-puppet IP.
- It analyses structure rather than brute-forcing, so it can miss folders with no external hint — pair with a wordlist tool if you need exhaustive coverage.
- Findings are candidates; open and confirm each manually.

## Overlaps ("do both")
- Pairs with `[[waybackurls]]` — waybackurls supplies historical archived paths, which Dirhunt can validate and expand against the live site; together they cover past and present directory exposure.

## Trust & verifiability
`trust: community` — a mature, MIT-licensed recon tool; results are candidate paths from crawling and public sources, so verify each at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dirhunt |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
