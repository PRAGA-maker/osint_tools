---
id: gitcolombo
name: Gitcolombo
description: Use when you have a GitHub `username`, repo or org URL and want the real names/emails behind its commits — returns name, email and correlated associate identities.
url: https://github.com/soxoj/gitcolombo
category: social-networks
path:
- social-networks
bestFor: Extracting contributor names, emails and cross-account identity links from a git repo, user or org's commit history.
selectorsIn:
- username
- domain
selectorsOut:
- name
- email
- associate
- username
status: live
pricing: free
costNote: Free and open source (MIT). No paid tier; the only cost is an optional GitHub API token to raise rate limits.
opsec: passive
opsecNote: Reads public commit metadata via git and the GitHub API — it never contacts the subject and leaves no trace on their profile. Authenticated API calls are tied to YOUR token, so use a sock-puppet GitHub account/token, not your real one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: By soxoj (author of Maigret), a well-regarded OSINT developer; open source and auditable on GitHub.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- maigret
- socid-extractor
- marple
- osint-namecheckers-list
- mailto-analyzer
- 1c-database-converter
- awesome-osint-mcp-servers
- counter-osint-guide-for-russians
- fravia-soxoj
- maigret-via-socid-extractor-soxoj-ecosystem
- username-generation-guide
aliases:
- gitcolombo
- soxoj gitcolombo
tags:
- Social Media
- Github
- git-metadata
- email-extraction
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Gitcolombo

> A soxoj CLI (and browser build) that mines git commit history to surface the real names and emails behind contributors and correlate seemingly unrelated accounts.

## When to use
You have a GitHub `username`, or a specific repo/org URL, and want the identities behind the code: the real `name`s and `email` addresses commit authors used, plus links where one email maps to several display names or one person committed under multiple accounts. Developers routinely leak a personal email or legal name in commit metadata even when their profile is pseudonymous — this extracts it.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install gitcolombo` (needs Python 3.10+ and the `git` binary), or use the no-install web build at gitcolombo.soxoj.com for a single repo.
2. Scan a repo: `gitcolombo -u https://github.com/soxoj/maigret`
3. Scan every public repo of a user: `gitcolombo --nickname octocat`
4. Scan a local clone (recursively): `gitcolombo -d ./maigret -r`
5. Read the output: per-person names, emails, author/committer counts, and correlations — emails sharing a name, different names tied to one email.
6. Pivot: feed a recovered `email` into `[[mailto-analyzer]]` / breach lookups; feed a recovered `username`/`name` into `[[maigret]]` and `[[socid-extractor]]`.

## Inputs → Outputs
- **In:** GitHub `username`, or a repo/org URL (`domain`)
- **Out:** commit-author `name`s, `email`s, correlated `associate` identities, per-account statistics
- **Empty/negative result looks like:** contributors show only `noreply@github.com` / `users.noreply.github.com` emails and GitHub handles — the account used GitHub's email-privacy feature, so no personal email leaked.

## Gotchas & OpSec
- GitHub's "keep my email private" replaces real emails with `<id>+<user>@users.noreply.github.com`; those are dead ends for personal email but still confirm the account link.
- Rate limits: unauthenticated GitHub API runs hit caps fast on large orgs — add a token, but use a burner account's token.
- Squash-merge and rebase workflows can collapse or rewrite authorship; the metadata reflects what's in history, which may be edited.
- OpSec: passive — the subject is never notified.

## Overlaps ("do both")
- Pairs with `[[maigret]]` and `[[socid-extractor]]` — Gitcolombo gets the real name/email out of commits; those two expand a recovered handle across the wider web.

## Trust & verifiability
`trust: community` — open-source (MIT) tooling from a respected OSINT author; every claim it makes is reproducible from the git log you can inspect yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gitcolombo |
| category | social-networks |
| selectorsIn → selectorsOut | username, domain → name, email, associate, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
