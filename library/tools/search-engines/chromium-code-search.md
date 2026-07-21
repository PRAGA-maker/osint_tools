---
id: chromium-code-search
name: Chromium Code Search
description: Use when you have an `email`, `username` or string and want to find it in the Chromium source tree — returns committer `name`/`email` and code context where the string appears.
url: https://source.chromium.org
category: search-engines
path:
- search-engines
bestFor: Searching the vast Chromium/Chrome open-source codebase for a string, symbol, contributor, or leaked identifier.
selectorsIn:
- email
- username
- name
selectorsOut:
- email
- name
status: live
pricing: free
costNote: Free public code browser hosted by Google; no account. Searchable via web UI.
opsec: passive
opsecNote: You query Google's public code-search index, not any target's own infrastructure; the person whose string you search is not notified. Fully passive. Use a VPN if you want the query off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's official code browser for the Chromium project. The code and commit metadata are authentic first-party open-source records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- source.chromium.org
- cs.chromium.org
- Chromium code search
tags:
- toddington
- curated-directory
- specialty-search
- code-search
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Chromium Code Search

> Google's fast, indexed browser of the Chromium source tree — search hundreds of millions of lines for a string, symbol, contributor email, or leaked identifier.

## When to use
Your subject is a software developer who has contributed to Chromium/Chrome (or you have a string — an email, handle, internal hostname, or distinctive identifier — that might appear in that codebase). Source code and commit metadata routinely expose real names, emails (AUTHORS/OWNERS files, commit authorship), usernames, and organisational fingerprints. This is a targeted way to tie a person to contributions and to surface identifiers embedded in code.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://source.chromium.org and enter your search — plain string, symbol name, or regex (it supports powerful filtering by path/file).
2. To find a person: search their suspected email or username; check OWNERS/AUTHORS files and blame/commit history for authorship.
3. Open a result to see the file, surrounding code, and (via git history links) the committer name/email and dates.
4. Note any additional emails, handles, or organisation domains revealed alongside your target string.
5. Pivot: a committer email feeds email-OSINT and breach checks; a handle feeds `[[sherlock]]`/`[[whatsmyname]]`; a contribution timeline corroborates employment/skills.

## Inputs → Outputs
- **In:** `email` / `username` / `name` / code string
- **Out:** `email` and `name` of committers, code context, contribution history
- **Empty/negative result looks like:** no matches — the string isn't in Chromium's tree (the person likely never contributed there, or used a different identity). Absence here says nothing about other codebases; try GitHub search, `[[debian-code-search]]`, and grep.app.

## Gotchas & OpSec
- Scope is Chromium/Chrome only — a developer active elsewhere won't appear; this is one codebase, not all code.
- Commit emails can be role/no-reply addresses or intentionally anonymised — corroborate before attributing.
- Fully passive — you query Google's public index, never the subject.

## Overlaps ("do both")
- Pairs with `[[debian-code-search]]` (all Debian-packaged source) and GitHub/grep.app code search — each indexes a different corpus, so run several to find a developer's full code footprint.

## Trust & verifiability
`trust: trusted` — Google's first-party, authoritative view of the open-source Chromium tree; the code and commit metadata are genuine, though identity attribution from commit emails still needs corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chromium-code-search |
| category | search-engines |
| selectorsIn → selectorsOut | email, username, name → email, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
