---
id: woboq-code-browser
name: Woboq Code Browser (codebrowser.dev)
description: Use when you need to read/navigate a C/C++ open-source codebase in the browser — returns cross-referenced, hyperlinked source for projects like Qt and LLVM.
url: https://codebrowser.dev/
category: search-engines
path:
- search-engines
bestFor: Browsing and jumping through the source of major C/C++ open-source projects with IDE-like cross-references.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to browse the hosted codebases online (the underlying generator is also open-source).
opsec: passive
opsecNote: Passive read-only source browsing; you view static generated pages and disclose nothing about a subject. No account, no target contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-known developer tool by Woboq (now at codebrowser.dev); it renders public open-source code faithfully, so accuracy tracks the upstream repository.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Woboq Code Browser
- code.woboq.org
- codebrowser.dev
tags:
- toddington
- curated-directory
- specialty-search
- code-browsing
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Woboq Code Browser (codebrowser.dev)

> An IDE-in-the-browser view of major C/C++ open-source codebases (Qt, LLVM, and more) — a niche developer/reference tool rather than a people-search resource.

## When to use
Your investigation has a technical angle and you need to read or navigate a large C/C++ open-source codebase without cloning it — for example, to understand how a piece of software behaves, verify a claim about a project, or follow a function referenced in a leaked snippet. Woboq renders the source with clickable cross-references (jump to definition/usages), which makes reading unfamiliar code far easier. Its OSINT relevance is indirect: it aids technical understanding, not finding individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://codebrowser.dev/ (formerly code.woboq.org) and pick a hosted project (e.g. Qt, LLVM).
2. Browse the file tree or use the code navigation to jump between definitions and usages.
3. Read the cross-referenced source to understand behaviour or confirm a technical detail.
4. For a project not hosted here, note the tool's generator is open-source and can be run against other codebases.
5. Pivot: technical findings support (not replace) code-authorship OSINT — pair with repository-level tools (GitHub search, commit history) to tie code to people.

## Inputs → Outputs
- **In:** a project/file to read (no personal selector)
- **Out:** hyperlinked, cross-referenced source code for that project
- **Empty/negative result looks like:** the project or symbol isn't among the hosted codebases — coverage is limited to the projects Woboq publishes, so most code won't be here. Use the upstream repo or a code-search engine instead.

## Gotchas & OpSec
- Scope is limited to the specific open-source projects hosted; it is not a general code-search engine across all of GitHub.
- It shows code, not authorship metadata — for who wrote what, use repository tools with commit history.

## Overlaps ("do both")
- Pairs with GitHub code search and repository history tools — Woboq gives a clean, navigable read of a hosted project; those give breadth across all repos and the author/commit trail that ties code to people.

## Trust & verifiability
`trust: trusted` — an established developer tool that faithfully renders public open-source code; reliability equals the upstream repository it was generated from.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | woboq-code-browser |
| category | search-engines |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
