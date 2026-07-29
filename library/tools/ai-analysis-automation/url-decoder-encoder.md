---
id: url-decoder-encoder
name: URL Decoder/Encoder
description: Use when you have a percent-encoded URL/parameter and want to read or build it — returns the decoded/encoded string in the browser.
url: https://meyerweb.com/eric/tools/dencoder/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Quick percent-encode/decode of URLs and query parameters.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free single-purpose web page (Eric Meyer's dencoder); no account.
opsec: passive
opsecNote: Passive and client-side — the encode/decode runs in your browser (JavaScript), so the string isn't sent anywhere. Still, avoid pasting anything you wouldn't want in your browser history; for extreme sensitivity use a local decoder.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing single-purpose utility by web-standards author Eric Meyer; trivial, deterministic, client-side.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- online-tools
aliases:
- meyerweb dencoder
- dencoder
tags:
- encoding
- url
- utilities
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# URL Decoder/Encoder

> A tiny, client-side page for percent-encoding and decoding URLs and query strings.

## When to use
You have a percent-encoded URL or parameter — from a captured link, a redirect, a log, or a tracking URL — and want to read what it actually says, or you need to encode a string to build a valid URL. This is a single-purpose analysis aid; it produces no OSINT selectors of its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://meyerweb.com/eric/tools/dencoder/.
2. Paste the string into the box.
3. Click **Decode** to turn `%20`/`%3D`-style sequences into readable text, or **Encode** to do the reverse.
4. Read the result; a decoded URL often reveals embedded parameters (targets, IDs, redirect destinations).
5. Pivot: a decoded value (an email, another URL, an ID) becomes a fresh selector for your workflow.

## Inputs → Outputs
- **In:** a URL/percent-encoded string (no OSINT selector)
- **Out:** the decoded or encoded string
- **Empty/negative result looks like:** unchanged text (it wasn't actually encoded) or an obviously wrong result if you chose the opposite operation — flip encode/decode.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive/client-side — nothing is transmitted; only browser-history hygiene applies.
- It handles URL percent-encoding only — not Base64/hex/JWT; use a broader toolbox for those.

## Overlaps ("do both")
- Overlaps with `[[online-tools]]`, which covers URL encoding plus Base64/hex/JWT/hashing — prefer that when you need more than percent-encoding.

## Trust & verifiability
`trust: community` — a trivial, deterministic client-side utility from a reputable author; outputs are self-verifying (re-encode to confirm).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | url-decoder-encoder |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
