---
id: societe-ninja
name: societe.ninja
description: Use when you have a `name` or `employer-org` tied to France and want to map a person to French companies they run or are registered against — returns `employer-org`, officer `name`, registered `address` and filed documents.
url: https://www.societe.ninja/
category: public-records
path:
- public-records
bestFor: Free search of the French company register (SIRENE/RCS) by company or by director/officer name.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free public-data search; company fiches, actes (incorporation docs) and bilans (financial statements) are downloadable at no cost. Beneficial-ownership (bénéficiaires effectifs) register is legally gated to lawyers/notaries/journalists.
opsec: passive
opsecNote: You query a third-party aggregator of open French registry data; nothing reaches the target. The operator (cybertron.fr) sees your IP and search terms — use a sock-puppet browser/IP if the investigation is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent French project (cybertron.fr) re-serving official INSEE/INPI open data; the underlying records are authoritative but the presentation layer is third-party, so confirm critical facts against the official source.
missingPersonsRelevance: high
coverage:
- fr
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- pappers
aliases:
- societe ninja
- cybertron societe
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# societe.ninja

> A free, fast front-end to the French company register — pivot a person's name into the companies they direct, own, or are registered against.

## When to use
Your subject has a France nexus (French address, employer, or a French-sounding business) and you need to tie a `name` to registered companies, or work the other direction from an `employer-org` to its officers and registered `address`. Because you can search **by director/officer**, this turns a bare name into a corporate footprint: incorporations, active/dormant status, registered offices, and filed documents (actes and bilans) that often carry a date of birth month/year, home-adjacent registered address, and co-directors (associates).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.societe.ninja/ in a clean/sock-puppet browser.
2. Choose your search mode:
   - **Simple/keyword** — type a company name or a person's `name`.
   - **Advanced** — filter by NAF/APE activity code, status (active/radiée), or dirigeant (officer).
3. Run the search and open a company **fiche**: read the SIREN/SIRET, registered `address`, NAF code, status, and the list of dirigeants/officers.
4. Download **actes** (incorporation/statutes) and **bilans** (accounts) where available — these documents often name co-directors, capital contributors, and month/year of birth for officers.
5. Pivot: an officer `name` + registered `address` feeds people-search and electoral/address tools; co-directors are `associate` leads; the company itself feeds `[[pappers]]` for cross-checking.

## Inputs → Outputs
- **In:** `name` (as company or officer), `employer-org`, or `address`
- **Out:** `employer-org` records, officer/`name` lists, registered `address`, downloadable documents (actes, bilans)
- **Empty/negative result looks like:** no fiches returned, or only unrelated companies — the person may hold no French registration, may use a variant spelling, or the business is a sole trader (micro-entreprise) with thin filings.

## Gotchas & OpSec
- Human-in-the-loop: none for ordinary search; the **bénéficiaires effectifs** (beneficial-ownership) register is restricted by French law to avocats, notaires, huissiers, comptables and journalistes, requested via email — don't expect it on a normal lookup.
- OpSec: **passive** — the target is never contacted; only the site operator sees your queries.
- It re-serves open data; a slightly stale or mis-parsed fiche is possible — confirm anything decision-critical against the official INPI/data.gouv source.

## Overlaps ("do both")
- Pairs with `[[pappers]]` — both wrap the French register; cross-check officer lists and dates between them, and use whichever exposes the specific document (acte vs. bilan) you need.

## Trust & verifiability
`trust: community` — an independent project surfacing authoritative INSEE/INPI open data. The source records are official, but because a third party parses and presents them, verify names, dates, and addresses against the primary register before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | societe-ninja |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
