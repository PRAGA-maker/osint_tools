---
id: tldr
name: TLDR
description: Use when you have a shell command name and want concise, example-driven usage help at the terminal — returns practical examples instead of a full man page.
url: https://github.com/tldr-pages/tldr
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Getting fast, example-first usage for OSINT CLI tools and standard Unix commands without reading a full man page.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (community-maintained, CC BY 4.0). Multiple free clients; the pages are also browsable at tldr.inbrowser.app with no install.
opsec: passive
opsecNote: A local documentation lookup — it queries the tldr-pages content cache, not any target. It touches no investigation subject and leaks nothing about your case; the only network traffic is fetching/updating the community page cache from GitHub.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Long-running, widely adopted open-source project (tens of thousands of GitHub stars) with public contribution history; content is community-reviewed via pull request.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- tldr-pages
- tldr
tags:
- Code
- cli-utility
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# TLDR

> A community "simplified man pages" project: type `tldr <command>` and get a handful of copy-paste examples instead of a wall of flags — support tooling for a CLI-heavy OSINT workflow.

## When to use
Not an investigative data source — it's an **enabler**. When you're at the terminal running OSINT CLI tooling (or standard Unix commands for grepping dumps, wrangling files, curling APIs) and can't remember the invocation, `tldr <command>` gives the common patterns instantly. Reach for it to move faster through a command-line pipeline, not to look up a subject.

## How to use it (`bestInteractionPattern`: cli)
1. Install a client: `pipx install tldr` (Python), `npm install -g tldr` (Node), or `brew install tlrc` / `cargo install tlrc --locked` (Rust).
2. Run `tldr <command>` — e.g. `tldr tar`, `tldr curl`, `tldr nmap` — to see concise, example-first usage.
3. First run downloads the page cache; refresh later with the client's update command (e.g. `tldr --update`).
4. No network to any target needed — for zero install, browse the same pages at `https://tldr.inbrowser.app`.
5. Copy the example you need into your working command line.

## Inputs → Outputs
- **In:** a command name (not an investigation selector)
- **Out:** example-driven usage snippets for that command
- **Empty/negative result looks like:** "page not found" for a command tldr-pages doesn't cover yet — fall back to the tool's own `--help` or `man`.

## Gotchas & OpSec
- No human-in-the-loop and no target interaction — safe to run at any time.
- Pages are community-curated summaries, not exhaustive; for rare flags still consult the real man page or `--help`.
- Keep the cache updated so examples reflect current tool versions.

## Overlaps ("do both")
- Complements every CLI-based tool in the library (recon, DNS, image, metadata utilities) — use tldr to recall their invocation quickly; it does not replace any tool's own documentation.

## Trust & verifiability
`trust: trusted` — a mature, high-visibility open-source project with public, PR-reviewed contributions; there is no data-quality risk because it produces documentation, not investigative findings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tldr |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
