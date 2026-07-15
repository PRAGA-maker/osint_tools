---
id: people-search-4
name: People Search (peoplesearch.ph)
description: Use when you have a `name` and need Philippines-focused people-finding resources — a portal of missing-persons, adoption, public-records and directory links plus its own missing-persons registry.
url: https://www.peoplesearch.ph
category: public-records
path:
- public-records
bestFor: A launch-pad of Philippine and international people-finding resources, including a missing-persons registry, rather than a single data-returning search.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free portal; browsing categories, registries and links costs nothing. It is a signpost/registry site, not a paid database.
opsec: passive
opsecNote: Browsing the portal and its link categories is passive. Note that POSTING to its Missing Persons / Friends & Family registries is a public disclosure — anything you submit (names, photos, contact info) becomes visible and indexable, so treat registry posts as active outreach and mind what you reveal about a case.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: A themed link-directory / registry portal for the Philippines; it aggregates third-party resources and user-submitted registry entries rather than authoritative records, so provenance varies by link.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- peoplesearch.ph
tags:
- court
- inmate
- missing-persons
- philippines
- directory
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# People Search (peoplesearch.ph)

> A Philippines-oriented people-finding **portal** — a curated set of resource categories (missing persons, adoption, phone/address, public records, school directories) plus its own community registries. A signpost, not a database.

## When to use
You have a `name` for someone with a Philippine connection and want a jumping-off point: which registries, public-records links, and directory resources to try, and where to post or search a missing-persons/adoption case. Directly relevant to missing-persons work — it hosts Missing Persons, Adoption, and Friends & Family registries — but it *routes* you to data more than it returns records itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.peoplesearch.ph and browse the category that fits your case (Missing Persons, Adoption, Phone & Address, Public Records, School/University directories).
2. Follow the linked resources for the Philippines (and some international) sources; run your name against each destination tool.
3. To use the registries, search existing entries for the subject, or submit a new entry — understanding this is a public post subject to the site's review.
4. Pivot: a hit in a registry yields contact/reporter details and possibly a photo; linked directories feed school/employer and public-records searches.

## Inputs → Outputs
- **In:** `name`
- **Out:** links to resources; registry entries (`name`, reporter contact, sometimes `social-profile`/photo)
- **Empty/negative result looks like:** categories that are mostly outbound links with no matching registry entry. Absence in the registry is not evidence of anything — it is a small, self-submitted dataset; the value is the curated routing, not coverage.

## Gotchas & OpSec
- **Portal, not a search engine:** most of its power is directing you to other tools; judge each linked resource on its own merits (some links may be stale).
- **Registry posts are public** and manually reviewed (`manual-review` human-in-loop) — do not disclose sensitive case details you wouldn't want indexed.
- Mixed provenance: user-submitted registry data is unverified — corroborate before acting.

## Overlaps ("do both")
- Pairs with authoritative Philippine sources and dedicated missing-persons databases — use this to discover *which* tools to run, then rely on official registries/records for the actual data.

## Trust & verifiability
`trust: unverified` — a curated directory and community-registry portal, not an authoritative record source. Treat it as a navigation aid and verify any lead through the primary source it points to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | people-search-4 |
| category | public-records |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
