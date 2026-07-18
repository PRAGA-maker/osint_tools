---
id: github-gist
name: GitHub gist
description: Use when you have a `username`, `email`, or keyword and want code/text snippets a person shared — returns gists that can leak `email`, credentials, and `social-profile` links.
url: https://gist.github.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a developer's shared snippets (and the secrets/identity crumbs in them) by author or keyword.
selectorsIn:
- username
- email
selectorsOut:
- email
- social-profile
status: live
pricing: free
costNote: Free to browse and search public gists; a GitHub account is only needed to create or star them.
opsec: passive
opsecNote: Reading public gists is passive and doesn't notify the author. Searching while logged into your real GitHub ties the activity to your account and can show in your history — use a sock-puppet account or log out for sensitive queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party GitHub service; the gists are authentic user-published content (though the accuracy of what's inside them is the author's, not GitHub's).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- github
aliases:
- gist.github.com
- GitHub Gist
tags:
- pastebins
- github
- code
- leaks
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# GitHub gist

> GitHub's snippet-sharing service — a pastebin developers use casually, which makes it a reliable source of leaked emails, tokens, and identity crumbs tied to a username.

## When to use
You have a developer's GitHub `username` (or a suspected one, or an `email`/keyword) and want to see what they've published as gists. Gists are where people paste config files, scripts, dotfiles, and quick notes — often containing hardcoded `email` addresses, API keys/tokens, internal hostnames, or links to other `social-profile`s. Useful for confirming a handle belongs to a real person and for pivoting from a coding identity outward.

## How to use it (`bestInteractionPattern`: web-manual)
1. For a known author: go to `https://gist.github.com/<username>` to list their public gists.
2. To search content: use GitHub's gist search (`https://gist.github.com/search?q=...`) or a site-scoped web search (`site:gist.github.com "term"`), querying an email, name, or keyword.
3. Open gists and read the raw content — check comments in code, commit history (gists are git repos), and revisions for data later edited out.
4. Note that a gist's revision history can expose secrets the author tried to remove.
5. Pivot: a leaked `email` feeds email-OSINT/breach checks; a linked handle feeds username search; the parent GitHub profile via [[github]].

## Inputs → Outputs
- **In:** `username` (author) or an `email`/keyword to search
- **Out:** public gists, and from them `email`, credentials/tokens, hostnames, and `social-profile` links
- **Empty/negative result looks like:** the user has no public gists, or your keyword returns nothing — they may keep snippets private or not use gists; check their main GitHub repos instead.

## Gotchas & OpSec
- Human-in-the-loop: none; open browsing.
- Gist search is weaker than repo/code search — combine it with `site:gist.github.com` web searches for better recall.
- Secret-hunting: check **revisions**, not just the current version — edited-out keys often remain in history.
- OpSec: passive and unnotifying; still search from a non-attributable account so it isn't tied to your real GitHub identity.

## Overlaps ("do both")
- Pairs with [[github]] — the profile/repos give the person's broader project footprint; gists catch the throwaway snippets (and leaks) that never made it into a repo.

## Trust & verifiability
`trust: trusted` — it's GitHub's own first-party service, so the gists are genuine author-published content; the *reliability of what a gist claims* is the author's, so verify any factual crumb independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-gist |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email → email, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
