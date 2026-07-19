---
id: united-states-marine-corps-occupation-codes
name: United States Marine Corps – Occupation Codes
description: Use when you have a USMC MOS `document-id` code and want to decode the Marine's job specialty — returns the occupation/role behind the code.
url: https://en.wikipedia.org/wiki/List_of_United_States_Marine_Corps_MOS
category: search-engines
path:
- search-engines
bestFor: Translating a US Marine Corps Military Occupational Specialty (MOS) code into the plain-language job it denotes.
selectorsIn:
- document-id
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free Wikipedia reference article; no account or payment.
opsec: passive
opsecNote: Static reference reading on Wikipedia — no target interaction, no footprint toward the subject. Fully safe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Wikipedia-maintained list; crowd-sourced but well-cited and stable for a reference table of codes. Cross-check critical codes against official USMC MCO 1200.17 documentation.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- USMC MOS list
- Marine Corps MOS codes
tags:
- toddington
- curated-directory
- specialty-search
- military
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# United States Marine Corps – Occupation Codes

> A reference table that decodes US Marine Corps MOS codes into the actual jobs — turning a cryptic 4-digit specialty found in a record into "infantry rifleman," "intelligence analyst," etc.

## When to use
You have a US Marine's Military Occupational Specialty (MOS) code — a 4-digit `document-id`-style identifier that appears on discharge papers (DD-214), unit rosters, résumés, or a subject's own social posts — and you need to know what job it means. Decoding it tells you the person's training, likely postings, and skill set, which shapes where else to look (unit associations, veteran groups, security-cleared career paths).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.wikipedia.org/wiki/List_of_United_States_Marine_Corps_MOS.
2. Ctrl-F the 4-digit code (e.g. `0311`) or browse by Occupational Field (the first two digits group the field).
3. Read the mapped title and field; note the broader occupational family for context.
4. Pivot: the decoded role feeds veteran-community searches, unit-history lookups, and résumé/LinkedIn correlation; the occupational field hints at clearances or specialized skills.

## Inputs → Outputs
- **In:** `document-id` (MOS code)
- **Out:** the job title / `employer-org`-context (branch + specialty)
- **Empty/negative result looks like:** code not in the table — may be a retired/reclassified MOS or a different branch's code (Army/Navy use different systems); verify the branch first.

## Gotchas & OpSec
- MOS codes are reclassified over time; a code valid in one era may map differently or be retired. Note the record's date.
- This is USMC only — an identical-looking number in an Army or Navy record means something else.
- OpSec: passive reference lookup; zero subject footprint.

## Overlaps ("do both")
- Complements military service-record and veteran-community tools: use this to decode the code, then those to find the person behind it.

## Trust & verifiability
`trust: community` — Wikipedia crowd-sourced but stable and well-referenced for this reference table; corroborate mission-critical decodes against official USMC MOS manuals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | united-states-marine-corps-occupation-codes |
| category | search-engines |
| selectorsIn → selectorsOut | document-id → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
