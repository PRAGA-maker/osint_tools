---
id: goosh-org
name: Goosh
description: Use when you want a fast, keyboard-driven shell interface to run Google/web searches from a command line in the browser — returns web/image results as text you can chain with commands.
url: https://goosh.org/
category: search-engines
path:
- search-engines
bestFor: Rapid, keyboard-only searching via a unix-shell-style command interface in the browser.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open-source (Artistic License/GPL); runs in the browser, no account.
opsec: passive
opsecNote: Goosh is a front-end that issues queries to Google Custom Search — results ultimately come from Google under your session/IP, so standard search-privacy hygiene applies (use a sock-puppet browser). It's not an anonymiser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A long-standing open-source hobby project (explicitly "not an official Google product"); functional but dependent on Google Custom Search, whose result depth is narrower than full Google.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- goosh
- goosh.org
- google shell
tags:
- search
- command-line
- shell-ui
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Goosh

> A browser-based command-line for search — type `google`, `images`, `wiki` and friends like unix commands and get results inline, no mouse required.

## When to use
Goosh is a *workflow* tool, not a new data source: it wraps web search in a fast, keyboard-driven shell. Reach for it when you're doing rapid iterative searching (a `name`, alias, or keyword through many query variants) and want to move faster than a mouse-driven browser — type a command, read results, refine, repeat. The underlying results come from Google Custom Search, so it's about speed and ergonomics, not unique coverage.

## How to use it (`bestInteractionPattern`: cli)
1. Open https://goosh.org/ — you get a shell prompt in the browser.
2. Type `help` (or `h`) for the command list.
3. Run searches like commands: `google <query>`, `images <query>`, `wiki <topic>`, etc.
4. Chain and iterate quickly with keyboard-only navigation through results.
5. Pivot: open promising `document-id`s (result links) in the browser and continue in your normal toolchain.

## Inputs → Outputs
- **In:** `name` / keyword (as a shell command argument)
- **Out:** `document-id` (search result links), inline
- **Empty/negative result looks like:** few/no results — remember it's backed by Google *Custom* Search, which is narrower than full Google; if a query comes up thin, re-run it in a normal engine before concluding nothing exists.

## Gotchas & OpSec
- Backed by Google Custom Search: result depth is more limited than google.com — don't treat "nothing in goosh" as "nothing on Google."
- It's a search front-end, not privacy tooling; queries still go to Google under your session.
- Hobby project — occasional quirks/outages are possible.

## Overlaps ("do both")
- Complements full-featured search engines and dorking: use Goosh for fast iterative passes, then a mainstream engine (with `site:`/`filetype:` operators) for depth on the promising leads.

## Trust & verifiability
`trust: community` — an open-source community project; it's just a UI over Google Custom Search, so trust the underlying results as you would any Google search and verify each source directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | goosh-org |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
