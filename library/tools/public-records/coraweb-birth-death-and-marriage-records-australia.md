---
id: coraweb-birth-death-and-marriage-records-australia
name: Coraweb — Australian Birth, Death & Marriage Records
description: Use when you have a `name` and an Australian connection and want a curated directory of BDM/vital-record and genealogy sources to search — returns pointers to dob, address and associate (family) records.
url: https://coraweb.com.au/websites/birth-death-and-marriage-records/
category: public-records
path:
- public-records
bestFor: A curated launchpad of Australian birth/death/marriage and genealogy record sites (by state and nationally).
selectorsIn:
- name
selectorsOut:
- name
- dob
- address
- associate
status: live
pricing: free
costNote: The Coraweb directory is free to browse. Individual destination registries and archives it links to vary — many state BDM index searches are free, but ordering a certificate or accessing some databases costs money at the destination.
opsec: passive
opsecNote: Browsing the directory leaks nothing about the subject. OpSec risk begins only at a destination site where you enter a name — assess each linked registry separately. No login on Coraweb itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Coraweb (Cora Num's long-running Australian genealogy site) is a respected curated directory of links, not a data source; trust attaches to the official state BDM registries and archives it points at.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- Cora Web
- Cora Num genealogy directory
tags:
- toddington
- curated-directory
- genealogy
- vital-records
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Coraweb — Australian Birth, Death & Marriage Records

> A hand-curated Australian genealogy directory — not a search engine — that collects the state and national BDM/vital-record and family-history sites in one place so you know where to look.

## When to use
You have a `name` with an Australian connection and need to find that person (or their family) in birth, death or marriage records, obituaries, or historical/ancestral archives, and you want a vetted map of which registries and databases exist per state rather than guessing. Relevant to missing-persons and genealogical identity work in Australia.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://coraweb.com.au/websites/birth-death-and-marriage-records/.
2. Scan the categorised links — state BDM registry indexes (NSW, VIC, QLD, etc.), national archives, and specialty/genealogy databases.
3. Click through to the relevant registry and search the subject's name there.
4. Read the destination's output — most state BDM index searches confirm an event (birth/death/marriage) with date and parties; full certificates usually require a paid order.
5. Pivot: a death record anchors an obituary search and next-of-kin (`associate`); a marriage record links partners; birth records tie to parents. Feed confirmed names/dates into broader people-search.

## Inputs → Outputs
- **In:** `name` (best with an Australian state and approximate year)
- **Out:** links leading to `dob`/event dates, `associate` (family/parties to the event), and `address`/place — via the destination registries, not Coraweb itself
- **Empty/negative result looks like:** Coraweb always renders its directory (it doesn't search), so an empty result only occurs at a destination registry — treat each registry's "no records" independently, mindful of per-state privacy windows (recent records are often restricted).

## Gotchas & OpSec
- Coraweb returns nothing about a person by itself — it is a menu of links. Record the destination registry as your source, not Coraweb.
- Australian BDM indexes have privacy embargoes (e.g. recent births/marriages restricted) — recent events may be deliberately absent.
- Some directory links rot over time; verify a destination is live before trusting it.
- OpSec: passive at the directory layer.

## Overlaps ("do both")
- Pairs with obituary and general people-search tools — Coraweb points you to the vital-record source; those expand a confirmed name into current contacts.

## Trust & verifiability
`trust: community` — a well-regarded independent Australian genealogy directory. Its reliability is really that of the official registries it links to; confirm every fact at the authoritative destination.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coraweb-birth-death-and-marriage-records-australia |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
