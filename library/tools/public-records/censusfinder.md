---
id: censusfinder
name: Censusfinder
url: http://censusfinder.com
category: public-records
path:
- public-records
description: Use when you have a `name` and want free online census/genealogy records — returns a curated directory of links to census indexes, transcriptions and family data by region.
bestFor: Finding which free online census/genealogy resources cover a given US/UK/Canada region, then searching them for a named person.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- dob
- associate
- address
status: live
pricing: free
costNote: Free directory of links; it hosts no records itself and charges nothing. Some sites it links to may have their own paywalls.
opsec: passive
opsecNote: Browsing a link directory is fully passive; nothing about the target is disclosed and no login is needed. Attribution risk only arises on the third-party record sites you follow through to.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing volunteer-maintained directory of free census/genealogy links (US 1790–1940, plus UK/Canada); it curates links rather than data, so quality depends on the destination sites.
missingPersonsRelevance: high
coverage:
- us
- uk
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Census Finder
- censusfinder.com
tags:
- genealogy
- family
- census
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Censusfinder

> A curated directory (best reached at www.censusfinder.com) of *free* online census and genealogy resources — the map that tells you which no-cost site to search for a person in a given region.

## When to use
You have a `name` (and a rough US state / UK / Canada region as `geolocation`) and want free census/genealogy records without paying an Ancestry-style subscription. Censusfinder points you to the free indexes, transcriptions, tax lists and directories that cover that place and period, which you then search for the individual. Good for building historical identity, DOB and family links on a budget.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open www.censusfinder.com (the apex `censusfinder.com` may not resolve; use the www host).
2. Browse to the region — a US state, or the UK/Canada sections.
3. Pick free resources for the relevant census year (1790–1940 for the US) — indexes, images, transcriptions.
4. Follow the link and search the destination site for the subject's `name`.
5. Pivot: household entries yield `associate` (family), `dob` and historical `address`; cross-check finds against `[[familysearch-2]]`.

## Inputs → Outputs
- **In:** `name` (+ optional region `geolocation`)
- **Out:** via linked sites — `name`, `dob`, `associate` (household), historical `address`
- **Empty/negative result looks like:** the directory lists few/no free resources for that region/year, or the linked sites return nothing. Censusfinder itself never returns person data — a "miss" is really the destination site's answer.

## Gotchas & OpSec
- It is a link directory, not a database: it holds no records and some links may be stale or now paywalled.
- The useful free coverage is uneven by region/year; expect to bounce through several destination sites.
- OpSec: browsing is passive; exposure only happens on the third-party sites you visit.

## Overlaps ("do both")
- Pairs with `[[familysearch-2]]` (a single large free archive) — Censusfinder widens the net to smaller free indexes FamilySearch may not include.

## Trust & verifiability
`trust: community` — a reputable, long-running volunteer link directory; reliability rests on the destination sites, so verify any record on its source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | censusfinder |
| category | public-records |
| selectorsIn → selectorsOut | name, geolocation → name, dob, associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
