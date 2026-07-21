---
id: gitleak
name: GitLeak
description: Use when you have a GitHub `username` and want the email address(es) they used to author commits — returns `email` (and thereby a real-name / employer pivot).
url: https://gitleak.io
category: social-networks
path:
- social-networks
bestFor: Turning a GitHub handle into the committer email addresses buried in that user's public commit history.
selectorsIn:
- username
selectorsOut:
- email
- name
status: live
pricing: free
costNote: Free web tool; also exposes a public API. No account required for basic username lookups.
opsec: passive
opsecNote: It reads public commit metadata via GitHub's data, not the target's private account, and does not notify the user. The email is already public in the commit log — this just aggregates it. Query from a sock-puppet session anyway.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small independent utility that surfaces commit-author emails GitHub already exposes; the data is authentic (it comes from the commits themselves), but the site is third-party.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- gitleak.io
- GitHub commit email finder
tags:
- github
- email-discovery
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# GitLeak

> A web tool that mines a GitHub user's public commit history to reveal the email address(es) attached to their commits — a fast `username` → `email` pivot for anyone technical.

## When to use
Your subject has a GitHub `username` and you need a real email address to move the investigation forward (email → breach data, other accounts, real name, employer). Git commits carry the author's email in their metadata, and unless the user enabled GitHub's private-email/noreply setting, that address is public in every commit — GitLeak collects it for you instead of you cloning repos and grepping the log by hand.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gitleak.io in a sock-puppet browser.
2. Enter the target's GitHub `username` and search.
3. Read the returned email address(es). Personal addresses (e.g. `firstname.lastname@gmail.com`) often leak a real name; corporate addresses leak an `employer-org`.
4. Optionally use the site's API to script the same lookup across a list of handles.
5. Pivot: run each recovered `email` through breach-lookup and account-existence tools (`[[account-live-com]]`, `[[behindtheemail-com]]`, HaveIBeenPwned-style checks) and through email→name reversers.

## Inputs → Outputs
- **In:** GitHub `username`
- **Out:** committer `email` address(es); frequently a `name` inferable from the address or the git author name
- **Empty/negative result looks like:** no emails returned — the user has GitHub's "keep my email private" enabled (commits show `...@users.noreply.github.com`), has no public commits, or the handle doesn't exist.

## Gotchas & OpSec
- A `noreply.github.com` result is a dead end for real email, but the numeric prefix still uniquely identifies the GitHub account.
- The git *author name* field is user-set and can be fake; the email is harder to fake but may be an old/burner address.
- OpSec: passive — the data is already public in the commit log and no notification is sent. Still, don't email or contact the address from an attributable account.

## Overlaps ("do both")
- Pairs with GitHub-profile and cross-platform username tools that map the handle's repos/activity, while this specifically extracts the email hidden in the commits.

## Trust & verifiability
`trust: community` — third-party site, but the emails are pulled from authentic commit metadata, so a positive result is verifiable by inspecting the user's commits directly on GitHub.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gitleak |
| category | social-networks |
| selectorsIn → selectorsOut | username → email, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
