---
id: oryon-osint-query-tool
name: Oryon OSINT Query Tool
description: Use when you have a `name`, `username`, `email`, or `domain` and want a spreadsheet that auto-builds investigation query links across dozens of services — returns targeted search URLs.
url: https://docs.google.com/spreadsheets/d/1_x3PXGOahhKT3-ePaWhb3hM1dVxjmBvsVlw6D6lilTQ/edit
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: One spreadsheet that turns a single selector into ready-made query links across many OSINT services.
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free public Google Sheet; make your own copy (File > Make a copy) to use it.
opsec: passive
opsecNote: Type selectors into YOUR OWN copy of the sheet — don't edit the shared master. Link generation is passive; you only expose yourself when you open a generated link, so do that from a sock-puppet browser/IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained Google Sheet (from the Oryon OSINT browser project); it only assembles links, so trust rests on the destination services.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Oryon OSINT QueryTool
- oryon query tool
tags:
- other-resources
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Oryon OSINT Query Tool

> A shareable Google Sheet that turns one selector into pre-built query links across reconnaissance, SOCMINT, domain, and darknet services — a link launcher, not a data source.

## When to use
Early in an investigation when you have a `name`, `username`, `email`, or `domain` and want breadth fast: paste the selector once and the sheet constructs the correct search URL for dozens of services so you can click through each. Useful as a checklist so you don't forget a platform.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the sheet, sign in to Google, and choose **File > Make a copy** so you have a private working copy.
2. Enter your selector into the designated input cell(s) — note the sheet's convention of replacing spaces with dots to preserve the hyperlink formulas.
3. The rows populate with clickable query links grouped by category (recon, SOCMINT, domain analysis, darknet, crypto).
4. Open the relevant links in a sock-puppet browser and work each result.
5. Pivot: feed discovered `social-profile`/`domain` hits into dedicated deep-dive tools.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, or `domain`
- **Out:** `social-profile`, `domain` (targeted query URLs across many services, not records)
- **Empty/negative result looks like:** the links populate but the destination services return nothing — the sheet always builds URLs, so "empty" is judged on each service, not the sheet.

## Gotchas & OpSec
- It **builds links only** — it never returns data itself. Evaluate results on each destination.
- Some listed services may be dead or changed since the sheet was last updated; a link that 404s means that service, not your query, is stale.
- Always work in your own copy so you don't clobber the shared master or leak your selectors to other viewers.

## Overlaps ("do both")
- Overlaps with `[[aware-online-com]]` and other query-builder hubs; do both, since each curates a different set of services and you want maximum platform coverage.

## Trust & verifiability
`trust: community` — a crowd-maintained spreadsheet; it only assembles queries, so verify every result on the service it points to and check that listed services are still live.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oryon-osint-query-tool |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, username, email, domain → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
