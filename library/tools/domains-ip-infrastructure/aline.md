---
id: aline
name: Aline
description: Use when you have a `domain` and want the documents it has exposed to Google — a CLI that runs filetype dorks and bulk-downloads the hits for metadata analysis, returning files rich in `metadata-exif` and `document-id`.
url: https://github.com/ferreiraklet/Aline
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Bulk-harvesting a domain's Google-indexed files (PDF, DOCX, XLSX, etc.) by filetype so you can mine them for author names, usernames, and software metadata.
selectorsIn:
- domain
selectorsOut:
- metadata-exif
- document-id
status: live
pricing: free
costNote: Free, open-source Python CLI (ferreiraklet/Aline); no account or key.
opsec: active
opsecNote: Two active footprints — heavy Google querying can trigger CAPTCHAs/temporary blocks on your IP, and downloading each file hits the hosting server directly, appearing in the target's access logs. Run Google searches sparingly and pull downloads through a VPN/sock-puppet egress.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small but real open-source tool (~30 stars, active commit history); it wraps Google dorking and downloading, so trust the mechanism, verify each downloaded file's provenance yourself.
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
- google-bug-bounty-dorks-generator
aliases:
- ferreiraklet/Aline
tags:
- Domain/IP/Links
- Website's files metadata analyze and files downloads
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Aline

> A tiny Python CLI that turns "site:target.com filetype:pdf" into an automatic download run — pull every indexed document off a domain, then strip their metadata.

## When to use
You have a `domain` and want the **documents it has leaked to Google** — PDFs, Office files, spreadsheets, config dumps — because those files carry metadata (author names, usernames, internal paths, software versions, sometimes GPS) that pivots into people and infrastructure. Aline runs the filetype dork and downloads the results in one step, so you can move straight to metadata extraction.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/ferreiraklet/Aline && cd Aline && pip3 install -r requirements.txt`.
2. Run a dork against the target, e.g. `python3 aline.py -D "site:target.com ext:pdf" -o pdfs.txt -r 20`, or use `-d target.com -f pdf` for domain+filetype targeting.
3. Aline queries Google, collects matching links, and downloads the files locally (output list saved with `-o`).
4. Feed the downloaded documents into a metadata tool (EXIF/`metadata-exif` extractor) to pull author, creator software, and embedded usernames.
5. Pivot those author names/usernames into people-search and username tools.

## Inputs → Outputs
- **In:** `domain` (+ filetype/dork parameters)
- **Out:** a folder of downloaded files → `metadata-exif`, `document-id`, embedded author/username strings
- **Empty/negative result looks like:** zero links returned — Google indexed no such files, the dork is too narrow, or Google served a CAPTCHA and blocked the query (retry later / different egress).

## Gotchas & OpSec
- **Google will rate-limit/CAPTCHA** aggressive automated dorking from one IP; pace it and expect intermittent blocks.
- Downloads are **active** and logged by the file's host — don't pull sensitive infrastructure without authorization; route through a VPN.
- Downloaded files can themselves be booby-trapped (malicious PDFs/macros); handle in a sandbox VM.
- Coverage is only what Google has indexed — not a complete file inventory.

## Overlaps ("do both")
- Pairs with [[google-bug-bounty-dorks-generator]] — use the generator to design and expand the dorks by hand, then hand the productive filetype dorks to Aline to bulk-download at scale.

## Trust & verifiability
`trust: community` — a straightforward open-source wrapper around Google + downloads; the tool is transparent, but every file it pulls must have its provenance and metadata verified independently before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aline |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → metadata-exif, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
