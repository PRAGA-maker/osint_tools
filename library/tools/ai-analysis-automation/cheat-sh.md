---
id: cheat-sh
name: cheat.sh
description: Use when you need instant command/tool syntax at the terminal (curl cheat.sh/<tool>) — a fast reference for the recon and analysis commands you run during an investigation.
url: https://github.com/chubin/cheat.sh
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Pulling concise, example-driven cheat sheets for CLI tools straight into the terminal.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; usable instantly via curl to cheat.sh, or self-hosted from the GitHub repo. No account.
opsec: passive
opsecNote: You query cheat.sh for command syntax, not anything about a target — no subject data is disclosed. If you're cautious about the public instance seeing your query topics, self-host it from the repo.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A popular open-source project (chubin/cheat.sh) aggregating community cheat sheets; content is community-sourced, so treat commands as guidance and understand them before running.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- cheat.sh
- cht.sh
tags:
- cli
- reference
- productivity
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# cheat.sh

> A one-line terminal cheat-sheet service: `curl cheat.sh/<tool>` returns concise, example-first usage for almost any command — the reference you keep open while running recon tooling.

## When to use
You're mid-investigation at the command line and need the syntax for a tool right now — `nmap` flags, a tricky `grep`/`jq`/`ffmpeg` invocation, a Python one-liner — without breaking flow to search a browser. cheat.sh returns terse, example-driven cheat sheets in the terminal. It's investigator productivity plumbing: it speeds up how you drive your OSINT CLI tools; it doesn't itself find anything about a subject.

## How to use it (`bestInteractionPattern`: cli)
1. Query directly: `curl cheat.sh/nmap` (or `cht.sh/<tool>`), or `curl cheat.sh/python/<question>` for language snippets.
2. Read the concise examples; append `~keyword` to search within a topic.
3. Optionally install the `cht.sh` client for tab-completion and a shell/editor integration.
4. For privacy or offline use, self-host the service from the GitHub repo.
5. Pivot: apply the recalled syntax to the actual recon/analysis tool you're running.

## Inputs → Outputs
- **In:** a tool name or how-to query (no person selector)
- **Out:** concise, example-based command cheat sheets. No person-level `selectorsOut`.
- **Empty/negative result looks like:** a sparse or missing sheet for an obscure tool — fall back to the tool's `--help`/man page or its docs.

## Gotchas & OpSec
- OpSec: passive; only your syntax questions leave the machine. Self-host if even that is sensitive.
- Community-sourced examples can be outdated or context-specific — understand a command before running it, especially anything destructive.
- It's a reference, not a doer — it won't perform recon, only remind you how.

## Overlaps ("do both")
- Complements every CLI OSINT tool in this library — cheat.sh is the quick-reference layer that makes driving those tools faster.

## Trust & verifiability
`trust: community` — a widely-used open-source aggregator of community cheat sheets; verifiable via the repo, but always read a command before executing it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cheat-sh |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
