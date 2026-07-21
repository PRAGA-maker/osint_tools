---
id: debian-code-search
name: Debian Code Search
description: Use when you have an `email`, `username` or string and want to find it across all Debian-packaged source — returns author `name`/`email` and code context wherever it appears.
url: https://codesearch.debian.net
category: search-engines
path:
- search-engines
bestFor: Regex-searching the entire corpus of open-source software packaged in Debian for a string, identifier, or contributor.
selectorsIn:
- email
- username
- name
selectorsOut:
- email
- name
status: live
pricing: free
costNote: Free public service run by the Debian project; no account. Supports regex search across all source packages.
opsec: passive
opsecNote: You query Debian's public code index, not any target's infrastructure; no one is notified. Fully passive. Use a VPN if you want the query off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Debian project service indexing the source of tens of thousands of packages. Authentic first-party open-source records; attribution from commit/author metadata still needs corroboration.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- paste-debian
- chromium-code-search
aliases:
- codesearch.debian.net
- Debian code search
tags:
- toddington
- curated-directory
- specialty-search
- code-search
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Debian Code Search

> A regex search engine over the source of every package in Debian — one query sweeps tens of thousands of open-source projects for a string, identifier, or contributor.

## When to use
Your subject is an open-source developer, or you have a string (email, username, distinctive function name, internal domain) that might appear anywhere in widely-packaged open-source software. Because Debian packages a huge slice of the FOSS ecosystem, Debian Code Search casts a far wider net than a single-project search: it can surface a developer's author lines, copyright headers, and embedded identifiers across many projects at once.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://codesearch.debian.net and enter a search — it supports powerful **regex** (e.g. an email pattern, a handle, a rare string).
2. To find a person: search their email or username; look in copyright/AUTHORS headers and code comments for authorship.
3. Open results to see the package, file, and surrounding code; note which projects the identifier spans.
4. Record any additional emails/handles/domains that co-occur with your target string.
5. Pivot: a discovered email feeds email-OSINT/breach checks; a handle feeds cross-platform username tools; the spread of projects profiles the developer's involvement.

## Inputs → Outputs
- **In:** `email` / `username` / `name` / regex string
- **Out:** `email` and `name` of authors, code context, list of packages containing the string
- **Empty/negative result looks like:** no matches — the string isn't in any Debian-packaged source (the person's work isn't packaged, or they used a different identifier). Try `[[chromium-code-search]]`, GitHub search, and grep.app for other corpora.

## Gotchas & OpSec
- Scope is source *packaged in Debian* — not all of GitHub; niche or proprietary code won't appear.
- Author/copyright lines can be stale, delegated, or anonymised — corroborate before attributing an identity.
- Fully passive — you query Debian's public index, never the subject.

## Overlaps ("do both")
- Pairs with `[[chromium-code-search]]` and GitHub/grep.app code search — each covers a different corpus; running several is how you find a developer's full cross-project code footprint.

## Trust & verifiability
`trust: trusted` — an official Debian project service over authentic open-source source; the code is genuine, while identity attribution from author metadata still warrants corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | debian-code-search |
| category | search-engines |
| selectorsIn → selectorsOut | email, username, name → email, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
