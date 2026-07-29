---
id: html-editor
name: HTML editor
description: Use when you have raw or scraped HTML and want to view/clean/preview it — a free online WYSIWYG+source editor for inspecting markup and converting rich text.
url: https://onlinehtmleditor.dev/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Quickly previewing, cleaning, or converting HTML/rich text (e.g. inspecting scraped markup or turning pasted content into clean HTML).
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free to use the core editor in-browser; a paid plan/free-trial covers advanced/collaboration features. The basic HTML/WYSIWYG editing you need for OSINT clean-up is free.
opsec: passive
opsecNote: The editor runs in your browser (built on CKEditor 5), but it is a hosted web page — don't paste sensitive case content or PII into a third-party site if you can avoid it. For anything sensitive, use a local editor. As a support utility it never contacts a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A hosted editor built on the well-known open-source CKEditor 5; dependable for its purpose. It's a formatting utility, not an intelligence source, so trust concerns are about pasting sensitive data, not accuracy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- onlinehtmleditor.dev
- online HTML editor
tags:
- developer-utility
- html
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# HTML editor

> A free in-browser HTML/WYSIWYG editor (CKEditor 5). A support utility for OSINT: inspect and clean scraped markup, or convert pasted rich text into tidy HTML.

## When to use
A minor-but-handy helper, not a data source. Two realistic uses: (1) **inspect scraped/exported HTML** — paste raw markup and toggle the source/preview to see how a page is structured or to pull out embedded links/text; (2) **clean or convert content** — turn messy pasted rich text (from Word/Google Docs) into clean HTML for a report. It produces no subject data; it just helps you handle markup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://onlinehtmleditor.dev/.
2. Paste HTML into the source view, or paste rich text into the WYSIWYG view.
3. Toggle between WYSIWYG and source to read structure and spot embedded links/attributes.
4. Clean up formatting and copy the resulting HTML out.
5. Keep sensitive content out of the hosted tool — use a local editor for anything confidential.

## Inputs → Outputs
- **In:** HTML source or rich text (not a subject selector)
- **Out:** cleaned/previewed HTML
- **Empty/negative result looks like:** N/A — it renders whatever you paste; malformed HTML simply previews imperfectly.

## Gotchas & OpSec
- Hosted third-party page — don't paste PII/case data; prefer a local editor for sensitive markup.
- It's a formatting aid, not analysis — for extracting data from many pages at scale, use a proper parser/scraper.
- Advanced features sit behind a paid tier; basic editing is free.

## Overlaps ("do both")
- Complements scraping/parsing tools and format converters like `[[transform-tools]]` — those extract/convert at scale; this is for quick manual inspection and clean-up of a single chunk of markup.

## Trust & verifiability
`trust: community` — built on the reputable open-source CKEditor 5; reliable for editing, with the only caution being not to paste sensitive data into a hosted service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | html-editor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
