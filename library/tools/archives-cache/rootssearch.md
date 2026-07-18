---
id: rootssearch
name: RootsSearch
description: Use when you have a name plus dates/places and want to search many genealogy sites at once — returns social-profile-style record hits and associate/dob leads across FamilySearch, Ancestry, and more.
url: https://rootssearch.io/search
category: archives-cache
path:
- archives-cache
bestFor: One-form, multi-site genealogy search (and a browser extension that auto-fills a person's details) across the major records providers.
selectorsIn:
- name
- dob
selectorsOut:
- associate
- dob
- address
status: live
pricing: freemium
costNote: The RootsSearch tool/extension is free; the destination sites it searches (Ancestry, FindMyPast) may paywall the full record while FamilySearch/FindAGrave are free.
opsec: passive
opsecNote: You enter a person's identifying details and hand them off to third-party genealogy sites; those sites log the query. No target is notified. Use a research account/clean browser, and remember genealogy records expose living relatives — handle sensitively.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Long-running open-source project (rootsdev), an official FamilySearch partner; it only forwards searches to reputable providers rather than hosting data itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Roots Search
- rootssearch.io
- RootsSearch Chrome extension
tags:
- archives-cache
- genealogy
- records-search
- browser-extension
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# RootsSearch

> A single search box (and a browser extension) that fires a person's name and dates at all the major genealogy sites at once — FamilySearch, Ancestry, MyHeritage, FindMyPast, FindAGrave, BillionGraves, and more.

## When to use
You have a `name` and some anchors — a `dob`, a birth/death place, a relative — and want to sweep the genealogy record set efficiently instead of retyping into each site. Records surfaced (censuses, births/marriages/deaths, burials) yield `associate` links (parents, spouses, children), confirmed `dob`, and historical `address`es — core building blocks for tracing a missing person's family and last-known ties.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Use the web form at https://rootssearch.io/search, or install the RootsSearch browser extension (Chrome/Firefox) for auto-fill.
2. Enter the person's name, birth/death years, and places; the more anchors, the tighter the results.
3. Click a target site (FamilySearch, Ancestry, FindMyPast, MyHeritage, FindAGrave, BillionGraves, etc.) — RootsSearch opens that site with the details pre-filled. With the extension, viewing a person on one genealogy site lets you re-search the rest in one click.
4. Read each site's hits; open free ones (FamilySearch, FindAGrave) fully, note paywalled ones. Pivot: named relatives become new `associate` subjects; a burial record confirms `dob`/death and location.

## Inputs → Outputs
- **In:** `name` (+ `dob`, birth/death place, relatives)
- **Out:** `associate` (family members), `dob`, `address` (historical residences from records)
- **Empty/negative result looks like:** each site returns no matching record — common for living people (records skew historical), very common names without anchors, or regions with thin digitized coverage.

## Gotchas & OpSec
- Human-in-the-loop: none in RootsSearch itself, but destination sites may require a login or subscription to view a full record (FamilySearch is free with a free account).
- OpSec: passive; targets aren't notified, but the genealogy sites log your searches. Genealogy data exposes living relatives — handle with care and use a research account.
- It's a launcher, not a database: RootsSearch holds no records; result quality is entirely the destination site's.

## Overlaps ("do both")
- Pairs with `[[familysearch]]` and other single-site genealogy tools — RootsSearch is the fast multi-site fan-out, while FamilySearch is where you do the deep, free record work once you've found a hit.

## Trust & verifiability
`trust: trusted` — it is an established open-source FamilySearch partner that merely forwards searches to reputable providers; verify each record on the source site it opens.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rootssearch |
| category | archives-cache |
| selectorsIn → selectorsOut | name, dob → associate, dob, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
