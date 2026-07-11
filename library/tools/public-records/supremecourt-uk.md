---
id: supremecourt-uk
name: supremecourt.uk (UK Supreme Court cases)
description: Use when you have a `name` and want to check if they are a party in a UK Supreme Court case — returns case parties, document-id citations, and associate links.
url: https://www.supremecourt.uk/current-cases/index.html
category: public-records
path:
- public-records
bestFor: Searching UK Supreme Court current and decided cases for parties, case status, and full judgments.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: free
costNote: Free and publicly accessible; case lists, details, and judgments are all free to read with no account.
opsec: passive
opsecNote: Public court information — searching does not notify parties and reveals only your IP to the court site. Fully passive; a sock-puppet browser is optional and only for broader case hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party UK judiciary (The Supreme Court of the United Kingdom); authoritative case and judgment records.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- canadian-legal-information-institute
- bailii
aliases:
- UK Supreme Court
- UKSC
- supremecourt.uk
tags:
- court
- legal
- case-law
- uk
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# supremecourt.uk (UK Supreme Court cases)

> The UK's highest court's own case database — party names, case status, and full judgments for appeals reaching the Supreme Court.

## When to use
You have a `name` and want to know whether the person (or a company/body linked to them) is a party in a case that reached the UK Supreme Court — the apex court for civil matters UK-wide and criminal matters in England, Wales and NI. A Supreme Court appeal is high-profile and well-documented: the case page and judgment name the parties (`associate`s: co-appellants, respondents, interveners) and lay out the dispute, giving a solid identity and timeline anchor. Note only a small number of cases ever reach this level.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.supremecourt.uk/current-cases/index.html.
2. Use the search box (exact terms, names, or phrases) and/or filter by status, date, and area of law.
3. Open a matching case for the parties, UKSC reference (`document-id`, e.g. `UKSC/2026/0072`), area of law, and summary; for decided cases, read the full judgment (neutral citation like `[2024] UKSC 7`).
4. Pivot: parties and interveners are `associate` leads; the neutral citation lets you pull the full judgment on BAILII/The National Archives Find Case Law; a company party feeds Companies House.

## Inputs → Outputs
- **In:** `name` (party or organization)
- **Out:** case name and parties, UKSC/neutral-citation `document-id`, `associate` links (co-parties, interveners, counsel), case status/dates
- **Empty/negative result looks like:** no hits — the vast majority of people never appear before the Supreme Court, so absence tells you almost nothing about wider legal history (check lower-court databases instead).

## Gotchas & OpSec
- Extremely narrow coverage — only cases granted permission to reach the Supreme Court. For most litigation, use lower-court/tribunal sources (BAILII, Find Case Law).
- Common names need disambiguation; confirm via the case facts before attributing to your subject.
- OpSec: passive — public court records, no notification to anyone.

## Overlaps ("do both")
- Pairs with [[bailii]] (broad UK & Irish case law across all courts) and, for other jurisdictions, [[canadian-legal-information-institute]] — use the Supreme Court site for apex cases and BAILII for everything below it.

## Trust & verifiability
`trust: trusted` — first-party UK judiciary. Case records and judgments are authoritative; the only analytic risk is name disambiguation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | supremecourt-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
