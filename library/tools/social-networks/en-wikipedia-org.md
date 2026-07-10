---
id: en-wikipedia-org
name: en.wikipedia.org (List of social networking websites)
url: https://en.wikipedia.org/wiki/List_of_social_networking_websites
category: social-networks
path:
- social-networks
description: Use when you have a `username` or `name` and want an exhaustive checklist of social platforms to search — returns a reference list of networks (with focus/region) to pivot into.
bestFor: A comprehensive, maintained reference list of social-networking sites to make sure you haven't missed a niche or regional platform.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free encyclopedia article; no account or payment. It is a reference list, not a search service.
opsec: passive
opsecNote: Reading a Wikipedia article is fully passive and anonymous; nothing about your target is disclosed. Attribution risk only arises later, when you visit the individual platforms it lists.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Wikipedia is community-edited but this list is well-referenced and actively maintained; treat it as a directory of platforms to check, not as data about any individual.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Wikipedia list of social networking websites
- list of social networks
tags:
- gsocialmedia
- General Social Media Sites
- reference-list
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# en.wikipedia.org (List of social networking websites)

> Not a search tool but a coverage checklist — Wikipedia's maintained list of social-networking sites, used to make sure you've considered every niche and regional platform a subject might use.

## When to use
You have a `username` or `name` and have already checked the mainstream networks, but want to be systematic about niche, professional, dating, or country-specific platforms (VK, Weibo, Nextdoor, Xing, etc.). This article enumerates hundreds of networks with their focus and user base — a map of *where else to look* when the obvious platforms come up empty.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.wikipedia.org/wiki/List_of_social_networking_websites.
2. Scan the table for platforms matching the subject's region, profession, age or interests.
3. Note the network's focus/country column to prioritise likely fits (e.g. a Russian subject → VK/OK; a professional → Xing).
4. Go to each candidate platform and search the `username`/`name` there (or via `[[username-search-tool]]`).
5. Pivot: any profile found on a listed network feeds the normal social-profile enrichment chain.

## Inputs → Outputs
- **In:** `username` / `name` (as the thing you'll search on each listed site)
- **Out:** a reference set of `social-profile` platforms to check — the list itself returns no personal data
- **Empty/negative result looks like:** not applicable — it always returns the same directory. The "negative" is when none of the listed platforms yield a profile for your subject.

## Gotchas & OpSec
- It contains **no** information about individuals — it is purely a list of platforms. Don't mistake it for a people-search.
- The list can lag on brand-new or defunct networks; cross-check currency before assuming a platform is live.
- OpSec: reading is passive; the active exposure is on the platforms you subsequently visit.

## Overlaps ("do both")
- Pairs with `[[username-search-tool]]` and `[[deepfind-me]]` — this widens the *set* of platforms to consider; those actually check a handle against many of them.

## Trust & verifiability
`trust: trusted` — a well-sourced, actively-maintained Wikipedia article; reliable as a directory of platforms, though (as with any wiki) verify a specific network's current status before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | en-wikipedia-org |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
