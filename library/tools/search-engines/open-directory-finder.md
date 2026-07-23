---
id: open-directory-finder
name: Open Directory Finder
description: Use when you have a `name`, filename, or keyword and want files sitting in exposed "open directory" web listings — returns direct links to documents, images, video, and archives.
url: https://odfinder.github.io/
category: search-engines
path:
- search-engines
bestFor: Finding files exposed in publicly-listed open directories via ready-made search-engine dorks.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free web tool; it builds and launches dork queries against public search engines, no account required.
opsec: passive
opsecNote: Building/running the search is passive (queries go to Google/Bing, not the file hosts). But CLICKING a resulting open-directory link connects you directly to that server, which logs your IP — treat that step as active and use a clean/VM browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community front end (odfinder.github.io) that constructs open-directory dork queries; the tool is simple and transparent, but the files it surfaces are unvetted and may be malicious or illegal.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-advanced-search
- filepursuit
aliases:
- ODfinder
- Open Directory Search
tags:
- open-directories
- dorks
- file-search
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Open Directory Finder

> A query-builder for open directories — turn a name or filename into search-engine dorks that surface publicly-exposed folder listings full of downloadable files.

## When to use
You are hunting for files that someone put on a web server with directory listing left on — leaked documents, a subject's uploaded media, backups, or archives that never got a proper page. Open Directory Finder assembles the "index of" style dorks for you, filtered by content type (documents, images, audio, video, software, archives), so you can find a `name` or filename sitting in an exposed directory.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://odfinder.github.io/.
2. Enter your term (a `name`, filename, or keyword) and pick a content-type category and Loose vs Strict matching.
3. Launch the generated query; it opens a search engine with the open-directory dork applied.
4. Review the hits — genuine open directories show a bare "Index of /" file listing.
5. Pivot: download only in an isolated VM; a recovered document → run `[[exiftool]]`/metadata tools; a directory path → explore parent folders for more.

## Inputs → Outputs
- **In:** `name`, filename, or keyword (+ content type)
- **Out:** links to open-directory listings and the files inside them (`document-id`/media)
- **Empty/negative result looks like:** only normal web pages, no "Index of" listings — nothing is exposed for that term, or search engines have de-indexed the directory.

## Gotchas & OpSec
- It's a dork builder, not an index — results are whatever the search engine returns; refine terms and try Loose/Strict both ways.
- Files in open directories are unvetted: assume some are malware, copyrighted, or illegal. Download only in a sandbox and within your authority.
- OpSec: querying is passive, but opening an open-directory link connects you straight to that server (which logs you) — use a clean/VM browser for that step.

## Overlaps ("do both")
- Pairs with `[[google-advanced-search]]` (write your own `intitle:"index of"` dorks for control) and `[[filepursuit]]` (a dedicated open-directory/file search index) — use all three to catch directories each misses.

## Trust & verifiability
`trust: community` — a transparent community query-builder; it reliably constructs the dorks, but makes no claim about the safety or legality of the files it surfaces — verify and sandbox everything.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-directory-finder |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
