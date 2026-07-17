---
id: tmdn-design-view
name: TMDN Design View
description: Use when you have an `employer-org`/`name` or design number and want registered industrial designs and their owners across the EU and beyond — returns document-id and owner.
url: https://www.tmdn.org/tmdsview-web/
category: public-records
path:
- public-records
bestFor: Searching millions of registered/applied industrial designs across EU national offices, EUIPO and international partners, and reading each design's owner/applicant.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- employer-org
- name
status: live
pricing: free
costNote: Free official consultation tool operated by the EU IP network (EUIPO + national offices); no account required.
opsec: passive
opsecNote: Read-only search of an official public register; the design owner is not notified. Safe from any browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official EU IP Network / EUIPO service aggregating participating offices' registers; the ownership and status data are authoritative for the offices covered.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- DesignView
- EUIPO DesignView
- tmdn.org DesignView
tags:
- Brand/trademark information search
- designs
- intellectual-property
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# TMDN Design View

> The EU IP network's free DesignView — one search across national, EUIPO and international registered-design databases, with owner and imagery.

## When to use
You want to tie a person or company to registered industrial/product designs, or to trace who owns a design. DesignView lets you search millions of designs by design number, applicant/owner `name` or `employer-org`, product indication (Locarno class), and more, across dozens of participating offices in one place. Useful for corroborating a business identity, tracing IP a subject controls, or finding company affiliations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tmdn.org/tmdsview-web/.
2. Search by applicant/owner `name`/`employer-org`, design number, or product indication; filter by office/territory.
3. Open a design record: representation images, owner/applicant `name`, application/registration numbers (`document-id`), dates, status, and the office.
4. Note that ownership/applicant name and status are official register data for that office.
5. Pivot: an owner company feeds corporate-registry and trademark (TMview) OSINT; a design number anchors a filing; a designer/representative is an `associate` lead.

## Inputs → Outputs
- **In:** owner/applicant `name`/`employer-org`, design number, or product indication
- **Out:** design records — `document-id` (filing numbers), owner/applicant `employer-org`/`name`, images, dates, legal status
- **Empty/negative result looks like:** no designs for the name/number — the party holds no registered design in the covered offices, or the name is spelled differently in the filing.

## Gotchas & OpSec
- Coverage is the **participating offices** — broad (EU + many international partners) but not every jurisdiction on earth.
- Owner names reflect the filing; corporate owners and holding entities may mask the individual.
- It covers designs only — use the sister TMview for trademarks.

## Overlaps ("do both")
- Pairs with TMview (trademarks) and national corporate registries — DesignView gives the design + owner, those connect the owner to marks and company officers.

## Trust & verifiability
`trust: trusted` — an official EU IP Network/EUIPO service aggregating national registers; ownership and status data are authoritative for the offices covered.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tmdn-design-view |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → document-id, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
