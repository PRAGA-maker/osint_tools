---
id: github-code-search
name: GitHub Code Search
description: Use when you have an `email`, `username`, domain or secret pattern and want to find it inside public code/commits on GitHub — returns matching code, repos and author `social-profile`s.
url: https://github.com/search?type=code
category: documents-metadata
path:
- documents-metadata
bestFor: Searching across public GitHub code and commits for emails, usernames, domains, hard-coded secrets, or a person's projects.
selectorsIn:
- email
- username
- domain
selectorsOut:
- social-profile
- email
status: live
pricing: free
costNote: Free; searching code requires being signed in to a (free) GitHub account.
opsec: passive
opsecNote: Searching public code is passive — the code authors aren't notified. Your queries are tied to your GitHub account, so use a dedicated/sock-puppet account, and treat any secrets you find as off-limits to actually use.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party GitHub search over real repositories; results are authoritative for what public code contains, though not exhaustive of all history.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- jsluice
- linkfinder
aliases:
- GitHub code search
tags:
- code-search
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# GitHub Code Search

> GitHub's own full-text code search — find where an email, username, domain, or secret pattern appears across millions of public repositories and commits, and whose projects contain it.

## When to use
A subject is (or might be) a developer, or an organisation's code is public: searching GitHub can surface their `email` in commit metadata, reused `username` handles, internal domains, project history, and — importantly — hard-coded secrets or references that leak infrastructure. It's also a fast way to tie a person to repositories and collaborators (`social-profile`, `associate`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in to a (dedicated) GitHub account and open https://github.com/search?type=code.
2. Query with qualifiers: a bare `email`/`username`/`domain`, or scoped searches like `"target@example.com"`, `user:handle`, `org:company`, `filename:.env`, `path:*.js "apikey"`.
3. Read matches in context; open the repo/commit to see author identity, dates and related files.
4. Check commit history and the author's profile/other repos for reuse of the same handle/email.
5. Pivot: an author `social-profile` and `email` feed username- and email-OSINT; endpoints/secrets feed `[[linkfinder]]`/`[[jsluice]]`-style analysis (surface only — never use found secrets).

## Inputs → Outputs
- **In:** an `email`, `username`, `domain`, filename or secret pattern
- **Out:** matching code/commits, repositories, and author `social-profile`/`email`
- **Empty/negative result looks like:** no hits means the term isn't in indexed *public* code — private repos, deleted history, or non-GitHub hosts won't appear; absence isn't proof of nonexistence.

## Gotchas & OpSec
- Human-in-the-loop: code search requires being logged in; queries are attributable to your account — use a puppet.
- Indexing isn't exhaustive of all history; combine with commit-search and mirrors for thoroughness.
- **Legal/ethical:** finding a secret is OSINT; using it to access anything is not — report/surface only.

## Overlaps ("do both")
- Pairs with dedicated secret-scanners and `[[linkfinder]]`/`[[jsluice]]` — GitHub search finds where things live in source, those analyse the endpoints/secrets within specific files.

## Trust & verifiability
`trust: trusted` — first-party GitHub search over real repositories; a match is authoritative for what the public code contains, though not a complete view of all code ever pushed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-code-search |
