---
id: ftp-google-dork
name: FTP Google Dork
description: Use when you have a `name`, filename or `domain` and want publicly indexed FTP-hosted files — returns exposed directory listings and document-ids on open FTP servers.
url: https://www.google.com/search?q=inurl%3Aftp+-inurl%3Ahttp+-inurl%3Ahttps+ftpsearchterm
category: search-engines
path:
- search-engines
- ftp-search
bestFor: Finding files, documents, or a person/company's name exposed on publicly indexed FTP servers via a Google dork.
selectorsIn:
- name
- domain
selectorsOut:
- document-id
- domain
status: live
pricing: free
costNote: Free — it is just a crafted Google query. No account or tooling beyond a browser.
opsec: passive
opsecNote: The search runs through Google; you never touch the FTP servers themselves, so nothing is disclosed to their owners. If you then OPEN a discovered ftp:// link you connect directly and reveal your IP — do that behind a VPN and only when appropriate.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A standard, widely-documented Google-dorking technique; reliability depends on Google's current indexing of ftp:// resources, which has thinned over the years.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- FTP dork
- inurl:ftp Google dork
tags:
- google-dorking
- ftp
- file-discovery
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# FTP Google Dork

> A Google dork that surfaces files sitting on open, indexed FTP servers — a way to find exposed documents, backups, or a name/company that shouldn't be public.

## When to use
You want to find files exposed on misconfigured or intentionally-public FTP servers — a `name`, a company, a filename, or a `domain` that appears in an indexed FTP directory. Useful for discovering leaked documents, exposed backups, media, or a subject's files where an FTP path was left open and Google crawled it.

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google, run a dork like `inurl:ftp -inurl:http -inurl:https "<search term>"` — replace `<search term>` with the `name`, filename, extension, or `domain` you're after.
2. Refine: add `intitle:"index of"` for directory listings, or `filetype:` / an extension (e.g. `pdf`, `xls`) to target document types.
3. Read the results: each hit is an indexed FTP path — open the listing to see filenames (`document-id`s) and the host `domain`.
4. Pivot: interesting filenames feed document analysis; the host domain feeds WHOIS/reverse-IP to attribute the server.

## Inputs → Outputs
- **In:** a `name`, filename, extension, or `domain` as the search term
- **Out:** indexed FTP directory listings — filenames/`document-id`s and host `domain`s
- **Empty/negative result looks like:** few or no results — Google indexes far fewer ftp:// resources than it once did, so a null result often reflects thin indexing rather than "nothing exposed." Try alternate dorks or a dedicated FTP search engine.

## Gotchas & OpSec
- Google's coverage of `ftp://` has **declined sharply** (many browsers and crawlers dropped native FTP), so this finds a shrinking slice — combine with purpose-built FTP indexers.
- Accessing files you find may be unauthorised depending on jurisdiction and context — discovery via search is passive, but **downloading** connects you directly to the host and can carry legal weight; proceed carefully and behind a VPN.
- Results are point-in-time cache entries; the live server may have changed or gone.

## Overlaps ("do both")
- Pair with dedicated FTP search engines and general Google dorking — the dork is quick and free, while specialised indexers catch FTP content Google no longer crawls.

## Trust & verifiability
`trust: community` — a legitimate, well-known technique, but it depends entirely on Google's indexing; verify any file by inspecting it directly (mindful of the OpSec/legal caveat) rather than trusting the snippet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ftp-google-dork |
| category | search-engines |
| selectorsIn → selectorsOut | name, domain → document-id, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
