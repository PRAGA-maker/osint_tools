---
id: osti-science-cinema-search
name: OSTI Science Cinema Search
description: Use when you have a researcher `name`/topic and want US DOE science videos — a speech-indexed multimedia search; returns science talks/videos and their author `associate`/affiliation context.
url: https://www.osti.gov/sciencecinema
category: public-records
path:
- public-records
bestFor: Finding US Department of Energy science videos/talks and the researchers in them via spoken-word (audio-indexed) search.
selectorsIn:
- name
selectorsOut:
- associate
- employer-org
status: live
pricing: free
costNote: Free US DOE (Office of Scientific and Technical Information) service; no account.
opsec: passive
opsecNote: Passive — you search a public government multimedia index, transmitting nothing about a subject. Standard government query-logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US DOE Office of Scientific and Technical Information (OSTI); authoritative for the DOE-funded research videos it indexes.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- department-of-energy-patents
- doe-data-explorer
- us-dept-of-energy-office-of-science-search
aliases:
- ScienceCinema
tags:
- toddington
- academic
- government-data
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# OSTI Science Cinema Search

> A US DOE multimedia search that indexes the *spoken words* in science videos — find talks featuring a researcher and the collaborators/affiliations around them.

## When to use
Your subject is a scientist/researcher (especially in DOE-funded fields — physics, energy, materials) and you want to find them on video: conference talks, lab presentations, interviews. ScienceCinema indexes the audio, so a search can hit a mention even when the name isn't in the title — surfacing collaborators (`associate`s) and institutional affiliations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.osti.gov/sciencecinema.
2. Search an author `name` or research topic.
3. Read the output: matching videos with the moments the term is spoken, plus contributors and affiliations.
4. Pivot: note co-presenters/collaborators as `associate`s and the institution as an `employer-org`; cross-check on CiteSeerX/Google Scholar/ORCID.

## Inputs → Outputs
- **In:** a researcher `name` or topic
- **Out:** science videos, plus contributor `associate`s and institutional `employer-org` context
- **Empty/negative result looks like:** no videos for a name means they aren't in DOE-funded video content — try scholarly-paper search instead.

## Gotchas & OpSec
- Narrow scope: US DOE-funded science media only — not general video or non-science figures.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Do both with `[[us-dept-of-energy-office-of-science-search]]` and `[[citeseerx]]` — those give papers/records; ScienceCinema adds video appearances and spoken mentions.

## Trust & verifiability
`trust: trusted` — official DOE/OSTI service; the indexed videos are authoritative primary media, citable directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osti-science-cinema-search |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
