---
id: grep-app
name: grep.app
description: Use when you have a `username`, `email`, `domain` or other string and want to find it committed in public code — returns the repos/files (and `social-profile` handles) that contain it.
url: https://grep.app/
category: documents-metadata
path:
- documents-metadata
bestFor: Regex/exact search across a half-million public GitHub repositories to find a leaked email, handle, key or domain hardcoded in code.
selectorsIn:
- username
- email
- domain
selectorsOut:
- social-profile
- domain
- email
status: live
pricing: free
costNote: Free to use with no account. Rate-limited on heavy automated use.
opsec: passive
opsecNote: You query grep.app's index, not GitHub or the target directly, so the developer whose code you search is not notified. Passive; only your search terms are disclosed to grep.app.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-known code-search engine (now "Grep by Vercel"), listed in Bellingcat's investigation toolkit; results link to the real public repositories so every hit is verifiable at source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Grep by Vercel
- grep app code search
tags:
- code-search
- github
- documents-metadata
source: bellingcat-toolkit
lastVerified: '2026-07-22'
enrichment: full
---

# grep.app

> Fast exact-string and regex search across ~500k public GitHub repositories — the way to find a username, email or domain that someone hardcoded and forgot.

## When to use
You have a distinctive selector — a `username`, `email`, personal `domain`, API key fragment, or an unusual string — and you suspect it may appear in public source code, config files or commit content. grep.app finds it across public repos in seconds, which can tie a developer's real name to a handle, surface a personal email in a commit, or reveal infrastructure hostnames.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://grep.app/.
2. Type the string, or enable **Use regular expression** (RE2) for patterns; toggle **Match case** / **Match whole words** as needed.
3. Filter the results by repository, path, or programming language to cut noise.
4. Open a hit to read it in context on grep.app, then click through to the real GitHub file/repo to verify and see surrounding commits, author and email.
5. Pivot: an author name/email on a matching repo feeds people-search; a leaked `domain`/host feeds infrastructure tools.

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, or any code/string (optionally regex)
- **Out:** matching public repos/files, and via those the committer's `social-profile`/`email` and referenced `domain`s
- **Empty/negative result looks like:** "No results" — the string is not in grep.app's indexed public repos; it is not proof it isn't in private code or unindexed repos.

## Gotchas & OpSec
- Indexes public GitHub only — a miss does not rule out private repos or other forges (GitLab, Bitbucket).
- Heavy automated querying can hit rate limits; for scale, use the official GitHub code search as a complement.
- OpSec: passive; no repo owner is notified of your search.

## Overlaps ("do both")
- Pairs with GitHub's own code search and with username-enumeration tools — grep.app's regex catches patterns GitHub's search misses, and vice versa.

## Trust & verifiability
`trust: trusted` — a reputable engine (Grep by Vercel) cited in Bellingcat's toolkit; every result links back to the authoritative public repo so you can confirm it firsthand.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | grep-app |
