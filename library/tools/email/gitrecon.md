---
id: gitrecon
name: Gitrecon
description: Use when you have a GitHub/GitLab username and want to harvest the emails, names, and linked accounts exposed in that user's commit history.
url: https://github.com/atiilla/gitrecon
category: email
path:
- email
bestFor: Extracting commit-leaked emails and identity data from a GitHub/GitLab user's public repositories.
selectorsIn:
- username
selectorsOut:
- email
- name
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source (Python CLI).
opsec: passive
opsecNote: Reads public GitHub/GitLab data via their APIs; the subject is not notified. Using a personal API token raises rate limits but ties the queries to that token's account.
humanInLoop: true
humanInLoopReason:
- api-key
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Open-source GitHub/GitLab recon tool (atiilla); outputs are derived from public commit metadata and are verifiable against the source repositories.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
aliases: []
tags:
- email-search-email-check
relatedTools:
- ghintel-secrets-ninja
- ghunt
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Gitrecon

> Open-source CLI that scrapes a GitHub/GitLab user's public commits to harvest emails, names, and linked accounts.

## When to use
Your subject or an associate is technical and has a GitHub/GitLab `username`. You want every `email` and `name` baked into their commit authorship (which often differs from their public profile email), plus linked `social-profile`s and other repos. A strong attribution pivot when a person's only durable online footprint is code.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install from the repo (`git clone https://github.com/atiilla/gitrecon`, then install requirements).
2. Run it against the target `username` (e.g. `gitrecon -u <username>`); optionally supply a GitHub token to lift rate limits.
3. Read the output: commit-author emails, display names, organizations, and linked accounts harvested across the user's repos.
4. Pivot: validate harvested `email`s, run them through breach-search, and feed `name`/handles into username enumeration.

## Inputs → Outputs
- **In:** GitHub/GitLab `username`
- **Out:** `email`(s), `name`(s), `social-profile`/org links, related `username`s/repos
- **Empty/negative result looks like:** only `noreply.github.com` addresses (user enabled email privacy), or no public commits — nothing to harvest.

## Gotchas & OpSec
- Commit emails appear only when the user did not enable GitHub's email-privacy setting; expect many `users.noreply.github.com` results.
- Human-in-the-loop: an API key/token is effectively required to avoid quick rate-limiting on larger accounts.
- OpSec: passive toward the subject; if you authenticate with a token, queries are tied to that account — use a burner token.

## Overlaps ("do both")
- Overlaps with the web tool `[[ghintel-secrets-ninja]]` (same GitHub-email goal, no install) and complements `[[ghunt]]` (Google accounts, not code hosting).

## Trust & verifiability
`trust: community` — open-source project; output is harvested public commit metadata you can confirm directly in the target's repositories.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gitrecon |
| category | email |
| selectorsIn → selectorsOut | username → email, name, social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes |
