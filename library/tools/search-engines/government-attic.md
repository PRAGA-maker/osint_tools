---
id: government-attic
name: Government Attic
description: Use when you have a `name`, agency or topic and want FOIA-released US federal documents about it — returns declassified/released government records that can name people and events.
url: https://www.governmentattic.org/
category: search-engines
path:
- search-engines
bestFor: Browsing an archive of FOIA-released US government documents you won't find via normal search.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- name
status: live
pricing: free
costNote: Free public archive; no account, no fees. Documents are PDFs you can read/download directly.
opsec: passive
opsecNote: You browse and download static PDFs from a public archive — nothing about the subject is queried live and no one is alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-running archive of genuine FOIA-released records; documents are primary-source government material, verifiable by their release letters/agency provenance.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- governmentattic.org
- Government Attic FOIA
tags:
- toddington
- curated-directory
- specialty-search
- foia
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Government Attic

> An eclectic archive of FOIA-released US federal documents — primary-source records (reports, manuals, correspondence, investigations) that rarely surface in a web search.

## When to use
You're researching a US federal agency, program, official, contractor, or incident and want the underlying documents — internal reports, IG investigations, personnel/policy records, correspondence — that were released under FOIA. Useful for corroborating a person's government role, finding named individuals in official records, or grounding a claim in primary material rather than secondary reporting.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.governmentattic.org/ and open the documents listing.
2. Browse by agency/topic, or use your browser/site search (and a `site:governmentattic.org` Google query) to find a `name`, `employer-org`, program, or keyword.
3. Open the PDF and read it as primary source — note release dates, agency, and any named individuals or case identifiers (`document-id`).
4. Pivot: named people → people-search / professional records; a program or case number → further FOIA requests or agency sources; corroborate a claim against the actual released text.

## Inputs → Outputs
- **In:** `name`, agency/`employer-org`, program, or keyword
- **Out:** FOIA-released US government PDFs (records that may name people, roles, and events) → `document-id`, `name` leads
- **Empty/negative result looks like:** no matching document — the archive is a curated, finite collection, not a comprehensive index, so most topics won't be present. Absence here means "not in this archive," not "no such record exists"; consider a direct FOIA request or other document sources.

## Gotchas & OpSec
- Coverage is idiosyncratic and finite — it's a hand-built collection of interesting releases, not a searchable index of all FOIA output. Don't infer anything from absence.
- Documents are often old and heavily redacted; treat redactions as gaps and dates as historical.
- Fully passive — static PDFs from a public site.

## Overlaps ("do both")
- Do both with FOIA reading rooms (agency FOIA libraries, FOIA.gov), the Internet Archive, and MuckRock: Government Attic surfaces specific released documents, while those cover broader/newer releases and let you request records that aren't yet public.

## Trust & verifiability
`trust: trusted` — the documents are authentic FOIA-released government records (primary sources), verifiable via their agency provenance and release letters; the curator adds no interpretation, so the material stands on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | government-attic |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → document-id, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
