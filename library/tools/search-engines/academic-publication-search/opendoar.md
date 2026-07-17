---
id: opendoar
name: OpenDOAR
description: Use when you want to find academic open-access repositories for an institution, country, or subject — returns a directory of repositories (with links) where a person's theses, papers, or affiliation records may live.
url: https://v2.sherpa.ac.uk/opendoar/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Locating the open-access repository of a university/institution to search for a subject's academic output.
selectorsIn:
- employer-org
- name
selectorsOut:
- document-id
- employer-org
status: live
pricing: free
costNote: Free directory maintained by Jisc/SHERPA; no account required to search or browse.
opsec: passive
opsecNote: You browse a directory of repositories; no target is contacted. The actual document searches happen on the linked repositories. Fully passive at this stage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-running authoritative directory of open-access repositories run by Jisc (SHERPA services); it points to genuine institutional repositories.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Open DOAR
- Directory of Open Access Repositories
tags:
- academic
- open-access
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# OpenDOAR

> The authoritative directory of open-access academic repositories — a signpost to *where* an institution's theses, papers, and scholarly output are hosted, so you can go search them for a subject.

## When to use
Your subject has an academic footprint — a student, researcher, or academic — and you want their scholarly output (a thesis, dissertation, papers) which often carries a full name, affiliation, dates, advisors, acknowledgements, and sometimes a photo or bio. OpenDOAR doesn't search the papers itself; it tells you which open-access repository a given `employer-org` (university/institution), country, or subject discipline uses, so you can then search that repository directly. It's a navigation layer for academic OSINT, hence low direct relevance but a useful route to identity-rich documents.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://v2.sherpa.ac.uk/opendoar/ (the OpenDOAR service under SHERPA).
2. Filter by institution name (`employer-org`), country, or subject discipline to find matching repositories.
3. Open a listed repository and follow its link to the actual archive.
4. Search that repository for your subject's `name` to find theses/papers and their metadata (affiliation, dates, advisors, acknowledgements).
5. Pivot: a thesis → advisor/co-author `associate` links, department affiliation, and a timeline; named acknowledgements → further people; institution → alumni/staff directories.

## Inputs → Outputs
- **In:** an institution (`employer-org`), country, or discipline — plus the subject's `name` to search the destination repository
- **Out:** pointers to the right open-access repositories (which then yield `document-id`s and affiliation data)
- **Empty/negative result looks like:** no repository listed for a small institution/country — not every body runs an OA repository. Try the institution's own library site, or a discipline-wide archive, directly.

## Gotchas & OpSec
- It's a **directory, not a search engine** for papers — it finds repositories; you search for the person on the destination.
- Coverage skews toward institutions that run formal OA repositories; smaller or non-Western bodies may be absent.
- OpSec: **passive** at the directory; apply the repository's own considerations when you search it.

## Overlaps ("do both")
- Pairs with Google Scholar, BASE, and CORE (which search *across* repositories' contents) — OpenDOAR maps the repositories; those search their documents. Use OpenDOAR to pinpoint an institution's archive, the aggregators for broad content search.

## Trust & verifiability
`trust: trusted` — an authoritative Jisc/SHERPA-maintained directory pointing to genuine institutional repositories; the documents you ultimately find carry their own authority as academic records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opendoar |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, name → document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
