---
id: github-recon
name: GitHub-Recon
description: Use when you have a `username`, `email`, `name`, or `domain` and want to dork GitHub for leaked identity data — returns real names, `email`s and profiles from commits, code and configs.
url: https://github.com/TheBinitGhimire/GitHub-Recon
category: search-engines
path:
- search-engines
bestFor: A dorking methodology/reference for surfacing secrets, emails, and real-identity leads from public GitHub activity.
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- email
- username
- social-profile
status: live
pricing: free
costNote: Free reference repository of GitHub dorks/techniques; GitHub search itself is free (some code-search features want a logged-in account).
opsec: passive
opsecNote: Searching public GitHub is passive — the target isn't notified. Running code-search often needs you to be logged in, which ties queries to that GitHub account; use a sock-puppet account, not your real one. You are reading published data, not accessing anything private.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A community reference (methodology, ~124 stars), not an executable tool. The techniques are sound; the data you find is real public GitHub content, verifiable in-repo.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gitrob
- trufflehog
- github-search
aliases:
- GitHub Recon
- GitHub-Recon
tags:
- github-dorking
- code-search
- leaks
- methodology
source: gh-topic-intelligence-gathering
lastVerified: '2026-07-17'
enrichment: full
---

# GitHub-Recon

> A playbook for mining GitHub: the dorks and techniques that turn a username, email, or domain into real names, secondary emails, and leaked secrets hiding in public code and commit history.

## When to use
Your subject is (or might be) a developer, or a target `domain`/organisation has code on GitHub. Developers routinely leak their real `name` and personal `email` in commit metadata, and hardcode credentials, internal hostnames, and other data in public repos. This reference teaches how to search GitHub systematically — by author, by email, by domain, by secret patterns — to pivot a `username`/`email` to a real identity and to surface an org's exposure. It's methodology you apply in GitHub's own search, not a program you run.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the repo at https://github.com/TheBinitGhimire/GitHub-Recon for the dork catalogue and workflow.
2. Apply the dorks in GitHub search (log into a sock-puppet GitHub account for full code-search): search a `username`'s repos/commits, an `email` (`author-email`), a `domain`, or secret keywords (`password`, `api_key`, etc.).
3. Inspect commit metadata (`git log` / commit author fields) — this is where real names and personal emails leak.
4. Verify any secret/lead in the actual repo before relying on it.
5. Pivot: a real `name`/`email` from commits feeds people-search and breach lookups; a leaked credential/domain feeds the technical side; the GitHub profile itself is a `social-profile` to cross-reference.

## Inputs → Outputs
- **In:** `username`, `email`, `name`, or `domain`
- **Out:** real `name`s and `email`s (from commits), `username`/`social-profile` links, leaked secrets/config
- **Empty/negative result looks like:** no meaningful hits — the subject isn't active on GitHub, uses a masked/`noreply` commit email, or the org keeps code private. Absence isn't proof they don't code.

## Gotchas & OpSec
- Many developers use GitHub's `@users.noreply.github.com` masked commit email — you may get a username but not a personal address.
- OpSec: passive to the target, but code-search wants a login — use a burner GitHub account so queries aren't tied to you.
- Treat any discovered secret ethically/legally; finding it is recon, using it is not.

## Overlaps ("do both")
- Pairs with `[[trufflehog]]` / `[[gitrob]]` (automated secret scanning of repos) and `[[github-search]]` — use this methodology to know *what* to search, those tools to scale the scanning.

## Trust & verifiability
`trust: community` — a reference repo, not a maintained tool; the techniques are standard and the data you find is genuine public GitHub content you can confirm in the repo/commit history yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-recon |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, domain → email, username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
