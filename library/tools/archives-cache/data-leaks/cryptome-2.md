---
id: cryptome-2
name: Cryptome
description: Use when you have a `name`, agency, or topic and want primary-source leaked documents and dossiers — returns filings, cables, dossiers, and disclosure files.
url: https://cryptome.org/
category: archives-cache
path:
- archives-cache
- data-leaks
bestFor: Full-text (Google-scoped) search of a long-running archive of leaked and prohibited primary-source documents.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- document-id
- associate
status: live
pricing: free
costNote: Free and open; no account. The site is a flat document archive funded by donations/document sales, not a paywall.
opsec: passive
opsecNote: Reading Cryptome is passive, but the archive hosts sensitive/classified material — accessing certain documents may itself be noteworthy on a monitored network. Use a clean browser/VPN, and be aware some files are large or contain live personal data. Use only the primary domain; the operators warn mirrors may be tampered with.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established since 1996 (John Young); a curated but independent archive — documents are primary sources of varying provenance, not editorially verified facts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wikileaks
- wikileaks-search
- gi-files
- leaked-cables
aliases:
- cryptome.org
- Cryptome archive
tags:
- leaks
- primary-sources
- documents
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Cryptome

> One of the oldest leak archives on the web — a flat, donor-run repository of prohibited documents, dossiers, and primary-source disclosures searchable via Google.

## When to use
You have a `name`, an `employer-org` (agency, company, facility), or a topic and want original documents rather than reporting about them — court filings, government cables, intelligence records, surveillance material, facility drawings, and dossiers on public figures. Cryptome is strongest for corroborating a claim with the underlying paper trail, or finding a named person inside a leaked disclosure that never made mainstream news.

## How to use it (`bestInteractionPattern`: web-manual)
1. The site has no rich internal search, so query Google scoped to the domain: `site:cryptome.org "<name>"` (or an agency/topic term).
2. Alternatively browse the dated index at https://cryptome.org/ — entries are listed reverse-chronologically with cryptic filenames.
3. Open the document (often a PDF, ZIP, or raw HTML) and read for the subject's name, role, associates, dates, and any document identifiers.
4. Preserve anything relevant immediately (download a copy) — archive entries can be removed by court order.
5. Pivot: names/associates found feed people-search; a document/case `document-id` feeds court-record lookups; an agency feeds further primary-source searches.

## Inputs → Outputs
- **In:** `name` / `employer-org` / topic keyword
- **Out:** primary-source documents naming the subject, `associate` links, `document-id`s (case/cable numbers)
- **Empty/negative result looks like:** no `site:` hits — the subject is not named in the indexed archive. Because Google indexes "most not all" of Cryptome, absence is weak evidence; a manual browse of the relevant date range may still surface something.

## Gotchas & OpSec
- Search is only as good as Google's coverage of the site; some files are unindexed, so combine `site:` search with manual index browsing.
- Documents are primary sources of mixed provenance — authenticate before treating as fact, and note some contain unredacted personal data.
- Use only `cryptome.org`; the operators explicitly warn that mirrors may be altered.

## Overlaps ("do both")
- Pairs with `[[wikileaks-search]]` and other leak archives — Cryptome and WikiLeaks hold different corpora, so a name absent from one may appear in the other; run both when building a document trail.

## Trust & verifiability
`trust: community` — a genuine, long-lived independent archive; the documents are authentic primary sources but unvetted and of varying reliability, so verify provenance before relying on any single file.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cryptome-2 |
| category | archives-cache |
| selectorsIn → selectorsOut | name, employer-org → name, document-id, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
