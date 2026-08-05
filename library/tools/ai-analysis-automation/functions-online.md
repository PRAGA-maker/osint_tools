---
id: functions-online
name: Functions Online
description: Use when you have an encoded/hashed string encountered mid-investigation (base64, url-encoded, md5, serialized PHP) and want to quickly transform or hash it in-browser — a decode/encode utility, not a data source.
url: https://www.functions-online.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Quick in-browser PHP-function encoding/decoding/hashing of strings during analysis.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: active
opsecNote: Input is processed server-side, so anything you paste leaves your machine and could be logged by the site. Never submit sensitive, evidentiary, or identifying payloads here — use a local/offline decoder (CyberChef desktop, a shell one-liner) for those.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party utility site that runs PHP functions on its own server; fine for throwaway public strings, but you cannot verify its logging, so treat it as untrusted with your data.
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
- functions-online.com
tags:
- decoding
- encoding
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Functions Online

> A browser-based runner for common PHP functions — a quick way to decode, encode, or hash a throwaway string without opening a terminal.

## When to use
You've encountered an opaque string during an investigation — a base64 blob, a URL-encoded parameter, an md5/sha hash to identify, a serialized PHP payload — and want to transform it fast. Functions Online exposes PHP's string/crypto/URL/array functions (`base64_decode`, `urldecode`, `md5`, `hash`, `json_decode`, `unserialize`, etc.) as web forms. It's a scratch utility to make encoded data readable so you can spot embedded selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.functions-online.com/ and pick the function category (String, Cryptography, URL, Array, etc.).
2. Select the specific function (e.g. `base64_decode`, `urldecode`, `unserialize`).
3. Paste the string (only non-sensitive/public data — see OpSec) and run it.
4. Read the transformed output; chain functions manually if the data is multi-layered.
5. Pivot: decoded content may reveal URLs, emails, or IDs → hand those to the relevant enrichment tool.

## Inputs → Outputs
- **In:** an encoded/hashed/serialized string (no person selector directly)
- **Out:** the decoded/encoded/hashed result (which may contain selectors to extract)
- **Empty/negative result looks like:** garbled output or an error — usually the wrong function/encoding; try another (e.g. the data was gzip'd or XOR'd, not plain base64).

## Gotchas & OpSec
- **Active/server-side:** your input is sent to and processed by a third-party server. Do NOT paste sensitive or evidentiary data — prefer a local decoder for anything real.
- No batch/chaining UI; multi-layer encodings mean running one function at a time.
- Results are only as reliable as an unverified third-party site — sanity-check important decodes locally.

## Overlaps ("do both")
- For anything sensitive or multi-step, prefer a local, offline decoder (a CyberChef instance or a shell one-liner); use Functions Online only for quick, disposable public strings.

## Trust & verifiability
`trust: unverified` — a convenient but opaque third-party utility with unknown logging; treat it as untrusted infrastructure and reserve it for non-sensitive scratch work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | functions-online |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
