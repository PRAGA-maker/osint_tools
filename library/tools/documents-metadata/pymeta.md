---
id: pymeta
name: PYMETA
description: Use when you have a `domain` and want to harvest usernames/author names from its public documents — searches the web for the org's files and extracts their metadata to a CSV.
url: https://github.com/m8sec/pymeta
category: documents-metadata
path:
- documents-metadata
bestFor: Discovering internal usernames, real names, software, and naming conventions from metadata in an organisation's public documents.
selectorsIn:
- domain
selectorsOut:
- name
- username
- metadata-exif
- employer-org
status: live
pricing: free
costNote: Free and open-source (Python; `pip3 install pymetasec`); requires exiftool. No account.
opsec: passive
opsecNote: pymeta queries Google/Bing for the documents (passive to the target — the search engines see the queries, the target site does not) and then downloads the files it finds. The download step fetches files from the hosting server, so there is light contact; route through a sock-puppet egress if the target must not see downloads.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A maintained open-source rewrite of PowerMeta (m8sec); popular in the recon community, inspectable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- crosslinked
aliases:
- pymeta
- pymetasec
tags:
- Image Search and Identification
- Exif Analyze and editing
- document-metadata
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# PYMETA

> A document-metadata harvester: it finds an organisation's public files via search engines, downloads them, and pulls the author names, usernames and software baked into their metadata.

## When to use
You have a `domain` (an employer, org, or personal site) and want to surface the people behind it: office documents, PDFs and spreadsheets routinely embed the author's real `name`, network `username`, and the software/OS used. pymeta automates the "search → download → extract" loop into a CSV, revealing usernames and naming conventions that feed account-enumeration and email-format guessing.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install pymetasec` and ensure `exiftool` is present.
2. Harvest a domain's documents: `pymeta -d example.com`.
3. Or analyse local files you already have: `pymeta -dir Downloads/`.
4. Open the `pymeta_report.csv` — review extracted authors, usernames, software/versions, and paths.
5. Pivot: extracted `username`s/`name`s feed username-enumeration and email-pattern guessing; software/versions hint at the org's tech.

## Inputs → Outputs
- **In:** `domain` (or a local directory of documents)
- **Out:** CSV of `name`s, `username`s, software/versions, paths (`metadata-exif`), tied to the `employer-org`
- **Empty/negative result looks like:** an empty/near-empty CSV — the org publishes few indexed documents, or its files were scrubbed of metadata.

## Gotchas & OpSec
- The search step is passive; the **download** step fetches from the host — use a sock-puppet egress if that matters.
- Metadata can be stale (old employees) or scrubbed (privacy-conscious orgs) — treat names/usernames as leads.
- Depends on search-engine coverage; pair with direct crawling if the site isn't well-indexed.

## Overlaps ("do both")
- Pairs with `[[crosslinked]]` (which scrapes LinkedIn for employee names) — pymeta gives usernames/real names from documents, crosslinked gives them from LinkedIn; combine to build the org's people/username map.

## Trust & verifiability
`trust: community` — open-source and inspectable; extracted metadata is factual (it's read straight from the files), though its accuracy about *current* personnel is not guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pymeta |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain → name, username, metadata-exif, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
