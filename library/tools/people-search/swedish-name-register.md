---
id: swedish-name-register
name: Swedish Name Register
description: Use when you have a Swedish `name` and want to gauge how common it is (name frequency) — returns population counts to judge how distinctive a name is.
url: https://scb.se/hitta-statistik/sverige-i-siffror/namnsok/
category: people-search
path:
- people-search
bestFor: Estimating how many people in Sweden share a given first name or surname, to judge whether a name is rare enough to narrow a search.
selectorsIn:
- name
selectorsOut:
- name
status: degraded
pricing: free
costNote: Free government statistics. Note: SCB stopped producing name statistics in 2024 and now redirects users to Skatteverket (Swedish Tax Agency) for live name-frequency search.
opsec: passive
opsecNote: This is aggregate census/registry statistics — you query counts, not individuals, so nobody is identified or alerted. Entirely passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by SCB (Statistics Sweden), the national statistics agency; frequency data is authoritative, but the SCB tool itself was discontinued in 2024 and the live equivalent now lives at Skatteverket.
missingPersonsRelevance: medium
coverage:
- se
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- SCB namnsök
- Statistics Sweden name search
- Skatteverket name search
tags:
- bellingcat-toolkit
- people
- sweden
- name-frequency
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
---

# Swedish Name Register

> A Swedish name-frequency lookup: how many people in Sweden carry a given first name or surname — a distinctiveness gauge that tells you whether a name will narrow a search or drown you in duplicates.

## When to use
You have a Swedish `name` and need to know how much signal it carries. A surname held by 40 people is a strong lead; one held by 40,000 is nearly useless on its own. Use it to prioritise: rare names justify direct enumeration, common ones demand extra selectors (DOB, place, associate) before searching. Note the tooling moved — SCB retired its name statistics in **2024** and points users to **Skatteverket**.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the SCB page (https://scb.se/hitta-statistik/sverige-i-siffror/namnsok/). If it shows the discontinuation notice, follow it to **Skatteverket's** name search.
2. On Skatteverket, enter the first name to see how many people currently have it (and as a first vs additional name), or search the most common surnames.
3. Read the count: single/low-hundreds = distinctive; tens of thousands = common.
4. Pivot: for a distinctive Swedish name, move to Swedish people/registry search and directory sources; for a common one, gather more selectors first.

## Inputs → Outputs
- **In:** `name` (Swedish first name or surname)
- **Out:** `name` frequency — a population count / commonness ranking
- **Empty/negative result looks like:** a name not present in the register (very rare, foreign, or misspelled) returns no count — that itself signals an unusual name worth pursuing directly.

## Gotchas & OpSec
- Coverage is **Sweden only**; useless for names outside the Swedish population register.
- The original SCB tool is discontinued (2024) — if the SCB page no longer functions, use Skatteverket's equivalent; the underlying data is the same lineage.
- OpSec: passive aggregate statistics; no individual is queried.

## Overlaps ("do both")
- Use alongside Swedish people-search/registry tools — this tells you *how hard* the name will be to resolve; those actually resolve it. Run this first to set expectations.

## Trust & verifiability
`trust: trusted` — authoritative national statistics; the only caveat is that you may need to switch from the retired SCB page to Skatteverket for a live query.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | swedish-name-register |
| category | people-search |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
