---
id: faviconhash
name: FaviconHash
description: Use when you have a website/favicon and want its hash to find every other host serving the same icon — returns a favicon hash and pivot links (Shodan/Censys) to related domains and ip-addresses.
url: https://kriztalz.sh/favicon-hash/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Computing a site's favicon hash (MMH3/MD5/SHA256) to pivot in Shodan/Censys/FOFA and cluster related infrastructure.
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: 100% free and browser-based; no account or registration.
opsec: passive
opsecNote: Hashing the favicon and searching Shodan/Censys is passive (those services scanned the hosts, not you). Note the tool fetches the favicon on your behalf; if the source IP matters, fetch the icon yourself and hash it offline.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small personal security-tools site; the technique (MMH3 favicon hashing for Shodan pivoting) is standard and the output is trivially verifiable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- favicon hash generator
- mmh3 favicon
tags:
- favicon
- pivot
- infrastructure
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# FaviconHash

> Compute a website's favicon hash and jump straight to Shodan/Censys/FOFA searches for every other host serving the same icon — a fast infrastructure-pivot trick.

## When to use
You have a `domain`/site and want to find its related or hidden infrastructure by its favicon. Scanning engines (Shodan, Censys, FOFA) index the MMH3 hash of each host's favicon, so a shared, distinctive icon links a subject's other servers — including ones behind different domains or a CDN's origin. This tool computes the hash and hands you the pivot queries. Infrastructure recon, not people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://kriztalz.sh/favicon-hash/ and enter the target site URL (or upload its favicon).
2. Read the generated hashes (MMH3 for Shodan, plus MD5/SHA256) and the favicon preview.
3. Click the provided **Shodan/Censys/ZoomEye/FOFA** links (e.g. Shodan `http.favicon.hash:<mmh3>`) to list every host with the same icon.
4. Review those hosts' `ip-address`es and `domain`s to cluster related infrastructure.
5. Pivot: a related `ip-address` → [[ipvoid]]/[[whois-arin]]; a related `domain` → [[certkit-certificate-transparency-log-search]].

## Inputs → Outputs
- **In:** a `domain`/site URL (or a favicon file).
- **Out:** the favicon's MMH3/MD5/SHA256 hash and ready-made scanner-search links → related `ip-address`es and `domain`s.
- **Empty/negative result looks like:** a common/default favicon (or none) that matches thousands of unrelated hosts, or a unique icon that Shodan simply hasn't indexed — a generic hash isn't a useful pivot.

## Gotchas & OpSec
- Generic/framework default favicons produce huge, meaningless match sets — only distinctive icons make good pivots.
- The pivot's power comes from Shodan/Censys/FOFA coverage; a host not scanned by them won't appear.
- The tool fetches the favicon for you; to keep your source IP off the target, fetch and hash the icon locally instead.

## Overlaps ("do both")
- Pairs with [[certkit-certificate-transparency-log-search]] and [[ipvoid]]: favicon hashing finds hosts sharing an icon, CT/WHOIS confirm whether they share an owner.

## Trust & verifiability
`trust: community` — a small personal tool implementing a standard technique; the hash is deterministic and any pivot result is checkable directly in Shodan/Censys.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | faviconhash |
