---
id: yasni-2
name: Yasni
description: Use when you have a `name` and want an aggregated web/people profile — links, mentions, and contact leads pulled from across the open web — returns social-profile and associate leads.
url: http://www.yasni.co.uk
category: people-search
path:
- people-search
bestFor: Name-centric web aggregation — pulling together a person's public web mentions, profiles, and links into one people-profile page.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
- email
status: degraded
pricing: free
costNote: Free name search; the operator also sells reputation-management services. Coverage is strongest for German/European names and has aged.
opsec: passive
opsecNote: You search an aggregator of already-public web content, not the subject directly. Note Yasni also lets people claim/manage their own profile — a subject may see aggregate interest indirectly, but a search itself sends no target-facing signal. Use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A German people-search aggregator (yasni GmbH); it collates open-web mentions, so results are only as accurate as the sources and can conflate same-named people.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pipl
- webmii
aliases:
- yasni.com
- yasni.co.uk
tags:
- people-search
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Yasni

> A name-centric web aggregator — enter a person's name and get a collated profile of their public web mentions, links, and contact leads.

## When to use
You have a `name` and want a fast, broad sweep of where that name appears on the open web — profiles, news, directories, and links — assembled into one page. Useful early in a case to map the surface area and spot `social-profile`/`associate` leads worth chasing. Strongest for European (especially German) names; weaker and staler elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open yasni (the `.com` is the main live site; `.co.uk` historically fronted UK searches) and enter the `name`.
2. Review the aggregated results: linked profiles, mentions, associated names, and any surfaced contact details.
3. Disambiguate — Yasni conflates same-named individuals, so filter by location/context.
4. Pivot: a surfaced `social-profile` feeds account enrichment; associated names feed relationship mapping; a surfaced email feeds email-OSINT.

## Inputs → Outputs
- **In:** `name` (+ location/context to disambiguate)
- **Out:** `social-profile` links, `associate` (co-mentioned names), sometimes `email`/contact leads
- **Empty/negative result looks like:** thin or irrelevant results — common for names with little public web footprint or outside its stronger European coverage. Same-name noise can also masquerade as hits; verify each.

## Gotchas & OpSec
- Aggregation conflates people with the same name — never assume all results are one person.
- Coverage has aged and skews European; treat gaps as a coverage artefact, not evidence.
- OpSec: passive; it collates already-public content.

## Overlaps ("do both")
- Pairs with `[[pipl]]` and `[[webmii]]` — other name-aggregators with different source weightings; cross-run to catch what each misses and to confirm which hits are the same individual.

## Trust & verifiability
`trust: unverified` — a mention-aggregator with no per-result validation; use it to generate leads and always confirm identity and links at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yasni-2 |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, associate, email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
