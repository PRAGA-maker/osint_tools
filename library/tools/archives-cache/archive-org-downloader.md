---
id: archive-org-downloader
name: Archive-org-Downloader
description: Use when you have an archive.org `document-id`/URL for a borrow-only book and want the full text offline — returns a downloaded PDF you can then read for names, addresses and other leads.
url: https://github.com/MiniGlome/Archive.org-Downloader
category: archives-cache
path:
- archives-cache
bestFor: Downloading full borrow-only books/documents from archive.org as a searchable PDF instead of the 1-hour/14-day online loan.
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free, open-source Python script. Requires a free archive.org account (email + password) — no payment.
opsec: active
opsecNote: You must log in with an archive.org account, so the download is tied to that identity — use a dedicated sock-puppet account, never a personal one. The script "borrows" the item under your account to fetch the page images, which archive.org logs. Downloading many items quickly can trip rate limits or account flags.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source utility (MiniGlome) that automates archive.org's own lending viewer; it does not alter content, only stitches the borrowed page images into a PDF.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
relatedTools:
- waymore
aliases:
- Archive.org-Downloader
- MiniGlome archive downloader
tags:
- Archives
- Tools for working with web archives
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Archive-org-Downloader

> A Python script that turns a borrow-only archive.org book into a full offline PDF, so a scanned yearbook, directory, or local-history volume becomes searchable evidence instead of a 1-hour loan.

## When to use
You have found a relevant scanned item on archive.org — an old telephone/city directory, school yearbook, church or genealogy record, local newspaper run, out-of-print reference — that is "borrow only" (viewable one hour to 14 days, no download button). You want the whole thing offline to OCR/search for a subject's `name`, `address`, `associate`, employer, or `dob`.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install deps: `pip install -r requirements.txt` (needs Python 3, `requests`, `tqdm`, `img2pdf`).
2. Have a free archive.org account ready (use a sock-puppet one).
3. Run against the item URL:
   `python3 archive-org-downloader.py -e sock@puppet.tld -p 'Passw0rd' -r 0 -u https://archive.org/details/<item-id>`
   - `-r 0` = highest image resolution (largest file); raise the number for smaller/faster.
   - `-u` a single URL, or `-f file.txt` for a list of URLs, `-d` for output directory, `-j` to keep JPGs instead of PDF.
4. Open the resulting PDF, OCR it if needed, and search for your selectors.
5. Pivot: names/addresses pulled from a directory feed people-search and public-records tools; use `[[waymore]]` when the lead is a web page rather than an archive.org item.

## Inputs → Outputs
- **In:** an archive.org item `document-id`/URL (single, or a file of URLs)
- **Out:** a downloaded PDF (or JPG set) of the full item — a `document-id` you now hold locally and can mine for `name`, `address`, `associate`
- **Empty/negative result looks like:** an auth error ("must have a registered account") means the login failed; a permissions error means the item is not lendable/is fully restricted, not that the tool broke.

## Gotchas & OpSec
- **Human-in-the-loop: account-login.** A valid archive.org login is mandatory; the fetch is attributable to that account, so isolate it.
- Respect copyright/lending terms — this bypasses the loan window, so treat downloads as investigative working copies, not for redistribution.
- Bulk runs can be rate-limited or flagged; space them out.

## Overlaps ("do both")
- Pairs with `[[waymore]]` — WayMore maps a domain's archived web footprint, while this pulls full borrow-only archive.org documents; use WayMore for sites and this for scanned books/records.

## Trust & verifiability
`trust: community` — a widely used open-source script that only automates archive.org's authorised lending viewer; the PDF is a faithful copy of the scan, so verifiability rests on archive.org's own provenance for the item.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archive-org-downloader |
| category | archives-cache |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
