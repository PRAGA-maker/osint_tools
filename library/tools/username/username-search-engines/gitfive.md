---
id: gitfive
name: GitFive
description: Use when you have a GitHub `username` or `email` and want to unmask the person behind it — returns linked emails, name/username history, SSH keys and probable secondary GitHub accounts.
url: https://github.com/mxrch/GitFive
category: username
path:
- username
- username-search-engines
bestFor: Deep GitHub-account OSINT — mapping a handle or email to the real identity, linked emails and other accounts a developer controls.
selectorsIn:
- username
- email
selectorsOut:
- email
- name
- username
- social-profile
status: live
pricing: free
costNote: Free, open-source (mxrch); no payment. Requires Python 3.10+ and a GitHub account/token for API access.
opsec: active
opsecNote: GitFive queries the GitHub API authenticated as your token, so activity ties to that account — use a dedicated secondary GitHub account, never your real one. It stays under rate limits by design, but the developer explicitly restricts use to personal/criminal-investigation/open-source contexts.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: A well-regarded open-source tool by researcher mxrch (also behind GHunt); auditable and effective, but it relies on GitHub behaviour (commit metadata, API fields) that can change.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
aliases:
- mxrch GitFive
tags:
- username-search
- github
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- ghunt
---

# GitFive

> A CLI that turns a GitHub handle or email into a developer's identity graph — leaked commit emails, name/username history, SSH keys, and the other accounts they quietly control.

## When to use
Your subject is a developer or has a GitHub `username`/`email` in their footprint, and you want to unmask and expand it. GitHub leaks a lot: commit author emails, historical usernames, SSH public keys, and behavioural links between accounts. GitFive harvests these to map a handle to a real `name`/`email` and to surface probable secondary GitHub accounts the same person runs. Reach for it whenever a GitHub identity is a pivot point.

## How to use it (`bestInteractionPattern`: cli)
1. Install via pipx (`pipx install gitfive`) with Python 3.10+ and Git present.
2. Authenticate with a **secondary** GitHub account/token when prompted.
3. Run against a handle (`gitfive user <username>`) or an email (`gitfive email <address>`); batch email lists are supported.
4. Read the JSON/console output: linked emails, username/name history, SSH keys, cloned-repo analysis, and candidate secondary accounts.
5. Pivot: a recovered commit `email` feeds `[[palenath]]`/Holehe and `[[account-live-com]]`; a real `name` feeds people-search; secondary accounts expand the footprint.

## Inputs → Outputs
- **In:** GitHub `username` or `email` (or a list of emails)
- **Out:** linked `email`s, `name`/`username` history, SSH public keys, and probable secondary GitHub `social-profile`s
- **Empty/negative result looks like:** sparse output — the account has private-email/commit settings enabled, few public commits, or no linkable signals; a quiet result means low GitHub exposure, not necessarily a wrong target.

## Gotchas & OpSec
- Use a burner GitHub token: queries are authenticated and attributable.
- Signal depends on the target's hygiene: developers who enable "keep my email private" leak far less.
- Maintenance: GitHub changes API/commit exposure over time; verify the tool is current if output looks thin.
- OpSec: **active** — authenticated GitHub API calls tie to your account.

## Overlaps ("do both")
- Pairs with `[[palenath]]`/Holehe — GitFive extracts the commit email, Holehe maps where else it's registered.
- Pairs with `[[account-live-com]]` — confirm a recovered email is a live provider account.
- Pairs with `[[sherlock]]`-style username hunters — GitFive is GitHub-deep, they are breadth-across-platforms.

## Trust & verifiability
`trust: community` — an auditable, well-known open-source tool; its findings come straight from GitHub's own exposed metadata, so they are verifiable, but coverage depends on the target's privacy settings and GitHub's current behaviour.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gitfive |
