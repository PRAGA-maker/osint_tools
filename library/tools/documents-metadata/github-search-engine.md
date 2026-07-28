---
id: github-search-engine
name: GitHub Search Engine (Google CSE)
description: Use when you have a `username`, `email`, or `domain` and want to find leaked references across GitHub via a Google Custom Search — returns code/repo hits and `social-profile`/`domain` leads.
url: https://cse.google.com/cse?cx=1b053c8ec746d6611
category: documents-metadata
path:
- documents-metadata
bestFor: Full-text searching GitHub content through Google's index to surface leaked secrets, emails, and mentions.
selectorsIn:
- username
- email
- domain
selectorsOut:
- social-profile
- email
- domain
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account.
opsec: passive
opsecNote: Queries go to Google (which indexes GitHub), not to the repo owners, so this is passive and unattributed to the target. Because it uses Google's cache, it can even surface content since deleted from GitHub — good for you, but handle any exposed secrets responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Google CSE scoped to GitHub; results are Google's index, so quality is high but coverage lags GitHub's native, real-time search.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- GitHub Google CSE
- github custom search
tags:
- document-and-slides-search
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# GitHub Search Engine (Google CSE)

> A Google Custom Search Engine scoped to GitHub — full-text search of repos, code, and docs through Google's index, which sometimes surfaces content already deleted from GitHub itself.

## When to use
You have a `username`, `email`, `domain`, API key fragment, or other distinctive string and want to see whether it appears in public GitHub content — leaked credentials in commits, a developer's email in config files, internal hostnames, or a subject's coding footprint. Because it rides Google's index, it complements (and sometimes beats) GitHub's own search, especially for cached/removed content.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at https://cse.google.com/cse?cx=1b053c8ec746d6611.
2. Enter the selector — an `email`, `username`, `domain`, or a quoted secret pattern (e.g. `"AKIA"` for AWS keys, `"password="`).
3. Review results; each links to the GitHub page (or Google's cache) where the string appears.
4. Corroborate against GitHub's native search (`https://github.com/search`) which is real-time but indexes differently.
5. Pivot: a committer's `email`/`username` links to their GitHub `social-profile` and other repos; a leaked secret is a (responsibly handled) finding.

## Inputs → Outputs
- **In:** `username`, `email`, or `domain` (or any distinctive string)
- **Out:** `social-profile` (GitHub accounts), `email`, `domain` — code/repo hits containing the term
- **Empty/negative result looks like:** no results means Google hasn't indexed that string on GitHub — try GitHub's native search and vary the query; absence here isn't proof it's not on GitHub.

## Gotchas & OpSec
- Rides **Google's index**, so it lags GitHub's live state — new commits may not appear yet, and it can show cached/deleted content.
- Handle any exposed credentials/PII responsibly and legally; finding a secret doesn't authorize using it.
- Passive: repo owners aren't notified of your search.

## Overlaps ("do both")
- Do both this and GitHub's native code search — different indexes catch different hits; pair with dedicated secret-scanners for credential hunting.

## Trust & verifiability
`trust: community` — a third-party CSE over Google's index; results are real GitHub content you can open and verify directly, but coverage differs from GitHub's own search, so use both.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-search-engine |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, email, domain → social-profile, email, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
