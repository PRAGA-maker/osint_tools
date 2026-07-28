---
id: free-translator
name: Free translator
description: Use when you have foreign-language text or a foreign-language page tied to a subject and need a quick gist translation — returns translated text, no personal selectors.
url: http://www.free-translator.com
category: translation-language
path:
- translation-language
bestFor: Quick free machine translation of short text snippets or a web page across ~100 languages.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free machine translation; capped at roughly 200 words per text request. No account.
opsec: passive
opsecNote: Anything you paste is sent to a third-party translation service — do not paste sensitive case text, credentials, or PII you must keep confidential. Translating a URL causes the service to fetch that page, so avoid pasting a private/target-controlled URL you don't want fetched by a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Dated third-party translation portal that brokers to underlying MT engines; quality and uptime are inconsistent, so treat output as gist only.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- free-translator.com
tags:
- translation
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# Free translator

> An old, no-signup machine-translation portal — a quick gist tool for foreign-language snippets, superseded by better engines but usable when you just need the sense.

## When to use
Low-relevance, language-support only. Reach for it when a subject's post, document, or a foreign-language web page is in a language you don't read and you need a fast gist to decide whether it matters — before committing to a careful translation. It returns translated text, not any data about a person. For anything you'll cite or act on, verify with a stronger engine or a human translator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.free-translator.com in a browser.
2. Choose the text-translation tool, pick source and target languages (auto-detect where offered), and paste up to ~200 words — or use the web-page tool and paste a public URL.
3. Submit and read the translated output for gist.
4. For longer material, translate in chunks; for a page, prefer the text tool over the URL tool when the source URL is sensitive.
5. Pivot: use the gist to triage, then route anything decisive through a higher-quality translation.

## Inputs → Outputs
- **In:** foreign-language text or a public page URL (free text — not a personal selector)
- **Out:** machine-translated text (no personal selectors)
- **Empty/negative result looks like:** a blank/garbled result, a timeout, or an error page — the site is dated and intermittently unreliable; fall back to another engine.

## Gotchas & OpSec
- Uptime and quality are inconsistent — it is a legacy portal; keep a mainstream MT engine as backup.
- Do **not** paste confidential case text, PII, or credentials — it goes to a third party.
- The URL-translation mode makes the service fetch the page; don't feed it a private or target-controlled link you don't want a third party retrieving.

## Overlaps ("do both")
- Cross-check with any other machine-translation tool in this category — running a doubtful passage through a second engine catches mistranslations that change meaning, which matters when the text is evidentiary.

## Trust & verifiability
`trust: unverified` — a dated broker to underlying MT engines with no transparency on which. Treat every output as gist; confirm anything you'll rely on with a stronger translator or a qualified human.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-translator |
| category | translation-language |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
