---
id: un-security-council-consolidated-list
name: UN Security Council Consolidated List
description: Use when you have a `name` (person or entity) and want to check UN sanctions designation — returns match status plus aliases, DOB, and listing narrative.
url: https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- terrorism-and-extremism
- sanctions-and-watchlists
bestFor: Authoritative check of whether a person or entity is under UN Security Council sanctions, with identifying details.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
status: live
pricing: free
costNote: Free official UN resource; downloadable in HTML, PDF, and XML. No account.
opsec: passive
opsecNote: You read/download an official UN list; the subject is never contacted and no query is tied to a specific target when you download the full list. Prefer downloading the full dataset and searching locally to leak nothing to any server.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party United Nations Security Council source — the authoritative global consolidated sanctions list, updated as designations change.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- un-data
aliases:
- UN Consolidated Sanctions List
- UNSC Consolidated List
- UN sanctions list
tags:
- sanctions
- watchlist
- due-diligence
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# UN Security Council Consolidated List

> The United Nations' authoritative consolidated sanctions list: is this person or entity designated by the Security Council, and what are the identifying details behind the listing?

## When to use
You have a `name` for an individual or organisation and need to know whether they are subject to UN Security Council sanctions (arms embargoes, asset freezes, travel bans) across all sanctions regimes — Al-Qaida/ISIL, Taliban, DPRK, and others. Each entry carries identifiers useful for confirming identity and pivoting: aliases, `dob`, place of birth, nationality, passport/ID numbers, and a narrative summary of why they were listed (often naming `associate`s). This is due-diligence/adjudication; missing-persons relevance is low and indirect (confirming an identity against an official record).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list.
2. Either browse/search the on-page HTML list, or download the consolidated dataset — offered as **HTML, PDF, and XML**. For repeatable matching, take the XML and search it locally.
3. Search your `name` and every plausible transliteration/alias (the list is heavy with Arabic/Cyrillic transliterations, so exact spelling matters).
4. Read the matched entry: aliases, `dob`, place of birth, nationality, document IDs, listing date, and narrative.
5. Pivot: identifiers (passport numbers, `dob`, `associate` names in the narrative) feed identity confirmation and further record checks; cross-check against OFAC/EU lists for coverage the UN list omits.

## Inputs → Outputs
- **In:** `name` (person or entity)
- **Out:** designation status, aliases, `dob`, place of birth, nationality, document IDs, `associate` names, listing narrative
- **Empty/negative result looks like:** no match — the subject is not UN-designated; this does NOT mean they're clear of *other* sanctions bodies (OFAC, EU, UK) — the UN list is one authority among several.

## Gotchas & OpSec
- **Transliteration is the main pitfall** — the same person can be spelled many ways; search all variants and use the alias fields.
- A negative here is narrow: only UN Security Council designations. Always cross-check OFAC SDN, EU, and national lists for full coverage.
- Names are common; confirm with `dob`/passport before asserting a match (false positives on shared names).
- OpSec: passive; downloading the full list and matching offline leaks nothing about who you're checking.

## Overlaps ("do both")
- Cross-run with OFAC SDN, the EU consolidated list, and UK OFSI — each sanctions body designates different parties, and only the union gives full coverage. Complements `[[un-data]]` for broader UN datasets.

## Trust & verifiability
`trust: trusted` — this is the UN's own primary record, so a designation is authoritative; the caveats are transliteration/spelling and the list's scope being limited to UN Security Council measures.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | un-security-council-consolidated-list |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name → name, dob, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
