---
id: paulschou-binary-translator
name: Paulschou Binary Translator (xlate)
description: Use when you have an encoded string (binary, hex, octal, base64, ASCII/ANSI) and want to convert it to readable text or between formats — returns the decoded/re-encoded value.
url: https://paulschou.com/tools/xlate
category: translation-language
path:
- translation-language
bestFor: Fast in-browser conversion between text and binary/hex/octal/decimal/base64 encodings.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free single-page web tool; no account. (Occasionally unreachable — server returned a transient 5xx at last check — but historically stable.)
opsec: passive
opsecNote: You paste your string into a third-party page, so don't decode anything sensitive (keys, credentials, case data) there — for that, use an offline converter. For harmless CTF-style or public encoded blobs it's fine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing personal-site utility (paulschou.com); simple and reliable in function, but a one-person site with no uptime guarantee.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- xlate
- paulschou xlate
tags:
- encoding
- decoder
- translation
source: metaosint
lastVerified: '2026-08-05'
enrichment: full
---

# Paulschou Binary Translator (xlate)

> A simple, long-lived web converter: paste text or an encoded blob and translate it across ASCII/ANSI, binary, octal, decimal, hexadecimal and base64.

## When to use
You've pulled a string that isn't plain text — a run of 1s and 0s, a hex dump, a base64 blob, a decimal char sequence — and need it human-readable, or you need to encode a value the other way. Common in document/metadata analysis, CTF-style puzzles, and decoding obfuscated fragments found during an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://paulschou.com/tools/xlate (if it's momentarily down, retry — it 5xx's occasionally).
2. Paste your value into the field for its current format (text, hex, binary, octal, decimal, base64).
3. The tool renders the equivalent in the other formats simultaneously — read off the one you need.
4. Pivot: feed decoded text into search/translation tools, or re-encode a value to match a target format.

## Inputs → Outputs
- **In:** none as a selector — an encoded/plain string you paste
- **Out:** none as a selector — the same value converted across encodings
- **Empty/negative result looks like:** garbled output means the input wasn't actually in the format you selected — try a different source encoding or check for stray whitespace/delimiters.

## Gotchas & OpSec
- Third-party page: don't paste sensitive material; use an offline/CyberChef-local converter for anything private.
- Availability wobbles (single personal site) — status marked `degraded`; keep a fallback converter handy.
- It handles simple encodings, not encryption — a base64 string decodes, an encrypted blob won't.

## Overlaps ("do both")
- CyberChef does the same conversions plus far more (and can run fully offline); use xlate for a quick one-off and CyberChef for anything complex or sensitive.

## Trust & verifiability
`trust: community` — a dependable little personal-site utility for format conversion; the operation is deterministic and easy to sanity-check by re-encoding the result.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | paulschou-binary-translator |
| category | translation-language |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
