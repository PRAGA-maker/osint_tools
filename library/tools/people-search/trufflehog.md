---
id: trufflehog
name: TruffleHog
description: Use when you have a subject's code presence (`username`/`domain` — GitHub org, repo, site) and want secrets and contact data leaked in commits — returns email, credentials and linked identities.
url: https://trufflesecurity.com/trufflehog
category: people-search
path:
- people-search
bestFor: Scanning git repos, GitHub orgs and other sources for leaked secrets, API keys, and the emails/identities embedded in commit history.
selectorsIn:
- username
- domain
selectorsOut:
- email
- social-profile
- name
status: live
pricing: free
costNote: TruffleHog's core scanner is free and open-source (Truffle Security); an enterprise SaaS exists, but CLI scanning of public repos is free.
opsec: active
opsecNote: TruffleHog clones and scans the target's repositories, so your machine pulls their code from GitHub/GitLab. Scanning public repos is low-risk but not invisible (clones/API calls are logged by the host). Run from a research environment; never scan repos you're not authorised to, and handle any real secrets you find responsibly (do not use them).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely used, well-maintained open-source secret scanner from Truffle Security; reliable at what it does, though it's a secrets scanner repurposed for identity OSINT rather than a people-search engine.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- TruffleHog
- trufflehog
tags:
- bellingcat-toolkit
- people
- secrets
- github
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
---

# TruffleHog

> A secret scanner that digs through git history for leaked credentials — and, for OSINT, for the emails, names and linked accounts a subject baked into their commits.

## When to use
Your subject has a code presence — a GitHub/GitLab `username`, an org, a specific repo, or a `domain` whose site is on git — and you want what's hidden in commit history. Beyond the API keys and secrets TruffleHog is built to find, commit metadata and configs routinely leak the author's real `email`, name, private hostnames, and links to other accounts. It's a strong pivot when a developer or technically-active subject has left a git trail.

## How to use it (`bestInteractionPattern`: cli)
1. Install TruffleHog (binary/Docker/`pip`), per the docs.
2. Scan a target source: `trufflehog github --org=<org>` or `trufflehog git https://github.com/<user>/<repo>.git`.
3. Review findings: verified secrets, plus (from `git log`/configs) committer `email`s and names, and references to other services (`social-profile`).
4. Focus on identity artefacts (author emails, usernames, self-hosted domains) rather than only the secrets.
5. Pivot: a committer email feeds email OSINT; leaked usernames feed cross-platform enumeration; a private domain feeds infrastructure research.

## Inputs → Outputs
- **In:** `username`/org/repo or `domain` (a git-backed source)
- **Out:** `email` (committer addresses), `social-profile` (linked services/accounts), `name` (commit authors)
- **Empty/negative result looks like:** no secrets and generic/anonymised commit authors — meaning good hygiene or a scrubbed history, not that the person has no code presence.

## Gotchas & OpSec
- It's a **secrets scanner**, not a name-search engine — the people-OSINT value is the identity metadata it surfaces along the way.
- **Active:** cloning/scanning touches the host; only scan authorised/public targets and route via a research environment.
- Handle any live credential you find ethically — report/ignore, never use it.

## Overlaps ("do both")
- Pairs with GitHub-focused OSINT (searching a user's repos/commits by hand) and `[[buster]]` — TruffleHog automates the deep commit-history sweep; manual GitHub search catches profile-level links.

## Trust & verifiability
`trust: community` — a mature, trusted open-source scanner; findings are concrete (you can open the commit), so verify each leaked email/identity directly in the repo history.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trufflehog |
| category | people-search |
| selectorsIn → selectorsOut | username, domain → email, social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
