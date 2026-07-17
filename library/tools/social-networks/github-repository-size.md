---
id: github-repository-size
name: GitHub Repository Size
description: Use when you have a GitHub `social-profile`/repo and want its total size and per-file/folder sizes shown inline — a browsing aid, not a person lookup (no selectors out).
url: https://chrome.google.com/webstore/detail/github-repository-size/apnjnioapinblneaedefcnopcjepgkci
category: social-networks
path:
- social-networks
bestFor: Seeing a GitHub repository's total size and each file/folder's size directly on the repo page before cloning or triaging it.
selectorsIn:
- social-profile
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome/Edge extension; uses the public GitHub API. Anonymous use is rate-limited; adding a token raises limits.
opsec: passive
opsecNote: The extension calls GitHub's public API for the repo you're viewing — the same data anyone sees. If you add a personal access token to raise rate limits, that token ties the calls to your account; use a throwaway GitHub account's token for sensitive triage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A small third-party open-source browser extension; low-risk (read-only repo metadata) but unaffiliated with GitHub — review its permissions before installing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- GitHub repo size extension
tags:
- Social Media
- Github
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# GitHub Repository Size

> A lightweight browser extension that adds total-repo and per-file size figures to any GitHub repo page — a triage convenience when a subject's code repositories are part of the investigation.

## When to use
You are examining a subject's or organisation's GitHub presence (`social-profile`) and want to size up their repositories before downloading — spotting the large repos, the bulky binary/data blobs, or oddly heavy files worth inspecting (leaked datasets, media, archives) without cloning everything. A minor but genuine efficiency tool for GitHub-centric OSINT.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store (works in Chromium browsers).
2. Navigate to any GitHub repository page.
3. The extension displays the repo's total size in the header and appends a size column to the file/folder listing.
4. Use the sizes to prioritise which files/folders to open, download, or clone.
5. Pivot: an unexpectedly large data/media file is a lead — download and examine it (metadata, contents) with your usual tools.

## Inputs → Outputs
- **In:** `social-profile` (a GitHub repo/user page you're viewing)
- **Out:** none about a subject — it renders total and per-file sizes to guide your review.
- **Empty/negative result looks like:** sizes don't render — usually GitHub API rate-limiting (add a token) or a UI change the extension hasn't caught up with; refresh or check for an update.

## Gotchas & OpSec
- Depends on GitHub's public API and page structure; either changing can break it — verify against the repo's own "Download ZIP" size if in doubt.
- Anonymous API calls are rate-limited; a token raises limits but should be from a throwaway account.
- OpSec: passive read-only metadata; review the extension's requested permissions before installing any third-party add-on.

## Overlaps ("do both")
- Complements GitHub's native search and code-search OSINT — this only sizes what you're already viewing; use it alongside tools that find the repos and mine their contents.

## Trust & verifiability
`trust: community` — a small unaffiliated extension surfacing public GitHub metadata; low-stakes and cross-checkable against GitHub's own figures.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-repository-size |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
