---
id: gitleaks
name: GitLeaks
description: Use when you have a target's git repo/`username` and want secrets and committer identities buried in its history — returns leaked credentials plus committer emails/names.
url: https://github.com/gitleaks/gitleaks
category: search-engines
path:
- search-engines
- code-search
bestFor: Scanning a git repository's full history for hardcoded secrets, API keys, and (as a byproduct) committer email/name identity leaks.
selectorsIn:
- username
selectorsOut:
- password
- email
status: live
pricing: free
costNote: Free and open source (MIT). Install via Homebrew, Docker, Go, or a prebuilt binary; no account.
opsec: active
opsecNote: Scanning a *remote* target repo means cloning it — that clone is a normal git fetch the host (e.g. GitHub) can log against your IP. Clone from a sock-puppet/VPN'd environment. Scanning a repo you already have locally is passive. Never act on or attempt to use any live credential you find.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Widely-adopted (28k+ stars) open-source secret scanner by Zachary Rice; reproducible on your own machine, so results are verifiable and not a third-party black box.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- gitleaks
tags:
- code-search
- secrets-scanning
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# GitLeaks

> An open-source CLI that rakes a git repo's entire history for secrets — and, usefully for OSINT, exposes the committer emails and names embedded in every commit.

## When to use
You've tied a subject to a git repository (their GitHub/GitLab `username`, a project they contributed to) and want to mine its history. Beyond the security use (finding leaked keys/passwords), gitleaks surfaces the author/committer `email` and `name` recorded in commit metadata — often a real address a person forgot was public — plus any hardcoded personal accounts in old commits.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `brew install gitleaks` (or Docker / `go install` / a release binary).
2. For a local repo you already cloned: `gitleaks git -v path_to_repo` (passive).
3. For a remote target: clone it first (from a sock-puppet/VPN'd shell), then run the same command; or scan a directory with `gitleaks dir -v path`.
4. Read the report (add `-f json` for structured output): each finding gives file, line, commit hash, rule, and the matched secret with an entropy score.
5. Separately, harvest identities from history: `git log --format='%ae %an'` on the cloned repo pairs with gitleaks findings to build the committer's email/name set.
6. Pivot: a committer email feeds email-OSINT and breach lookups; a leaked personal token/username feeds account-existence checks.

## Inputs → Outputs
- **In:** a git repo tied to a `username` (local clone, remote URL, or directory)
- **Out:** `password`/secret findings (keys, tokens, passwords) and committer `email`/name identities from commit metadata
- **Empty/negative result looks like:** "no leaks found" — the scanned history has no rule matches; identities may still be readable via `git log` even when gitleaks finds no secrets.

## Gotchas & OpSec
- Regex/entropy detection yields false positives — verify a "secret" is real before treating it as a lead, and never actually use a live credential.
- Scanning a remote repo requires cloning it (active, logged by the host); prefer scanning an already-local copy when possible.
- Tune with a TOML config/allowlist to cut noise on large histories.
- Ethical/legal: only scan repos you're authorized to examine within your engagement.

## Overlaps ("do both")
- Pairs with GitHub/GitLab profile and code-search tools — those find *which* repos belong to a subject; gitleaks then mines each repo's history for the secrets and identities inside.

## Trust & verifiability
`trust: trusted` — mature, popular open-source tool you run yourself; every finding is reproducible and inspectable, with no reliance on a third-party service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gitleaks |
| category | search-engines |
| selectorsIn → selectorsOut | username → password, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
