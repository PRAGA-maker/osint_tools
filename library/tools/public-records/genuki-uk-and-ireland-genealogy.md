---
id: genuki-uk-and-ireland-genealogy
name: Genuki UK & Ireland Genealogy
description: Use when you have a `name` plus a UK/Ireland place and want a curated, locality-by-locality reference to the parish and historical records that cover it — returns address (place), associate leads.
url: http://www.genuki.org.uk/index.php
category: public-records
path:
- public-records
bestFor: A trusted UK & Ireland genealogy reference organised by county/parish to locate the right historical records.
selectorsIn:
- name
- address
selectorsOut:
- address
- associate
status: live
pricing: free
costNote: Free, volunteer-run reference (a registered UK charity). No account; it links out to record collections that may have their own pricing.
opsec: passive
opsecNote: Reading a reference/directory and following it to historical archives is fully passive — no living subject is contacted. No login required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: GENUKI is a long-established, charity-run genealogy reference maintained by volunteers; authoritative as a signpost to sources, though it is a reference/index rather than a searchable records database itself.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- GENUKI
- Genealogy of the UK and Ireland
tags:
- toddington
- curated-directory
- specialty-search
- genealogy
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Genuki UK & Ireland Genealogy

> The reference "virtual library" for UK & Ireland family history — organised by county and parish, it tells you which historical records exist for a place and where to find them.

## When to use
You are researching a person's UK/Irish ancestry or historical footprint and have a `name` tied to a place (`address`/parish/county), and you need to know *which* records — parish registers, censuses, monumental inscriptions, local histories — cover that locality and how to access them. GENUKI is a signpost/reference organised geographically, not a name-search database; use it to find the right source, then search that source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.genuki.org.uk and navigate by hierarchy: UK & Ireland → country → county → parish/town.
2. Read the locality page: available parish registers, census coverage, cemeteries, local record repositories, and links to online collections.
3. Follow those links to the actual archives/indexes and search your `name` there.
4. Use the historical/locality context (place names, boundary changes) to search the right jurisdiction and period.
5. Pivot: records found via GENUKI's links yield ancestors and relatives (`associate`), places (`address`), and dates that anchor an identity.

## Inputs → Outputs
- **In:** `name` + a UK/Ireland place (`address`/parish/county)
- **Out:** references/links to records that reveal `address` (places), `associate` (family/ancestors), historical context
- **Empty/negative result looks like:** a locality page thin on records, or no coverage for a very recent period — GENUKI leans historical; it points to sources rather than returning a person, so "no record here" means check the linked archive directly.

## Gotchas & OpSec
- It's a reference/index, not a searchable people database — the records live in the collections it links to.
- Strongest for historical (pre-20th-century) genealogy; limited for living-person research.
- Volunteer-maintained, so depth varies by county/parish.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with [[ancestor-hunt]] and FamilySearch-style archives — GENUKI tells you *what records exist for a place*; those hold the searchable records.

## Trust & verifiability
`trust: trusted` — a reputable, long-running charity reference; reliable as a signpost, but verify every genealogical fact against the primary record it directs you to.
