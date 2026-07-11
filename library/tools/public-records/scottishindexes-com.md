---
id: scottishindexes-com
name: Scottish Indexes
description: Use when you have a `name` linked to Scotland and want historical Scottish records — returns free indexed entries (Court of Session, census, BMD, prison, mental-health records) with residence, occupation and dates.
url: https://www.scottishindexes.com/cssearch.aspx
category: public-records
path:
- public-records
bestFor: Free indexing of Scottish genealogy and legal records to place a person by residence, occupation and date.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- associate
- dob
status: live
pricing: free
costNote: The indexes are free to search; the site funds itself via optional record-transcription/research services and donations, but no payment is needed to search and read index entries.
opsec: passive
opsecNote: Searching queries Scottish Indexes' own historical databases — no living subject is contacted (records are largely historical). No account required. Use a sock-puppet browser only if you care about not logging searches against your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-regarded independent Scottish genealogy project (Graham and Emma Maxwell) that indexes primary Scottish records; the indexes are volunteer/expert-compiled and widely cited. Transcription errors are possible, as with any index.
missingPersonsRelevance: high
coverage:
- gb-sct
auth: none
api: false
localInstall: false
registration: false
aliases:
- scottishindexes.com
- Scottish Indexes Court of Session
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- scotland
- genealogy
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Scottish Indexes

> A free, well-regarded index into Scottish historical records — Court of Session cases, census, BMD, prison and mental-health registers — used to place a Scottish subject by residence, occupation and date.

## When to use
You have a `name` (with an approximate era, place or occupation) tied to Scotland and want to reconstruct their history or family. Scottish Indexes offers searchable indexes across legal and civil records — including 700,000+ Court of Session entries plus census, birth/marriage/death, prison and mental-health registers — revealing residence, occupation, dates and associated parties. Strong for deceased Scottish subjects and for growing the `associate` graph via older relatives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.scottishindexes.com/ and pick the relevant search (Court of Session at cssearch.aspx, or the census/BMD/other index pages).
2. Enter `name` (forename + surname, with an alternative-surname option), optionally occupation, residence, organisation, keyword, and a year range (+/- up to 20 years).
3. Read the indexed entries: residence (`address`), occupation, dates, and named parties.
4. Note reference details to order or locate the full original record if needed.
5. Pivot: a residence narrows electoral/parish searches; named co-parties/relatives are `associate` leads; dates approximate a `dob`; occupation may give an `employer-org`.

## Inputs → Outputs
- **In:** `name` (+ optional occupation, residence, year range)
- **Out:** residence/`address`, occupation, approximate `dob`/dates, related parties (`associate`), record references
- **Empty/negative result looks like:** no index hits — the person predates/postdates the indexed sets, wasn't in Scotland, or the name is spelled differently. Use the alternative-surname and year-tolerance options before concluding absence.

## Gotchas & OpSec
- Indexes are historical; recent/living subjects mostly won't appear.
- It's an index, not always the full record — some entries point you to originals held elsewhere.
- Transcription/spelling variance is real; search variants and use the +/- year range.

## Overlaps ("do both")
- Pairs with ScotlandsPeople (the official paid registry), `[[findmypast-co-uk]]` and general genealogy sites — Scottish Indexes' free legal-record coverage (Court of Session, prison, asylum) complements the civil BMD/census focus of the big providers.

## Trust & verifiability
`trust: trusted` — a respected, expert-run Scottish genealogy project indexing primary records for free; authoritative as an index, with ordinary transcription caveats.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scottishindexes-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address → name, address, associate, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
