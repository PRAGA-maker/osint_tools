---
id: regular-expression-analyzer
name: Regular Expression Analyzer
description: Use when you have a regex (from a config, a scraper, or someone else's code) and want it parsed into a readable tree to understand what it matches — a code-comprehension utility, no selectors.
url: https://xenon.stanford.edu/~xusch/regexp/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Decomposing an unfamiliar or dense regular expression into a visual tree so you can see what it actually matches.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free academic web page; no account. Note it is an old (c. 2007) Stanford personal page and may not always be reachable.
opsec: passive
opsecNote: You paste a regex pattern, not target data, into a static analyzer page — nothing sensitive need leave your side. Avoid pasting patterns that themselves embed a target's literal identifier if you'd rather not send it to a third-party page; otherwise this is inert.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-author academic utility from ~2007; still online but unmaintained, so treat availability as best-effort and prefer a modern alternative when it matters.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- palladio
- stanford-large-network-dataset-collection
- swap-stanford-edu
aliases:
- regexp analyzer
tags:
- code
- regex
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Regular Expression Analyzer

> A minimal academic page that parses a regex into a tree-like structure — a "help me read someone else's regex" aid, not an investigative data source.

## When to use
When an investigation hands you a dense regular expression — inside a scraper you inherited, a log-parsing config, a WAF rule, or malware that validates input — and you need to understand what it matches without reverse-engineering it in your head. This tool renders the pattern's structure as a tree so its groups, alternations, and quantifiers are legible. It supports Java, JavaScript, and Perl regex flavors. It returns no OSINT selectors; it's a comprehension aid. Because the page is old and sometimes unreachable, keep a modern alternative in mind (see Overlaps).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://xenon.stanford.edu/~xusch/regexp/ (if it fails to load, use a modern alternative — see below).
2. Select the regex flavor (Java / JavaScript / Perl) that matches the source you're analyzing.
3. Paste the regular expression and submit.
4. Read the generated tree: it breaks the expression into its structural components so you can trace what each part matches.
5. Pivot: once you understand the pattern, apply it (or reason about what data it was designed to capture) in the tool where you found it.

## Inputs → Outputs
- **In:** a regular expression string (+ chosen flavor) — no OSINT selector
- **Out:** a tree-structured breakdown of the pattern (no selectors)
- **Empty/negative result looks like:** a parse error for a pattern that doesn't fit the selected flavor, or the page failing to load at all (it's an old, unmaintained host). Either case → switch to a maintained tool.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; you send only the pattern. It's fine unless the regex literally embeds a target identifier you'd rather not paste to a third-party page.
- **Reliability caveat:** this is a ~2007 Stanford personal page. It may be intermittently or permanently unreachable, hence `status: degraded`. Don't build a workflow around it.

## Overlaps ("do both")
- Superseded in practice by modern, maintained regex explainers (e.g. regex101, debuggex) that show matches, groups, and step-by-step evaluation with live test strings. Prefer those; keep this only as a fallback tree-view.

## Trust & verifiability
`trust: community` — an unmaintained single-author academic utility. Its output (a structural parse) is easy to sanity-check against the pattern, but availability is not guaranteed and it should not be relied upon as a stable tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | regular-expression-analyzer |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
