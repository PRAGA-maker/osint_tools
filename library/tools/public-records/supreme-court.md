---
id: supreme-court
name: Supreme Court of Canada Judgments (Lexum)
description: Use when you have a `name` and want to find whether that person was a party in a Supreme Court of Canada case — returns name, document-id, associate.
url: https://scc-csc.lexum.com/scc-csc/fr/nav.do
category: public-records
path:
- public-records
bestFor: Searching the full free archive of Supreme Court of Canada judgments by party name to place a person in litigation.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: free
costNote: Fully free public access; the entire judgment archive since 1876 is open with no account or paywall.
opsec: passive
opsecNote: Searching published judgments is passive and anonymous — the subject is never notified. Nothing you enter is attributable to the person; still search from a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Supreme Court of Canada judgment site operated by Lexum in partnership with the Court; judgments are the authoritative legal record.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- SCC Cases
- Lexum SCC
- scc-csc.lexum.com
tags:
- court
- inmate
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
---

# Supreme Court of Canada Judgments (Lexum)

> The free, official archive of every Supreme Court of Canada decision since 1876 — searchable by party name.

## When to use
You have a `name` and want to know whether the subject appears as a party, appellant, respondent or intervener in a Supreme Court of Canada case. A judgment places the person in a specific dispute, dates the event, gives a citable neutral citation (`document-id`), and names the opposing parties and counsel (`associate`) — all strong corroboration and pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site (available in English at `.../en/nav.do` and French at `.../fr/nav.do`).
2. Use the search box or the alphabetical case-name navigation; enter the subject's `name` (try surname-only and full-name variants — case styles use surnames).
3. Read the results:
   - Each hit is a judgment with a neutral citation (`document-id`, e.g. `2019 SCC 42`), the date, the parties, and the full HTML/PDF text.
   - Open the judgment to read the facts — it will name co-parties, counsel and lower-court history (`associate` and follow-on leads).
4. Pivot: the case name and citation feed lower-court databases (CanLII) and news archives; parties named alongside your subject become new search targets.

## Inputs → Outputs
- **In:** `name` (party surname)
- **Out:** `name` (as styled in the case), `document-id` (neutral citation), `associate` (co-parties, counsel)
- **Empty/negative result looks like:** no matching case name — meaning the person was not a *named party at the SCC level* (they may still appear in lower courts, which this archive does not cover). Use CanLII for lower courts.

## Gotchas & OpSec
- Only Supreme Court of Canada matters live here; most litigation never reaches the SCC, so absence is expected and not meaningful. For provincial/federal courts use CanLII.
- Common surnames produce many unrelated cases — confirm the individual via the facts, not the name alone.
- OpSec: fully passive and anonymous.

## Overlaps ("do both")
- Pairs with CanLII and provincial court registries — the SCC archive is authoritative but shallow (top court only); CanLII gives the far larger lower-court body where most people actually appear.

## Trust & verifiability
`trust: trusted` — the official SCC judgment repository maintained by Lexum with the Court; the text is the primary legal record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | supreme-court |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
