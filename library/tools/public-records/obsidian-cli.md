---
id: obsidian-cli
name: Obsidian CLI
description: Use when you keep case notes in an Obsidian vault and want to open, search, create and edit them from the terminal — returns scripted, automatable note management for your investigation workflow.
url: https://github.com/Yakitrak/obsidian-cli
category: public-records
path:
- public-records
bestFor: Automating and scripting an investigator's Obsidian case-notes vault from the command line.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (MIT). No account; a local install via Homebrew/Scoop/AUR or a Go build.
opsec: passive
opsecNote: Investigator-side tooling — it manipulates your own local notes and never contacts a target or any remote service, so it leaks nothing about the subject. Keep the vault itself on an encrypted disk since case notes are sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source project (Yakitrak/obsidian-cli, ~1.6k GitHub stars, MIT); community-maintained tooling, not a data source, so trust is about code quality rather than data accuracy.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Yakitrak obsidian-cli
- NotesMD CLI
tags:
- Databases and data analyzes
- workflow-automation
- note-taking
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Obsidian CLI

> A small Go command-line tool for driving an Obsidian vault from the terminal — the glue that lets an OSINT workflow write findings into structured case notes automatically.

## When to use
You run investigations out of an Obsidian vault and want to script it: append a new finding to a case note from a shell pipeline, open or search notes without the GUI, or run it headless on a server. This is **investigator tooling**, not a data source — it never finds information about a subject; it organises what you've already found. Reach for it when you're automating an OSINT pipeline and want each tool's output to land in your notes.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `brew install obsidian-cli` (macOS/Linux), Scoop (Windows), AUR (Arch), or `go install` from source (Go 1.19+).
2. Point it at your vault (it reads Obsidian's config to locate vaults and respects excluded files / daily-note settings).
3. Use subcommands to `open`, `search`, `list`, `create`, `update`, `move`, `delete` notes and edit frontmatter — e.g. pipe a tool's result into `create`/`update` to log it.
4. Combine with other CLI OSINT tools in a script so each lookup writes straight into the relevant case note.

## Inputs → Outputs
- **In:** none (operates on your local vault, not on target selectors)
- **Out:** none (manages notes; it doesn't return data about a person)
- **Empty/negative result looks like:** a command error usually means a wrong vault path or missing note — fix the vault name/path; it has no "no match on the subject" state because it isn't a lookup tool.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a scriptable CLI.
- OpSec: passive and self-contained — it touches only your local files and no network, so it can't leak your investigation to a target. The real risk is the vault's own sensitivity: keep case notes encrypted at rest.
- It requires an existing Obsidian vault; it isn't a note app itself, just a controller for one.

## Overlaps ("do both")
- Complements the actual data-gathering tools in this library rather than overlapping them — pair it with any CLI collector (recon, scrapers) so their output is captured into notes automatically.

## Trust & verifiability
`trust: community` — a well-starred MIT open-source project; because it produces no external data, "trust" here is about code safety (review before running on a sensitive vault), not data reliability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | obsidian-cli |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
