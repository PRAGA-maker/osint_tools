---
id: dumpsterdiver
name: DumpsterDiver
description: Use when you have a `domain`'s file dump / repo / large dataset and want to surface hardcoded secrets (keys, passwords) via entropy analysis — returns leaked credentials and suspicious strings.
url: https://github.com/securing/DumpsterDiver
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Entropy/pattern scanning of large file sets to find API keys, SSH keys and passwords.
selectorsIn:
- domain
selectorsOut:
- domain
- password
status: live
pricing: free
costNote: Free/open-source Python tool; no account. Note the repo was archived (read-only) in Feb 2025 but still runs.
opsec: passive
opsecNote: Passive — it analyses files you have already collected locally; it does not touch the subject's servers. Handle any discovered credentials responsibly and never use them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Published by securing (a known security firm); archived/read-only since Feb 2025, so no further updates, but the tool is functional and reputable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- jsleak
aliases:
- securing/DumpsterDiver
tags:
- Domain/IP/Links
- Website's files metadata analyze and files downloads
- secrets
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# DumpsterDiver

> A Python tool that scans large collections of files for hardcoded secrets — API keys, SSH/Azure/AWS keys, passwords — using Shannon-entropy and pattern rules.

## When to use
You have already collected a large set of files tied to a `domain`/target — a downloaded website, a code repo, a data dump, exported archives — and want to sweep them for accidentally-committed credentials and high-entropy strings that look like keys. It's an offline analysis tool for material you already hold, not a live scanner.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install Python 3 requirements.
2. Point it at a folder: `python3 DumpsterDiver.py -p [folder_path]` (it also unpacks archives and can scan git logs).
3. Tune `config.yaml` — entropy thresholds, file types, and rule logic for specific credential types (AWS, Azure, SSH, etc.).
4. Read console output or export JSON with the discovered secrets and suspicious strings.
5. Pivot: a leaked key/credential characterises the target's security exposure; associated files may hold further identifying detail.

## Inputs → Outputs
- **In:** a local `domain`/target file set (folder, repo, archive)
- **Out:** `password`/secrets (keys, tokens, passwords), plus the `domain`/paths they were found in
- **Empty/negative result looks like:** no high-entropy or rule-matching strings (clean dataset) — a valid finding, not a failure. Expect some false positives on random-looking but benign data.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must triage entropy false positives.
- OpSec: **passive/offline** — it never contacts the subject; the sensitivity is in what you collected and any secrets you find. Never use discovered credentials.
- Archived (read-only) since Feb 2025: functional but unmaintained; expect no dependency updates.

## Overlaps ("do both")
- Pairs with `[[jsleak]]` — jsleak pulls secrets/links live from a site's JavaScript, DumpsterDiver sweeps an offline file dump; use both to cover live and collected sources.

## Trust & verifiability
`trust: community` — from a reputable security firm and widely used, though now archived; every hit is heuristic (entropy/regex), so confirm a "secret" is real before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dumpsterdiver |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
