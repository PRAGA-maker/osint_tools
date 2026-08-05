---
id: document-search
name: Document Search
description: Use when you have a `name` or company (`employer-org`) and want documents about them — a one-page dashboard that fires the query across Companies House, EDGAR, Pastebin, Scribd, Drive and more.
url: https://one-plus.github.io/DocumentSearch
category: search-engines
path:
- search-engines
bestFor: Sweeping a person or company name across corporate-filing, regulatory, paste and document-hosting sites from a single search dashboard.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- employer-org
- associate
status: live
pricing: free
costNote: Free static web dashboard (hosted on GitHub Pages); no account. It just builds and opens searches on third-party sites, which have their own free/paid tiers.
opsec: passive
opsecNote: The dashboard is a static page that constructs query URLs — loading it reveals nothing. Exposure happens when you run each search: the destination site (Companies House, Scribd, Pastebin, etc.) sees your query and IP. Use a sock-puppet browser/VPN for the searches themselves.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community "search-multiplexer" dashboard that only assembles queries against reputable third-party sources; result quality is entirely each destination's, and some sites (electoral rolls, hacker forums) vary in reliability.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- DocumentSearch
tags:
- document-search
- multi-source-search
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# Document Search

> A single dashboard that takes a name or company and multiplexes it across document- and filing-heavy sources — Companies House, FCA, SEC EDGAR, Pastebin, Google Drive/Dropbox/Scribd/SlideShare/ISSUU, electoral rolls and the Google Hacking Database.

## When to use
You have a subject `name` or an `employer-org` and you want the paper trail: corporate filings, regulatory records, uploaded documents, presentations, and pastes that mention them. Instead of visiting a dozen sites, this dashboard pre-builds the searches so you can run the same identity across all of them and see where documents surface.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://one-plus.github.io/DocumentSearch in a sock-puppet browser.
2. Enter the person or company name in the relevant field (for Companies House, remove spaces as instructed).
3. Launch the searches per source — corporate registries (Companies House/EDGAR/FCA), document hosts (Scribd/Drive/ISSUU), and paste/leak sources (Pastebin, GHDB).
4. Pivot: a filing yields officers/addresses (`associate`, `employer-org`); a hosted document or paste yields a `document-id` and often more selectors (emails, phones) to chase.

## Inputs → Outputs
- **In:** `name` (person) or `employer-org` (company)
- **Out:** `document-id` (hosted files/filings), `employer-org` + officer `associate` (registry records), leads from pastes
- **Empty/negative result looks like:** each source returns nothing — common for people with no corporate footprint or common names; broaden with alternate name spellings and jurisdiction-specific registries.

## Gotchas & OpSec
- It only assembles queries — it holds no data, so freshness and coverage are each destination's, and some links break as those sites change URLs.
- Registry searches are jurisdiction-specific (Companies House = UK, EDGAR = US); match the source to the subject's country.
- Paste/leak and "hacker forum" links can surface sensitive/unlawful data — handle findings appropriately.

## Overlaps ("do both")
- Complements a dedicated corporate-registry tool: use this for the fast multi-source sweep, then go deep in the single registry (full filing history, beneficial owners) that returned the hit.

## Trust & verifiability
`trust: community` — a convenience dashboard over reputable sources; verify every hit at its authoritative source (the registry filing, the actual document) rather than trusting the dashboard's routing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | document-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → document-id, employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
