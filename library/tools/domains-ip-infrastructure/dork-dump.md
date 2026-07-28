---
id: dork-dump
name: DORK DUMP
description: Use when you have a `domain` and want the public documents Google has indexed on it — downloads them and returns their `metadata-exif`.
url: https://github.com/dievus/msdorkdump
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Harvesting a domain's Google-indexed files (pdf/doc/xls/ppt…) and extracting their embedded metadata.
selectorsIn:
- domain
selectorsOut:
- metadata-exif
- name
status: live
pricing: free
costNote: Free and open-source (GPL-3.0). Runs locally; no account or API key.
opsec: active
opsecNote: The document search is Google-dork queries (passive against the target). But it then downloads each file, so the target's web server / CDN sees direct download requests from your IP. Run behind a VPN/proxy if attribution matters.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Open-source Python tool by researcher "dievus" (~200 GitHub stars); auditable but maintained by one author.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- geemail-user-finder
- mayorsecdnsscan
- oh365userfinder
aliases:
- msdorkdump
- MSDorkDump
tags:
- document-metadata
- google-dorking
- metadata-extraction
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# DORK DUMP

> A Python tool that Google-dorks a domain for public documents, downloads them, and runs ExifTool over each — turning "files on their website" into names, usernames, software, and timestamps.

## When to use
You have a `domain` connected to your subject (their organisation, small business, club, personal site) and you want everything Google has indexed on it in the common office/PDF formats. Document metadata is a classic OSINT goldmine: `Author`/`Creator` fields leak real `name`s and usernames, `Company` fields leak `employer-org`, and creation software/paths can hint at the machine that made the file. Genuinely useful in missing-person work when the subject or their contacts published documents.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/dievus/msdorkdump && cd msdorkdump`.
2. Install deps: `pip3 install -r requirements.txt` (Linux users also install `exiftool`; it's bundled for Windows).
3. Run: `python3 msdorkdump.py -t example.com -d` — `-t` sets the target domain, `-d` downloads the files it finds.
4. It issues Google `site:example.com filetype:pdf` (and doc/docx/xls/xlsx/ppt/pptx/csv) queries, downloads hits into a folder, and prints ExifTool metadata for each.
5. Pivot: `name`/username from `Author` fields feeds people- and username-search; `Company`/`employer-org` feeds corporate lookups.

## Inputs → Outputs
- **In:** `domain`
- **Out:** downloaded documents plus their `metadata-exif` (Author, Creator, Company, software, timestamps), which often yield a `name`
- **Empty/negative result looks like:** Google returns no indexed files for the domain (small/new/robots-blocked sites), or the files carry scrubbed/empty metadata — no author fields to pivot on.

## Gotchas & OpSec
- Human-in-the-loop: Google rate-limits automated dorking; run too fast and queries start timing out or returning CAPTCHAs — pace it or run in smaller batches.
- OpSec: downloading the files is **active** — the host logs your IP fetching each document; use a VPN/proxy for sensitive targets.
- Only sees what Google has *indexed*; combine with a direct site crawl for completeness.

## Overlaps ("do both")
- Pairs with `[[amass]]` — Amass finds the subdomains/hosts, DORK DUMP harvests the documents (and metadata) indexed on them.
- Related to `[[mayorsecdnsscan]]` and `[[oh365userfinder]]` in the same domain-recon workflow.

## Trust & verifiability
`trust: community` — small open-source project; the code is readable and the metadata it reports comes straight from ExifTool on the actual downloaded files, so results are verifiable against the source documents.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dork-dump |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → metadata-exif, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (rate-limit) |
