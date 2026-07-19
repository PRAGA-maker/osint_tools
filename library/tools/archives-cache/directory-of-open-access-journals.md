---
id: directory-of-open-access-journals
name: Directory of Open Access Journals (DOAJ)
description: Use when you have a `name`/topic and want peer-reviewed open-access articles and journals — returns free full-text scholarly records for research and person-profiling.
url: https://doaj.org/search/journals
category: archives-cache
path:
- archives-cache
bestFor: Searching a curated index of vetted open-access journals and articles for free, full-text scholarly literature.
selectorsIn:
- name
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free, community-funded, non-profit index; no account needed to search or read. All indexed content is genuinely open-access (free full text).
opsec: passive
opsecNote: You search a public scholarly index; nothing about your subject is exposed and no one is contacted. Fully passive — standard browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: DOAJ is a widely trusted, independent, non-profit whitelist of vetted open-access journals with published inclusion criteria — a standard reference for legitimate OA literature.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- DOAJ
tags:
- Archives of documents/newspapers
- academic
- open-access
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Directory of Open Access Journals (DOAJ)

> A vetted, non-profit index of ~20,000 open-access journals and millions of free full-text articles — a clean source of legitimate scholarly literature.

## When to use
You have a person's `name`, an institution, or a research topic and want free, full-text peer-reviewed literature. In OSINT this supports academic person-profiling — an academic's publications reveal their `employer-org`/affiliation, co-authors (`associate`s), research focus, and timeline — and it's a reliable place to read primary research behind a claim without hitting paywalls. Its whitelist nature also helps you avoid predatory journals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://doaj.org — search journals at `/search/journals` or articles at `/search/articles`.
2. Query by author `name`, keyword, title, or institution; filter by subject, language, or country.
3. Read the results: for a person, their articles list affiliations, co-authors, and dates; open the free full text directly.
4. For bulk work, use the DOAJ API to pull records programmatically.
5. Pivot: an author's affiliation feeds institutional lookups; co-authors feed associate mapping; dates build an academic timeline.

## Inputs → Outputs
- **In:** author `name` / institution / topic keyword
- **Out:** open-access article and journal records → affiliations (`employer-org`), co-author `name`s, dates, full text
- **Empty/negative result looks like:** no matches — the person may not publish in open-access venues (much research sits in paywalled journals DOAJ doesn't index), so absence is not evidence they've published nothing.

## Gotchas & OpSec
- Open-access only: DOAJ indexes vetted OA journals, so paywalled/subscription literature won't appear — combine with a broader scholarly index (e.g. an OpenAlex/Semantic Scholar) for full coverage.
- Name ambiguity: common names collide; disambiguate via affiliation, ORCID, and co-authors.
- OpSec: fully passive scholarly search.

## Overlaps ("do both")
- Complements broader academic search engines — DOAJ guarantees free full text and legitimacy; a wider index (including paywalled records) fills coverage gaps DOAJ intentionally excludes.

## Trust & verifiability
`trust: trusted` — an independent non-profit whitelist with transparent inclusion criteria, standard in the research community. Records are reliable; still disambiguate authors carefully before attributing a paper to your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | directory-of-open-access-journals |
| category | archives-cache |
| selectorsIn → selectorsOut | name → employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
