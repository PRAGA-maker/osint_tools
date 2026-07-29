---
id: paul-hensel-s-general-informational-data-page
name: Paul Hensel’s International Data Page
description: Use when you need country/state-level reference datasets for context — returns curated links to political-science, geography, and demographic data archives.
url: http://www.paulhensel.org/dataintl.html
category: public-records
path:
- public-records
bestFor: Finding authoritative international-relations, geographic, and demographic datasets for country-level background.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free academic resource page; the datasets it links are mostly free/open (some via ICPSR or project sites).
opsec: passive
opsecNote: A static academic link page — reading it touches no target and leaks nothing. Normal session hygiene applies on the destination archives.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Prof. Paul R. Hensel (University of North Texas), a recognised political scientist. Authoritative curation, but last updated ~2018, so some links have rotted as researchers moved.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- paulhensel.org data page
- ICOW data
tags:
- academic-data
- reference
- country-data
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Paul Hensel’s International Data Page

> An academic's curated index of international-relations and country-level datasets — states, capabilities, alliances, geography, and demographics — with direct links to the source archives.

## When to use
Background/context tool, not a people-lookup: when an investigation needs authoritative country- or state-level data — historical state lists, borders and contiguity, capital-to-capital distances, territorial claims, military/demographic capabilities, or pointers into big archives like ICPSR and CIESIN. Useful for grounding geopolitical context around a subject, org, or location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.paulhensel.org/dataintl.html.
2. Scan the sections: states & systems (COW, Gleditsch-Ward, ICOW), capabilities (military, industrial, demographic), alliances & organisations (ATOP, COW), geography (contiguity, distances, territorial claims), and links to archives (ICPSR, CIESIN, Harvard CID).
3. Follow the link to the dataset you need and download from the source.
4. Verify the link is live — some have rotted since the ~2018 update — and prefer the dataset's current canonical home if it moved.
5. Pivot: geographic/demographic context feeds `geolocation` and area analysis; archive links feed deeper record research.

## Inputs → Outputs
- **In:** none (a curated data-link directory)
- **Out:** links to country/state-level datasets and major social-science archives
- **Empty/negative result looks like:** a dead link or a dataset that moved with its author — search the dataset name to find its current host.

## Gotchas & OpSec
- Last refreshed around 2018; expect some link rot. Treat it as a high-quality map to well-known datasets rather than a live catalogue.
- Scope is international-relations / country-level — it holds no personal data and won't help identify individuals directly.

## Overlaps ("do both")
- Complements other reference/data directories; use it specifically for authoritative political-science and geographic datasets that general OSINT lists usually omit.

## Trust & verifiability
`trust: trusted` — curated by a recognised academic, pointing to primary datasets. The curation is reliable; verify individual links, since the page is no longer actively maintained.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | paul-hensel-s-general-informational-data-page |
