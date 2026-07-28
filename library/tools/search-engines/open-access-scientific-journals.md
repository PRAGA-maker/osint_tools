---
id: open-access-scientific-journals
name: Open Access Scientific Journals (PagePress)
description: Use when you have a `name` (an author/researcher) and want their open-access publications and affiliations from this OA publisher — returns name, employer-org, associate leads.
url: https://www.pagepress.org
category: search-engines
path:
- search-engines
bestFor: Finding a researcher's freely readable papers, affiliations, and co-authors within an open-access journal publisher.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Open-access publisher — articles are free to read in full; no account needed to search or read.
opsec: passive
opsecNote: Searching a public academic publisher is passive; you never contact the subject. Author names, affiliations, and emails printed in papers are self-published by the authors, but handle any contact details you find ethically.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: PagePress is one open-access publisher (primarily biomedical/scientific journals). Legitimate but narrow — it indexes only its own titles, so treat it as one source among many, not a comprehensive scholarly search.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- open-access-scholarly-journals
- google-scholar
tags:
- academic-resources-and-grey-literature
- open-access
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Open Access Scientific Journals (PagePress)

> An open-access academic publisher whose full-text articles are free to read — useful for pulling a researcher's papers, affiliations, and co-authors when your subject is an academic.

## When to use
Your subject is (or claims to be) a researcher/academic and you want to confirm publications, current/past `employer-org` affiliation, co-authors (`associate`), and sometimes a contact email printed on a paper. Because it's open access, you get the full text, not just an abstract behind a paywall. Its scope is limited to this publisher's own (largely biomedical) journals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to pagepress.org and use the search for the author `name` (or a paper title/keyword).
2. Open matching articles; read the author block for affiliation, corresponding-author email, and co-authors.
3. Note dates to place the person at an institution during a period.
4. Because coverage is narrow, always re-run the name on a broad scholarly index.
5. Pivot: an affiliation → institution directory; a co-author → the wider research network; an ORCID/email → people search.

## Inputs → Outputs
- **In:** `name` (author) or title/keyword
- **Out:** `name` (co-authors), `employer-org` (affiliation), `associate` (collaborators), sometimes a contact email
- **Empty/negative result looks like:** no hits — very likely because the person simply didn't publish with *this* publisher, not that they've never published. Confirm on a comprehensive index before concluding.

## Gotchas & OpSec
- **Narrow index:** this is a single publisher; absence here says almost nothing. Use it to enrich, never to rule out.
- Affiliations reflect the time of publication and may be out of date.
- Passive; treat any contact details ethically and lawfully.

## Overlaps ("do both")
- Always pair with `[[google-scholar]]` (comprehensive cross-publisher search) and `[[open-access-scholarly-journals]]`; those give breadth, this gives free full text within its own titles.

## Trust & verifiability
`trust: community` — a legitimate OA publisher, but scope-limited. Author-supplied metadata is generally reliable; verify affiliation/identity across multiple publications and a broad index.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-access-scientific-journals |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
