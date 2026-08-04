---
id: code-repository-google-cse
name: Code Repository Google CSE
description: Use when you have a `username`, `email` or keyword and want to search across code-hosting sites at once — returns matching repos/code via a pre-built Google Custom Search.
url: https://cipher387.github.io/code_repository_google_custom_search_engines/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: One-shot Google Custom Search across ~15 code-repository services (GitHub, GitLab, Bitbucket, etc.) for leaked code, handles or secrets.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Google Custom Search Engine page hosted on GitHub Pages; no account. Subject to Google's normal search rate limits/captcha.
opsec: passive
opsecNote: Searches Google's index, not the repos directly, so it does not alert repo owners. Passive. Use a sock-puppet browser to avoid captcha attribution.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Built by cipher387, a well-known OSINT resource curator; it is a convenience wrapper over Google CSE, so results are as good as Google's index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- cipher387 code repository CSE
tags:
- Code
- custom-search-engine
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Code Repository Google CSE

> A pre-built Google Custom Search across ~15 code-hosting services — for finding a subject's code, handles, or leaked secrets in one query.

## When to use
You have a `username`, `email`, or distinctive keyword and want to sweep many code-hosting platforms at once for a subject's repositories, committed handles, or accidentally-committed secrets/credentials. Developers reuse usernames and leak identifiers in code, making this a useful pivot for technical subjects.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cipher387.github.io/code_repository_google_custom_search_engines/.
2. Enter the `username`, `email`, or keyword; the CSE queries GitHub, GitLab, Bitbucket and other code hosts via Google.
3. Review the results across platforms; open promising repos/profiles.
4. Pivot: a matched code account gives you commit emails, other repos, and often a real name in commit metadata.

## Inputs → Outputs
- **In:** `username`, `email`, or keyword
- **Out:** matching repos/profiles across code hosts (`social-profile` links)
- **Empty/negative result looks like:** no results — Google may not have indexed the content, or the identifier is not in public code; try a code-specific search (GitHub search) directly.

## Gotchas & OpSec
- Human-in-the-loop: Google may present a **captcha** on heavy use — solve manually.
- OpSec: passive (you query Google's index, not the repos).
- It relies on Google's index — recent or private content will be missed; complement with native platform search.

## Overlaps ("do both")
- Complements native GitHub/GitLab search and secret-scanning tools: this CSE casts a wide cross-platform net, native search and scanners go deeper on a single host.

## Trust & verifiability
`trust: community` — a convenience wrapper by a respected curator; reliability equals Google's coverage, so treat gaps as index limitations, not proof of absence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | code-repository-google-cse |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
