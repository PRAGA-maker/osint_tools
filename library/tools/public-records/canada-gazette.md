---
id: canada-gazette
name: Canada Gazette
description: Use when you have a `name` or `employer-org` and want official Canadian public notices — returns bankruptcies, name changes, government appointments, and regulatory notices.
url: https://www.gazette.gc.ca/accueil-home-eng.html
category: public-records
path:
- public-records
bestFor: Searching the official Government of Canada record for public legal notices — insolvencies, legal name changes, appointments, and regulatory actions.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free to search and read online (1998–present; earlier issues via Library and Archives Canada). Only submitting a notice for publication carries a fee.
opsec: passive
opsecNote: Passive — you search a static official publication; no subject is notified and nothing leaks. Fully OpSec-safe; ordinary clean-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official newspaper of the Government of Canada; entries are authoritative primary-source public records published by the federal government.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- gazette.gc.ca
- Gazette du Canada
tags:
- public-records
- official-notices
- canada
- legal
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Canada Gazette

> The Government of Canada's official record — the authoritative place where legal notices (bankruptcies, name changes, appointments, regulations) are published, all free and searchable.

## When to use
You have a `name` or `employer-org` tied to a Canadian subject and want official, primary-source public notices about them: a personal insolvency/bankruptcy, a legal name change, a federal appointment, a company's regulatory action, or a proclamation. Because it's the government's own publication, a hit here is authoritative — strong corroboration for a person's status, timeline, or official dealings, useful in both people-tracing and background work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.gazette.gc.ca/accueil-home-eng.html.
2. Use standard or advanced search (publications 1998–present online; 1841–1997 via Library and Archives Canada).
3. Query the subject `name`, company, or keyword; narrow by Part I (notices, proposed regulations), Part II (regulations), or Part III (Acts).
4. Read the notice for names, dates, addresses, and the official action recorded.
5. Pivot: a bankruptcy/name-change notice feeds identity/timeline work; an appointment ties a person to a role/org; a company notice feeds corporate-registry research.

## Inputs → Outputs
- **In:** a `name`, `employer-org`, or keyword (Canada)
- **Out:** official public notices naming individuals/organizations — insolvencies, `name` changes, appointments, regulatory actions
- **Empty/negative result looks like:** no results means no matching *federally-gazetted* notice — many events are provincial or never gazetted, so absence here is not proof; check provincial gazettes and registries too.

## Gotchas & OpSec
- **Federal scope:** it carries federal notices; much personal legal activity (many name changes, provincial matters) appears in provincial gazettes/registries instead — don't treat absence as conclusive.
- Common names produce noise — corroborate a match with dates/addresses in the notice.
- Bilingual (English/French); some notices may be easier to find under the French heading.

## Overlaps ("do both")
- Pairs with provincial gazettes and Canadian corporate/insolvency registries — the Canada Gazette is the authoritative federal layer, and those cover the provincial and company-level records it doesn't.

## Trust & verifiability
`trust: trusted` — it is the official Government of Canada publication; entries are authoritative primary-source records, verifiable by their publication date and part reference.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canada-gazette |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
