---
id: gitgot
name: GitGot
description: Use when you have an `employer-org` or `domain` and want to sweep public GitHub for leaked secrets tied to it — returns exposed `email` and `password`/credential material.
url: https://github.com/BishopFox/GitGot
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Rapidly triaging public GitHub/gist search hits for a company or domain to surface leaked credentials and contact data.
selectorsIn:
- employer-org
- domain
selectorsOut:
- email
- password
status: live
pricing: free
costNote: Free, open-source (BishopFox). You supply your own free GitHub personal access token; GitHub's code-search API has no per-search charge.
opsec: passive
opsecNote: Searches only public GitHub content, so the target is not alerted. However, every query runs under YOUR authenticated GitHub token and is logged by GitHub — use a dedicated research account, never your primary identity, and don't clone/download leaked secrets you find.
humanInLoop: true
humanInLoopReason:
- api-key
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool from Bishop Fox, a well-known offensive-security firm; ~1.6k stars, still receiving commits. Code is auditable but community-maintained, not a hosted service with guarantees.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
relatedTools:
- jsluice
aliases:
- BishopFox GitGot
- GitGot secret scanner
tags:
- github
- secrets
- auditing
source: osintambition-social
lastVerified: '2026-08-04'
enrichment: full
---

# GitGot

> A feedback-driven grep over public GitHub: search for an org/domain, then interactively prune the noise until only the real leaked secrets remain.

## When to use
You have an `employer-org` name or a `domain` and want to know what that entity has accidentally committed to public GitHub — API keys, passwords, internal emails, config files. In a people-context this surfaces staff emails and credentials tied to a workplace, which can corroborate an association or open a new contact channel. Reach for it when a plain GitHub search returns thousands of hits and you need a human-in-the-loop way to whittle them down fast.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/BishopFox/GitGot`, install the `ssdeep` dependency, then `pip3 install -r requirements.txt` (or run the bundled `gitgot-docker.sh`).
2. Add a **GitHub personal access token** (from a throwaway research account) to the config so the code-search API is reachable.
3. Run a query: `./gitgot.py -q example.com` (or `-q '"Company Name"'` for an exact phrase, `--gist -q CompanyName` to search gists).
4. Triage interactively: for each hit GitGot lets you blacklist a file, repo, user, or *fuzzy-similar* content (via ssdeep) so near-duplicate noise disappears from the remaining results.
5. Save/resume long sweeps with `-r example.com.state`.
6. Pivot: real hits give you `email` addresses and `password`/token material — feed emails into email-OSINT tools and treat any live secret as evidence only, do not use it.

## Inputs → Outputs
- **In:** `employer-org` (company name) or `domain`
- **Out:** `email`, `password`/credential strings, plus file/repo locations of the leak
- **Empty/negative result looks like:** GitGot exhausts the result pages with nothing left after blacklisting — meaning no distinctive public leak for that query (not proof the org has zero exposure; try phrase variants and gists).

## Gotchas & OpSec
- Human-in-the-loop: you MUST supply a GitHub API token (`api-key`), and the whole workflow is manual triage (`manual-review`) — it does not auto-classify secrets for you.
- OpSec: passive toward the target (public data only) but every search is tied to your GitHub token and logged; use a dedicated account.
- Legal/ethical: finding a credential is not licence to use it. Record the location, stop there.

## Overlaps ("do both")
- Pairs with `[[jsluice]]` — GitGot finds secrets sitting in repos/gists; jsluice extracts endpoints and secrets out of the JavaScript those repos ship, so together they cover source-at-rest and shipped-artifact leakage.

## Trust & verifiability
`trust: community` — authored by Bishop Fox and open-source, so you can read exactly what it does, but it's a community tool you run yourself, not a vetted hosted service; validate every hit by opening the referenced file directly on GitHub.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gitgot |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org, domain → email, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key, manual-review) |
