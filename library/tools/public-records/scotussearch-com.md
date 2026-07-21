---
id: scotussearch-com
name: SCOTUS Search
description: Use when you have a `name` and want to find where it appears in US Supreme Court oral arguments (as a party, attorney or speaker) — returns the matching argument statements, case names and speakers.
url: https://www.scotussearch.com/
category: public-records
path:
- public-records
bestFor: Full-text search of US Supreme Court oral-argument transcripts by name, party, speaker or case since the 1950s.
selectorsIn:
- name
selectorsOut:
- name
status: live
pricing: free
costNote: Completely free (BETA); no account or payment required.
opsec: passive
opsecNote: Searching public court-argument transcripts is passive and anonymous — no target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free BETA research tool indexing public SCOTUS oral-argument transcripts (1.4M+ statements across ~6,800 arguments); a third-party index of authoritative primary transcripts.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- scotussearch.com
- SCOTUS Search
tags:
- court-records
- supreme-court
- legal-search
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# SCOTUS Search

> A full-text search engine over US Supreme Court oral arguments — 1.4M+ individual statements across ~6,800 arguments since the 1950s, searchable by party, attorney, speaker or case.

## When to use
You want to tie a `name` to US Supreme Court litigation at the oral-argument stage — as a **petitioner, respondent, or arguing attorney** — or to see exactly what a specific justice/advocate said in a case. Niche, but when a subject was party to or argued a Supreme Court case, this pinpoints the case, the role, and the verbatim exchange. (It indexes *oral arguments*, not opinions or filings.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.scotussearch.com/.
2. Search by petitioner/respondent `name`, case name, docket number, or specific speaker; filter by time period or search the argument text itself.
3. Read the returned statements — the case, who spoke, and the passage matching your query.
4. Follow the case to its full record (opinions/filings) on an authoritative source like the Supreme Court's own site or Oyez.
5. Pivot: a confirmed party/attorney role links the subject to a case, era and legal team (`associate`s), and to the broader public record around that litigation.

## Inputs → Outputs
- **In:** `name` (party, attorney, or speaker), case name, or docket
- **Out:** matching oral-argument statements with case name and speaker (`name`)
- **Empty/negative result looks like:** no matches — the person was never a party/attorney/speaker in an *argued* Supreme Court case, or the case falls outside the indexed range (roughly 1950s–2010s). Most people will have no hits; a blank is expected and unremarkable.

## Gotchas & OpSec
- **Oral arguments only** — not opinions, briefs or lower-court records; use a general court-records source for those.
- BETA and third-party; coverage is time-bounded, so verify against the official transcript/audio (e.g. Oyez, supremecourt.gov).
- OpSec: **passive** — public transcripts, nothing exposed.

## Overlaps ("do both")
- Pairs with Oyez, CourtListener and PACER — SCOTUS Search is the fast name-in-argument finder; those provide the full opinions, dockets and filings behind the case.

## Trust & verifiability
`trust: community` — a free third-party index of authoritative public transcripts. The underlying source is reliable; confirm any specific quote or role against the official Supreme Court transcript/audio.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scotussearch-com |
| category | public-records |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
