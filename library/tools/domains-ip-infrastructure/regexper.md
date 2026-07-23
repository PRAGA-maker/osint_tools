---
id: regexper
name: Regexper
description: Use when you have a regular expression and want to understand or debug it — pastes a regex and returns a railroad-diagram visualization; a helper for building extraction patterns, not a data source.
url: https://regexper.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Visualizing a regular expression as a railroad diagram to verify what it matches before using it to scrape/extract data.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (GitLab); runs entirely in your browser, no account.
opsec: passive
opsecNote: The regex is rendered client-side in your browser; it is not a query about any target, so there is no subject-facing footprint. Avoid pasting a regex that itself embeds sensitive literals (a specific target email/phone) into the shared-permalink feature, since permalinks encode the pattern into a URL.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Small open-source utility by Jeff Avallone; source is public on GitLab, so its behavior is auditable, but it is a community project, not an institutional tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- regexper.com
- regex visualizer
tags:
- regex
- pattern-building
- investigator-utility
- source-code-analysis
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Regexper

> Paste a regular expression, get a railroad diagram — a sanity-check utility for the regex patterns you use to pull selectors out of scraped text.

## When to use
Not a lookup tool. Reach for it while *building* OSINT tooling: when you've written (or copied) a regex to extract emails, phone numbers, usernames, crypto wallets, or IDs from scraped pages/logs and want to confirm it matches what you think before running it at scale. The diagram makes an opaque pattern legible so you don't silently miss or over-match selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://regexper.com/.
2. Paste your regular expression into the box and press Display / Enter.
3. Read the railroad diagram: branches, character classes, quantifiers, and groups are drawn left-to-right so you can trace exactly what the pattern accepts.
4. Download the diagram as SVG/PNG or grab a permalink to share; adjust the regex and re-render until it matches your target selector cleanly.

## Inputs → Outputs
- **In:** a regular-expression string (no OSINT selector — this is a developer aid)
- **Out:** a visual railroad diagram of the pattern (SVG/PNG), no subject data
- **Empty/negative result looks like:** a parse error if the regex is malformed — fix the syntax and re-submit.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — everything renders client-side; nothing is queried about a target. Don't paste patterns containing sensitive literals into the permalink feature (the pattern is encoded in the shared URL).
- It visualizes syntax, not runtime behavior against your data — still test the regex against real sample text.

## Overlaps ("do both")
- Complements live regex testers (e.g. regex101-style tools) — Regexper shows the *structure* of a pattern, while a tester shows *matches against sample input*; use both when a pattern misbehaves.

## Trust & verifiability
`trust: unverified` — an open-source personal project; its code is public on GitLab so you can audit exactly how it parses, but treat it as a convenience utility rather than an authoritative tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | regexper |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
