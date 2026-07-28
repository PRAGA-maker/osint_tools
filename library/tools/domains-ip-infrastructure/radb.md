---
id: radb
name: RADb
description: Use when you have an `ip-address`, prefix or ASN and want its Internet Routing Registry records — returns the registered route objects, origin AS and maintainer/contact behind the routing.
url: https://www.radb.net/query
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Looking up who registered the routing for an IP prefix or AS number (route objects, origin AS, maintainer, contacts) via the Internet Routing Registry.
selectorsIn:
- ip-address
- domain
selectorsOut:
- employer-org
- email
- ip-address
status: live
pricing: freemium
costNote: Public WHOIS query and the RADb dataset are free to search; only registering/maintaining your own route objects requires a paid membership.
opsec: passive
opsecNote: A read-only registry lookup — you query RADb/Merit's database, never the target network, so the subject sees nothing. No login needed for queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: RADb is the Internet Routing Registry operated by Merit Network; records are self-published by network operators, so entries are authoritative for who claimed a route but can be stale or aspirational.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- who-is
- whois-arin
- criminal-ip-search
aliases:
- RADB
- Merit RADb
- Internet Routing Registry
tags:
- Domain/IP investigation
- routing-registry
- asn
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# RADb

> The Internet Routing Registry front-end from Merit Network — resolve an IP prefix or AS number to the route objects, origin AS and maintainer/contacts its operator registered.

## When to use
You have an `ip-address`, a network prefix, or an ASN tied to a subject's infrastructure and you want the routing-layer paperwork behind it: which AS is authorised to originate the prefix, who the registered maintainer is, and any contact/`email` attributes attached. This complements plain WHOIS — WHOIS tells you who was *allocated* an address; the routing registry tells you who actually announces it and manages the routing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.radb.net/query.
2. Enter an object to look up: an IP/prefix (e.g. `193.0.0.0/21`), an `as-set`/`aut-num` (e.g. `AS3333`), a maintainer, or a route object.
3. Optionally restrict which source registries to search (RADb mirrors many IRRs — RIPE, ARIN, etc.).
4. Read the returned objects: `route`/`route6` (prefix + origin AS), `aut-num` (the AS and its policy), `mntner` (maintainer) and `person`/`role` contacts with `email` and org fields.
5. Pivot: the origin AS and maintainer feed WHOIS/ARIN org lookups (`[[whois-arin]]`, `[[who-is]]`); contacts and org names feed people/company OSINT; the prefix feeds scanner lookups like `[[criminal-ip-search]]`.

## Inputs → Outputs
- **In:** `ip-address` / prefix / ASN (or maintainer/route object name)
- **Out:** route objects, origin AS, `employer-org` (maintainer/org), contact `email`s, related `ip-address` prefixes
- **Empty/negative result looks like:** "no entries found" means no IRR route object is registered for that query in the searched sources — common for networks that don't publish to RADb; fall back to RIR WHOIS.

## Gotchas & OpSec
- IRR data is **self-published and voluntary**, so it can be stale, aspirational, or missing — a prefix with no route object is normal, not proof of nothing.
- RADb mirrors multiple registries; the same prefix may have conflicting objects across sources — note which `source:` each came from.
- Passive and unauthenticated for queries; nothing reaches the target network.

## Overlaps ("do both")
- Pairs with `[[who-is]]` and `[[whois-arin]]` — RIR WHOIS gives the allocation/holder, RADb gives the routing intent and maintainer. Together they triangulate who controls an address block.
- Feeds `[[criminal-ip-search]]` for what the hosts inside the prefix actually expose.

## Trust & verifiability
`trust: trusted` — operated by Merit Network as the long-standing Internet Routing Registry; the records are authoritative as *self-declarations* by network operators. Verify freshness via the object's `last-modified`/`changed` fields and cross-check RIR WHOIS.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radb |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → employer-org, email, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
