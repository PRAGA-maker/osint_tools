---
id: favfreak
name: FavFreak
description: Use when you have a `domain` or a list of hosts and want to cluster them by favicon hash to discover related assets — returns grouped hosts/`ip-address`es sharing a favicon.
url: https://github.com/devanshbatham/FavFreak
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fingerprinting infrastructure by favicon.ico hash to find sibling servers, admin panels, and shared tech behind an organisation.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open source (MIT). Pairs with Shodan's http.favicon.hash search; a Shodan account is needed to act on the hashes at scale.
opsec: active
opsecNote: FavFreak itself fetches each target's /favicon.ico directly, so the target's web server logs your requests (an active touch). Route through a proxy/VPN. The follow-on pivot — searching the mmh3 hash in Shodan — is passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source recon tool by devanshbatham; widely used in bug-bounty workflows. Read the code before running, as with any recon script.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- FavFreak favicon hash
tags:
- favicon-hash
- asset-discovery
- recon
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# FavFreak

> Weaponises favicon.ico: computes each host's favicon hash and groups hosts by it, so identical favicons reveal servers that belong together.

## When to use
You have a set of subdomains/hosts (or a single `domain`) for an organisation and want to find *other* assets owned by the same entity — admin panels, staging boxes, VPN portals — that share the same favicon. Because many app stacks ship a default favicon, the mmh3 hash becomes a pivot: search it in Shodan/Censys to enumerate every internet-facing host with the same icon. It is an infrastructure-mapping tool; missing-persons value is indirect (mapping the full footprint behind a suspect site).

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/devanshbatham/FavFreak && pip3 install mmh3`.
2. Feed it a list of URLs (with scheme) on stdin:
   ```
   cat urls.txt | python3 favfreak.py -o output
   ```
3. FavFreak fetches each `/favicon.ico`, computes the mmh3 hash, and groups the hosts by hash — also matching known fingerprints (e.g. specific CMS/panels).
4. Pivot: take a produced hash and search Shodan `http.favicon.hash:<hash>` (or Censys) to enumerate every other host on the internet serving that favicon — that list is the related-asset set.

## Inputs → Outputs
- **In:** `domain` / list of hosts (URLs)
- **Out:** hosts grouped by favicon hash + the mmh3 hashes; feeding those to Shodan yields related `domain`s and `ip-address`es
- **Empty/negative result looks like:** each host in its own unique-hash bucket / no fingerprint match — means favicons are unique per host, so this pivot won't cluster them; fall back to other recon.

## Gotchas & OpSec
- The real power is the Shodan/Censys pivot on the hash, not FavFreak's local grouping — budget a Shodan lookup.
- A default/shared favicon (e.g. a common framework) produces huge, low-signal clusters; a custom favicon gives a tight, high-value cluster.
- OpSec: **active** — FavFreak requests the favicon from each target host, which is logged. Use a proxy; do the hash search in Shodan (passive) rather than re-fetching.

## Overlaps ("do both")
- Pairs with Shodan/Censys (the hash consumers) and with subdomain-enumeration tools that produce FavFreak's input list — enumerate hosts first, then cluster them here, then expand via favicon-hash search.

## Trust & verifiability
`trust: community` — a well-known, MIT-licensed bug-bounty tool; inspect the short Python source before running and confirm any discovered asset independently, since favicon collisions produce false groupings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | favfreak |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
