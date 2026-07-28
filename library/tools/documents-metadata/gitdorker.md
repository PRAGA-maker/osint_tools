---
id: gitdorker
name: GitDorker
description: Use when you have a `username`, `employer-org`, or `domain` and want secrets/emails/keys exposed across public GitHub — returns `email` and `password`/credential leads.
url: https://github.com/obheda12/GitDorker
category: documents-metadata
path:
- documents-metadata
bestFor: Dorking GitHub for leaked secrets, emails, and credentials tied to a person, org, or domain.
selectorsIn:
- username
- employer-org
- domain
selectorsOut:
- email
- password
status: live
pricing: free
costNote: Free and open-source; you supply your own free GitHub personal access token(s) — no paid tier.
opsec: passive
opsecNote: Runs against GitHub's search API using YOUR token, not the subject — passive toward the target. But heavy dorking can trip GitHub's abuse/rate-limit protections on the account whose token you use, so use a dedicated research GitHub account, ideally two tokens.
humanInLoop: true
humanInLoopReason:
- api-key
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source recon tool by obheda12, widely cited in bug-bounty and OSINT guides; results are only as good as the dork list and must be manually validated.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: true
relatedTools: []
aliases:
- GitDorker.py
tags:
- github-dorking
- secrets
- recon
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# GitDorker

> A Python GitHub-dorking harness that runs a curated dork list against GitHub's search API to surface secrets, emails, and credentials in public repos.

## When to use
You have a `username`, an `employer-org` name, or a `domain` and want to know what a person or organization has accidentally committed to public GitHub — API keys, passwords, `.env` files, internal emails, hostnames. Useful for enriching an identity (finding a subject's coding aliases, work email, or leaked infrastructure) and for authorized exposure assessments.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/obheda12/GitDorker && cd GitDorker`, then `pip3 install -r requirements.txt` (Python 3). Docker is also supported.
2. Create a **GitHub personal access token** (two, from different accounts, is recommended to spread rate limits) and put them one-per-line in a token file.
3. Run: `python3 GitDorker.py -tf TOKENSFILE -q <target-query> -d <dorkfile> -o <output>`, where `-q` is your selector (username / org / domain / endpoint) and `-d` points at a dork list (e.g. `Dorks/alldorksv3`).
4. GitHub caps search at ~30 req/min; the tool sleeps to stay under it — a full dork run takes roughly 5 minutes per query.
5. Read the output list of matching files/URLs, then **manually open each hit** — dorks produce many false positives.
6. Pivot: a leaked `email` feeds email-OSINT; a leaked credential/host feeds infrastructure mapping.

## Inputs → Outputs
- **In:** `username`, `employer-org`, or `domain` (most effective with a specific org/username/endpoint)
- **Out:** GitHub file URLs that may contain `email`, `password`/API-key, and other `document-id`-style secrets
- **Empty/negative result looks like:** no matching files across the dork list — either nothing is exposed for that selector, or the query was too broad; refine to a specific org/username.

## Gotchas & OpSec
- Human-in-the-loop: **requires your own GitHub API token(s)** (`api-key`) and you must manually triage results; GitHub rate limits throttle large runs.
- Only searches **public** repos — it cannot see private code.
- OpSec: passive toward the subject, but the searches are logged against your GitHub account; never use your primary account's token.

## Overlaps ("do both")
- Pair with other GitHub-recon tools (e.g. trufflehog-style secret scanners) — GitDorker finds *where* to look via dorks; a secret scanner validates *what's actually a live credential*.

## Trust & verifiability
`trust: community` — a well-regarded open-source tool, but it only surfaces candidate hits; every finding needs manual verification and secrets should be confirmed (and reported responsibly), never assumed live.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gitdorker |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, employer-org, domain → email, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
