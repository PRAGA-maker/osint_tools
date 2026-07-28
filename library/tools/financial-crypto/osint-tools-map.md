---
id: osint-tools-map
name: OSINT Tools Map
description: Use when you have a country/region (or a `name`/`employer-org` tied to one) and need the local public registries and records to search — returns links to business registries, court records, cadastre, phonebooks and more by geography.
url: https://cybdetective.com/osintmap/
category: financial-crypto
path:
- financial-crypto
bestFor: Finding which public registries, court and property records exist for a given country/region before you start searching.
selectorsIn:
- employer-org
- name
- geolocation
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free interactive directory; the individual registries it links to have their own access/pricing.
opsec: passive
opsecNote: The map itself is a passive directory — you only touch a source when you follow a link out. Apply OpSec at the destination registry, not here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated by Cyber Detective (a well-regarded OSINT curator). It points to sources rather than holding data; verify each linked registry's current availability.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cybdetective-com
- quick-geolocation-search
aliases:
- OSINT Map
- cybdetective osintmap
tags:
- bellingcat-toolkit
- companies-finance
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# OSINT Tools Map

> A worldwide, click-through map of official public-records sources — pick a country/region and see which registries, court records, cadastres and directories you can actually search there.

## When to use
You know *where* to look (a country, state, or city) but not *what* is available there. Before hunting for a person or company, use the map to enumerate the local sources: business registries, court records, property/cadastral maps, vehicle databases, phonebooks, cemetery/genealogy records. Especially useful for jurisdictions you don't work in often, where you'd otherwise not know a registry exists.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cybdetective.com/osintmap/.
2. Navigate to the country/region of interest (drill from continent → country → state/city).
3. Read the list of record types available there and click through to the actual registry.
4. Run your `name`/`employer-org`/`address` query on that destination source.
5. Pivot: a business registry entry yields officers/`associate`s and an `address`; a court record yields case parties.

## Inputs → Outputs
- **In:** a geography, plus the `name`/`employer-org` you'll search there
- **Out:** links to jurisdiction-specific registries → (via them) `employer-org` officers, `associate`s, `address`es, court records
- **Empty/negative result looks like:** a sparse entry for a country with few digitised records — the map can only list what exists; thin coverage reflects the jurisdiction, not a tool failure.

## Gotchas & OpSec
- Human-in-the-loop: none for the map; destination registries may need accounts/CAPTCHAs.
- OpSec: passive here; the real exposure is at each linked source — read that tool's notes before querying.
- Links can rot; confirm the destination registry still works and note the map is a signpost, not the data.

## Overlaps ("do both")
- Pairs with `[[cybdetective-com]]` (the same curator's broader toolset) and `[[quick-geolocation-search]]` — use the map to scope sources by country, then the geolocation/search tools to work a specific lead.

## Trust & verifiability
`trust: community` — a respected curator's directory; reliable as a pointer, but each linked registry is the authoritative source and must be verified in situ.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-tools-map |
| category | financial-crypto |
| selectorsIn → selectorsOut | employer-org, name, geolocation → employer-org, associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
