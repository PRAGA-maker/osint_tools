---
id: usarmy-occupation-codes-united-states
name: USArmy Occupation Codes (United States)
description: Use when you have a US Army MOS code or role reference for a subject and want to decode it — returns the `employer-org`/job meaning to interpret military records and background.
url: https://en.wikipedia.org/wiki/List_of_United_States_Army_careers
category: search-engines
path:
- search-engines
bestFor: Decoding US Army MOS codes / career fields mentioned in a subject's records into a plain-language role.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free Wikipedia reference page; no account or payment.
opsec: passive
opsecNote: A public reference page — you look up a code, not a person. No target-side footprint and nothing that could alert a subject; browse normally (Wikipedia sees only that the page was viewed).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Wikipedia-maintained list; MOS/career-field entries are factual and generally sourced, but confirm any specific code against the official US Army MOS listing before relying on it.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- List of United States Army careers
- Army MOS codes
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# USArmy Occupation Codes (United States)

> A reference list of US Army careers and Military Occupational Specialty (MOS) codes — a decoder ring for the military job references you find in a subject's paper trail.

## When to use
You have a document, résumé, obituary, social post, or record that names a US Army MOS code or career field for a subject (e.g. "11B", "68W", "31B") and you need to know what it means. Decoding the role tells you the person's likely skills, postings, and community — useful when building context on a veteran, corroborating a claimed background, or generating leads (unit, base, VSO networks).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.wikipedia.org/wiki/List_of_United_States_Army_careers.
2. Use in-page find (Ctrl/Cmd-F) for the MOS code or job title you have (`employer-org` reference).
3. Read the decoded career field / occupational specialty and its branch.
4. Pivot: the decoded role points you to relevant units, bases, and veteran communities; corroborate the specific code against the official Army MOS list, then feed the name into people-search/records tools.

## Inputs → Outputs
- **In:** a US Army MOS code or career-field reference (`employer-org`)
- **Out:** the plain-language military occupation / branch it maps to (`employer-org` context)
- **Empty/negative result looks like:** the code isn't on the list — it may be a Navy/Air Force/Marine code, an outdated/renumbered MOS, or a misread; check the correct service's occupation list instead.

## Gotchas & OpSec
- Fully passive, no login — it's a Wikipedia page.
- MOS codes are reused and reorganised over time; a code's meaning can differ by era, so note the year of the source record.
- This decodes a role only — it does not identify a specific soldier; use it as interpretation, then pivot to person-level sources.

## Overlaps ("do both")
- Complements the official US Army MOS listing and DoD sources — Wikipedia is faster to search, the official listing is authoritative; confirm there before relying on a decode.

## Trust & verifiability
`trust: community` — Wikipedia-maintained, so treat it as a quick decoder and verify the specific code against the Army's official MOS documentation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usarmy-occupation-codes-united-states |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
