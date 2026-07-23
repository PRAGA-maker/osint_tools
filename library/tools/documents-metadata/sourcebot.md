---
id: sourcebot
name: Sourcebot
description: Use when you have a `username` or `email` and want to search across a set of indexed code repositories for leaked identifiers, secrets or authorship traces — returns matching `email`/`username` mentions in code.
url: https://www.sourcebot.dev/
category: documents-metadata
path:
- documents-metadata
bestFor: Fast regex + symbol code search across many self-indexed repos to hunt for leaked identifiers and authorship.
selectorsIn:
- username
- email
selectorsOut:
- email
- username
status: live
pricing: freemium
costNote: Basic tier is free and open source (self-hosted via a single Docker container); a Pro tier (~$20/user/month) adds AI features. Your code/index stays on your own infrastructure.
opsec: passive
opsecNote: You index and search repositories on your own self-hosted instance, so queries never touch the target or a third-party service. The only exposure is when Sourcebot pulls public repos to index — that fetch comes from your host/IP, so use a neutral egress if the target org would notice.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Open-source project with a public GitHub repo; self-hosted so you can audit exactly what it does, but it is a code-search engine, not an OSINT data source in itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Sourcebot.dev
tags:
- code-search
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Sourcebot

> A self-hosted code-search platform (regex + symbol-aware, plus an "ask" LLM layer) you point at a target's repositories to hunt for leaked emails, usernames and authorship.

## When to use
You have a subject's `username` or `email` and want to comb through a body of source code — a target org's public GitHub/GitLab repos, a leaked codebase, mirrored projects — for where that identifier appears: committed credentials, hard-coded contact addresses, author strings, internal handles. Sourcebot indexes those repos once and gives you fast, branch-aware search across all of them.

## How to use it (`bestInteractionPattern`: docker)
1. Deploy Sourcebot as a single Docker container on your own host (their setup CLI does this in minutes), or try the public demo first at sourcebot.dev.
2. Point it at the repositories to index — GitHub/GitLab orgs, users, or specific repos.
3. Search with regex or symbol queries for the `email`/`username`/handle of interest across every indexed repo and branch.
4. Read the hits — file, line, branch, and commit context around each match.
5. Pivot: a leaked email/handle feeds account-existence and breach tooling; a distinctive author string feeds a wider username sweep.

## Inputs → Outputs
- **In:** `username`, `email` (as search terms), plus the repo set you index
- **Out:** file/line/branch hits containing those identifiers → confirmed `email`/`username` mentions and authorship traces
- **Empty/negative result looks like:** zero matches across indexed repos — which only means the term is absent from *what you indexed*, not from all of the target's code. Widen the repo set before concluding nothing exists.

## Gotchas & OpSec
- It searches only what you index — it is not an internet-wide code search. Coverage is entirely a function of the repos you add.
- Self-hosting means setup overhead (Docker) but keeps your queries and index fully private.
- OpSec: passive — queries hit your own instance; the only outbound trace is the repo clone/index step, which comes from your host.

## Overlaps ("do both")
- Pairs with public code-search engines (e.g. GitHub code search) — those cover the whole platform but rate-limit and log you; Sourcebot gives private, unlimited, multi-repo search over the specific targets you care about.

## Trust & verifiability
`trust: community` — open-source and self-hosted, so behavior is auditable and results are your own to verify; the tool is only as reliable as the repositories you choose to index.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sourcebot |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, email → email, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | no |
