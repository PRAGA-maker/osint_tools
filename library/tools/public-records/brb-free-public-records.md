---
id: brb-free-public-records
name: BRB Free Public Records
description: Use when you have a `name` or `employer-org` and need the right free US public-record source — returns a curated directory pointing to address, employer-org, and records data.
url: https://www.brbpub.com/free-public-records/
category: public-records
path:
- public-records
bestFor: A curated directory of free US government public-record sources — state/county sites, courts, licensing boards, unclaimed funds — organized so you find the authoritative source fast.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: The directory is free; it links to government sources that are themselves free. Some on-site search boxes may redirect to a paid partner (e.g. Intelius) — stick to the government links.
opsec: passive
opsecNote: Browsing the directory is passive and reveals nothing about your target. The one caveat: some embedded search widgets route to commercial data brokers — avoid those and follow the direct government links to keep the trail clean and free.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: BRB Publications is a long-established authority on public-record sourcing; its directory points to genuine government agencies, though BRB itself is a commercial publisher.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- state-corrections-links
- michigan-state-records
aliases:
- BRBPub
- BRB Publications
- brbpub free public records
tags:
- toddington
- curated-directory
- specialty-search
- public-records
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# BRB Free Public Records

> A trusted, curated index of *free* US government public-record sources — the fast way to find the authoritative agency instead of landing on a paywalled data broker.

## When to use
You have a `name` (or `employer-org`) and a US jurisdiction and want to search official public records without paying an aggregator. BRB's directory routes you to the correct free government source by record type and state — court dockets, county recorder/property, occupational-licensing boards, unclaimed funds, corporate filings. Ideal as the "where do I actually look?" step before diving into a specific agency's search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.brbpub.com/free-public-records/.
2. Choose the record category and the state/county you need (state & local sites, federal courts, licensing boards, unclaimed funds, international).
3. Follow the link to the government agency's own search.
4. Search there by name/organization; read the official record — `address`, business/licensing details, filings.
5. Pivot: licensing hits corroborate occupation/`employer-org`; property/court hits feed address and timeline. For incarceration specifically, use [[state-corrections-links]].

## Inputs → Outputs
- **In:** `name` / `employer-org` (searched at the linked source)
- **Out:** a route to the authoritative free source, which yields `address`, `employer-org`/licensing details, and other public records
- **Empty/negative result looks like:** BRB lists no free source for a niche record type, or the linked agency has no online search — some records are still offline/request-only; that's a coverage gap, not a dead end.

## Gotchas & OpSec
- It's a *directory*, not a search engine — the data lives on each government site.
- Watch for on-page search widgets that redirect to a paid broker; BRB discloses it is **not** FCRA-compliant, so never use results for hiring/tenant/credit decisions.
- OpSec: passive — following government links reveals nothing about your target.

## Overlaps ("do both")
- Pairs with [[state-corrections-links]] (inmate locators) and aggregators like [[michigan-state-records]] — use BRB to reach free official sources, aggregators only to generate leads you then verify officially.

## Trust & verifiability
`trust: trusted` — BRB Publications is a recognized authority on public-record sourcing and points to genuine government agencies. The directory is reliable for *where* to look; verifiability rests with the official source it links to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | brb-free-public-records |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
