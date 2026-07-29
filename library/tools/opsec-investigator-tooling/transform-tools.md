---
id: transform-tools
name: Transform Tools
description: Use when you have data in one format and need it in another — a free web collection of converters (JSON↔schemas, CSV, Markdown, HTML) for wrangling OSINT data.
url: https://transform.tools/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Quickly converting between data formats (JSON, CSV, Markdown, HTML, GraphQL, code) while cleaning up collected OSINT data.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source; no account. Runs in the browser (most converters process input client-side).
opsec: passive
opsecNote: Most transform.tools converters run entirely in your browser (client-side), so data typically isn't sent to a server — but verify that for any given converter before pasting sensitive material, and prefer not to paste raw PII/case identifiers into a web tool at all. For truly sensitive data, use a local/offline converter instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A popular open-source developer utility (public source on GitHub); a format-conversion helper, not a data source, so trust concerns are limited to where a given converter processes your input.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- transform.tools
tags:
- data-wrangling
- developer-utility
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Transform Tools

> A free, open-source hub of in-browser format converters. A data-wrangling utility for OSINT workflows — reshape collected data between formats without writing a one-off script.

## When to use
You've collected data in one shape and need it in another to analyze or import it: an API's JSON into a typed schema or SQL, a `.csv` into JSON for a script, Markdown notes into HTML for a report, HTML into JSX, and many more. Reach for it to save time cleaning and converting between formats mid-investigation. It's plumbing — it produces no subject data, it just reshapes what you already have.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://transform.tools/ and pick the converter matching your source→target formats.
2. Paste your input on the left (or upload where supported).
3. Read the converted output on the right and copy it out.
4. Feed the result into your analysis/visualization tool or script.
5. For sensitive input, confirm the converter runs client-side (or use a local tool) before pasting — see OpSec.

## Inputs → Outputs
- **In:** data in a source format (not a subject selector)
- **Out:** the same data in your chosen target format
- **Empty/negative result looks like:** a parse error or empty output — usually malformed input; fix the source syntax and retry.

## Gotchas & OpSec
- Most converters are client-side, but don't assume — verify per converter before pasting anything sensitive; better yet, keep raw PII out of web tools.
- It transforms format, not meaning — a bad conversion can silently mangle data; spot-check the output.
- No persistence — it's a one-shot converter, not storage.

## Overlaps ("do both")
- Complements analysis/visualization tools like `[[observable]]` and `[[highcharts]]` — use Transform Tools to get your data into the shape those expect, then analyze/plot it there.

## Trust & verifiability
`trust: community` — a well-known open-source developer utility; it's a format converter, not an intelligence source, so verify only where a given converter processes your input and always sanity-check the converted result.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | transform-tools |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
