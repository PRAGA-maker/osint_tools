---
id: shellcheck-net
name: shellcheck.net
description: Use when you have a shell script (yours or one recovered from a target) and want to understand or debug it — returns annotated warnings explaining each issue.
url: https://www.shellcheck.net/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Linting and explaining bash/sh scripts online or via CLI during analysis.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (GPLv3); the web version and the CLI are both free with no account.
opsec: passive
opsecNote: Investigator-side/analysis tool. If you paste a script into the web version, that text leaves your machine and hits shellcheck.net — do NOT paste sensitive or attributable script content there; install the CLI and run it locally for anything confidential.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Widely-used GPLv3 open-source project (koalaman/shellcheck) packaged in most Linux distros and integrated into major editors.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- ShellCheck
- shellcheck
tags:
- Code
- static-analysis
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# shellcheck.net

> An online (and CLI) shell-script linter — paste or pipe a bash/sh script and get plain-language explanations of every bug, bashism, and quoting error.

## When to use
During analysis you have a shell script — one you are writing to automate collection, or one recovered from a target host/repo — and need to understand what it does or why it misbehaves. ShellCheck annotates each line with the problem and a link explaining it, which doubles as a fast way to reverse-engineer an unfamiliar script.

## How to use it (`bestInteractionPattern`: cli)
1. For quick, non-sensitive checks: open https://www.shellcheck.net/ and paste the script; read the inline warnings.
2. For anything confidential: install locally (`apt install shellcheck`, `brew install shellcheck`, or your package manager) and run `shellcheck script.sh`.
3. Read each `SCxxxx` code — click through to its wiki page for the rationale and fix.
4. Integrate into an editor/CI if you author collection tooling regularly.

## Inputs → Outputs
- **In:** none (a shell script you supply — not an OSINT selector)
- **Out:** none (annotated lint warnings, not subject data)
- **Empty/negative result looks like:** "No issues detected!" — the script is clean by ShellCheck's rules (not a guarantee it is logically correct).

## Gotchas & OpSec
- The web version transmits your script to a third-party server — use the local CLI for sensitive or attributable content.
- It checks style/portability/quoting, not intent — a malicious script can be perfectly ShellCheck-clean.
- Only handles POSIX sh / bash-family scripts, not other languages.

## Overlaps ("do both")
- Pairs with local sandbox/VM analysis tooling — ShellCheck explains what a recovered script *says*, while a sandbox shows what it *does* when run safely.

## Trust & verifiability
`trust: trusted` — mature GPLv3 open-source linter with a large user base and distro packaging; its warnings are well-documented and reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shellcheck-net |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
