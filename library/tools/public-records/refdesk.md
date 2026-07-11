---
id: refdesk
name: RefDesk
description: Use when you have a starting `name`/`employer-org` and want a curated jump-off directory of people-finder, public-records and reference sites — returns links onward to `address`, `employer-org` lookups.
url: https://www.refdesk.com/
category: public-records
path:
- public-records
bestFor: A curated meta-index of free reference, people-search and public-records resources to branch from.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free reference portal; no account or payment.
opsec: passive
opsecNote: It is a link directory — browsing RefDesk itself is passive and reveals nothing about your target. OpSec exposure happens on the third-party sites you click through to; apply hygiene there.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, well-known reference portal; it curates links rather than holding data, so quality depends on the linked destinations.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Refdesk.com
- Reference Desk
tags:
- toddington
- curated-directory
- reference-sites
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# RefDesk

> A veteran "reference desk" link portal: a curated meta-index of free people-finder, public-records, news and reference sites — a place to branch from, not a data source itself.

## When to use
You're early in a case with a `name` or `employer-org` and want a vetted, categorized set of jumping-off points — white/yellow pages, public records, government and demographic databases, news archives, reference tools — without hunting them individually. Treat RefDesk as an index that points you at the actual lookup tools, not as something that returns data on a person directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.refdesk.com/.
2. Navigate to the relevant category (e.g. people/business search, public records, news, reference).
3. Follow a curated link to the underlying tool (a white-pages site, a government database, etc.).
4. Run your actual lookup on that destination site.
5. Pivot: the destination tools return the real selectors (address, employer, records); RefDesk's role ends once it routes you there.

## Inputs → Outputs
- **In:** none directly — you bring a `name`/`employer-org` to use on the linked tools
- **Out:** onward links to people-search, public-records and reference sites (which then yield `address`, `employer-org`, etc.)
- **Empty/negative result looks like:** RefDesk always "works" as a directory; a dead/outdated link is the real failure mode — some entries are stale, so expect a few broken destinations.

## Gotchas & OpSec
- It holds no personal data — it's a directory; don't expect to "search a person" on RefDesk itself.
- As an older portal, some links are outdated or dead; verify the destination still exists.
- US-leaning link set, though it includes international reference resources.

## Overlaps ("do both")
- Pairs with other OSINT link directories (Toddington's own list, OSINT Framework) — cross-reference because each curator's link set differs and ages differently.

## Trust & verifiability
`trust: community` — a reputable, long-lived reference portal, but it only curates links; judge each destination on its own merits and expect some link rot.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | refdesk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
