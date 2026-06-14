---
id: ghintel-secrets-ninja
name: ghintel.secrets.ninja
description: Use when you have a GitHub username/email and want to surface a developer's commit-derived emails, repos, and identity intel.
url: https://ghintel.secrets.ninja/
category: email
path:
- email
bestFor: GitHub OSINT — pulling emails, repos, and identity signals tied to a GitHub user.
selectorsIn:
- username
- email
selectorsOut:
- email
- name
- social-profile
- username
status: unknown
pricing: free
costNote: Free web tool hosted under the secrets.ninja domain.
opsec: passive
opsecNote: Queries GitHub's public data via the tool's backend; the subject is not notified. The username/email you search is disclosed to the third-party site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community-hosted GitHub-intel tool on the secrets.ninja domain; not independently verified here. Treat as a convenience wrapper around public GitHub data and corroborate findings.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GHIntel
tags:
- email
- Email Related Sites
relatedTools:
- gitrecon
- ghunt
source: uk-osint
lastVerified: ''
enrichment: full
---

# ghintel.secrets.ninja

> A community web tool for GitHub OSINT — surfaces a developer's commit-derived emails, repositories, and identity signals from a GitHub handle.

## When to use
Your subject (or an associate) is a developer or has a `username` you suspect maps to a GitHub account. You want to extract the `email`(s) baked into their commit history, find their `name`, linked `social-profile`s, and other repos — useful pivots when standard people-search comes up empty for a technical person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ghintel.secrets.ninja/.
2. Enter the GitHub `username` (or an `email` to reverse-search, if supported).
3. Read the output: commit emails, associated repositories, profile metadata, and any linked accounts.
4. Pivot: feed extracted `email`s into breach-search and validation; feed `name`/handles into username-enumeration tools.

## Inputs → Outputs
- **In:** GitHub `username` (or `email`)
- **Out:** commit-derived `email`(s), `name`, `social-profile` links, related repos/`username`s
- **Empty/negative result looks like:** no commit emails exposed (user enabled GitHub's email privacy / used the noreply address), or the handle has no public activity.

## Gotchas & OpSec
- Commit emails are only exposed if the user did not enable GitHub's "keep my email private" setting; many show only `user@users.noreply.github.com`.
- This is a third-party wrapper — verify any email against GitHub directly before relying on it.
- OpSec: passive; nothing is sent to the subject, but your query is logged by the hosting site.

## Overlaps ("do both")
- Pairs with the CLI tool `[[gitrecon]]` (deeper, scriptable GitHub/GitLab harvesting) and is complementary to `[[ghunt]]` for Google rather than GitHub identities.

## Trust & verifiability
`trust: unverified` — community-hosted tool, not tested during enrichment. Its findings derive from public GitHub data and should be confirmed at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghintel-secrets-ninja |
| category | email |
| selectorsIn → selectorsOut | username, email → email, name, social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
