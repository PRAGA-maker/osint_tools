---
id: html-sanitizer-tool
name: HTML Sanitizer Tool
description: Use when you have raw HTML/text scraped during an investigation and want to safely escape special characters before displaying or storing it — an ancillary display-safety utility, not a data source.
url: https://defuse.ca/html-sanitize.htm
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Escaping HTML special characters so untrusted scraped markup renders as inert text.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web utility on defuse.ca; no account.
opsec: passive
opsecNote: Whatever you paste is sent to defuse.ca to be processed. Do not paste sensitive case data into a third-party site — for anything private, use the equivalent local one-liner (the page publishes its PHP/JS logic) instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of Taylor Hornby's long-standing defuse.ca toolbox; simple and reputable, but this is a developer utility, not an OSINT data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- big-number-calculator
- defuse
- text-and-file-hash-calculator
- x86-and-x64-intel-assembler
aliases:
- HTML escape tool
- defuse.ca html-sanitize
tags: []
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# HTML Sanitizer Tool

> A minimal web utility that escapes HTML special characters (`<`, `>`, `&`, quotes) into entities — turning untrusted scraped markup into inert, safe-to-display text.

## When to use
This is an **ancillary utility**, not an investigative lookup. Reach for it when you've scraped raw HTML or user-generated text and need to display or embed it safely (e.g. in a report, a note, or a rendered page) without the markup executing. It converts special characters to entities so pasted content can't inject script or break your layout. It returns no data about a person and has no direct missing-persons value.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://defuse.ca/html-sanitize.htm.
2. Paste the raw text/HTML into the input box (options for tab width and line-break handling).
3. Submit; copy the escaped output where `<`→`&lt;`, `>`→`&gt;`, `&`→`&amp;`, etc.
4. For sensitive material, instead run the equivalent locally — the page shows the underlying PHP so you never upload the content.

## Inputs → Outputs
- **In:** arbitrary text/HTML (no investigative selector)
- **Out:** HTML-escaped text (no investigative selector)
- **Empty/negative result looks like:** identical output to input when the text contains no special characters — expected, not an error.

## Gotchas & OpSec
- **It escapes, it does not sanitize** — it will not strip scripts from HTML you intend to *render*; it makes the whole string display as literal text. Don't rely on it as an XSS filter for live rendering.
- Passive, but your pasted content goes to defuse.ca — keep case-sensitive material off third-party sites and use the published local code.
- Purely a formatting helper; it yields no intelligence on a subject.

## Overlaps ("do both")
- Sits alongside the other defuse.ca utilities `[[defuse]]`, `[[text-and-file-hash-calculator]]`, and `[[big-number-calculator]]` — a small toolbox for handling/normalizing artifacts, not for finding people.

## Trust & verifiability
`trust: community` — a simple, transparent utility from a well-known security author; it does exactly one deterministic thing, but it is a developer helper with no evidentiary or lookup role.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | html-sanitizer-tool |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
