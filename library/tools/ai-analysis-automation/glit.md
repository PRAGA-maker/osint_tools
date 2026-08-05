---
id: glit
name: Glit
description: Use when you have a `username`/`employer-org` on GitHub and want the real emails behind it — returns `email` addresses (and `associate` handles) mined from commit history.
url: https://github.com/shadawck/glit
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Harvesting author emails from a GitHub user's, org's, or repo's commit history.
selectorsIn:
- username
- employer-org
selectorsOut:
- email
- associate
status: live
pricing: free
costNote: Free and open-source (Rust CLI). No account needed for public repos; a GitHub token raises rate limits.
opsec: passive
opsecNote: It reads public commit metadata via the GitHub API — the target isn't notified. Use your own (ideally sock-puppet) GitHub token for rate limits; the query looks like ordinary API traffic, not contact.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: A maintained open-source Rust tool (shadawck/glit, ~58 stars); the emails come straight from Git commit metadata, so accuracy is high but includes noise (bot/no-reply/old addresses).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- gitrecon
- theharvester
- emailharvester
aliases:
- glit-cli
- shadawck/glit
tags:
- github
- email-harvesting
- commit-metadata
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Glit

> A CLI that walks a GitHub user's, org's, or repo's commit history and pulls out every author email — the fast way from a `username` to the real addresses developers commit with.

## When to use
Your subject (or an `employer-org`) has a GitHub presence and you want the `email` addresses tied to it. Developers routinely commit with a personal or work email that Git records in every commit's author/committer fields — even when the profile hides contact info. Glit scrapes those across all repos, exposing addresses and, via co-committers, `associate` handles. Ideal for pivoting a code footprint into contactable identities.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `cargo install glit-cli` (or grab a release binary and put it on your PATH).
2. Run against the scope you have:
   - repo: `glit repo -u https://github.com/<owner>/<repo>`
   - user: `glit user -u https://github.com/<username>`
   - org: `glit org -u https://github.com/<org>`
3. Add `-a` to scan all branches, `-o` to export JSON, `-v` for verbose (commit hash + username per email).
4. Set a GitHub token in the environment to avoid API rate limits on large orgs.
5. Pivot: each `email` → breach/account-existence checks and other email tools; co-committer usernames → `associate` leads.

## Inputs → Outputs
- **In:** `username` / `employer-org` (a GitHub user, org, or repo URL)
- **Out:** `email` addresses from commit metadata + contributor `associate` handles
- **Empty/negative result looks like:** no emails returned — the account only ever committed via GitHub's `noreply` privacy address, or has no public commits. Filter out `users.noreply.github.com` and bot addresses; those aren't real leads.

## Gotchas & OpSec
- Results include noise: GitHub `noreply` addresses, CI/bot emails, and stale addresses from years ago — triage before acting.
- Large orgs hit API rate limits fast; supply a token.
- OpSec: passive (public API reads); still, use a sock-puppet token rather than your primary identity.

## Overlaps ("do both")
- Pair with `[[gitrecon]]` (similar Git email/OSINT recon) and feed harvested addresses into `[[theharvester]]` / `[[emailharvester]]` workflows — each catches emails and sources the others miss.

## Trust & verifiability
`trust: community` — an open-source tool reading authoritative Git commit metadata; the data is real but must be de-noised (privacy/bot addresses) and each address confirmed live before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | glit |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, employer-org → email, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
