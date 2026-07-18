---
id: searchcode
name: Searchcode
description: Use when you have a `username`, `email` or distinctive string and want to find it in public source code — returns code files across GitHub/GitLab/Bitbucket that expose handles, contacts and leaked secrets.
url: https://searchcode.com/
category: search-engines
path:
- search-engines
- code-search
bestFor: Full-text search across billions of lines of public code for a name, handle, email, or leaked string.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
- email
status: live
pricing: freemium
costNote: Free to search on the web; an API is offered (currently free during beta / no key for basic use). No account needed for manual searches.
opsec: passive
opsecNote: Searchcode queries its own index, so the developer/repo whose code you find is not notified. Note that searching for a live secret (API key, password) that you then use would be active and possibly illegal — treat found secrets as evidence, do not exercise them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running independent code-search engine indexing public repositories; results are real code, but its index is a subset of all public code and can lag GitHub's live state.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- searchcode.com
- searchcode source
tags:
- code-search
- source-code
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Searchcode

> A free full-text search engine over public source code — the fast way to find a handle, email, or leaked string across GitHub, GitLab, Bitbucket and more.

## When to use
You have a `username`, `email`, real name, or a distinctive string (an internal hostname, a project codename, a phone number) and want to know if it appears in **public code**. Developers leave a rich footprint in repositories: commit author names/emails, hardcoded contact addresses, personal handles in comments and configs, and sometimes accidentally committed secrets. Searchcode lets you grep all of that at once without cloning anything — useful for tying a coder identity together, or for spotting a leak tied to a target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://searchcode.com/.
2. Search the selector — quote an `email` (`"john@example.com"`), a `username`, a full name, or a unique string.
3. Use filters (language, source/repository) to narrow; the results show the matching file, surrounding context, and a link back to the source repo.
4. Open the source repo to pull more: the author's other commits, their GitHub/GitLab profile (`social-profile`), and other emails/handles they use.
5. Pivot: a discovered email/handle feeds email/username OSINT; a leaked secret is evidence to document (and, if it's the subject's own exposure, to flag) — never actually use it.

## Inputs → Outputs
- **In:** `username`, `email`, real name, or distinctive string
- **Out:** matching public code files → developer `social-profile`, additional `email`s/handles, repo links, and any exposed strings/secrets
- **Empty/negative result looks like:** no matches — the term isn't in Searchcode's indexed public code (it may still be on GitHub live; Searchcode indexes a subset), or the person doesn't publish code. Also try GitHub's own code search and Grep.app.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — you're reading an index; no repo owner is alerted. But if you *use* a discovered credential, that becomes active and likely unlawful — document, don't exploit.
- Its index is a **subset** of public code and can be stale relative to GitHub; a blank here doesn't mean the string is nowhere. Cross-check with GitHub code search / grep.app.
- Common strings return huge noisy result sets — quote exact values and use language/source filters.

## Overlaps ("do both")
- Do both with GitHub's native code search and other code-search engines — indexes and freshness differ, so each catches repos the others miss. Feed any surfaced developer profile into username/email tools.

## Trust & verifiability
`trust: community` — an independent engine returning real, inspectable code (verify by opening the linked repo); reliability is limited only by index coverage and freshness, not by data fabrication.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchcode |
| category | search-engines |
| selectorsIn → selectorsOut | username, email → social-profile, email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
