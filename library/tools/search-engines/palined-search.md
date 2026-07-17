---
id: palined-search
name: Palined Search
description: Use when you have a filename, `name`, or keyword and want to find open web/FTP directories exposing files (documents, media, backups) — returns links to indexed open directories.
url: http://palined.com/search/
category: search-engines
path:
- search-engines
bestFor: Finding open directories and exposed files via crafted Google queries for a filename or keyword.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free query-builder front end; it constructs Google searches (open-directory dorks), so it relies on Google, not its own index. No account.
opsec: passive
opsecNote: The search itself runs through Google and is passive. But downloading files from a stranger's open directory can expose you to malware and to server logs — fetch through a sandbox/VPN and never execute retrieved files.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A simple community query-builder that automates open-directory Google dorks; it adds no index or verification of its own, and any files found are unvetted third-party content.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- filepursuit-com
- opendirsearch-abifog-com
- google-ftp-search
aliases:
- Palined Search
- palined.com/search
- open directory search
tags:
- toddington
- specialty-search
- open-directory
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Palined Search

> A query-builder that turns a keyword or filename into Google "open directory" dorks — a fast way to surface exposed web/FTP folders and the files sitting in them.

## When to use
You want files rather than pages: a leaked document, a specific filename, media, or backups that someone left in a publicly-listed directory. Palined constructs the fiddly Google queries (index-of / open-directory patterns combined with your term) that expose these folders. Tie it to a `name`, a project, a distinctive filename, or a document type and it can surface material that never appears in normal search — old CVs, spreadsheets, photo dumps, or config/backup files.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://palined.com/search/ and enter your keyword/filename, choosing the file type or open-directory pattern.
2. Run the generated Google query; results are directory listings and direct file links.
3. Preview cautiously — note filenames, dates, and paths before downloading anything.
4. Retrieve files only through a sandbox/VPN; never open executables or macros from an unknown directory.
5. Pivot: a found document's metadata (`metadata-exif`, author, org) feeds identity/employer leads; a directory's path/host feeds infrastructure lookups.

## Inputs → Outputs
- **In:** `name`, filename, or keyword (+ optional file type)
- **Out:** links to open directories and exposed files (`document-id`) matching the query
- **Empty/negative result looks like:** no directory hits — nothing relevant is publicly listed/indexed, or your dork is too narrow; broaden the term or try another open-directory tool.

## Gotchas & OpSec
- It's a Google front end: results are only as good as Google's current index and dork behaviour; effectiveness varies as Google changes.
- Legal/ethical care: "publicly listed" is not "authorised to take" — mind the legal line before downloading, and don't access anything credential-protected.
- Malware risk: files in open directories are unvetted; sandbox everything and never execute.
- OpSec: the search is passive, but file downloads hit third-party servers that log requests — use a VPN.

## Overlaps ("do both")
- Pairs with `[[filepursuit-com]]`, `[[opendirsearch-abifog-com]]`, and `[[google-ftp-search]]` — each builds/searches open-directory and FTP indexes differently, so run the same filename through several to catch folders any one misses.

## Trust & verifiability
`trust: unverified` — a thin convenience wrapper over Google dorks with no index or vetting of its own; useful for discovery, but every file it surfaces is unverified third-party content to handle with care.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | palined-search |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
