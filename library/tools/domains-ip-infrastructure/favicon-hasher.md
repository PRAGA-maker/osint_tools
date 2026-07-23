---
id: favicon-hasher
name: Favicon Hasher
description: Use when you have a `domain` and want its favicon hash to find related/mirror infrastructure — returns MMH3/MD5/etc hashes plus one-click Shodan/Censys/ZoomEye pivots.
url: https://faviconhasher.codejavu.tech/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Turning a site's favicon into a search hash to discover other hosts serving the same icon.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free web tool; the downstream engines it links to (Shodan, Censys, ZoomEye, FOFA, Netlas) have their own free/paid tiers.
opsec: passive
opsecNote: "The tool fetches the target's favicon to hash it (a single, low-noise request), and the actual infrastructure search happens on Shodan/Censys against their pre-collected scan data — not against the target. Effectively passive. Your queries are logged by faviconhasher.tech and the search engines you pivot into; use a sock-puppet session for sensitive targets."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community reconnaissance utility (codejavu.tech); the hashing is deterministic and verifiable, and it merely constructs search-engine query URLs, so there's little to trust beyond correct hashing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- FaviconHasher
- favicon hash generator
tags:
- Domain/IP/Links
- Favicon search
- infrastructure
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Favicon Hasher

> Hashes a site's favicon (MMH3, MD5, SHA256, phash/dhash) and hands you ready-made Shodan/Censys/ZoomEye/FOFA queries to find every other host serving the same icon.

## When to use
You have a `domain` and suspect it shares infrastructure with other sites — a phishing kit, a cluster of scam pages, mirrored panels, or a target's other properties reusing the same custom favicon. Since search engines like Shodan index favicon hashes, finding the hash lets you enumerate related hosts and their `ip-address`es. Infrastructure/attribution work, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://faviconhasher.codejavu.tech/ and enter the target `domain` (or paste a favicon URL/file).
2. It fetches the favicon and computes multiple hashes (MMH3 is the one Shodan/Censys use).
3. Click a generated pivot link (Shodan `http.favicon.hash:`, Censys, ZoomEye, FOFA, Netlas, etc.) to list every indexed host with that favicon.
4. Read the engine's results: other domains/IPs serving the same icon — likely shared operator or kit.
5. Pivot discovered `ip-address`es/`domain`s into passive-DNS or reputation tools.

## Inputs → Outputs
- **In:** `domain` (or favicon file/URL)
- **Out:** favicon hashes; via the pivots, related `domain`s and `ip-address`es sharing the icon
- **Empty/negative result looks like:** the pivot engine returns few/no other hosts — the favicon is unique or generic (a default framework icon matches thousands and is noise, not signal).

## Gotchas & OpSec
- A default/CMS favicon (WordPress, cPanel) matches huge numbers of unrelated hosts — only distinctive custom icons give a clean cluster.
- The hash that matters for Shodan is MMH3 of the base64-encoded favicon; make sure you pivot with the right one.
- Downstream engines may need a (free) account and have their own rate limits.

## Overlaps ("do both")
- Feeds directly into Shodan/Censys and pairs with passive-DNS tools like [[dns-dumpster]] and IP mapping like [[ipinfo-map]] — the favicon hash finds the sibling hosts, those tools flesh out each one.

## Trust & verifiability
`trust: community` — a small but deterministic utility; the hash is reproducible and the value comes from the well-established engines it queries, so verify any cluster directly in Shodan/Censys.
