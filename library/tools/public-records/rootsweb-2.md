---
id: rootsweb-2
name: RootsWeb
description: Use when you have a `name` and want ancestry/family links — returns user-submitted family trees (WorldConnect), relatives, birth/death dates and genealogy mailing-list posts.
url: https://home.rootsweb.com
category: public-records
path:
- public-records
bestFor: Free genealogy research — mining community family trees and mailing lists for relatives, dates and ancestral links.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- name
- address
status: live
pricing: free
costNote: Free, Ancestry-funded community site; no payment required (some deep links may bounce to Ancestry.com, which is paid for its own collections).
opsec: passive
opsecNote: You search a public genealogy archive, not the subject — no notification reaches anyone. WorldConnect trees are user-submitted and public; be aware that querying and any tree you upload are public. Use a sock-puppet browser; do not post a living subject's details into public trees or lists.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Hosted and funded by Ancestry.com, but the content is overwhelmingly user-submitted (WorldConnect trees, list posts), so reliability varies contributor to contributor; treat as leads, not proof.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- RootsWeb
- WorldConnect
- rootsweb.com
tags:
- genealogy
- family
- ancestry
- family-trees
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- rootsweb
- support-rootsweb-com
---

# RootsWeb

> The web's oldest free genealogy community — Ancestry-run WorldConnect trees and mailing lists holding 600M+ individuals of user-submitted family history.

## When to use
You have a `name` and want to build out the family around it — parents, siblings, spouses, children, birth/death dates — especially for older or deceased individuals whose relatives may help locate or identify a subject. Strong for cold-case and missing-person genealogy where you need to reconstruct a family tree and find living `associate`s to approach.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://home.rootsweb.com.
2. Use the WorldConnect (Community Trees) search: enter the subject's `name`, and where known a birth/death year or place to narrow it.
3. Read the tree hits: each shows the person's `dob`/death date, place, and linked relatives (`associate`) — click through the tree to expand parents, spouses and descendants.
4. Cross-reference the RootsWeb mailing lists / message boards (searchable by surname and locality) for researcher posts that add detail or corrections.
5. Verify: user-submitted trees carry errors and copy each other's mistakes — corroborate any date/link against a primary source before relying on it.
6. Pivot: a living relative feeds people-search (`[[radaris-people-and-business-search-north-america]]`); a confirmed event feeds a vital-records order (`[[nz-certificates-online-new-zealand]]` / `[[familysearch]]`).

## Inputs → Outputs
- **In:** `name` (optionally + year/place)
- **Out:** family-tree entries with `associate`/relatives, `dob`/death dates, `name` variants, and ancestral place/`address` clues
- **Empty/negative result looks like:** no matching tree or list post — common for common names without a place, or for living people (trees skew to deceased/historical). Absence means "no contributor has submitted this," not that the family isn't documented elsewhere.

## Gotchas & OpSec
- Content is **user-submitted** — treat every date and relationship as a lead. Errors propagate as contributors copy each other's trees.
- Historical churn: RootsWeb went through a 2023 outage/migration; WorldConnect and mailing lists are back online, but some old deep links may be stale or redirect to Ancestry.com.
- OpSec: **passive** and public; do not upload a living subject's details to public trees/lists.

## Overlaps ("do both")
- Pairs with `[[familysearch]]` and `[[legacy]]` — FamilySearch adds indexed primary records to corroborate RootsWeb's community trees, and obituary sites confirm death dates and surviving relatives. Do both: get the tree structure here, verify the facts there.

## Trust & verifiability
`trust: community` — Ancestry hosts and funds it, but the data is contributor-generated. Reliable as a map of who-relates-to-whom to investigate; confirm specific facts against primary vital/census records before treating them as established.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rootsweb-2 |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, name, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
