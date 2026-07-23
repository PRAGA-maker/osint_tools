---
id: github-search
name: Github Search
description: Use when you have an `employer-org`, `domain`, or `username` and want to mine GitHub for employees, leaked secrets, endpoints, and subdomains — returns `username`, `email`, `associate`, and `domain` leads.
url: https://github.com/gwen001/github-search
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Reconnaissance across GitHub — finding an organisation's developers, exposed secrets, endpoints, and subdomains from code.
selectorsIn:
- employer-org
- domain
- username
selectorsOut:
- username
- email
- associate
- domain
status: live
pricing: free
costNote: Open source (MIT); free to run. Requires one or more free GitHub personal access tokens to authenticate the search API.
opsec: passive
opsecNote: Queries GitHub's search API, not the target's own servers, so the subject sees nothing. GitHub logs the queries against your token — use a dedicated (sock-puppet) GitHub account's token, not your real one.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source toolset by gwen001 (1.5k+ stars); widely used in recon/bug-bounty, but community-maintained.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- gwen001 github-search
- github-dorks
tags:
- Code
- github-recon
source: cyb-detective
lastVerified: '2026-07-23'
---

# Github Search

> A collection of command-line GitHub recon scripts: dork the search API for an org's people, secrets, endpoints, and subdomains, then harvest the repos.

## When to use
You have an `employer-org`, a `domain`, or a `username` and want to exploit GitHub as an intelligence source: enumerate the developers/employees who commit to an org, surface accidentally committed secrets and API keys, pull endpoints and subdomains referenced in code, and map the repositories involved. Strong for building an org's people graph and its technical footprint.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and add one or more GitHub tokens (`.tokens` file, or `GITHUB_TOKEN=token1,token2`).
2. Pick the script for the job: `github-employees.py` (people), `github-dorks.py` / `github-secrets.py` (leaked secrets), `github-endpoints.py` (URLs/APIs), `github-subdomains.py` (hostnames), `git-pillage.py` (repo harvesting).
3. Run against the org/domain/user, e.g. `github-employees.py -o <org>` or `github-subdomains.py -d <domain>`.
4. Pivot: employee `username`s feed cross-platform people search and often reveal a real `name`/`email` in commit metadata; endpoints/subdomains feed infrastructure mapping; `associate` links come from co-committers.

## Inputs → Outputs
- **In:** `employer-org`, `domain`, or `username`
- **Out:** `username` (employees/contributors), `email` (from commits), `associate` (co-committers), `domain` (endpoints/subdomains), plus leaked-secret findings
- **Empty/negative result looks like:** no results (org has no public code, or your token hit rate limits) — verify the token works and the org name is exact before concluding there's nothing.

## Gotchas & OpSec
- Human-in-the-loop: you must supply GitHub token(s); multiple tokens spread the search-API rate limit.
- Handle any discovered secrets responsibly and legally — finding a leaked key is not authorisation to use it.
- OpSec: **passive** toward the target, but tied to your GitHub token; use a dedicated account.

## Overlaps ("do both")
- Pairs with commit-email extractors and username search engines — this finds the accounts and code; those resolve the developer behind a handle into a real identity.

## Trust & verifiability
`trust: community` — a well-known open-source recon toolset; verify each finding (an employee link, a subdomain, a "secret") at its source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-search |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | employer-org, domain, username → username, email, associate, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
