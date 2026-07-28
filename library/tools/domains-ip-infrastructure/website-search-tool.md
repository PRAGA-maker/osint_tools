---
id: website-search-tool
name: Website Search Tool (Aware-Online)
description: Use when you have a `domain` and want a guided query builder that fans it out across WHOIS, archives, shared-analytics-ID, and backlink lookups — returns targeted investigation links.
url: https://www.aware-online.com/en/osint-tools/website-search-tool/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Turning a single domain into ready-made queries across WHOIS, archives, shared-ID, and backlink services.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free query-builder page from Aware Online Academy; no account.
opsec: passive
opsecNote: The page constructs search URLs client-side and you can enter placeholder data then edit the URL. It's passive until you open a generated link — do that from a sock-puppet browser. A few destinations (some historical-WHOIS archives) are paid.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated URL builder from a reputable OSINT training academy; it only assembles links, so reliability rests on the destination services.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- aware-online-com
aliases:
- Aware Online website search tool
tags:
- domain-and-ip-research
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Website Search Tool (Aware-Online)

> The domain-focused module of Aware-Online's OSINT toolkit: enter a domain and it builds the right queries across WHOIS registrars, web archives, shared-analytics-ID lookups, backlink finders, and more.

## When to use
You have a `domain` and want a structured, checklist-style way to investigate it — registration history, whether its text/source appears elsewhere, shared Google Analytics/AdSense IDs (a classic way to link sites owned by the same operator), related TLDs, and who links to or discusses it. Handy so you don't forget an angle when profiling a website tied to your subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.aware-online.com/en/osint-tools/website-search-tool/.
2. Enter the `domain` (or placeholder data you'll edit into the URL later).
3. Click the category you need — WHOIS (SIDN, Who.is, DomainBigData, Whoxy), Wayback/archives, shared-ID/analytics lookup, related-TLD finder, backlink/mention search.
4. It opens the constructed query on the destination service; read results there.
5. Pivot: a shared analytics ID or a matching registrant links this `domain` to others; hosting/WHOIS gives an `ip-address` and registrant to chase further.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` (related/linked domains, WHOIS/registrant hints), `ip-address` (via the hosting/WHOIS destinations) — delivered as targeted query URLs, not records
- **Empty/negative result looks like:** the query opens on the destination with no hits; because the tool only builds URLs, judge "empty" on each service.

## Gotchas & OpSec
- It's a **query builder**, not a database — no data comes from Aware-Online itself; evaluate on the destination.
- A few destinations (historical-WHOIS archives) are paid; free ones cover most needs.
- Passive until you open a link; use a clean browser/IP for the click-through.

## Overlaps ("do both")
- Part of `[[aware-online-com]]`'s suite; do both this and dedicated WHOIS/DNS/certificate-transparency tools — the builder orients you across services, the specialists go deep.

## Trust & verifiability
`trust: community` — a curated link builder from a reputable academy; it assembles queries only, so verify every result at the authoritative destination service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | website-search-tool |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
