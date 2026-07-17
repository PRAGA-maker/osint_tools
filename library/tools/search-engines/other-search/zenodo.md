---
id: zenodo
name: Zenodo
description: Use when you have a `name` (or research topic) and want the person's datasets, software, papers and affiliations — returns creator records with ORCID, employer/affiliation and linked outputs.
url: https://zenodo.org/
category: search-engines
path:
- search-engines
- other-search
bestFor: Finding a researcher's published datasets, code and papers — with ORCID and affiliation — in a free open-access repository.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free and open access, operated by CERN and OpenAIRE. No account needed to search or download; an account is only required to upload.
opsec: passive
opsecNote: Searching is anonymous public browsing; the subject is not notified. A REST API exists for scripted queries if you want to avoid manual browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and operated by CERN and OpenAIRE — a reputable, long-running scholarly infrastructure; records include DOIs and often ORCID, making authorship verifiable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- zenodo.org
tags:
- academic
- research
- datasets
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Zenodo

> CERN/OpenAIRE's open research repository — a way to tie a person to their datasets, code and papers, complete with ORCID and institutional affiliation.

## When to use
Your subject is (or may be) a researcher, academic, developer, or student. You have a `name` and want to enumerate their scholarly output — datasets, software releases, preprints, presentations — and pull the identifying metadata attached to it: ORCID, listed affiliation (`employer-org`), co-authors (`associate`), and dated DOIs. Good for confirming a claimed identity, mapping a professional network, or establishing where and when someone worked.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://zenodo.org/ and search the subject's `name` (try name variants and add a discipline keyword to cut noise).
2. Open a matching record and read the metadata block:
   - creators (often with clickable ORCID),
   - affiliation / community,
   - upload date and version history,
   - description, funding, and linked/related identifiers.
3. Follow the ORCID out to the person's full publication profile; note co-authors as `associate` leads.
4. Pivot: affiliation → institutional directory/staff page; ORCID → ORCID.org profile; DOI/version dates → timeline of activity. For bulk work, use the REST API.

## Inputs → Outputs
- **In:** `name` (or topic/keyword)
- **Out:** research records with creator `name`(s), ORCID, `employer-org` affiliation, and dated `document-id` outputs (DOIs)
- **Empty/negative result looks like:** no records, or only same-name false matches — Zenodo only holds what researchers chose to deposit, so absence means "nothing deposited here," not "not a researcher." Disambiguate common names via ORCID/affiliation before trusting a hit.

## Gotchas & OpSec
- Passive and anonymous — safe to search freely.
- Self-deposited and lightly curated: anyone can upload, so a record's *claims* (title, affiliation) are only as good as the depositor. ORCID/DOI raise confidence.
- Name collisions are common; always disambiguate with ORCID or affiliation before attributing work to your subject.

## Overlaps ("do both")
- Complements general scholarly search (Google Scholar, ORCID, institutional repositories): Zenodo surfaces datasets and software that paper-centric engines often miss, while those catch journal articles Zenodo lacks. Run both.

## Trust & verifiability
`trust: trusted` — the platform is authoritative infrastructure (CERN/OpenAIRE) and records carry DOIs and frequently ORCID, so authorship is verifiable; the caveat is that deposits are self-submitted, so verify the *content* of a record, not just its presence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zenodo |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
