---
id: eyedex
name: EyeDex
description: Use when you have a `name`, filename, or keyword and want files sitting in public open directories — returns matching files across indexed open-directory servers.
url: https://www.eyedex.org/
category: documents-metadata
path:
- documents-metadata
bestFor: Searching publicly-exposed open directories for files by name/keyword across many servers at once.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to search; no account. It indexes links to files on open directories — it does not host them.
opsec: passive
opsecNote: Searching EyeDex's index is passive and doesn't alert anyone. But *opening* a found file downloads it from a stranger's open directory over your IP and can expose you to malware or illegal content — do that only in a sandbox/VM on a sock-puppet IP, if at all.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party crawler of open directories with no accountable operator; results point to unvetted files on random servers, so treat everything as untrusted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- eyedex
- eyedex.org
- open directory search
tags:
- file-search
- open-directory
- documents-metadata
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# EyeDex

> An open-directory search engine — indexes files exposed on misconfigured/public web servers so you can search petabytes of them by name or keyword.

## When to use
You're hunting for a specific file that may have been left in a public "open directory" (a web server listing its files with no index page) — leaked documents, media, backups, datasets that mention your subject. EyeDex crawls these directories across hundreds of servers and lets you search by `name`/filename/keyword, returning direct links to the files. It's a niche discovery surface that normal search engines under-index.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.eyedex.org/.
2. Search a `name`, filename fragment, or keyword tied to your subject/case.
3. Scan results: filenames, sizes, and the host server/directory they live on.
4. Before opening anything, switch to a disposable VM on a sock-puppet IP — files come from unknown servers.
5. Pivot: filenames, folder paths, and embedded metadata (`document-id`, dates, names) become new selectors.

## Inputs → Outputs
- **In:** `name` / filename / keyword
- **Out:** links to matching files in open directories (`document-id`, sizes, host paths)
- **Empty/negative result looks like:** no matches — the file isn't in EyeDex's crawl of open directories; that's the common case, so absence proves little. Try alternate filenames/keywords.

## Gotchas & OpSec
- **Untrusted content:** results are files on strangers' servers — expect malware risk, illegal material, and dead links. Never open on your working machine.
- Coverage is opportunistic (whatever open directories it found) — far from comprehensive.
- OpSec: **passive** to search; *downloading* is an active, risky pull over your IP — sandbox it.

## Overlaps ("do both")
- Complements other file/open-directory search engines and general dorking — each crawls a different slice of the open-directory space, so run more than one when chasing a specific file.

## Trust & verifiability
`trust: unverified` — an anonymous, opaque crawler pointing to unvetted files; useful as a lead source, but verify provenance and handle every result defensively.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eyedex |
| category | documents-metadata |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
