---
id: the-open-syllabus-project
name: The Open Syllabus Project
description: Use when you have an author `name` or a text/title and want to see which universities and courses assign it — returns employer-org (institutions) and teaching context.
url: https://www.opensyllabus.org/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Finding where a book, text or author is taught across universities, or profiling an academic by their assigned/authored works.
selectorsIn:
- name
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Core exploration tools (Explorer, Course Matcher) are free; a print store and some institutional analytics are paid but not needed for OSINT use.
opsec: passive
opsecNote: Queries a public research archive of aggregated syllabi; nothing touches any individual. Fully passive — no account, no subject notification.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A non-profit academic archive (Columbia-affiliated origins) of 30M+ syllabi widely cited in higher-ed research; data is aggregated and methodologically documented.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Open Syllabus
- opensyllabus.org
tags:
- academic
- syllabi
- education
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# The Open Syllabus Project

> A non-profit archive of 30M+ college syllabi — search a text or author to see which institutions and courses assign it, or profile an academic through the works tied to their teaching.

## When to use
Two OSINT angles. (1) You have an author or a specific work and want to know which universities/courses teach it — useful for tracing a person's intellectual footprint or influence. (2) You are profiling an academic `name` and want corroborating context: books they authored that appear on syllabi, or fields/institutions where their work is assigned. It is an **institution- and text-level** archive, not a professor directory — it surfaces what is taught and where, not per-instructor rosters.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.opensyllabus.org/ and launch the "Explorer".
2. Search a text `name`/title or an author `name`.
3. Read the results: how often the work is assigned, the "Teaching Score," the fields it appears in, and the institutions/countries where it shows up.
4. Use Course Matcher to see comparable courses across schools.
5. Pivot: an institution (`employer-org`) where an author is heavily taught → search that university's faculty pages; a co-assigned author → map an intellectual/associate network.

## Inputs → Outputs
- **In:** author or text `name`/title
- **Out:** assigning institutions (`employer-org`), fields, teaching frequency, associated authors/texts
- **Empty/negative result looks like:** a title with a near-zero teaching score or no matches — the work isn't (or is rarely) assigned in the corpus, which skews toward English-language and North-American/European syllabi.

## Gotchas & OpSec
- Corpus is a sample, not a census — heavily weighted to US/UK/anglophone institutions; absence ≠ never taught.
- It does not name individual instructors for a given course — do not expect professor-level attribution.
- Best as a corroborating/context source, not a primary identifier.
- OpSec: passive, no account needed.

## Overlaps ("do both")
- Complements academic-publication and faculty-directory searches: Open Syllabus shows *what is taught where*; those show *who teaches and who published*.

## Trust & verifiability
`trust: trusted` — an established non-profit academic archive with documented methodology and wide scholarly citation; figures are aggregate estimates from a large but non-exhaustive syllabus corpus.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-open-syllabus-project |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
