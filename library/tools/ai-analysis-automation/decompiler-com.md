---
id: decompiler-com
name: Decompiler.com
description: Use when you have a compiled artifact (JAR/class, APK/DEX, .NET EXE/DLL, .pyc, SWF, Lua) and want readable source in-browser — returns decompiled code to inspect for embedded artefacts.
url: https://www.decompiler.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Drag-and-drop online decompilation of Java/Android/.NET/Python/Flash/Lua artifacts without local tooling.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free in-browser decompilation; no account for basic use.
opsec: active
opsecNote: You UPLOAD the artifact to decompiler.com's servers — the file leaves your machine and is processed by a third party. Never upload confidential, proprietary, or restricted samples; use a local decompiler (jadx, dnSpy, uncompyle6) for anything sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A convenient online decompiler covering many formats; fine for quick triage, but a third-party upload service with no strong provenance guarantees.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- decompiler.com
tags:
- decompiler
- reverse-engineering
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Decompiler.com

> A drag-and-drop online decompiler for many formats: turn a JAR, APK, .NET binary, .pyc or SWF into readable source in the browser.

## When to use
A niche RE tool, not a people-finder. When an investigation involves a compiled artifact — a suspect Android APK, a Java/.NET binary, a Python `.pyc` — and you want to read its source quickly to understand behaviour and extract artefacts (hardcoded URLs, `domain`s, API keys, account handles, endpoints). Those extracted strings are the OSINT payoff; the tool itself analyses code.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.decompiler.com/.
2. Drag in the artifact (`.jar/.class`, `.apk/.dex/.aab`, `.exe/.dll`, `.pyc`, `.swf`, `.luac`).
3. Browse the decompiled source online or download it.
4. Scan for embedded URLs, domains, keys, and identifiers; use the bundled JWT/Base64 tools as needed.
5. Pivot: hand any recovered `domain`/URL/handle/key to the matching OSINT/infrastructure tool.

## Inputs → Outputs
- **In:** a compiled artifact (not an OSINT selector)
- **Out:** decompiled source code (extract embedded strings/domains/keys manually)
- **Empty/negative result looks like:** failed/garbled decompilation — the format is unsupported, obfuscated, or packed; try a specialised local decompiler.

## Gotchas & OpSec
- **Upload = disclosure** — third-party server; keep confidential/restricted samples off it and decompile locally instead.
- Obfuscated/packed code decompiles poorly; deobfuscate first.
- Decompiled output approximates the original — variable names/structure may be lost.

## Overlaps ("do both")
- Complements local decompilers (jadx for APK, dnSpy/ILSpy for .NET) and `[[oda-the-online-disassembler]]` — use this for fast no-install triage, local tools for depth and for anything you can't upload.

## Trust & verifiability
`trust: community` — a handy multi-format service, but third-party; for sensitive artefacts reproduce the decompilation locally so nothing is uploaded.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | decompiler-com |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
