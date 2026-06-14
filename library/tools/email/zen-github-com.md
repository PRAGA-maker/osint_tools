---
id: zen-github-com
name: Zen (github.com)
description: Use when you have a GitHub username/repo/org and want the real email addresses behind it — Zen harvests emails and names from GitHub commit metadata.
url: https://github.com/s0md3v/Zen?utm_source=substack&utm_medium=email
category: email
path:
- email
bestFor: Pulling email addresses (and names) of a GitHub user, repo contributors, or org members from public commit data.
selectorsIn:
- username
- social-profile
- employer-org
selectorsOut:
- email
- name
status: live
pricing: free
costNote: Free, open-source. May need a GitHub API token to avoid rate limits at scale.
opsec: passive
opsecNote: Reads public GitHub commit/API data; does not contact the person. Unauthenticated requests are anonymous; an API token ties queries to your GitHub account.
humanInLoop: false
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by s0md3v (well-known security tooling author). Code is public and inspectable; results depend on what users exposed in their commit metadata.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- Zen by s0md3v
- s0md3v/Zen
tags:
- email
- github
- commit-metadata
source: uk-osint
lastVerified: ''
enrichment: full
---

# Zen (github.com)

> An open-source CLI by s0md3v that extracts the email addresses and names hidden in public GitHub commit metadata for a given user, repository, or organization.

## When to use
You have a GitHub `username`/profile (`social-profile`) or know the subject contributes to a repo or `employer-org`, and you want the real `email` (and often real `name`) behind that account. GitHub commits embed the author's configured email, which the web UI hides but the API exposes — Zen automates pulling those. Strong pivot when a missing person or an associate is technical and has a GitHub footprint.

## How to use it (`bestInteractionPattern`: cli)
1. Clone/install from https://github.com/s0md3v/Zen and run it with Python.
2. Point it at a target: a GitHub username, a repository, or an organization (per the tool's usage; it enumerates commits/members).
3. (Recommended) Supply a GitHub API token to lift the unauthenticated rate limit when enumerating large repos/orgs.
4. Read the harvested `email` + `name` pairs. Pivot: verify each address ([[verify-email-address]]), reverse-search it, and use local-parts as `username` seeds across other platforms.

## Inputs → Outputs
- **In:** `username` / `social-profile` (GitHub) or `employer-org` (GitHub org / repo)
- **Out:** `email`, `name` (author identities found in commit metadata)
- **Empty/negative result looks like:** no emails returned — the user committed only with GitHub's noreply privacy email, made no commits, or the repo/org has no exposed author data. Absence is not proof; it usually means privacy email was used.

## Gotchas & OpSec
- Many users now use GitHub's `users.noreply.github.com` privacy email — Zen will surface that placeholder, not a real address. Watch for it.
- Unauthenticated runs hit GitHub's low rate limit fast; a token (`api-key`) is effectively required for org/large-repo enumeration.
- OpSec: **passive** toward the subject (no contact). But an API token links your queries to *your* GitHub account — use a sock/dedicated token if attribution matters; unauthenticated requests are anonymous but rate-limited.

## Overlaps ("do both")
- Pairs with [[verify-email-address]] / [[verifyemail-r]] to confirm harvested addresses are live, and with username-search tools to turn a recovered `email`/handle into broader account coverage.

## Trust & verifiability
`trust: community` — open-source and code-auditable, from a recognized security tooling author. Output fidelity depends entirely on what the target exposed in their commit history, so corroborate any recovered address before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zen-github-com |
| category | email |
| selectorsIn → selectorsOut | username, social-profile, employer-org → email, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
